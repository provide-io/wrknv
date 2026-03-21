# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#
# wrknv/workenv/managers/tf_base.py
#
"""
Tf Manager Base
===============
Base class for Tf (IBM Terraform/OpenTofu) managers that use ~/.terraform.versions
directory structure. This implementation is compatible with tfswitch and
designed for managing Tf tool versions.
"""

from __future__ import annotations

from abc import abstractmethod
from datetime import datetime
import hashlib
import json
import os
import pathlib
import shutil
import sys
from typing import TYPE_CHECKING

from provide.foundation import logger
import semver

from .base import BaseToolManager, ToolManagerError

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


class TfVersionsManager(BaseToolManager):
    """
    Base class for managers using ~/.terraform.versions directory.

    This directory structure is compatible with tfswitch, allowing users to
    use either tool interchangeably while providing enhanced metadata tracking
    for advanced features. Supports both IBM Terraform (formerly HashiCorp) and OpenTofu.
    """

    def xǁTfVersionsManagerǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(None)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = None
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_3(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path(None).expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_4(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("XX~/.terraform.versionsXX").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_5(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.TERRAFORM.VERSIONS").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_6(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=None, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_7(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=None)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_8(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_9(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, )

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_10(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=False, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_11(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=False)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_12(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = None

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_13(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = None
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_14(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path * "metadata.json"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_15(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "XXmetadata.jsonXX"
        self._load_metadata()

    def xǁTfVersionsManagerǁ__init____mutmut_16(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get venv bin directory for copying active binaries
        self.venv_bin_dir = self._get_venv_bin_dir()

        # Metadata file for enriched information
        self.metadata_file = self.install_path / "METADATA.JSON"
        self._load_metadata()
    
    xǁTfVersionsManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ__init____mutmut_1': xǁTfVersionsManagerǁ__init____mutmut_1, 
        'xǁTfVersionsManagerǁ__init____mutmut_2': xǁTfVersionsManagerǁ__init____mutmut_2, 
        'xǁTfVersionsManagerǁ__init____mutmut_3': xǁTfVersionsManagerǁ__init____mutmut_3, 
        'xǁTfVersionsManagerǁ__init____mutmut_4': xǁTfVersionsManagerǁ__init____mutmut_4, 
        'xǁTfVersionsManagerǁ__init____mutmut_5': xǁTfVersionsManagerǁ__init____mutmut_5, 
        'xǁTfVersionsManagerǁ__init____mutmut_6': xǁTfVersionsManagerǁ__init____mutmut_6, 
        'xǁTfVersionsManagerǁ__init____mutmut_7': xǁTfVersionsManagerǁ__init____mutmut_7, 
        'xǁTfVersionsManagerǁ__init____mutmut_8': xǁTfVersionsManagerǁ__init____mutmut_8, 
        'xǁTfVersionsManagerǁ__init____mutmut_9': xǁTfVersionsManagerǁ__init____mutmut_9, 
        'xǁTfVersionsManagerǁ__init____mutmut_10': xǁTfVersionsManagerǁ__init____mutmut_10, 
        'xǁTfVersionsManagerǁ__init____mutmut_11': xǁTfVersionsManagerǁ__init____mutmut_11, 
        'xǁTfVersionsManagerǁ__init____mutmut_12': xǁTfVersionsManagerǁ__init____mutmut_12, 
        'xǁTfVersionsManagerǁ__init____mutmut_13': xǁTfVersionsManagerǁ__init____mutmut_13, 
        'xǁTfVersionsManagerǁ__init____mutmut_14': xǁTfVersionsManagerǁ__init____mutmut_14, 
        'xǁTfVersionsManagerǁ__init____mutmut_15': xǁTfVersionsManagerǁ__init____mutmut_15, 
        'xǁTfVersionsManagerǁ__init____mutmut_16': xǁTfVersionsManagerǁ__init____mutmut_16
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ__init____mutmut_orig)
    xǁTfVersionsManagerǁ__init____mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ__init__'

    @property
    @abstractmethod
    def tool_prefix(self) -> str:
        """Prefix for version files (e.g., 'terraform' or 'opentofu')."""

    def xǁTfVersionsManagerǁ_load_metadata__mutmut_orig(self) -> None:
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

    def xǁTfVersionsManagerǁ_load_metadata__mutmut_1(self) -> None:
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

    def xǁTfVersionsManagerǁ_load_metadata__mutmut_2(self) -> None:
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

    def xǁTfVersionsManagerǁ_load_metadata__mutmut_3(self) -> None:
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

    def xǁTfVersionsManagerǁ_load_metadata__mutmut_4(self) -> None:
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

    def xǁTfVersionsManagerǁ_load_metadata__mutmut_5(self) -> None:
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
    
    xǁTfVersionsManagerǁ_load_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_load_metadata__mutmut_1': xǁTfVersionsManagerǁ_load_metadata__mutmut_1, 
        'xǁTfVersionsManagerǁ_load_metadata__mutmut_2': xǁTfVersionsManagerǁ_load_metadata__mutmut_2, 
        'xǁTfVersionsManagerǁ_load_metadata__mutmut_3': xǁTfVersionsManagerǁ_load_metadata__mutmut_3, 
        'xǁTfVersionsManagerǁ_load_metadata__mutmut_4': xǁTfVersionsManagerǁ_load_metadata__mutmut_4, 
        'xǁTfVersionsManagerǁ_load_metadata__mutmut_5': xǁTfVersionsManagerǁ_load_metadata__mutmut_5
    }
    
    def _load_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_load_metadata__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_load_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _load_metadata.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_load_metadata__mutmut_orig)
    xǁTfVersionsManagerǁ_load_metadata__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_load_metadata'

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_orig(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_1(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_2(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_3(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_4(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_5(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_6(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_7(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_8(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_9(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_10(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_11(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_12(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_13(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_14(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_15(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_16(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_17(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_18(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_19(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_20(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_21(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_22(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_23(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_24(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_25(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_26(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_27(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_28(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_29(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_30(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_31(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_32(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_33(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_34(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_35(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_36(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_37(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_38(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_39(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_40(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_41(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_42(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_43(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_44(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_45(self) -> None:
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
            self._save_metadata()

    def xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_46(self) -> None:
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
            self._save_metadata()
    
    xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_1': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_1, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_2': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_2, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_3': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_3, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_4': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_4, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_5': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_5, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_6': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_6, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_7': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_7, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_8': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_8, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_9': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_9, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_10': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_10, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_11': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_11, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_12': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_12, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_13': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_13, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_14': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_14, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_15': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_15, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_16': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_16, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_17': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_17, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_18': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_18, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_19': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_19, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_20': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_20, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_21': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_21, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_22': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_22, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_23': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_23, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_24': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_24, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_25': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_25, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_26': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_26, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_27': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_27, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_28': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_28, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_29': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_29, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_30': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_30, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_31': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_31, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_32': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_32, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_33': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_33, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_34': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_34, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_35': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_35, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_36': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_36, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_37': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_37, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_38': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_38, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_39': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_39, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_40': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_40, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_41': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_41, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_42': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_42, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_43': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_43, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_44': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_44, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_45': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_45, 
        'xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_46': xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_46
    }
    
    def _migrate_metadata_format(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _migrate_metadata_format.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_orig)
    xǁTfVersionsManagerǁ_migrate_metadata_format__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_migrate_metadata_format'

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_orig(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_1(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open(None) as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_2(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("XXwXX") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_3(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("W") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_4(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(None, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_5(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, None, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_6(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=None, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_7(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=None, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_8(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=None)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_9(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_10(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_11(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_12(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_13(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, )
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_14(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=3, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_15(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=False, default=str)
        except Exception as e:
            logger.warning(f"Failed to save metadata: {e}")

    def xǁTfVersionsManagerǁ_save_metadata__mutmut_16(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2, sort_keys=True, default=str)
        except Exception as e:
            logger.warning(None)
    
    xǁTfVersionsManagerǁ_save_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_save_metadata__mutmut_1': xǁTfVersionsManagerǁ_save_metadata__mutmut_1, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_2': xǁTfVersionsManagerǁ_save_metadata__mutmut_2, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_3': xǁTfVersionsManagerǁ_save_metadata__mutmut_3, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_4': xǁTfVersionsManagerǁ_save_metadata__mutmut_4, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_5': xǁTfVersionsManagerǁ_save_metadata__mutmut_5, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_6': xǁTfVersionsManagerǁ_save_metadata__mutmut_6, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_7': xǁTfVersionsManagerǁ_save_metadata__mutmut_7, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_8': xǁTfVersionsManagerǁ_save_metadata__mutmut_8, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_9': xǁTfVersionsManagerǁ_save_metadata__mutmut_9, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_10': xǁTfVersionsManagerǁ_save_metadata__mutmut_10, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_11': xǁTfVersionsManagerǁ_save_metadata__mutmut_11, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_12': xǁTfVersionsManagerǁ_save_metadata__mutmut_12, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_13': xǁTfVersionsManagerǁ_save_metadata__mutmut_13, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_14': xǁTfVersionsManagerǁ_save_metadata__mutmut_14, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_15': xǁTfVersionsManagerǁ_save_metadata__mutmut_15, 
        'xǁTfVersionsManagerǁ_save_metadata__mutmut_16': xǁTfVersionsManagerǁ_save_metadata__mutmut_16
    }
    
    def _save_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_save_metadata__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_save_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _save_metadata.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_save_metadata__mutmut_orig)
    xǁTfVersionsManagerǁ_save_metadata__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_save_metadata'

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_orig(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_1(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = None
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_2(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path * "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_3(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "XXRECENTXX"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_4(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "recent"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_5(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = None

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_6(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = None
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_7(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(None)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_8(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = None

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_9(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = None
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_10(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name == "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_11(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "XXtofuXX" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_12(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "TOFU" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_13(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "XXopentofuXX"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_14(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "OPENTOFU"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_15(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = None

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_16(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_17(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_18(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_19(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_20(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_21(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_22(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_23(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_24(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_25(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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

    def xǁTfVersionsManagerǁ_update_recent_file__mutmut_26(self) -> None:
        """Update the RECENT file with current installed versions."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get all installed versions for this tool
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"
        installed_versions = self.get_installed_versions()

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
    
    xǁTfVersionsManagerǁ_update_recent_file__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_update_recent_file__mutmut_1': xǁTfVersionsManagerǁ_update_recent_file__mutmut_1, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_2': xǁTfVersionsManagerǁ_update_recent_file__mutmut_2, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_3': xǁTfVersionsManagerǁ_update_recent_file__mutmut_3, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_4': xǁTfVersionsManagerǁ_update_recent_file__mutmut_4, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_5': xǁTfVersionsManagerǁ_update_recent_file__mutmut_5, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_6': xǁTfVersionsManagerǁ_update_recent_file__mutmut_6, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_7': xǁTfVersionsManagerǁ_update_recent_file__mutmut_7, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_8': xǁTfVersionsManagerǁ_update_recent_file__mutmut_8, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_9': xǁTfVersionsManagerǁ_update_recent_file__mutmut_9, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_10': xǁTfVersionsManagerǁ_update_recent_file__mutmut_10, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_11': xǁTfVersionsManagerǁ_update_recent_file__mutmut_11, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_12': xǁTfVersionsManagerǁ_update_recent_file__mutmut_12, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_13': xǁTfVersionsManagerǁ_update_recent_file__mutmut_13, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_14': xǁTfVersionsManagerǁ_update_recent_file__mutmut_14, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_15': xǁTfVersionsManagerǁ_update_recent_file__mutmut_15, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_16': xǁTfVersionsManagerǁ_update_recent_file__mutmut_16, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_17': xǁTfVersionsManagerǁ_update_recent_file__mutmut_17, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_18': xǁTfVersionsManagerǁ_update_recent_file__mutmut_18, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_19': xǁTfVersionsManagerǁ_update_recent_file__mutmut_19, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_20': xǁTfVersionsManagerǁ_update_recent_file__mutmut_20, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_21': xǁTfVersionsManagerǁ_update_recent_file__mutmut_21, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_22': xǁTfVersionsManagerǁ_update_recent_file__mutmut_22, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_23': xǁTfVersionsManagerǁ_update_recent_file__mutmut_23, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_24': xǁTfVersionsManagerǁ_update_recent_file__mutmut_24, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_25': xǁTfVersionsManagerǁ_update_recent_file__mutmut_25, 
        'xǁTfVersionsManagerǁ_update_recent_file__mutmut_26': xǁTfVersionsManagerǁ_update_recent_file__mutmut_26
    }
    
    def _update_recent_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_update_recent_file__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_update_recent_file__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_recent_file.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_update_recent_file__mutmut_orig)
    xǁTfVersionsManagerǁ_update_recent_file__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_update_recent_file'

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_orig(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_1(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = None
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_2(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path * "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_3(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "XXRECENTXX"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_4(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "recent"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_5(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = None

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_6(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = None
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_7(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(None)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_8(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = None

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_9(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = None

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_10(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name == "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_11(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "XXtofuXX" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_12(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "TOFU" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_13(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "XXopentofuXX"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_14(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "OPENTOFU"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_15(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = None

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_16(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(None, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_17(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, None)

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_18(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get([])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_19(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, )

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_20(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version not in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_21(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(None)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_22(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(None, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_23(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, None)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_24(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_25(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, )

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_26(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(1, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_27(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = None

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_28(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:6]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_29(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open(None) as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_30(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("XXwXX") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_31(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("W") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_32(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(None, f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_33(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, None)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_34(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(f)
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_35(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, )
        except Exception as e:
            logger.warning(f"Failed to update RECENT file with active version: {e}")

    def xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_36(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        recent_file = self.install_path / "RECENT"
        recent_data = {}

        # Read existing RECENT file if it exists
        if recent_file.exists():
            try:
                with recent_file.open() as f:
                    recent_data = json.load(f)
            except Exception:
                recent_data = {}

        # Get tool key
        tool_key = self.tool_name if self.tool_name != "tofu" else "opentofu"

        # Get current list of versions
        current_versions = recent_data.get(tool_key, [])

        # Remove version if it exists
        if version in current_versions:
            current_versions.remove(version)

        # Add version at the beginning
        current_versions.insert(0, version)

        # Keep only the 5 most recent
        recent_data[tool_key] = current_versions[:5]

        # Write updated RECENT file
        try:
            with recent_file.open("w") as f:
                json.dump(recent_data, f)
        except Exception as e:
            logger.warning(None)
    
    xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_1': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_1, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_2': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_2, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_3': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_3, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_4': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_4, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_5': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_5, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_6': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_6, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_7': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_7, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_8': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_8, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_9': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_9, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_10': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_10, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_11': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_11, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_12': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_12, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_13': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_13, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_14': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_14, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_15': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_15, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_16': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_16, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_17': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_17, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_18': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_18, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_19': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_19, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_20': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_20, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_21': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_21, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_22': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_22, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_23': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_23, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_24': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_24, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_25': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_25, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_26': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_26, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_27': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_27, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_28': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_28, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_29': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_29, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_30': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_30, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_31': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_31, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_32': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_32, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_33': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_33, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_34': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_34, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_35': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_35, 
        'xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_36': xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_36
    }
    
    def _update_recent_file_with_active(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_recent_file_with_active.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_orig)
    xǁTfVersionsManagerǁ_update_recent_file_with_active__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_update_recent_file_with_active'

    def xǁTfVersionsManagerǁget_binary_path__mutmut_orig(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        # In tf versions format, binaries are stored as prefix_version
        binary_name = f"{self.tool_prefix}_{version}"
        return self.install_path / binary_name

    def xǁTfVersionsManagerǁget_binary_path__mutmut_1(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        # In tf versions format, binaries are stored as prefix_version
        binary_name = None
        return self.install_path / binary_name

    def xǁTfVersionsManagerǁget_binary_path__mutmut_2(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        # In tf versions format, binaries are stored as prefix_version
        binary_name = f"{self.tool_prefix}_{version}"
        return self.install_path * binary_name
    
    xǁTfVersionsManagerǁget_binary_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁget_binary_path__mutmut_1': xǁTfVersionsManagerǁget_binary_path__mutmut_1, 
        'xǁTfVersionsManagerǁget_binary_path__mutmut_2': xǁTfVersionsManagerǁget_binary_path__mutmut_2
    }
    
    def get_binary_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁget_binary_path__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁget_binary_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_binary_path.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁget_binary_path__mutmut_orig)
    xǁTfVersionsManagerǁget_binary_path__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁget_binary_path'

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_orig(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_1(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = None

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_2(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = None
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_3(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() or item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_4(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(None):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_5(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = None
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_6(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(None):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_7(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(None)

        return sorted(versions, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_8(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(None, key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_9(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=None, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_10(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=None)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_11(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(key=self._version_sort_key, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_12(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, reverse=True)

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_13(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, )

    def xǁTfVersionsManagerǁget_installed_versions__mutmut_14(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=self._version_sort_key, reverse=False)
    
    xǁTfVersionsManagerǁget_installed_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁget_installed_versions__mutmut_1': xǁTfVersionsManagerǁget_installed_versions__mutmut_1, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_2': xǁTfVersionsManagerǁget_installed_versions__mutmut_2, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_3': xǁTfVersionsManagerǁget_installed_versions__mutmut_3, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_4': xǁTfVersionsManagerǁget_installed_versions__mutmut_4, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_5': xǁTfVersionsManagerǁget_installed_versions__mutmut_5, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_6': xǁTfVersionsManagerǁget_installed_versions__mutmut_6, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_7': xǁTfVersionsManagerǁget_installed_versions__mutmut_7, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_8': xǁTfVersionsManagerǁget_installed_versions__mutmut_8, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_9': xǁTfVersionsManagerǁget_installed_versions__mutmut_9, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_10': xǁTfVersionsManagerǁget_installed_versions__mutmut_10, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_11': xǁTfVersionsManagerǁget_installed_versions__mutmut_11, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_12': xǁTfVersionsManagerǁget_installed_versions__mutmut_12, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_13': xǁTfVersionsManagerǁget_installed_versions__mutmut_13, 
        'xǁTfVersionsManagerǁget_installed_versions__mutmut_14': xǁTfVersionsManagerǁget_installed_versions__mutmut_14
    }
    
    def get_installed_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁget_installed_versions__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁget_installed_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_versions.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁget_installed_versions__mutmut_orig)
    xǁTfVersionsManagerǁget_installed_versions__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁget_installed_versions'

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_orig(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_1(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_2(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_3(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_4(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_5(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_6(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_7(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_8(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_9(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_10(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_11(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_12(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_13(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_14(self, version: str) -> tuple[int, ...]:
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

    def xǁTfVersionsManagerǁ_version_sort_key__mutmut_15(self, version: str) -> tuple[int, ...]:
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
    
    xǁTfVersionsManagerǁ_version_sort_key__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_version_sort_key__mutmut_1': xǁTfVersionsManagerǁ_version_sort_key__mutmut_1, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_2': xǁTfVersionsManagerǁ_version_sort_key__mutmut_2, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_3': xǁTfVersionsManagerǁ_version_sort_key__mutmut_3, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_4': xǁTfVersionsManagerǁ_version_sort_key__mutmut_4, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_5': xǁTfVersionsManagerǁ_version_sort_key__mutmut_5, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_6': xǁTfVersionsManagerǁ_version_sort_key__mutmut_6, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_7': xǁTfVersionsManagerǁ_version_sort_key__mutmut_7, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_8': xǁTfVersionsManagerǁ_version_sort_key__mutmut_8, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_9': xǁTfVersionsManagerǁ_version_sort_key__mutmut_9, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_10': xǁTfVersionsManagerǁ_version_sort_key__mutmut_10, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_11': xǁTfVersionsManagerǁ_version_sort_key__mutmut_11, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_12': xǁTfVersionsManagerǁ_version_sort_key__mutmut_12, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_13': xǁTfVersionsManagerǁ_version_sort_key__mutmut_13, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_14': xǁTfVersionsManagerǁ_version_sort_key__mutmut_14, 
        'xǁTfVersionsManagerǁ_version_sort_key__mutmut_15': xǁTfVersionsManagerǁ_version_sort_key__mutmut_15
    }
    
    def _version_sort_key(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_version_sort_key__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_version_sort_key__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _version_sort_key.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_version_sort_key__mutmut_orig)
    xǁTfVersionsManagerǁ_version_sort_key__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_version_sort_key'

    def xǁTfVersionsManagerǁget_installed_version__mutmut_orig(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_1(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = None

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_2(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "XXworkenvXX" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_3(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "WORKENV" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_4(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" not in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_5(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = None
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_6(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(None, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_7(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, None)
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_8(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get({})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_9(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, )
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_10(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["XXworkenvXX"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_11(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["WORKENV"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_12(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = None

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_13(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "XXopentofu_versionXX" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_14(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "OPENTOFU_VERSION" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_15(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name != "tofu" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_16(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "XXtofuXX" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_17(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "TOFU" else f"{self.tool_name}_version"

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfVersionsManagerǁget_installed_version__mutmut_18(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            # Use 'opentofu_version' for tofu tool
            tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

            if tool_key not in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None
    
    xǁTfVersionsManagerǁget_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁget_installed_version__mutmut_1': xǁTfVersionsManagerǁget_installed_version__mutmut_1, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_2': xǁTfVersionsManagerǁget_installed_version__mutmut_2, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_3': xǁTfVersionsManagerǁget_installed_version__mutmut_3, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_4': xǁTfVersionsManagerǁget_installed_version__mutmut_4, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_5': xǁTfVersionsManagerǁget_installed_version__mutmut_5, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_6': xǁTfVersionsManagerǁget_installed_version__mutmut_6, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_7': xǁTfVersionsManagerǁget_installed_version__mutmut_7, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_8': xǁTfVersionsManagerǁget_installed_version__mutmut_8, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_9': xǁTfVersionsManagerǁget_installed_version__mutmut_9, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_10': xǁTfVersionsManagerǁget_installed_version__mutmut_10, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_11': xǁTfVersionsManagerǁget_installed_version__mutmut_11, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_12': xǁTfVersionsManagerǁget_installed_version__mutmut_12, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_13': xǁTfVersionsManagerǁget_installed_version__mutmut_13, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_14': xǁTfVersionsManagerǁget_installed_version__mutmut_14, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_15': xǁTfVersionsManagerǁget_installed_version__mutmut_15, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_16': xǁTfVersionsManagerǁget_installed_version__mutmut_16, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_17': xǁTfVersionsManagerǁget_installed_version__mutmut_17, 
        'xǁTfVersionsManagerǁget_installed_version__mutmut_18': xǁTfVersionsManagerǁget_installed_version__mutmut_18
    }
    
    def get_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁget_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁget_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_version.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁget_installed_version__mutmut_orig)
    xǁTfVersionsManagerǁget_installed_version__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁget_installed_version'

    def xǁTfVersionsManagerǁset_installed_version__mutmut_orig(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_1(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = None

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_2(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "XXworkenvXX" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_3(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "WORKENV" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_4(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_5(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = None
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_6(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["XXworkenvXX"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_7(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["WORKENV"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_8(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_9(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["XXworkenvXX"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_10(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["WORKENV"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_11(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = None

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_12(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["XXworkenvXX"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_13(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["WORKENV"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_14(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = None

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_15(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "XXopentofu_versionXX" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_16(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "OPENTOFU_VERSION" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_17(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name != "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_18(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "XXtofuXX" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_19(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "TOFU" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_20(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = None
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_21(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["XXworkenvXX"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_22(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["WORKENV"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_23(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(None)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfVersionsManagerǁset_installed_version__mutmut_24(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        # Use 'opentofu_version' for tofu tool
        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(None)
    
    xǁTfVersionsManagerǁset_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁset_installed_version__mutmut_1': xǁTfVersionsManagerǁset_installed_version__mutmut_1, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_2': xǁTfVersionsManagerǁset_installed_version__mutmut_2, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_3': xǁTfVersionsManagerǁset_installed_version__mutmut_3, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_4': xǁTfVersionsManagerǁset_installed_version__mutmut_4, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_5': xǁTfVersionsManagerǁset_installed_version__mutmut_5, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_6': xǁTfVersionsManagerǁset_installed_version__mutmut_6, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_7': xǁTfVersionsManagerǁset_installed_version__mutmut_7, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_8': xǁTfVersionsManagerǁset_installed_version__mutmut_8, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_9': xǁTfVersionsManagerǁset_installed_version__mutmut_9, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_10': xǁTfVersionsManagerǁset_installed_version__mutmut_10, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_11': xǁTfVersionsManagerǁset_installed_version__mutmut_11, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_12': xǁTfVersionsManagerǁset_installed_version__mutmut_12, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_13': xǁTfVersionsManagerǁset_installed_version__mutmut_13, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_14': xǁTfVersionsManagerǁset_installed_version__mutmut_14, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_15': xǁTfVersionsManagerǁset_installed_version__mutmut_15, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_16': xǁTfVersionsManagerǁset_installed_version__mutmut_16, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_17': xǁTfVersionsManagerǁset_installed_version__mutmut_17, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_18': xǁTfVersionsManagerǁset_installed_version__mutmut_18, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_19': xǁTfVersionsManagerǁset_installed_version__mutmut_19, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_20': xǁTfVersionsManagerǁset_installed_version__mutmut_20, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_21': xǁTfVersionsManagerǁset_installed_version__mutmut_21, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_22': xǁTfVersionsManagerǁset_installed_version__mutmut_22, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_23': xǁTfVersionsManagerǁset_installed_version__mutmut_23, 
        'xǁTfVersionsManagerǁset_installed_version__mutmut_24': xǁTfVersionsManagerǁset_installed_version__mutmut_24
    }
    
    def set_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁset_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁset_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_installed_version.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁset_installed_version__mutmut_orig)
    xǁTfVersionsManagerǁset_installed_version__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁset_installed_version'

    def xǁTfVersionsManagerǁremove_version__mutmut_orig(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_1(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = None

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_2(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(None)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_3(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(None)

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_4(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = None
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_5(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key not in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_6(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() != version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_7(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(None, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_8(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, None)
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_9(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version("")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_10(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, )
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_11(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "XXXX")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(f"Could not clear {self.tool_name} version in config")

    def xǁTfVersionsManagerǁremove_version__mutmut_12(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.tool_name} {version}")

            # Update metadata
            version_key = f"{self.tool_prefix}_{version}"
            if version_key in self.metadata:
                del self.metadata[version_key]
                self._save_metadata()

            # Update RECENT file
            self._update_recent_file()

        # Update config if this was the current version
        if self.get_installed_version() == version:
            try:
                self.config.set_tool_version(self.tool_name, "")
            except Exception:
                if logger.is_debug_enabled():
                    logger.debug(None)
    
    xǁTfVersionsManagerǁremove_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁremove_version__mutmut_1': xǁTfVersionsManagerǁremove_version__mutmut_1, 
        'xǁTfVersionsManagerǁremove_version__mutmut_2': xǁTfVersionsManagerǁremove_version__mutmut_2, 
        'xǁTfVersionsManagerǁremove_version__mutmut_3': xǁTfVersionsManagerǁremove_version__mutmut_3, 
        'xǁTfVersionsManagerǁremove_version__mutmut_4': xǁTfVersionsManagerǁremove_version__mutmut_4, 
        'xǁTfVersionsManagerǁremove_version__mutmut_5': xǁTfVersionsManagerǁremove_version__mutmut_5, 
        'xǁTfVersionsManagerǁremove_version__mutmut_6': xǁTfVersionsManagerǁremove_version__mutmut_6, 
        'xǁTfVersionsManagerǁremove_version__mutmut_7': xǁTfVersionsManagerǁremove_version__mutmut_7, 
        'xǁTfVersionsManagerǁremove_version__mutmut_8': xǁTfVersionsManagerǁremove_version__mutmut_8, 
        'xǁTfVersionsManagerǁremove_version__mutmut_9': xǁTfVersionsManagerǁremove_version__mutmut_9, 
        'xǁTfVersionsManagerǁremove_version__mutmut_10': xǁTfVersionsManagerǁremove_version__mutmut_10, 
        'xǁTfVersionsManagerǁremove_version__mutmut_11': xǁTfVersionsManagerǁremove_version__mutmut_11, 
        'xǁTfVersionsManagerǁremove_version__mutmut_12': xǁTfVersionsManagerǁremove_version__mutmut_12
    }
    
    def remove_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁremove_version__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁremove_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    remove_version.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁremove_version__mutmut_orig)
    xǁTfVersionsManagerǁremove_version__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁremove_version'

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_orig(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_1(self, file_path: pathlib.Path, algorithm: str = "XXsha256XX") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_2(self, file_path: pathlib.Path, algorithm: str = "SHA256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_3(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = None
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_4(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(None)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_5(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open(None) as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_6(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("XXrbXX") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_7(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("RB") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_8(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(None, b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_9(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), None):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_10(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_11(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), ):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_12(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: None, b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_13(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(None), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_14(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4097), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_15(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b"XXXX"):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_16(self, file_path: pathlib.Path, algorithm: str = "sha256") -> str:
        """Calculate hash of a file."""
        hash_func = hashlib.new(algorithm)
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(None)
        return hash_func.hexdigest()
    
    xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_1': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_1, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_2': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_2, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_3': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_3, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_4': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_4, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_5': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_5, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_6': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_6, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_7': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_7, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_8': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_8, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_9': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_9, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_10': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_10, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_11': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_11, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_12': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_12, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_13': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_13, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_14': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_14, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_15': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_15, 
        'xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_16': xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_16
    }
    
    def _calculate_file_hash(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _calculate_file_hash.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_orig)
    xǁTfVersionsManagerǁ_calculate_file_hash__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_calculate_file_hash'

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_orig(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_1(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = None
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_2(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir * f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_3(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=None)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_4(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=False)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_5(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(None, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_6(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, None)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_7(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_8(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, )

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_9(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = None
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_10(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name != "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_11(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "XXtofuXX":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_12(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "TOFU":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_13(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = None

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_14(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "XXtofuXX"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_15(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "TOFU"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_16(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = ""
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_17(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(None):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_18(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() or file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_19(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name not in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_20(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = None
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_21(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    return

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_22(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_23(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(None)

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_24(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = None
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_25(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(None)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_26(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(None, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_27(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, None)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_28(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_29(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, )

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_30(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(None)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_31(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(None)

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_32(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = None

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_33(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(None)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_34(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(None, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_35(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, None, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_36(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, None)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_37(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_38(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_39(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, )

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_40(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_41(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(None):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_42(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(None)

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_43(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(None, ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_44(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=None)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_45(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(ignore_errors=True)

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_46(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, )

    def xǁTfVersionsManagerǁ_install_from_archive__mutmut_47(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            binary_name = self.executable_name
            if self.tool_name == "tofu":
                binary_name = "tofu"

            binary_path = None
            for file_path in extract_dir.rglob(f"{binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    binary_name,
                    f"{binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.tool_name} binary not found in archive")

            # Copy to tf versions location
            target_path = self.get_binary_path(version)
            shutil.copy2(binary_path, target_path)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = self._calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            shutil.rmtree(extract_dir, ignore_errors=False)
    
    xǁTfVersionsManagerǁ_install_from_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_install_from_archive__mutmut_1': xǁTfVersionsManagerǁ_install_from_archive__mutmut_1, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_2': xǁTfVersionsManagerǁ_install_from_archive__mutmut_2, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_3': xǁTfVersionsManagerǁ_install_from_archive__mutmut_3, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_4': xǁTfVersionsManagerǁ_install_from_archive__mutmut_4, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_5': xǁTfVersionsManagerǁ_install_from_archive__mutmut_5, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_6': xǁTfVersionsManagerǁ_install_from_archive__mutmut_6, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_7': xǁTfVersionsManagerǁ_install_from_archive__mutmut_7, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_8': xǁTfVersionsManagerǁ_install_from_archive__mutmut_8, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_9': xǁTfVersionsManagerǁ_install_from_archive__mutmut_9, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_10': xǁTfVersionsManagerǁ_install_from_archive__mutmut_10, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_11': xǁTfVersionsManagerǁ_install_from_archive__mutmut_11, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_12': xǁTfVersionsManagerǁ_install_from_archive__mutmut_12, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_13': xǁTfVersionsManagerǁ_install_from_archive__mutmut_13, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_14': xǁTfVersionsManagerǁ_install_from_archive__mutmut_14, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_15': xǁTfVersionsManagerǁ_install_from_archive__mutmut_15, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_16': xǁTfVersionsManagerǁ_install_from_archive__mutmut_16, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_17': xǁTfVersionsManagerǁ_install_from_archive__mutmut_17, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_18': xǁTfVersionsManagerǁ_install_from_archive__mutmut_18, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_19': xǁTfVersionsManagerǁ_install_from_archive__mutmut_19, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_20': xǁTfVersionsManagerǁ_install_from_archive__mutmut_20, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_21': xǁTfVersionsManagerǁ_install_from_archive__mutmut_21, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_22': xǁTfVersionsManagerǁ_install_from_archive__mutmut_22, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_23': xǁTfVersionsManagerǁ_install_from_archive__mutmut_23, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_24': xǁTfVersionsManagerǁ_install_from_archive__mutmut_24, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_25': xǁTfVersionsManagerǁ_install_from_archive__mutmut_25, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_26': xǁTfVersionsManagerǁ_install_from_archive__mutmut_26, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_27': xǁTfVersionsManagerǁ_install_from_archive__mutmut_27, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_28': xǁTfVersionsManagerǁ_install_from_archive__mutmut_28, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_29': xǁTfVersionsManagerǁ_install_from_archive__mutmut_29, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_30': xǁTfVersionsManagerǁ_install_from_archive__mutmut_30, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_31': xǁTfVersionsManagerǁ_install_from_archive__mutmut_31, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_32': xǁTfVersionsManagerǁ_install_from_archive__mutmut_32, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_33': xǁTfVersionsManagerǁ_install_from_archive__mutmut_33, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_34': xǁTfVersionsManagerǁ_install_from_archive__mutmut_34, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_35': xǁTfVersionsManagerǁ_install_from_archive__mutmut_35, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_36': xǁTfVersionsManagerǁ_install_from_archive__mutmut_36, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_37': xǁTfVersionsManagerǁ_install_from_archive__mutmut_37, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_38': xǁTfVersionsManagerǁ_install_from_archive__mutmut_38, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_39': xǁTfVersionsManagerǁ_install_from_archive__mutmut_39, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_40': xǁTfVersionsManagerǁ_install_from_archive__mutmut_40, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_41': xǁTfVersionsManagerǁ_install_from_archive__mutmut_41, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_42': xǁTfVersionsManagerǁ_install_from_archive__mutmut_42, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_43': xǁTfVersionsManagerǁ_install_from_archive__mutmut_43, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_44': xǁTfVersionsManagerǁ_install_from_archive__mutmut_44, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_45': xǁTfVersionsManagerǁ_install_from_archive__mutmut_45, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_46': xǁTfVersionsManagerǁ_install_from_archive__mutmut_46, 
        'xǁTfVersionsManagerǁ_install_from_archive__mutmut_47': xǁTfVersionsManagerǁ_install_from_archive__mutmut_47
    }
    
    def _install_from_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_install_from_archive__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_install_from_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _install_from_archive.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_install_from_archive__mutmut_orig)
    xǁTfVersionsManagerǁ_install_from_archive__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_install_from_archive'

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_orig(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_1(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = None

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_2(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = None
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_3(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(None)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_4(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = None

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_5(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(None)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_6(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = None
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_7(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(None)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_8(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = None

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_9(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 1

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_10(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = None
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_11(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = None
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_12(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(None)

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_13(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(None))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_14(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = None

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_15(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "XXtoolXX": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_16(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "TOOL": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_17(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "XXversionXX": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_18(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "VERSION": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_19(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "XXinstalled_atXX": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_20(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "INSTALLED_AT": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_21(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "XXdownload_urlXX": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_22(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "DOWNLOAD_URL": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_23(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "XXchecksum_urlXX": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_24(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "CHECKSUM_URL": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_25(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "XXarchive_pathXX": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_26(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "ARCHIVE_PATH": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_27(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(None),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_28(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "XXarchive_sizeXX": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_29(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "ARCHIVE_SIZE": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_30(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 1,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_31(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "XXbinary_pathXX": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_32(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "BINARY_PATH": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_33(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(None),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_34(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "XXbinary_sizeXX": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_35(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "BINARY_SIZE": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_36(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "XXbinary_sha256XX": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_37(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "BINARY_SHA256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_38(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "XXsignature_filesXX": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_39(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "SIGNATURE_FILES": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_40(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(None) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_41(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "XXplatformXX": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_42(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "PLATFORM": self.get_platform_info(),
            "wrknv_version": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_43(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "XXwrknv_versionXX": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_44(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "WRKNV_VERSION": "0.3.0",  # Track which version of wrknv installed this
        }

        self._save_metadata()

    def xǁTfVersionsManagerǁ_update_install_metadata__mutmut_45(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
        """Update metadata for installed version with comprehensive information."""
        version_key = f"{self.tool_prefix}_{version}"

        # Get download URL for source tracking
        download_url = self.get_download_url(version)
        checksum_url = self.get_checksum_url(version)

        # Get file size
        binary_path = self.get_binary_path(version)
        file_size = binary_path.stat().st_size if binary_path.exists() else 0

        # Look for signature files
        sig_patterns = [
            f"{self.tool_prefix}_*.asc",
            f"{self.tool_prefix}_*SHA256SUMS.sig",
            f"{self.tool_name}_*.asc",
        ]
        signature_files = []
        for pattern in sig_patterns:
            signature_files.extend(self.install_path.glob(pattern))

        self.metadata[version_key] = {
            "tool": self.tool_name,
            "version": version,
            "installed_at": datetime.now().isoformat(),
            "download_url": download_url,
            "checksum_url": checksum_url if checksum_url else None,
            "archive_path": str(archive_path),
            "archive_size": archive_path.stat().st_size if archive_path.exists() else 0,
            "binary_path": str(binary_path),
            "binary_size": file_size,
            "binary_sha256": binary_hash,
            "signature_files": [str(f) for f in signature_files],
            "platform": self.get_platform_info(),
            "wrknv_version": "XX0.3.0XX",  # Track which version of wrknv installed this
        }

        self._save_metadata()
    
    xǁTfVersionsManagerǁ_update_install_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_1': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_1, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_2': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_2, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_3': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_3, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_4': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_4, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_5': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_5, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_6': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_6, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_7': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_7, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_8': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_8, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_9': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_9, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_10': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_10, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_11': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_11, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_12': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_12, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_13': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_13, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_14': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_14, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_15': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_15, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_16': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_16, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_17': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_17, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_18': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_18, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_19': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_19, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_20': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_20, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_21': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_21, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_22': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_22, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_23': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_23, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_24': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_24, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_25': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_25, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_26': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_26, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_27': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_27, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_28': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_28, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_29': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_29, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_30': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_30, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_31': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_31, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_32': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_32, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_33': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_33, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_34': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_34, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_35': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_35, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_36': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_36, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_37': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_37, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_38': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_38, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_39': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_39, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_40': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_40, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_41': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_41, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_42': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_42, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_43': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_43, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_44': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_44, 
        'xǁTfVersionsManagerǁ_update_install_metadata__mutmut_45': xǁTfVersionsManagerǁ_update_install_metadata__mutmut_45
    }
    
    def _update_install_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_update_install_metadata__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_update_install_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_install_metadata.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_update_install_metadata__mutmut_orig)
    xǁTfVersionsManagerǁ_update_install_metadata__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_update_install_metadata'

    def xǁTfVersionsManagerǁcreate_symlink__mutmut_orig(self, version: str) -> None:
        """Copy active tf binaries to venv bin directory for direct access.

        This replaces symlinks with a copy strategy that works on all platforms
        including Windows. The active binaries are copied to the venv's bin
        directory where they can be executed directly.
        """
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping activation")
            return

        # Track the active version in metadata first
        self.set_installed_version(version)

        # Copy all active tf binaries to venv bin directory
        self._copy_active_binaries_to_venv()

        logger.info(f"Copied {self.tool_name} {version} to venv bin directory")

    def xǁTfVersionsManagerǁcreate_symlink__mutmut_1(self, version: str) -> None:
        """Copy active tf binaries to venv bin directory for direct access.

        This replaces symlinks with a copy strategy that works on all platforms
        including Windows. The active binaries are copied to the venv's bin
        directory where they can be executed directly.
        """
        binary_path = None
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping activation")
            return

        # Track the active version in metadata first
        self.set_installed_version(version)

        # Copy all active tf binaries to venv bin directory
        self._copy_active_binaries_to_venv()

        logger.info(f"Copied {self.tool_name} {version} to venv bin directory")

    def xǁTfVersionsManagerǁcreate_symlink__mutmut_2(self, version: str) -> None:
        """Copy active tf binaries to venv bin directory for direct access.

        This replaces symlinks with a copy strategy that works on all platforms
        including Windows. The active binaries are copied to the venv's bin
        directory where they can be executed directly.
        """
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping activation")
            return

        # Track the active version in metadata first
        self.set_installed_version(version)

        # Copy all active tf binaries to venv bin directory
        self._copy_active_binaries_to_venv()

        logger.info(f"Copied {self.tool_name} {version} to venv bin directory")

    def xǁTfVersionsManagerǁcreate_symlink__mutmut_3(self, version: str) -> None:
        """Copy active tf binaries to venv bin directory for direct access.

        This replaces symlinks with a copy strategy that works on all platforms
        including Windows. The active binaries are copied to the venv's bin
        directory where they can be executed directly.
        """
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping activation")
            return

        # Track the active version in metadata first
        self.set_installed_version(version)

        # Copy all active tf binaries to venv bin directory
        self._copy_active_binaries_to_venv()

        logger.info(f"Copied {self.tool_name} {version} to venv bin directory")

    def xǁTfVersionsManagerǁcreate_symlink__mutmut_4(self, version: str) -> None:
        """Copy active tf binaries to venv bin directory for direct access.

        This replaces symlinks with a copy strategy that works on all platforms
        including Windows. The active binaries are copied to the venv's bin
        directory where they can be executed directly.
        """
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(None)
            return

        # Track the active version in metadata first
        self.set_installed_version(version)

        # Copy all active tf binaries to venv bin directory
        self._copy_active_binaries_to_venv()

        logger.info(f"Copied {self.tool_name} {version} to venv bin directory")

    def xǁTfVersionsManagerǁcreate_symlink__mutmut_5(self, version: str) -> None:
        """Copy active tf binaries to venv bin directory for direct access.

        This replaces symlinks with a copy strategy that works on all platforms
        including Windows. The active binaries are copied to the venv's bin
        directory where they can be executed directly.
        """
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping activation")
            return

        # Track the active version in metadata first
        self.set_installed_version(None)

        # Copy all active tf binaries to venv bin directory
        self._copy_active_binaries_to_venv()

        logger.info(f"Copied {self.tool_name} {version} to venv bin directory")

    def xǁTfVersionsManagerǁcreate_symlink__mutmut_6(self, version: str) -> None:
        """Copy active tf binaries to venv bin directory for direct access.

        This replaces symlinks with a copy strategy that works on all platforms
        including Windows. The active binaries are copied to the venv's bin
        directory where they can be executed directly.
        """
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, skipping activation")
            return

        # Track the active version in metadata first
        self.set_installed_version(version)

        # Copy all active tf binaries to venv bin directory
        self._copy_active_binaries_to_venv()

        logger.info(None)
    
    xǁTfVersionsManagerǁcreate_symlink__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁcreate_symlink__mutmut_1': xǁTfVersionsManagerǁcreate_symlink__mutmut_1, 
        'xǁTfVersionsManagerǁcreate_symlink__mutmut_2': xǁTfVersionsManagerǁcreate_symlink__mutmut_2, 
        'xǁTfVersionsManagerǁcreate_symlink__mutmut_3': xǁTfVersionsManagerǁcreate_symlink__mutmut_3, 
        'xǁTfVersionsManagerǁcreate_symlink__mutmut_4': xǁTfVersionsManagerǁcreate_symlink__mutmut_4, 
        'xǁTfVersionsManagerǁcreate_symlink__mutmut_5': xǁTfVersionsManagerǁcreate_symlink__mutmut_5, 
        'xǁTfVersionsManagerǁcreate_symlink__mutmut_6': xǁTfVersionsManagerǁcreate_symlink__mutmut_6
    }
    
    def create_symlink(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁcreate_symlink__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁcreate_symlink__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_symlink.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁcreate_symlink__mutmut_orig)
    xǁTfVersionsManagerǁcreate_symlink__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁcreate_symlink'

    def xǁTfVersionsManagerǁset_global_version__mutmut_orig(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_1(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = None
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_2(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_3(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_4(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(None)
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_5(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = None
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_6(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" * "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_7(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() * ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_8(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / "XX.localXX" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_9(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".LOCAL" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_10(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "XXbinXX"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_11(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "BIN"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_12(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=None, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_13(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=None)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_14(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_15(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, )

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_16(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=False, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_17(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=False)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_18(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = None

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_19(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "XXtofuXX" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_20(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "TOFU" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_21(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name != "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_22(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "XXtofuXX" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_23(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "TOFU" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_24(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "XXterraformXX"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_25(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "TERRAFORM"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_26(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name != "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_27(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "XXntXX":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_28(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "NT":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_29(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name = ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_30(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name -= ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_31(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += "XX.exeXX"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_32(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".EXE"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_33(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = None

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_34(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir * target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_35(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(None, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_36(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, None)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_37(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_38(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, )

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_39(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name == "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_40(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "XXntXX":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_41(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "NT":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_42(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(None)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_43(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(494)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_44(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "XXglobalXX" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_45(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "GLOBAL" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_46(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_47(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_48(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["XXglobalXX"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_49(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["GLOBAL"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_50(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = None

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_51(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "XXopentofu_versionXX" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_52(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "OPENTOFU_VERSION" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_53(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name != "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_54(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "XXtofuXX" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_55(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "TOFU" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_56(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = None
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_57(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["XXglobalXX"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_58(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["GLOBAL"][tool_key] = version
        self._save_metadata()

        logger.info(f"Set {self.tool_name} {version} as global system version at {target_path}")

    def xǁTfVersionsManagerǁset_global_version__mutmut_59(self, version: str) -> None:
        """Set a version as the global system version by copying to ~/.local/bin/."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot set global version")
            return

        # Ensure ~/.local/bin directory exists
        local_bin_dir = pathlib.Path.home() / ".local" / "bin"
        local_bin_dir.mkdir(parents=True, exist_ok=True)

        # Determine target executable name
        target_name = "tofu" if self.tool_name == "tofu" else "terraform"

        if os.name == "nt":  # Windows
            target_name += ".exe"

        target_path = local_bin_dir / target_name

        # Copy the binary to ~/.local/bin
        shutil.copy2(binary_path, target_path)

        # Make executable on Unix systems
        if os.name != "nt":
            target_path.chmod(0o755)

        # Update metadata to track global version
        if "global" not in self.metadata:
            self.metadata["global"] = {}

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        self.metadata["global"][tool_key] = version
        self._save_metadata()

        logger.info(None)
    
    xǁTfVersionsManagerǁset_global_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁset_global_version__mutmut_1': xǁTfVersionsManagerǁset_global_version__mutmut_1, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_2': xǁTfVersionsManagerǁset_global_version__mutmut_2, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_3': xǁTfVersionsManagerǁset_global_version__mutmut_3, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_4': xǁTfVersionsManagerǁset_global_version__mutmut_4, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_5': xǁTfVersionsManagerǁset_global_version__mutmut_5, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_6': xǁTfVersionsManagerǁset_global_version__mutmut_6, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_7': xǁTfVersionsManagerǁset_global_version__mutmut_7, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_8': xǁTfVersionsManagerǁset_global_version__mutmut_8, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_9': xǁTfVersionsManagerǁset_global_version__mutmut_9, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_10': xǁTfVersionsManagerǁset_global_version__mutmut_10, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_11': xǁTfVersionsManagerǁset_global_version__mutmut_11, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_12': xǁTfVersionsManagerǁset_global_version__mutmut_12, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_13': xǁTfVersionsManagerǁset_global_version__mutmut_13, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_14': xǁTfVersionsManagerǁset_global_version__mutmut_14, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_15': xǁTfVersionsManagerǁset_global_version__mutmut_15, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_16': xǁTfVersionsManagerǁset_global_version__mutmut_16, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_17': xǁTfVersionsManagerǁset_global_version__mutmut_17, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_18': xǁTfVersionsManagerǁset_global_version__mutmut_18, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_19': xǁTfVersionsManagerǁset_global_version__mutmut_19, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_20': xǁTfVersionsManagerǁset_global_version__mutmut_20, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_21': xǁTfVersionsManagerǁset_global_version__mutmut_21, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_22': xǁTfVersionsManagerǁset_global_version__mutmut_22, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_23': xǁTfVersionsManagerǁset_global_version__mutmut_23, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_24': xǁTfVersionsManagerǁset_global_version__mutmut_24, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_25': xǁTfVersionsManagerǁset_global_version__mutmut_25, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_26': xǁTfVersionsManagerǁset_global_version__mutmut_26, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_27': xǁTfVersionsManagerǁset_global_version__mutmut_27, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_28': xǁTfVersionsManagerǁset_global_version__mutmut_28, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_29': xǁTfVersionsManagerǁset_global_version__mutmut_29, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_30': xǁTfVersionsManagerǁset_global_version__mutmut_30, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_31': xǁTfVersionsManagerǁset_global_version__mutmut_31, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_32': xǁTfVersionsManagerǁset_global_version__mutmut_32, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_33': xǁTfVersionsManagerǁset_global_version__mutmut_33, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_34': xǁTfVersionsManagerǁset_global_version__mutmut_34, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_35': xǁTfVersionsManagerǁset_global_version__mutmut_35, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_36': xǁTfVersionsManagerǁset_global_version__mutmut_36, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_37': xǁTfVersionsManagerǁset_global_version__mutmut_37, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_38': xǁTfVersionsManagerǁset_global_version__mutmut_38, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_39': xǁTfVersionsManagerǁset_global_version__mutmut_39, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_40': xǁTfVersionsManagerǁset_global_version__mutmut_40, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_41': xǁTfVersionsManagerǁset_global_version__mutmut_41, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_42': xǁTfVersionsManagerǁset_global_version__mutmut_42, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_43': xǁTfVersionsManagerǁset_global_version__mutmut_43, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_44': xǁTfVersionsManagerǁset_global_version__mutmut_44, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_45': xǁTfVersionsManagerǁset_global_version__mutmut_45, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_46': xǁTfVersionsManagerǁset_global_version__mutmut_46, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_47': xǁTfVersionsManagerǁset_global_version__mutmut_47, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_48': xǁTfVersionsManagerǁset_global_version__mutmut_48, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_49': xǁTfVersionsManagerǁset_global_version__mutmut_49, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_50': xǁTfVersionsManagerǁset_global_version__mutmut_50, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_51': xǁTfVersionsManagerǁset_global_version__mutmut_51, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_52': xǁTfVersionsManagerǁset_global_version__mutmut_52, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_53': xǁTfVersionsManagerǁset_global_version__mutmut_53, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_54': xǁTfVersionsManagerǁset_global_version__mutmut_54, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_55': xǁTfVersionsManagerǁset_global_version__mutmut_55, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_56': xǁTfVersionsManagerǁset_global_version__mutmut_56, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_57': xǁTfVersionsManagerǁset_global_version__mutmut_57, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_58': xǁTfVersionsManagerǁset_global_version__mutmut_58, 
        'xǁTfVersionsManagerǁset_global_version__mutmut_59': xǁTfVersionsManagerǁset_global_version__mutmut_59
    }
    
    def set_global_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁset_global_version__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁset_global_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_global_version.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁset_global_version__mutmut_orig)
    xǁTfVersionsManagerǁset_global_version__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁset_global_version'

    def xǁTfVersionsManagerǁget_global_version__mutmut_orig(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_1(self) -> str | None:
        """Get the currently set global version."""
        if "XXglobalXX" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_2(self) -> str | None:
        """Get the currently set global version."""
        if "GLOBAL" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_3(self) -> str | None:
        """Get the currently set global version."""
        if "global" in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_4(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = None

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_5(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "XXopentofu_versionXX" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_6(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "OPENTOFU_VERSION" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_7(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name != "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_8(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "XXtofuXX" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_9(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "TOFU" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_10(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(None)

    def xǁTfVersionsManagerǁget_global_version__mutmut_11(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["XXglobalXX"].get(tool_key)

    def xǁTfVersionsManagerǁget_global_version__mutmut_12(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["GLOBAL"].get(tool_key)
    
    xǁTfVersionsManagerǁget_global_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁget_global_version__mutmut_1': xǁTfVersionsManagerǁget_global_version__mutmut_1, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_2': xǁTfVersionsManagerǁget_global_version__mutmut_2, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_3': xǁTfVersionsManagerǁget_global_version__mutmut_3, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_4': xǁTfVersionsManagerǁget_global_version__mutmut_4, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_5': xǁTfVersionsManagerǁget_global_version__mutmut_5, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_6': xǁTfVersionsManagerǁget_global_version__mutmut_6, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_7': xǁTfVersionsManagerǁget_global_version__mutmut_7, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_8': xǁTfVersionsManagerǁget_global_version__mutmut_8, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_9': xǁTfVersionsManagerǁget_global_version__mutmut_9, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_10': xǁTfVersionsManagerǁget_global_version__mutmut_10, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_11': xǁTfVersionsManagerǁget_global_version__mutmut_11, 
        'xǁTfVersionsManagerǁget_global_version__mutmut_12': xǁTfVersionsManagerǁget_global_version__mutmut_12
    }
    
    def get_global_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁget_global_version__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁget_global_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_global_version.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁget_global_version__mutmut_orig)
    xǁTfVersionsManagerǁget_global_version__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁget_global_version'

    def xǁTfVersionsManagerǁget_metadata_for_version__mutmut_orig(self, version: str) -> dict | None:
        """Get metadata for a specific version."""
        version_key = f"{self.tool_prefix}_{version}"
        return self.metadata.get(version_key)

    def xǁTfVersionsManagerǁget_metadata_for_version__mutmut_1(self, version: str) -> dict | None:
        """Get metadata for a specific version."""
        version_key = None
        return self.metadata.get(version_key)

    def xǁTfVersionsManagerǁget_metadata_for_version__mutmut_2(self, version: str) -> dict | None:
        """Get metadata for a specific version."""
        version_key = f"{self.tool_prefix}_{version}"
        return self.metadata.get(None)
    
    xǁTfVersionsManagerǁget_metadata_for_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁget_metadata_for_version__mutmut_1': xǁTfVersionsManagerǁget_metadata_for_version__mutmut_1, 
        'xǁTfVersionsManagerǁget_metadata_for_version__mutmut_2': xǁTfVersionsManagerǁget_metadata_for_version__mutmut_2
    }
    
    def get_metadata_for_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁget_metadata_for_version__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁget_metadata_for_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_metadata_for_version.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁget_metadata_for_version__mutmut_orig)
    xǁTfVersionsManagerǁget_metadata_for_version__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁget_metadata_for_version'

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_orig(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_1(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = None
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_2(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = None
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_3(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(None)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_4(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = None
                info["is_active"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_5(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(None)
                info["is_active"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_6(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = None
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_7(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["XXis_activeXX"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_8(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["IS_ACTIVE"] = True
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_9(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = False
                info["binary_exists"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_10(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = True
                info["binary_exists"] = None
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_11(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = True
                info["XXbinary_existsXX"] = binary_path.exists()
                return info
        return None

    def xǁTfVersionsManagerǁget_active_version_info__mutmut_12(self) -> dict | None:
        """Get detailed information about the currently active version."""
        version = self.get_installed_version()
        if version:
            info = self.get_metadata_for_version(version)
            if info:
                # Add current status
                binary_path = self.get_binary_path(version)
                info["is_active"] = True
                info["BINARY_EXISTS"] = binary_path.exists()
                return info
        return None
    
    xǁTfVersionsManagerǁget_active_version_info__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁget_active_version_info__mutmut_1': xǁTfVersionsManagerǁget_active_version_info__mutmut_1, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_2': xǁTfVersionsManagerǁget_active_version_info__mutmut_2, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_3': xǁTfVersionsManagerǁget_active_version_info__mutmut_3, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_4': xǁTfVersionsManagerǁget_active_version_info__mutmut_4, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_5': xǁTfVersionsManagerǁget_active_version_info__mutmut_5, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_6': xǁTfVersionsManagerǁget_active_version_info__mutmut_6, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_7': xǁTfVersionsManagerǁget_active_version_info__mutmut_7, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_8': xǁTfVersionsManagerǁget_active_version_info__mutmut_8, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_9': xǁTfVersionsManagerǁget_active_version_info__mutmut_9, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_10': xǁTfVersionsManagerǁget_active_version_info__mutmut_10, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_11': xǁTfVersionsManagerǁget_active_version_info__mutmut_11, 
        'xǁTfVersionsManagerǁget_active_version_info__mutmut_12': xǁTfVersionsManagerǁget_active_version_info__mutmut_12
    }
    
    def get_active_version_info(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁget_active_version_info__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁget_active_version_info__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_active_version_info.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁget_active_version_info__mutmut_orig)
    xǁTfVersionsManagerǁget_active_version_info__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁget_active_version_info'

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_orig(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_1(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = None
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_2(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get(None)
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_3(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("XXWRKENV_PROFILEXX")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_4(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("wrkenv_profile")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_5(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata or "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_6(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "XXworkenvXX" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_7(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "WORKENV" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_8(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" not in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_9(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "XX_current_profileXX" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_10(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_CURRENT_PROFILE" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_11(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" not in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_12(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["XXworkenvXX"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_13(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["WORKENV"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_14(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["XXworkenvXX"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_15(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["WORKENV"]["_current_profile"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_16(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["XX_current_profileXX"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_17(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_CURRENT_PROFILE"]

        # Default to 'default' profile
        return "default"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_18(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "XXdefaultXX"

    def xǁTfVersionsManagerǁ_get_current_profile__mutmut_19(self) -> str:
        """Get the current workenv profile name."""
        # Check environment variable first
        profile = os.environ.get("WRKENV_PROFILE")
        if profile:
            return profile

        # Check metadata for current profile setting
        if "workenv" in self.metadata and "_current_profile" in self.metadata["workenv"]:
            return self.metadata["workenv"]["_current_profile"]

        # Default to 'default' profile
        return "DEFAULT"
    
    xǁTfVersionsManagerǁ_get_current_profile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_get_current_profile__mutmut_1': xǁTfVersionsManagerǁ_get_current_profile__mutmut_1, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_2': xǁTfVersionsManagerǁ_get_current_profile__mutmut_2, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_3': xǁTfVersionsManagerǁ_get_current_profile__mutmut_3, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_4': xǁTfVersionsManagerǁ_get_current_profile__mutmut_4, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_5': xǁTfVersionsManagerǁ_get_current_profile__mutmut_5, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_6': xǁTfVersionsManagerǁ_get_current_profile__mutmut_6, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_7': xǁTfVersionsManagerǁ_get_current_profile__mutmut_7, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_8': xǁTfVersionsManagerǁ_get_current_profile__mutmut_8, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_9': xǁTfVersionsManagerǁ_get_current_profile__mutmut_9, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_10': xǁTfVersionsManagerǁ_get_current_profile__mutmut_10, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_11': xǁTfVersionsManagerǁ_get_current_profile__mutmut_11, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_12': xǁTfVersionsManagerǁ_get_current_profile__mutmut_12, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_13': xǁTfVersionsManagerǁ_get_current_profile__mutmut_13, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_14': xǁTfVersionsManagerǁ_get_current_profile__mutmut_14, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_15': xǁTfVersionsManagerǁ_get_current_profile__mutmut_15, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_16': xǁTfVersionsManagerǁ_get_current_profile__mutmut_16, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_17': xǁTfVersionsManagerǁ_get_current_profile__mutmut_17, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_18': xǁTfVersionsManagerǁ_get_current_profile__mutmut_18, 
        'xǁTfVersionsManagerǁ_get_current_profile__mutmut_19': xǁTfVersionsManagerǁ_get_current_profile__mutmut_19
    }
    
    def _get_current_profile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_get_current_profile__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_get_current_profile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_current_profile.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_get_current_profile__mutmut_orig)
    xǁTfVersionsManagerǁ_get_current_profile__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_get_current_profile'

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_orig(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_1(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") and (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_2(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(None, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_3(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, None) or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_4(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr("real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_5(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, ) or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_6(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "XXreal_prefixXX") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_7(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "REAL_PREFIX") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_8(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") or sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_9(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(None, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_10(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, None) and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_11(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr("base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_12(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, ) and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_13(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "XXbase_prefixXX") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_14(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "BASE_PREFIX") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_15(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix == sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_16(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = None

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_17(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(None)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_18(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "XXworkenvXX" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_19(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "WORKENV" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_20(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" not in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_21(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(None):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_22(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = None
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_23(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path * "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_24(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "XXScriptsXX" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_25(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_26(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "SCRIPTS" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_27(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name != "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_28(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "XXntXX" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_29(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "NT" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_30(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path * "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_31(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "XXbinXX"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_32(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "BIN"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_33(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = None
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_34(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path * "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_35(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "XXScriptsXX" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_36(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_37(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "SCRIPTS" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_38(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name != "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_39(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "XXntXX" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_40(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "NT" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_41(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path * "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_42(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "XXbinXX"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_43(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "BIN"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_44(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = None
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_45(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = None
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_46(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = None
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_47(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name * "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_48(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root * workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_49(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "XXbinXX"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_50(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "BIN"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_51(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = None

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_52(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" * "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_53(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() * ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_54(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / "XX.localXX" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_55(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".LOCAL" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_56(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "XXbinXX"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_57(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "BIN"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_58(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=None, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_59(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=None)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_60(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_61(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, )
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_62(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=False, exist_ok=True)
        return bin_dir

    def xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_63(self) -> pathlib.Path:
        """Get the current virtual environment's bin directory."""
        # First check if we're in a virtual environment
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            # We're in a virtual environment
            venv_path = pathlib.Path(sys.prefix)

            # Check if this is a wrknv (has 'workenv' in the path)
            if "workenv" in str(venv_path):
                # Use the workenv structure
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
            else:
                # Regular venv
                bin_dir = venv_path / "Scripts" if os.name == "nt" else venv_path / "bin"
        else:
            # Not in a venv, check for workenv directory relative to project root
            project_root = self._find_project_root()
            if project_root:
                workenv_dir_name = self.config.get_workenv_dir_name()
                bin_dir = project_root / workenv_dir_name / "bin"
                if bin_dir.exists():
                    return bin_dir

            # Fallback to .local/bin
            bin_dir = pathlib.Path.home() / ".local" / "bin"

        # Ensure directory exists
        bin_dir.mkdir(parents=True, exist_ok=False)
        return bin_dir
    
    xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_1': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_1, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_2': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_2, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_3': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_3, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_4': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_4, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_5': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_5, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_6': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_6, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_7': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_7, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_8': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_8, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_9': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_9, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_10': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_10, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_11': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_11, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_12': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_12, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_13': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_13, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_14': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_14, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_15': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_15, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_16': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_16, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_17': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_17, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_18': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_18, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_19': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_19, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_20': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_20, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_21': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_21, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_22': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_22, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_23': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_23, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_24': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_24, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_25': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_25, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_26': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_26, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_27': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_27, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_28': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_28, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_29': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_29, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_30': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_30, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_31': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_31, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_32': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_32, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_33': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_33, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_34': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_34, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_35': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_35, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_36': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_36, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_37': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_37, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_38': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_38, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_39': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_39, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_40': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_40, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_41': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_41, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_42': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_42, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_43': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_43, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_44': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_44, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_45': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_45, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_46': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_46, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_47': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_47, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_48': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_48, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_49': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_49, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_50': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_50, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_51': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_51, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_52': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_52, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_53': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_53, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_54': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_54, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_55': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_55, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_56': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_56, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_57': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_57, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_58': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_58, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_59': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_59, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_60': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_60, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_61': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_61, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_62': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_62, 
        'xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_63': xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_63
    }
    
    def _get_venv_bin_dir(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_venv_bin_dir.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_orig)
    xǁTfVersionsManagerǁ_get_venv_bin_dir__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_get_venv_bin_dir'

    def xǁTfVersionsManagerǁ_find_project_root__mutmut_orig(self) -> pathlib.Path | None:
        """Find the project root by looking for pyproject.toml."""
        current = pathlib.Path.cwd()

        while current != current.parent:
            if (current / "pyproject.toml").exists():
                return current
            current = current.parent

        return None

    def xǁTfVersionsManagerǁ_find_project_root__mutmut_1(self) -> pathlib.Path | None:
        """Find the project root by looking for pyproject.toml."""
        current = None

        while current != current.parent:
            if (current / "pyproject.toml").exists():
                return current
            current = current.parent

        return None

    def xǁTfVersionsManagerǁ_find_project_root__mutmut_2(self) -> pathlib.Path | None:
        """Find the project root by looking for pyproject.toml."""
        current = pathlib.Path.cwd()

        while current == current.parent:
            if (current / "pyproject.toml").exists():
                return current
            current = current.parent

        return None

    def xǁTfVersionsManagerǁ_find_project_root__mutmut_3(self) -> pathlib.Path | None:
        """Find the project root by looking for pyproject.toml."""
        current = pathlib.Path.cwd()

        while current != current.parent:
            if (current * "pyproject.toml").exists():
                return current
            current = current.parent

        return None

    def xǁTfVersionsManagerǁ_find_project_root__mutmut_4(self) -> pathlib.Path | None:
        """Find the project root by looking for pyproject.toml."""
        current = pathlib.Path.cwd()

        while current != current.parent:
            if (current / "XXpyproject.tomlXX").exists():
                return current
            current = current.parent

        return None

    def xǁTfVersionsManagerǁ_find_project_root__mutmut_5(self) -> pathlib.Path | None:
        """Find the project root by looking for pyproject.toml."""
        current = pathlib.Path.cwd()

        while current != current.parent:
            if (current / "PYPROJECT.TOML").exists():
                return current
            current = current.parent

        return None

    def xǁTfVersionsManagerǁ_find_project_root__mutmut_6(self) -> pathlib.Path | None:
        """Find the project root by looking for pyproject.toml."""
        current = pathlib.Path.cwd()

        while current != current.parent:
            if (current / "pyproject.toml").exists():
                return current
            current = None

        return None
    
    xǁTfVersionsManagerǁ_find_project_root__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_find_project_root__mutmut_1': xǁTfVersionsManagerǁ_find_project_root__mutmut_1, 
        'xǁTfVersionsManagerǁ_find_project_root__mutmut_2': xǁTfVersionsManagerǁ_find_project_root__mutmut_2, 
        'xǁTfVersionsManagerǁ_find_project_root__mutmut_3': xǁTfVersionsManagerǁ_find_project_root__mutmut_3, 
        'xǁTfVersionsManagerǁ_find_project_root__mutmut_4': xǁTfVersionsManagerǁ_find_project_root__mutmut_4, 
        'xǁTfVersionsManagerǁ_find_project_root__mutmut_5': xǁTfVersionsManagerǁ_find_project_root__mutmut_5, 
        'xǁTfVersionsManagerǁ_find_project_root__mutmut_6': xǁTfVersionsManagerǁ_find_project_root__mutmut_6
    }
    
    def _find_project_root(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_find_project_root__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_find_project_root__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _find_project_root.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_find_project_root__mutmut_orig)
    xǁTfVersionsManagerǁ_find_project_root__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_find_project_root'

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_orig(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_1(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_2(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning(None)
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_3(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("XXNo venv bin directory available for tf binary copyingXX")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_4(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("no venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_5(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("NO VENV BIN DIRECTORY AVAILABLE FOR TF BINARY COPYING")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_6(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["XXtofuXX", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_7(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["TOFU", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_8(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "XXterraformXX"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_9(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "TERRAFORM"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_10(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name != "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_11(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "XXtofuXX":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_12(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "TOFU":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_13(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = None
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_14(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(None)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_15(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = None

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_16(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(None)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_17(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = None
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_18(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = None
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_19(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(None)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_20(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = None

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_21(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "XXhctfXX" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_22(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "HCTF" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_23(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name != "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_24(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "XXterraformXX" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_25(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "TERRAFORM" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_26(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "XXtofuXX"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_27(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "TOFU"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_28(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name != "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_29(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "XXntXX":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_30(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "NT":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_31(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name = ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_32(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name -= ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_33(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += "XX.exeXX"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_34(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".EXE"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_35(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = None

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_36(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir * target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_37(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(None, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_38(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, None)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_39(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_40(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, )

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_41(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name == "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_42(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "XXntXX":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_43(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "NT":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_44(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(None)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_45(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(494)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_46(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(None)

            except Exception as e:
                logger.warning(f"Failed to copy {tool_name} binary: {e}")

    def xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_47(self) -> None:
        """Copy all active tf binaries to venv bin directory."""
        if not self.venv_bin_dir:
            logger.warning("No venv bin directory available for tf binary copying")
            return

        # Get active versions for both tools
        for tool_name in ["tofu", "terraform"]:
            try:
                # Create a temporary manager instance to get active version
                if tool_name == "tofu":
                    from .tofu import TofuManager

                    temp_manager = TofuManager(self.config)
                else:
                    from .terraform import TerraformManager

                    temp_manager = TerraformManager(self.config)

                active_version = temp_manager.get_installed_version()
                if active_version:
                    source_path = temp_manager.get_binary_path(active_version)
                    if source_path.exists():
                        # Terraform is copied as 'hctf', OpenTofu stays as 'tofu'
                        target_name = "hctf" if tool_name == "terraform" else "tofu"

                        if os.name == "nt":  # Windows
                            target_name += ".exe"

                        target_path = self.venv_bin_dir / target_name

                        # Copy the binary
                        shutil.copy2(source_path, target_path)

                        # Make executable on Unix systems
                        if os.name != "nt":
                            target_path.chmod(0o755)

                        if logger.is_debug_enabled():
                            logger.debug(f"Copied {tool_name} {active_version} to {target_path}")

            except Exception as e:
                logger.warning(None)
    
    xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_1': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_1, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_2': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_2, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_3': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_3, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_4': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_4, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_5': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_5, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_6': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_6, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_7': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_7, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_8': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_8, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_9': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_9, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_10': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_10, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_11': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_11, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_12': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_12, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_13': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_13, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_14': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_14, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_15': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_15, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_16': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_16, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_17': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_17, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_18': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_18, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_19': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_19, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_20': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_20, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_21': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_21, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_22': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_22, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_23': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_23, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_24': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_24, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_25': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_25, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_26': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_26, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_27': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_27, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_28': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_28, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_29': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_29, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_30': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_30, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_31': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_31, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_32': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_32, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_33': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_33, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_34': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_34, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_35': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_35, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_36': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_36, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_37': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_37, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_38': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_38, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_39': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_39, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_40': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_40, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_41': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_41, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_42': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_42, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_43': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_43, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_44': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_44, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_45': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_45, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_46': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_46, 
        'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_47': xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_47
    }
    
    def _copy_active_binaries_to_venv(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_orig"), object.__getattribute__(self, "xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _copy_active_binaries_to_venv.__signature__ = _mutmut_signature(xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_orig)
    xǁTfVersionsManagerǁ_copy_active_binaries_to_venv__mutmut_orig.__name__ = 'xǁTfVersionsManagerǁ_copy_active_binaries_to_venv'


# 🍲🥄📄🪄
