#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tf Manager Base
===============
Base class for Tf (IBM Terraform/OpenTofu) managers that use ~/.terraform.versions
directory structure. This implementation is compatible with tfswitch and
designed for managing Tf tool versions."""

from __future__ import annotations

from abc import abstractmethod
import os
import pathlib
from typing import TYPE_CHECKING

from provide.foundation import logger
from provide.foundation.file import safe_copy, safe_delete, safe_rmtree
from provide.foundation.time import provide_now

from wrknv.managers.base import BaseToolManager, ToolManagerError
from wrknv.managers.tf.bin_ops import copy_tf_binaries_to_workenv
from wrknv.managers.tf.metadata import TfMetadataManager
from wrknv.managers.tf.utils import (
    calculate_file_hash,
    get_tool_version_key,
    version_sort_key,
)
from wrknv.wenv.bin_manager import get_workenv_bin_dir

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


class TfManager(BaseToolManager):
    """
    Base class for Tf tool managers using ~/.terraform.versions directory.

    This directory structure is compatible with tfswitch, allowing users to
    use either tool interchangeably while providing enhanced metadata tracking
    for advanced features. Supports both IBM Terraform (formerly HashiCorp) and OpenTofu.
    """

    def xǁTfManagerǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(None)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = None
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_3(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path(None).expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_4(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("XX~/.terraform.versionsXX").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_5(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.TERRAFORM.VERSIONS").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_6(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=None, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_7(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=None)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_8(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_9(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, )

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_10(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=False, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_11(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=False)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_12(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = None

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_13(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(None)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_14(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = None
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_15(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(None, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_16(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, None)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_17(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_18(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, )
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_19(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = None
        self.metadata_file = self.metadata_manager.metadata_file

    def xǁTfManagerǁ__init____mutmut_20(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)
        # Override install path to use tf versions directory
        self.install_path = pathlib.Path("~/.terraform.versions").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for copying active binaries
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata manager
        self.metadata_manager = TfMetadataManager(self.install_path, self.tool_name)
        self.metadata_manager.load_metadata()

        # Expose metadata for backward compatibility
        self.metadata = self.metadata_manager.metadata
        self.metadata_file = None
    
    xǁTfManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁ__init____mutmut_1': xǁTfManagerǁ__init____mutmut_1, 
        'xǁTfManagerǁ__init____mutmut_2': xǁTfManagerǁ__init____mutmut_2, 
        'xǁTfManagerǁ__init____mutmut_3': xǁTfManagerǁ__init____mutmut_3, 
        'xǁTfManagerǁ__init____mutmut_4': xǁTfManagerǁ__init____mutmut_4, 
        'xǁTfManagerǁ__init____mutmut_5': xǁTfManagerǁ__init____mutmut_5, 
        'xǁTfManagerǁ__init____mutmut_6': xǁTfManagerǁ__init____mutmut_6, 
        'xǁTfManagerǁ__init____mutmut_7': xǁTfManagerǁ__init____mutmut_7, 
        'xǁTfManagerǁ__init____mutmut_8': xǁTfManagerǁ__init____mutmut_8, 
        'xǁTfManagerǁ__init____mutmut_9': xǁTfManagerǁ__init____mutmut_9, 
        'xǁTfManagerǁ__init____mutmut_10': xǁTfManagerǁ__init____mutmut_10, 
        'xǁTfManagerǁ__init____mutmut_11': xǁTfManagerǁ__init____mutmut_11, 
        'xǁTfManagerǁ__init____mutmut_12': xǁTfManagerǁ__init____mutmut_12, 
        'xǁTfManagerǁ__init____mutmut_13': xǁTfManagerǁ__init____mutmut_13, 
        'xǁTfManagerǁ__init____mutmut_14': xǁTfManagerǁ__init____mutmut_14, 
        'xǁTfManagerǁ__init____mutmut_15': xǁTfManagerǁ__init____mutmut_15, 
        'xǁTfManagerǁ__init____mutmut_16': xǁTfManagerǁ__init____mutmut_16, 
        'xǁTfManagerǁ__init____mutmut_17': xǁTfManagerǁ__init____mutmut_17, 
        'xǁTfManagerǁ__init____mutmut_18': xǁTfManagerǁ__init____mutmut_18, 
        'xǁTfManagerǁ__init____mutmut_19': xǁTfManagerǁ__init____mutmut_19, 
        'xǁTfManagerǁ__init____mutmut_20': xǁTfManagerǁ__init____mutmut_20
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTfManagerǁ__init____mutmut_orig)
    xǁTfManagerǁ__init____mutmut_orig.__name__ = 'xǁTfManagerǁ__init__'

    @property
    @abstractmethod
    def tool_prefix(self) -> str:
        """Prefix for version files (e.g., 'terraform' or 'opentofu')."""

    def _save_metadata(self) -> None:
        """Save metadata to JSON file."""
        self.metadata_manager.save_metadata()

    def xǁTfManagerǁ_update_recent_file__mutmut_orig(self) -> None:
        """Update the RECENT file with current installed versions."""
        installed_versions = self.get_installed_versions()
        self.metadata_manager.update_recent_file(installed_versions)

    def xǁTfManagerǁ_update_recent_file__mutmut_1(self) -> None:
        """Update the RECENT file with current installed versions."""
        installed_versions = None
        self.metadata_manager.update_recent_file(installed_versions)

    def xǁTfManagerǁ_update_recent_file__mutmut_2(self) -> None:
        """Update the RECENT file with current installed versions."""
        installed_versions = self.get_installed_versions()
        self.metadata_manager.update_recent_file(None)
    
    xǁTfManagerǁ_update_recent_file__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁ_update_recent_file__mutmut_1': xǁTfManagerǁ_update_recent_file__mutmut_1, 
        'xǁTfManagerǁ_update_recent_file__mutmut_2': xǁTfManagerǁ_update_recent_file__mutmut_2
    }
    
    def _update_recent_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁ_update_recent_file__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁ_update_recent_file__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_recent_file.__signature__ = _mutmut_signature(xǁTfManagerǁ_update_recent_file__mutmut_orig)
    xǁTfManagerǁ_update_recent_file__mutmut_orig.__name__ = 'xǁTfManagerǁ_update_recent_file'

    def xǁTfManagerǁ_update_recent_file_with_active__mutmut_orig(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        installed_versions = self.get_installed_versions()
        self.metadata_manager.update_recent_file_with_active(version, installed_versions)

    def xǁTfManagerǁ_update_recent_file_with_active__mutmut_1(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        installed_versions = None
        self.metadata_manager.update_recent_file_with_active(version, installed_versions)

    def xǁTfManagerǁ_update_recent_file_with_active__mutmut_2(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        installed_versions = self.get_installed_versions()
        self.metadata_manager.update_recent_file_with_active(None, installed_versions)

    def xǁTfManagerǁ_update_recent_file_with_active__mutmut_3(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        installed_versions = self.get_installed_versions()
        self.metadata_manager.update_recent_file_with_active(version, None)

    def xǁTfManagerǁ_update_recent_file_with_active__mutmut_4(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        installed_versions = self.get_installed_versions()
        self.metadata_manager.update_recent_file_with_active(installed_versions)

    def xǁTfManagerǁ_update_recent_file_with_active__mutmut_5(self, version: str) -> None:
        """Update RECENT file to put active version first."""
        installed_versions = self.get_installed_versions()
        self.metadata_manager.update_recent_file_with_active(version, )
    
    xǁTfManagerǁ_update_recent_file_with_active__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁ_update_recent_file_with_active__mutmut_1': xǁTfManagerǁ_update_recent_file_with_active__mutmut_1, 
        'xǁTfManagerǁ_update_recent_file_with_active__mutmut_2': xǁTfManagerǁ_update_recent_file_with_active__mutmut_2, 
        'xǁTfManagerǁ_update_recent_file_with_active__mutmut_3': xǁTfManagerǁ_update_recent_file_with_active__mutmut_3, 
        'xǁTfManagerǁ_update_recent_file_with_active__mutmut_4': xǁTfManagerǁ_update_recent_file_with_active__mutmut_4, 
        'xǁTfManagerǁ_update_recent_file_with_active__mutmut_5': xǁTfManagerǁ_update_recent_file_with_active__mutmut_5
    }
    
    def _update_recent_file_with_active(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁ_update_recent_file_with_active__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁ_update_recent_file_with_active__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_recent_file_with_active.__signature__ = _mutmut_signature(xǁTfManagerǁ_update_recent_file_with_active__mutmut_orig)
    xǁTfManagerǁ_update_recent_file_with_active__mutmut_orig.__name__ = 'xǁTfManagerǁ_update_recent_file_with_active'

    def xǁTfManagerǁget_binary_path__mutmut_orig(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        # In tf versions format, binaries are stored as prefix_version
        binary_name = f"{self.tool_prefix}_{version}"
        return self.install_path / binary_name

    def xǁTfManagerǁget_binary_path__mutmut_1(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        # In tf versions format, binaries are stored as prefix_version
        binary_name = None
        return self.install_path / binary_name

    def xǁTfManagerǁget_binary_path__mutmut_2(self, version: str) -> pathlib.Path:
        """Get path to the installed binary for a version."""
        # In tf versions format, binaries are stored as prefix_version
        binary_name = f"{self.tool_prefix}_{version}"
        return self.install_path * binary_name
    
    xǁTfManagerǁget_binary_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁget_binary_path__mutmut_1': xǁTfManagerǁget_binary_path__mutmut_1, 
        'xǁTfManagerǁget_binary_path__mutmut_2': xǁTfManagerǁget_binary_path__mutmut_2
    }
    
    def get_binary_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁget_binary_path__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁget_binary_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_binary_path.__signature__ = _mutmut_signature(xǁTfManagerǁget_binary_path__mutmut_orig)
    xǁTfManagerǁget_binary_path__mutmut_orig.__name__ = 'xǁTfManagerǁget_binary_path'

    def xǁTfManagerǁget_installed_versions__mutmut_orig(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_1(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = None

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_2(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = None
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_3(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() or item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_4(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(None):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_5(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = None
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_6(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(None):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_7(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(None)

        return sorted(versions, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_8(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(None, key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_9(self) -> list[str]:
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

    def xǁTfManagerǁget_installed_versions__mutmut_10(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=None)

    def xǁTfManagerǁget_installed_versions__mutmut_11(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(key=version_sort_key, reverse=True)

    def xǁTfManagerǁget_installed_versions__mutmut_12(self) -> list[str]:
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

    def xǁTfManagerǁget_installed_versions__mutmut_13(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, )

    def xǁTfManagerǁget_installed_versions__mutmut_14(self) -> list[str]:
        """Get all installed versions of this tool."""
        versions = []

        prefix = f"{self.tool_prefix}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                if self._is_version_dir(version):
                    versions.append(version)

        return sorted(versions, key=version_sort_key, reverse=False)
    
    xǁTfManagerǁget_installed_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁget_installed_versions__mutmut_1': xǁTfManagerǁget_installed_versions__mutmut_1, 
        'xǁTfManagerǁget_installed_versions__mutmut_2': xǁTfManagerǁget_installed_versions__mutmut_2, 
        'xǁTfManagerǁget_installed_versions__mutmut_3': xǁTfManagerǁget_installed_versions__mutmut_3, 
        'xǁTfManagerǁget_installed_versions__mutmut_4': xǁTfManagerǁget_installed_versions__mutmut_4, 
        'xǁTfManagerǁget_installed_versions__mutmut_5': xǁTfManagerǁget_installed_versions__mutmut_5, 
        'xǁTfManagerǁget_installed_versions__mutmut_6': xǁTfManagerǁget_installed_versions__mutmut_6, 
        'xǁTfManagerǁget_installed_versions__mutmut_7': xǁTfManagerǁget_installed_versions__mutmut_7, 
        'xǁTfManagerǁget_installed_versions__mutmut_8': xǁTfManagerǁget_installed_versions__mutmut_8, 
        'xǁTfManagerǁget_installed_versions__mutmut_9': xǁTfManagerǁget_installed_versions__mutmut_9, 
        'xǁTfManagerǁget_installed_versions__mutmut_10': xǁTfManagerǁget_installed_versions__mutmut_10, 
        'xǁTfManagerǁget_installed_versions__mutmut_11': xǁTfManagerǁget_installed_versions__mutmut_11, 
        'xǁTfManagerǁget_installed_versions__mutmut_12': xǁTfManagerǁget_installed_versions__mutmut_12, 
        'xǁTfManagerǁget_installed_versions__mutmut_13': xǁTfManagerǁget_installed_versions__mutmut_13, 
        'xǁTfManagerǁget_installed_versions__mutmut_14': xǁTfManagerǁget_installed_versions__mutmut_14
    }
    
    def get_installed_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁget_installed_versions__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁget_installed_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_versions.__signature__ = _mutmut_signature(xǁTfManagerǁget_installed_versions__mutmut_orig)
    xǁTfManagerǁget_installed_versions__mutmut_orig.__name__ = 'xǁTfManagerǁget_installed_versions'

    def xǁTfManagerǁget_installed_version__mutmut_orig(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_1(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = None

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_2(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "XXworkenvXX" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_3(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "WORKENV" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_4(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" not in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_5(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = None
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_6(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(None, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_7(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, None)
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_8(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get({})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_9(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, )
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_10(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["XXworkenvXX"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_11(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["WORKENV"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_12(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = None

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_13(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = get_tool_version_key(None)

            if tool_key in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None

    def xǁTfManagerǁget_installed_version__mutmut_14(self) -> str | None:
        """Get currently active version from metadata only (no system fallbacks)."""
        # Get current profile (default to 'default')
        profile = self._get_current_profile()

        # Check metadata for active version in workenv
        if "workenv" in self.metadata:
            profile_data = self.metadata["workenv"].get(profile, {})
            tool_key = get_tool_version_key(self.tool_name)

            if tool_key not in profile_data:
                return profile_data[tool_key]

        # No fallbacks - workenv is completely self-contained
        return None
    
    xǁTfManagerǁget_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁget_installed_version__mutmut_1': xǁTfManagerǁget_installed_version__mutmut_1, 
        'xǁTfManagerǁget_installed_version__mutmut_2': xǁTfManagerǁget_installed_version__mutmut_2, 
        'xǁTfManagerǁget_installed_version__mutmut_3': xǁTfManagerǁget_installed_version__mutmut_3, 
        'xǁTfManagerǁget_installed_version__mutmut_4': xǁTfManagerǁget_installed_version__mutmut_4, 
        'xǁTfManagerǁget_installed_version__mutmut_5': xǁTfManagerǁget_installed_version__mutmut_5, 
        'xǁTfManagerǁget_installed_version__mutmut_6': xǁTfManagerǁget_installed_version__mutmut_6, 
        'xǁTfManagerǁget_installed_version__mutmut_7': xǁTfManagerǁget_installed_version__mutmut_7, 
        'xǁTfManagerǁget_installed_version__mutmut_8': xǁTfManagerǁget_installed_version__mutmut_8, 
        'xǁTfManagerǁget_installed_version__mutmut_9': xǁTfManagerǁget_installed_version__mutmut_9, 
        'xǁTfManagerǁget_installed_version__mutmut_10': xǁTfManagerǁget_installed_version__mutmut_10, 
        'xǁTfManagerǁget_installed_version__mutmut_11': xǁTfManagerǁget_installed_version__mutmut_11, 
        'xǁTfManagerǁget_installed_version__mutmut_12': xǁTfManagerǁget_installed_version__mutmut_12, 
        'xǁTfManagerǁget_installed_version__mutmut_13': xǁTfManagerǁget_installed_version__mutmut_13, 
        'xǁTfManagerǁget_installed_version__mutmut_14': xǁTfManagerǁget_installed_version__mutmut_14
    }
    
    def get_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁget_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁget_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_version.__signature__ = _mutmut_signature(xǁTfManagerǁget_installed_version__mutmut_orig)
    xǁTfManagerǁget_installed_version__mutmut_orig.__name__ = 'xǁTfManagerǁget_installed_version'

    def xǁTfManagerǁset_installed_version__mutmut_orig(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_1(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = None

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_2(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "XXworkenvXX" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_3(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "WORKENV" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_4(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_5(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = None
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_6(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["XXworkenvXX"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_7(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["WORKENV"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_8(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_9(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["XXworkenvXX"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_10(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["WORKENV"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_11(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = None

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_12(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["XXworkenvXX"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_13(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["WORKENV"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_14(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = None
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_15(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(None)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_16(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = None
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_17(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["XXworkenvXX"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_18(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["WORKENV"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_19(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(None)

        # Note: actual venv copying happens in create_symlink()

        logger.info(f"Set {self.tool_name} active version to {version} in profile '{profile}'")

    def xǁTfManagerǁset_installed_version__mutmut_20(self, version: str) -> None:
        """Set the active version in metadata."""
        # Get current profile
        profile = self._get_current_profile()

        # Ensure workenv structure exists
        if "workenv" not in self.metadata:
            self.metadata["workenv"] = {}
        if profile not in self.metadata["workenv"]:
            self.metadata["workenv"][profile] = {}

        # Store active version in metadata under workenv profile
        tool_key = get_tool_version_key(self.tool_name)
        self.metadata["workenv"][profile][tool_key] = version
        self._save_metadata()

        # Also ensure it's at the front of RECENT
        self._update_recent_file_with_active(version)

        # Note: actual venv copying happens in create_symlink()

        logger.info(None)
    
    xǁTfManagerǁset_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁset_installed_version__mutmut_1': xǁTfManagerǁset_installed_version__mutmut_1, 
        'xǁTfManagerǁset_installed_version__mutmut_2': xǁTfManagerǁset_installed_version__mutmut_2, 
        'xǁTfManagerǁset_installed_version__mutmut_3': xǁTfManagerǁset_installed_version__mutmut_3, 
        'xǁTfManagerǁset_installed_version__mutmut_4': xǁTfManagerǁset_installed_version__mutmut_4, 
        'xǁTfManagerǁset_installed_version__mutmut_5': xǁTfManagerǁset_installed_version__mutmut_5, 
        'xǁTfManagerǁset_installed_version__mutmut_6': xǁTfManagerǁset_installed_version__mutmut_6, 
        'xǁTfManagerǁset_installed_version__mutmut_7': xǁTfManagerǁset_installed_version__mutmut_7, 
        'xǁTfManagerǁset_installed_version__mutmut_8': xǁTfManagerǁset_installed_version__mutmut_8, 
        'xǁTfManagerǁset_installed_version__mutmut_9': xǁTfManagerǁset_installed_version__mutmut_9, 
        'xǁTfManagerǁset_installed_version__mutmut_10': xǁTfManagerǁset_installed_version__mutmut_10, 
        'xǁTfManagerǁset_installed_version__mutmut_11': xǁTfManagerǁset_installed_version__mutmut_11, 
        'xǁTfManagerǁset_installed_version__mutmut_12': xǁTfManagerǁset_installed_version__mutmut_12, 
        'xǁTfManagerǁset_installed_version__mutmut_13': xǁTfManagerǁset_installed_version__mutmut_13, 
        'xǁTfManagerǁset_installed_version__mutmut_14': xǁTfManagerǁset_installed_version__mutmut_14, 
        'xǁTfManagerǁset_installed_version__mutmut_15': xǁTfManagerǁset_installed_version__mutmut_15, 
        'xǁTfManagerǁset_installed_version__mutmut_16': xǁTfManagerǁset_installed_version__mutmut_16, 
        'xǁTfManagerǁset_installed_version__mutmut_17': xǁTfManagerǁset_installed_version__mutmut_17, 
        'xǁTfManagerǁset_installed_version__mutmut_18': xǁTfManagerǁset_installed_version__mutmut_18, 
        'xǁTfManagerǁset_installed_version__mutmut_19': xǁTfManagerǁset_installed_version__mutmut_19, 
        'xǁTfManagerǁset_installed_version__mutmut_20': xǁTfManagerǁset_installed_version__mutmut_20
    }
    
    def set_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁset_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁset_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_installed_version.__signature__ = _mutmut_signature(xǁTfManagerǁset_installed_version__mutmut_orig)
    xǁTfManagerǁset_installed_version__mutmut_orig.__name__ = 'xǁTfManagerǁset_installed_version'

    def xǁTfManagerǁremove_version__mutmut_orig(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_1(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = None

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_2(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(None)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_3(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(None, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_4(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=None)
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

    def xǁTfManagerǁremove_version__mutmut_5(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_6(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, )
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

    def xǁTfManagerǁremove_version__mutmut_7(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=False)
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

    def xǁTfManagerǁremove_version__mutmut_8(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_9(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_10(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_11(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_12(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_13(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_14(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_15(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_16(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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

    def xǁTfManagerǁremove_version__mutmut_17(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            safe_delete(binary_path, missing_ok=True)
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
    
    xǁTfManagerǁremove_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁremove_version__mutmut_1': xǁTfManagerǁremove_version__mutmut_1, 
        'xǁTfManagerǁremove_version__mutmut_2': xǁTfManagerǁremove_version__mutmut_2, 
        'xǁTfManagerǁremove_version__mutmut_3': xǁTfManagerǁremove_version__mutmut_3, 
        'xǁTfManagerǁremove_version__mutmut_4': xǁTfManagerǁremove_version__mutmut_4, 
        'xǁTfManagerǁremove_version__mutmut_5': xǁTfManagerǁremove_version__mutmut_5, 
        'xǁTfManagerǁremove_version__mutmut_6': xǁTfManagerǁremove_version__mutmut_6, 
        'xǁTfManagerǁremove_version__mutmut_7': xǁTfManagerǁremove_version__mutmut_7, 
        'xǁTfManagerǁremove_version__mutmut_8': xǁTfManagerǁremove_version__mutmut_8, 
        'xǁTfManagerǁremove_version__mutmut_9': xǁTfManagerǁremove_version__mutmut_9, 
        'xǁTfManagerǁremove_version__mutmut_10': xǁTfManagerǁremove_version__mutmut_10, 
        'xǁTfManagerǁremove_version__mutmut_11': xǁTfManagerǁremove_version__mutmut_11, 
        'xǁTfManagerǁremove_version__mutmut_12': xǁTfManagerǁremove_version__mutmut_12, 
        'xǁTfManagerǁremove_version__mutmut_13': xǁTfManagerǁremove_version__mutmut_13, 
        'xǁTfManagerǁremove_version__mutmut_14': xǁTfManagerǁremove_version__mutmut_14, 
        'xǁTfManagerǁremove_version__mutmut_15': xǁTfManagerǁremove_version__mutmut_15, 
        'xǁTfManagerǁremove_version__mutmut_16': xǁTfManagerǁremove_version__mutmut_16, 
        'xǁTfManagerǁremove_version__mutmut_17': xǁTfManagerǁremove_version__mutmut_17
    }
    
    def remove_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁremove_version__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁremove_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    remove_version.__signature__ = _mutmut_signature(xǁTfManagerǁremove_version__mutmut_orig)
    xǁTfManagerǁremove_version__mutmut_orig.__name__ = 'xǁTfManagerǁremove_version'

    def xǁTfManagerǁ_install_from_archive__mutmut_orig(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_1(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = None
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_2(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir * f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_3(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=None)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_4(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=False)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_5(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(None, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_6(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, None)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_7(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_8(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, )

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_9(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name != "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_10(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "XXtofuXX":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_11(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "TOFU":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_12(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = None
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_13(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "XXtofuXX"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_14(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "TOFU"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_15(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name != "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_16(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "XXibmtfXX":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_17(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "IBMTF":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_18(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = None  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_19(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "XXterraformXX"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_20(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "TERRAFORM"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_21(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = None

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_22(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = ""
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_23(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(None):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_24(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() or file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_25(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name not in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_26(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = None
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_27(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    return

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_28(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_29(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    None
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_30(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = None
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_31(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(None)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_32(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(None, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_33(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, None, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_34(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=None)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_35(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_36(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_37(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, )

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_38(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=False)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_39(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(None)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_40(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(None)

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_41(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

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
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_42(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(None)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_43(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(None, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_44(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, None, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_45(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, None)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_46(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_47(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_48(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, )

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_49(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_50(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(None):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_51(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(None)

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_52(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(None, missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_53(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=None)

    def xǁTfManagerǁ_install_from_archive__mutmut_54(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(missing_ok=True)

    def xǁTfManagerǁ_install_from_archive__mutmut_55(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, )

    def xǁTfManagerǁ_install_from_archive__mutmut_56(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive in tf versions format."""
        # Extract to temporary directory
        extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find the binary in extracted files
            # Note: Archive contains binary with original name (terraform/tofu)
            # We search for the archive name, then copy to our target name
            if self.tool_name == "tofu":
                archive_binary_name = "tofu"
            elif self.tool_name == "ibmtf":
                archive_binary_name = "terraform"  # IBM Terraform binary is named "terraform" in archive
            else:
                archive_binary_name = self.executable_name

            binary_path = None
            for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
                if file_path.is_file() and file_path.name in [
                    archive_binary_name,
                    f"{archive_binary_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(
                    f"{self.tool_name} binary not found in archive (looking for {archive_binary_name})"
                )

            # Copy to tf versions location with the correct target name
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.tool_name} binary to: {target_path}")

            # Calculate installed binary hash
            binary_hash = calculate_file_hash(target_path)

            # Update metadata with comprehensive information
            self._update_install_metadata(version, archive_path, binary_hash)

            # Update RECENT file
            self._update_recent_file()

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.tool_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=False)
    
    xǁTfManagerǁ_install_from_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁ_install_from_archive__mutmut_1': xǁTfManagerǁ_install_from_archive__mutmut_1, 
        'xǁTfManagerǁ_install_from_archive__mutmut_2': xǁTfManagerǁ_install_from_archive__mutmut_2, 
        'xǁTfManagerǁ_install_from_archive__mutmut_3': xǁTfManagerǁ_install_from_archive__mutmut_3, 
        'xǁTfManagerǁ_install_from_archive__mutmut_4': xǁTfManagerǁ_install_from_archive__mutmut_4, 
        'xǁTfManagerǁ_install_from_archive__mutmut_5': xǁTfManagerǁ_install_from_archive__mutmut_5, 
        'xǁTfManagerǁ_install_from_archive__mutmut_6': xǁTfManagerǁ_install_from_archive__mutmut_6, 
        'xǁTfManagerǁ_install_from_archive__mutmut_7': xǁTfManagerǁ_install_from_archive__mutmut_7, 
        'xǁTfManagerǁ_install_from_archive__mutmut_8': xǁTfManagerǁ_install_from_archive__mutmut_8, 
        'xǁTfManagerǁ_install_from_archive__mutmut_9': xǁTfManagerǁ_install_from_archive__mutmut_9, 
        'xǁTfManagerǁ_install_from_archive__mutmut_10': xǁTfManagerǁ_install_from_archive__mutmut_10, 
        'xǁTfManagerǁ_install_from_archive__mutmut_11': xǁTfManagerǁ_install_from_archive__mutmut_11, 
        'xǁTfManagerǁ_install_from_archive__mutmut_12': xǁTfManagerǁ_install_from_archive__mutmut_12, 
        'xǁTfManagerǁ_install_from_archive__mutmut_13': xǁTfManagerǁ_install_from_archive__mutmut_13, 
        'xǁTfManagerǁ_install_from_archive__mutmut_14': xǁTfManagerǁ_install_from_archive__mutmut_14, 
        'xǁTfManagerǁ_install_from_archive__mutmut_15': xǁTfManagerǁ_install_from_archive__mutmut_15, 
        'xǁTfManagerǁ_install_from_archive__mutmut_16': xǁTfManagerǁ_install_from_archive__mutmut_16, 
        'xǁTfManagerǁ_install_from_archive__mutmut_17': xǁTfManagerǁ_install_from_archive__mutmut_17, 
        'xǁTfManagerǁ_install_from_archive__mutmut_18': xǁTfManagerǁ_install_from_archive__mutmut_18, 
        'xǁTfManagerǁ_install_from_archive__mutmut_19': xǁTfManagerǁ_install_from_archive__mutmut_19, 
        'xǁTfManagerǁ_install_from_archive__mutmut_20': xǁTfManagerǁ_install_from_archive__mutmut_20, 
        'xǁTfManagerǁ_install_from_archive__mutmut_21': xǁTfManagerǁ_install_from_archive__mutmut_21, 
        'xǁTfManagerǁ_install_from_archive__mutmut_22': xǁTfManagerǁ_install_from_archive__mutmut_22, 
        'xǁTfManagerǁ_install_from_archive__mutmut_23': xǁTfManagerǁ_install_from_archive__mutmut_23, 
        'xǁTfManagerǁ_install_from_archive__mutmut_24': xǁTfManagerǁ_install_from_archive__mutmut_24, 
        'xǁTfManagerǁ_install_from_archive__mutmut_25': xǁTfManagerǁ_install_from_archive__mutmut_25, 
        'xǁTfManagerǁ_install_from_archive__mutmut_26': xǁTfManagerǁ_install_from_archive__mutmut_26, 
        'xǁTfManagerǁ_install_from_archive__mutmut_27': xǁTfManagerǁ_install_from_archive__mutmut_27, 
        'xǁTfManagerǁ_install_from_archive__mutmut_28': xǁTfManagerǁ_install_from_archive__mutmut_28, 
        'xǁTfManagerǁ_install_from_archive__mutmut_29': xǁTfManagerǁ_install_from_archive__mutmut_29, 
        'xǁTfManagerǁ_install_from_archive__mutmut_30': xǁTfManagerǁ_install_from_archive__mutmut_30, 
        'xǁTfManagerǁ_install_from_archive__mutmut_31': xǁTfManagerǁ_install_from_archive__mutmut_31, 
        'xǁTfManagerǁ_install_from_archive__mutmut_32': xǁTfManagerǁ_install_from_archive__mutmut_32, 
        'xǁTfManagerǁ_install_from_archive__mutmut_33': xǁTfManagerǁ_install_from_archive__mutmut_33, 
        'xǁTfManagerǁ_install_from_archive__mutmut_34': xǁTfManagerǁ_install_from_archive__mutmut_34, 
        'xǁTfManagerǁ_install_from_archive__mutmut_35': xǁTfManagerǁ_install_from_archive__mutmut_35, 
        'xǁTfManagerǁ_install_from_archive__mutmut_36': xǁTfManagerǁ_install_from_archive__mutmut_36, 
        'xǁTfManagerǁ_install_from_archive__mutmut_37': xǁTfManagerǁ_install_from_archive__mutmut_37, 
        'xǁTfManagerǁ_install_from_archive__mutmut_38': xǁTfManagerǁ_install_from_archive__mutmut_38, 
        'xǁTfManagerǁ_install_from_archive__mutmut_39': xǁTfManagerǁ_install_from_archive__mutmut_39, 
        'xǁTfManagerǁ_install_from_archive__mutmut_40': xǁTfManagerǁ_install_from_archive__mutmut_40, 
        'xǁTfManagerǁ_install_from_archive__mutmut_41': xǁTfManagerǁ_install_from_archive__mutmut_41, 
        'xǁTfManagerǁ_install_from_archive__mutmut_42': xǁTfManagerǁ_install_from_archive__mutmut_42, 
        'xǁTfManagerǁ_install_from_archive__mutmut_43': xǁTfManagerǁ_install_from_archive__mutmut_43, 
        'xǁTfManagerǁ_install_from_archive__mutmut_44': xǁTfManagerǁ_install_from_archive__mutmut_44, 
        'xǁTfManagerǁ_install_from_archive__mutmut_45': xǁTfManagerǁ_install_from_archive__mutmut_45, 
        'xǁTfManagerǁ_install_from_archive__mutmut_46': xǁTfManagerǁ_install_from_archive__mutmut_46, 
        'xǁTfManagerǁ_install_from_archive__mutmut_47': xǁTfManagerǁ_install_from_archive__mutmut_47, 
        'xǁTfManagerǁ_install_from_archive__mutmut_48': xǁTfManagerǁ_install_from_archive__mutmut_48, 
        'xǁTfManagerǁ_install_from_archive__mutmut_49': xǁTfManagerǁ_install_from_archive__mutmut_49, 
        'xǁTfManagerǁ_install_from_archive__mutmut_50': xǁTfManagerǁ_install_from_archive__mutmut_50, 
        'xǁTfManagerǁ_install_from_archive__mutmut_51': xǁTfManagerǁ_install_from_archive__mutmut_51, 
        'xǁTfManagerǁ_install_from_archive__mutmut_52': xǁTfManagerǁ_install_from_archive__mutmut_52, 
        'xǁTfManagerǁ_install_from_archive__mutmut_53': xǁTfManagerǁ_install_from_archive__mutmut_53, 
        'xǁTfManagerǁ_install_from_archive__mutmut_54': xǁTfManagerǁ_install_from_archive__mutmut_54, 
        'xǁTfManagerǁ_install_from_archive__mutmut_55': xǁTfManagerǁ_install_from_archive__mutmut_55, 
        'xǁTfManagerǁ_install_from_archive__mutmut_56': xǁTfManagerǁ_install_from_archive__mutmut_56
    }
    
    def _install_from_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁ_install_from_archive__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁ_install_from_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _install_from_archive.__signature__ = _mutmut_signature(xǁTfManagerǁ_install_from_archive__mutmut_orig)
    xǁTfManagerǁ_install_from_archive__mutmut_orig.__name__ = 'xǁTfManagerǁ_install_from_archive'

    def xǁTfManagerǁ_update_install_metadata__mutmut_orig(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_1(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_2(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_3(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_4(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_5(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_6(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_7(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_8(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_9(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_10(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_11(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_12(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_13(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_14(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_15(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_16(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_17(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_18(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_19(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "XXinstalled_atXX": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_20(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "INSTALLED_AT": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_21(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_22(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_23(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_24(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_25(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_26(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_27(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_28(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_29(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_30(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_31(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_32(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_33(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_34(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_35(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_36(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_37(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_38(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_39(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_40(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_41(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_42(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_43(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_44(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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

    def xǁTfManagerǁ_update_install_metadata__mutmut_45(self, version: str, archive_path: pathlib.Path, binary_hash: str) -> None:
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
            "installed_at": provide_now().isoformat(),
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
    
    xǁTfManagerǁ_update_install_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁ_update_install_metadata__mutmut_1': xǁTfManagerǁ_update_install_metadata__mutmut_1, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_2': xǁTfManagerǁ_update_install_metadata__mutmut_2, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_3': xǁTfManagerǁ_update_install_metadata__mutmut_3, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_4': xǁTfManagerǁ_update_install_metadata__mutmut_4, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_5': xǁTfManagerǁ_update_install_metadata__mutmut_5, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_6': xǁTfManagerǁ_update_install_metadata__mutmut_6, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_7': xǁTfManagerǁ_update_install_metadata__mutmut_7, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_8': xǁTfManagerǁ_update_install_metadata__mutmut_8, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_9': xǁTfManagerǁ_update_install_metadata__mutmut_9, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_10': xǁTfManagerǁ_update_install_metadata__mutmut_10, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_11': xǁTfManagerǁ_update_install_metadata__mutmut_11, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_12': xǁTfManagerǁ_update_install_metadata__mutmut_12, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_13': xǁTfManagerǁ_update_install_metadata__mutmut_13, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_14': xǁTfManagerǁ_update_install_metadata__mutmut_14, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_15': xǁTfManagerǁ_update_install_metadata__mutmut_15, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_16': xǁTfManagerǁ_update_install_metadata__mutmut_16, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_17': xǁTfManagerǁ_update_install_metadata__mutmut_17, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_18': xǁTfManagerǁ_update_install_metadata__mutmut_18, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_19': xǁTfManagerǁ_update_install_metadata__mutmut_19, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_20': xǁTfManagerǁ_update_install_metadata__mutmut_20, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_21': xǁTfManagerǁ_update_install_metadata__mutmut_21, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_22': xǁTfManagerǁ_update_install_metadata__mutmut_22, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_23': xǁTfManagerǁ_update_install_metadata__mutmut_23, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_24': xǁTfManagerǁ_update_install_metadata__mutmut_24, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_25': xǁTfManagerǁ_update_install_metadata__mutmut_25, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_26': xǁTfManagerǁ_update_install_metadata__mutmut_26, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_27': xǁTfManagerǁ_update_install_metadata__mutmut_27, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_28': xǁTfManagerǁ_update_install_metadata__mutmut_28, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_29': xǁTfManagerǁ_update_install_metadata__mutmut_29, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_30': xǁTfManagerǁ_update_install_metadata__mutmut_30, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_31': xǁTfManagerǁ_update_install_metadata__mutmut_31, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_32': xǁTfManagerǁ_update_install_metadata__mutmut_32, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_33': xǁTfManagerǁ_update_install_metadata__mutmut_33, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_34': xǁTfManagerǁ_update_install_metadata__mutmut_34, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_35': xǁTfManagerǁ_update_install_metadata__mutmut_35, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_36': xǁTfManagerǁ_update_install_metadata__mutmut_36, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_37': xǁTfManagerǁ_update_install_metadata__mutmut_37, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_38': xǁTfManagerǁ_update_install_metadata__mutmut_38, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_39': xǁTfManagerǁ_update_install_metadata__mutmut_39, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_40': xǁTfManagerǁ_update_install_metadata__mutmut_40, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_41': xǁTfManagerǁ_update_install_metadata__mutmut_41, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_42': xǁTfManagerǁ_update_install_metadata__mutmut_42, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_43': xǁTfManagerǁ_update_install_metadata__mutmut_43, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_44': xǁTfManagerǁ_update_install_metadata__mutmut_44, 
        'xǁTfManagerǁ_update_install_metadata__mutmut_45': xǁTfManagerǁ_update_install_metadata__mutmut_45
    }
    
    def _update_install_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁ_update_install_metadata__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁ_update_install_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_install_metadata.__signature__ = _mutmut_signature(xǁTfManagerǁ_update_install_metadata__mutmut_orig)
    xǁTfManagerǁ_update_install_metadata__mutmut_orig.__name__ = 'xǁTfManagerǁ_update_install_metadata'

    def xǁTfManagerǁcreate_symlink__mutmut_orig(self, version: str) -> None:
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

    def xǁTfManagerǁcreate_symlink__mutmut_1(self, version: str) -> None:
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

    def xǁTfManagerǁcreate_symlink__mutmut_2(self, version: str) -> None:
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

    def xǁTfManagerǁcreate_symlink__mutmut_3(self, version: str) -> None:
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

    def xǁTfManagerǁcreate_symlink__mutmut_4(self, version: str) -> None:
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

    def xǁTfManagerǁcreate_symlink__mutmut_5(self, version: str) -> None:
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

    def xǁTfManagerǁcreate_symlink__mutmut_6(self, version: str) -> None:
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
    
    xǁTfManagerǁcreate_symlink__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁcreate_symlink__mutmut_1': xǁTfManagerǁcreate_symlink__mutmut_1, 
        'xǁTfManagerǁcreate_symlink__mutmut_2': xǁTfManagerǁcreate_symlink__mutmut_2, 
        'xǁTfManagerǁcreate_symlink__mutmut_3': xǁTfManagerǁcreate_symlink__mutmut_3, 
        'xǁTfManagerǁcreate_symlink__mutmut_4': xǁTfManagerǁcreate_symlink__mutmut_4, 
        'xǁTfManagerǁcreate_symlink__mutmut_5': xǁTfManagerǁcreate_symlink__mutmut_5, 
        'xǁTfManagerǁcreate_symlink__mutmut_6': xǁTfManagerǁcreate_symlink__mutmut_6
    }
    
    def create_symlink(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁcreate_symlink__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁcreate_symlink__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_symlink.__signature__ = _mutmut_signature(xǁTfManagerǁcreate_symlink__mutmut_orig)
    xǁTfManagerǁcreate_symlink__mutmut_orig.__name__ = 'xǁTfManagerǁcreate_symlink'

    def xǁTfManagerǁset_global_version__mutmut_orig(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_1(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_2(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_3(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_4(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_5(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_6(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_7(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_8(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_9(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_10(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_11(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_12(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_13(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_14(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_15(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_16(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_17(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_18(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_19(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_20(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_21(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_22(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_23(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_24(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_25(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_26(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_27(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_28(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_29(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_30(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_31(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_32(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_33(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_34(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_35(self, version: str) -> None:
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
        safe_copy(None, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_36(self, version: str) -> None:
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
        safe_copy(binary_path, None, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_37(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=None)

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

    def xǁTfManagerǁset_global_version__mutmut_38(self, version: str) -> None:
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
        safe_copy(target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_39(self, version: str) -> None:
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
        safe_copy(binary_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_40(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, )

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

    def xǁTfManagerǁset_global_version__mutmut_41(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=False)

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

    def xǁTfManagerǁset_global_version__mutmut_42(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_43(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_44(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_45(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_46(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_47(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_48(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_49(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_50(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_51(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_52(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_53(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_54(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_55(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_56(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_57(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_58(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_59(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_60(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_61(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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

    def xǁTfManagerǁset_global_version__mutmut_62(self, version: str) -> None:
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
        safe_copy(binary_path, target_path, overwrite=True)

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
    
    xǁTfManagerǁset_global_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁset_global_version__mutmut_1': xǁTfManagerǁset_global_version__mutmut_1, 
        'xǁTfManagerǁset_global_version__mutmut_2': xǁTfManagerǁset_global_version__mutmut_2, 
        'xǁTfManagerǁset_global_version__mutmut_3': xǁTfManagerǁset_global_version__mutmut_3, 
        'xǁTfManagerǁset_global_version__mutmut_4': xǁTfManagerǁset_global_version__mutmut_4, 
        'xǁTfManagerǁset_global_version__mutmut_5': xǁTfManagerǁset_global_version__mutmut_5, 
        'xǁTfManagerǁset_global_version__mutmut_6': xǁTfManagerǁset_global_version__mutmut_6, 
        'xǁTfManagerǁset_global_version__mutmut_7': xǁTfManagerǁset_global_version__mutmut_7, 
        'xǁTfManagerǁset_global_version__mutmut_8': xǁTfManagerǁset_global_version__mutmut_8, 
        'xǁTfManagerǁset_global_version__mutmut_9': xǁTfManagerǁset_global_version__mutmut_9, 
        'xǁTfManagerǁset_global_version__mutmut_10': xǁTfManagerǁset_global_version__mutmut_10, 
        'xǁTfManagerǁset_global_version__mutmut_11': xǁTfManagerǁset_global_version__mutmut_11, 
        'xǁTfManagerǁset_global_version__mutmut_12': xǁTfManagerǁset_global_version__mutmut_12, 
        'xǁTfManagerǁset_global_version__mutmut_13': xǁTfManagerǁset_global_version__mutmut_13, 
        'xǁTfManagerǁset_global_version__mutmut_14': xǁTfManagerǁset_global_version__mutmut_14, 
        'xǁTfManagerǁset_global_version__mutmut_15': xǁTfManagerǁset_global_version__mutmut_15, 
        'xǁTfManagerǁset_global_version__mutmut_16': xǁTfManagerǁset_global_version__mutmut_16, 
        'xǁTfManagerǁset_global_version__mutmut_17': xǁTfManagerǁset_global_version__mutmut_17, 
        'xǁTfManagerǁset_global_version__mutmut_18': xǁTfManagerǁset_global_version__mutmut_18, 
        'xǁTfManagerǁset_global_version__mutmut_19': xǁTfManagerǁset_global_version__mutmut_19, 
        'xǁTfManagerǁset_global_version__mutmut_20': xǁTfManagerǁset_global_version__mutmut_20, 
        'xǁTfManagerǁset_global_version__mutmut_21': xǁTfManagerǁset_global_version__mutmut_21, 
        'xǁTfManagerǁset_global_version__mutmut_22': xǁTfManagerǁset_global_version__mutmut_22, 
        'xǁTfManagerǁset_global_version__mutmut_23': xǁTfManagerǁset_global_version__mutmut_23, 
        'xǁTfManagerǁset_global_version__mutmut_24': xǁTfManagerǁset_global_version__mutmut_24, 
        'xǁTfManagerǁset_global_version__mutmut_25': xǁTfManagerǁset_global_version__mutmut_25, 
        'xǁTfManagerǁset_global_version__mutmut_26': xǁTfManagerǁset_global_version__mutmut_26, 
        'xǁTfManagerǁset_global_version__mutmut_27': xǁTfManagerǁset_global_version__mutmut_27, 
        'xǁTfManagerǁset_global_version__mutmut_28': xǁTfManagerǁset_global_version__mutmut_28, 
        'xǁTfManagerǁset_global_version__mutmut_29': xǁTfManagerǁset_global_version__mutmut_29, 
        'xǁTfManagerǁset_global_version__mutmut_30': xǁTfManagerǁset_global_version__mutmut_30, 
        'xǁTfManagerǁset_global_version__mutmut_31': xǁTfManagerǁset_global_version__mutmut_31, 
        'xǁTfManagerǁset_global_version__mutmut_32': xǁTfManagerǁset_global_version__mutmut_32, 
        'xǁTfManagerǁset_global_version__mutmut_33': xǁTfManagerǁset_global_version__mutmut_33, 
        'xǁTfManagerǁset_global_version__mutmut_34': xǁTfManagerǁset_global_version__mutmut_34, 
        'xǁTfManagerǁset_global_version__mutmut_35': xǁTfManagerǁset_global_version__mutmut_35, 
        'xǁTfManagerǁset_global_version__mutmut_36': xǁTfManagerǁset_global_version__mutmut_36, 
        'xǁTfManagerǁset_global_version__mutmut_37': xǁTfManagerǁset_global_version__mutmut_37, 
        'xǁTfManagerǁset_global_version__mutmut_38': xǁTfManagerǁset_global_version__mutmut_38, 
        'xǁTfManagerǁset_global_version__mutmut_39': xǁTfManagerǁset_global_version__mutmut_39, 
        'xǁTfManagerǁset_global_version__mutmut_40': xǁTfManagerǁset_global_version__mutmut_40, 
        'xǁTfManagerǁset_global_version__mutmut_41': xǁTfManagerǁset_global_version__mutmut_41, 
        'xǁTfManagerǁset_global_version__mutmut_42': xǁTfManagerǁset_global_version__mutmut_42, 
        'xǁTfManagerǁset_global_version__mutmut_43': xǁTfManagerǁset_global_version__mutmut_43, 
        'xǁTfManagerǁset_global_version__mutmut_44': xǁTfManagerǁset_global_version__mutmut_44, 
        'xǁTfManagerǁset_global_version__mutmut_45': xǁTfManagerǁset_global_version__mutmut_45, 
        'xǁTfManagerǁset_global_version__mutmut_46': xǁTfManagerǁset_global_version__mutmut_46, 
        'xǁTfManagerǁset_global_version__mutmut_47': xǁTfManagerǁset_global_version__mutmut_47, 
        'xǁTfManagerǁset_global_version__mutmut_48': xǁTfManagerǁset_global_version__mutmut_48, 
        'xǁTfManagerǁset_global_version__mutmut_49': xǁTfManagerǁset_global_version__mutmut_49, 
        'xǁTfManagerǁset_global_version__mutmut_50': xǁTfManagerǁset_global_version__mutmut_50, 
        'xǁTfManagerǁset_global_version__mutmut_51': xǁTfManagerǁset_global_version__mutmut_51, 
        'xǁTfManagerǁset_global_version__mutmut_52': xǁTfManagerǁset_global_version__mutmut_52, 
        'xǁTfManagerǁset_global_version__mutmut_53': xǁTfManagerǁset_global_version__mutmut_53, 
        'xǁTfManagerǁset_global_version__mutmut_54': xǁTfManagerǁset_global_version__mutmut_54, 
        'xǁTfManagerǁset_global_version__mutmut_55': xǁTfManagerǁset_global_version__mutmut_55, 
        'xǁTfManagerǁset_global_version__mutmut_56': xǁTfManagerǁset_global_version__mutmut_56, 
        'xǁTfManagerǁset_global_version__mutmut_57': xǁTfManagerǁset_global_version__mutmut_57, 
        'xǁTfManagerǁset_global_version__mutmut_58': xǁTfManagerǁset_global_version__mutmut_58, 
        'xǁTfManagerǁset_global_version__mutmut_59': xǁTfManagerǁset_global_version__mutmut_59, 
        'xǁTfManagerǁset_global_version__mutmut_60': xǁTfManagerǁset_global_version__mutmut_60, 
        'xǁTfManagerǁset_global_version__mutmut_61': xǁTfManagerǁset_global_version__mutmut_61, 
        'xǁTfManagerǁset_global_version__mutmut_62': xǁTfManagerǁset_global_version__mutmut_62
    }
    
    def set_global_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁset_global_version__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁset_global_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_global_version.__signature__ = _mutmut_signature(xǁTfManagerǁset_global_version__mutmut_orig)
    xǁTfManagerǁset_global_version__mutmut_orig.__name__ = 'xǁTfManagerǁset_global_version'

    def xǁTfManagerǁget_global_version__mutmut_orig(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_1(self) -> str | None:
        """Get the currently set global version."""
        if "XXglobalXX" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_2(self) -> str | None:
        """Get the currently set global version."""
        if "GLOBAL" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_3(self) -> str | None:
        """Get the currently set global version."""
        if "global" in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_4(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = None

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_5(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "XXopentofu_versionXX" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_6(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "OPENTOFU_VERSION" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_7(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name != "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_8(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "XXtofuXX" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_9(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "TOFU" else f"{self.tool_name}_version"

        return self.metadata["global"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_10(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["global"].get(None)

    def xǁTfManagerǁget_global_version__mutmut_11(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["XXglobalXX"].get(tool_key)

    def xǁTfManagerǁget_global_version__mutmut_12(self) -> str | None:
        """Get the currently set global version."""
        if "global" not in self.metadata:
            return None

        tool_key = "opentofu_version" if self.tool_name == "tofu" else f"{self.tool_name}_version"

        return self.metadata["GLOBAL"].get(tool_key)
    
    xǁTfManagerǁget_global_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁget_global_version__mutmut_1': xǁTfManagerǁget_global_version__mutmut_1, 
        'xǁTfManagerǁget_global_version__mutmut_2': xǁTfManagerǁget_global_version__mutmut_2, 
        'xǁTfManagerǁget_global_version__mutmut_3': xǁTfManagerǁget_global_version__mutmut_3, 
        'xǁTfManagerǁget_global_version__mutmut_4': xǁTfManagerǁget_global_version__mutmut_4, 
        'xǁTfManagerǁget_global_version__mutmut_5': xǁTfManagerǁget_global_version__mutmut_5, 
        'xǁTfManagerǁget_global_version__mutmut_6': xǁTfManagerǁget_global_version__mutmut_6, 
        'xǁTfManagerǁget_global_version__mutmut_7': xǁTfManagerǁget_global_version__mutmut_7, 
        'xǁTfManagerǁget_global_version__mutmut_8': xǁTfManagerǁget_global_version__mutmut_8, 
        'xǁTfManagerǁget_global_version__mutmut_9': xǁTfManagerǁget_global_version__mutmut_9, 
        'xǁTfManagerǁget_global_version__mutmut_10': xǁTfManagerǁget_global_version__mutmut_10, 
        'xǁTfManagerǁget_global_version__mutmut_11': xǁTfManagerǁget_global_version__mutmut_11, 
        'xǁTfManagerǁget_global_version__mutmut_12': xǁTfManagerǁget_global_version__mutmut_12
    }
    
    def get_global_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁget_global_version__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁget_global_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_global_version.__signature__ = _mutmut_signature(xǁTfManagerǁget_global_version__mutmut_orig)
    xǁTfManagerǁget_global_version__mutmut_orig.__name__ = 'xǁTfManagerǁget_global_version'

    def xǁTfManagerǁget_metadata_for_version__mutmut_orig(self, version: str) -> dict | None:
        """Get metadata for a specific version."""
        version_key = f"{self.tool_prefix}_{version}"
        return self.metadata.get(version_key)

    def xǁTfManagerǁget_metadata_for_version__mutmut_1(self, version: str) -> dict | None:
        """Get metadata for a specific version."""
        version_key = None
        return self.metadata.get(version_key)

    def xǁTfManagerǁget_metadata_for_version__mutmut_2(self, version: str) -> dict | None:
        """Get metadata for a specific version."""
        version_key = f"{self.tool_prefix}_{version}"
        return self.metadata.get(None)
    
    xǁTfManagerǁget_metadata_for_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁget_metadata_for_version__mutmut_1': xǁTfManagerǁget_metadata_for_version__mutmut_1, 
        'xǁTfManagerǁget_metadata_for_version__mutmut_2': xǁTfManagerǁget_metadata_for_version__mutmut_2
    }
    
    def get_metadata_for_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁget_metadata_for_version__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁget_metadata_for_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_metadata_for_version.__signature__ = _mutmut_signature(xǁTfManagerǁget_metadata_for_version__mutmut_orig)
    xǁTfManagerǁget_metadata_for_version__mutmut_orig.__name__ = 'xǁTfManagerǁget_metadata_for_version'

    def xǁTfManagerǁget_active_version_info__mutmut_orig(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_1(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_2(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_3(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_4(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_5(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_6(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_7(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_8(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_9(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_10(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_11(self) -> dict | None:
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

    def xǁTfManagerǁget_active_version_info__mutmut_12(self) -> dict | None:
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
    
    xǁTfManagerǁget_active_version_info__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁget_active_version_info__mutmut_1': xǁTfManagerǁget_active_version_info__mutmut_1, 
        'xǁTfManagerǁget_active_version_info__mutmut_2': xǁTfManagerǁget_active_version_info__mutmut_2, 
        'xǁTfManagerǁget_active_version_info__mutmut_3': xǁTfManagerǁget_active_version_info__mutmut_3, 
        'xǁTfManagerǁget_active_version_info__mutmut_4': xǁTfManagerǁget_active_version_info__mutmut_4, 
        'xǁTfManagerǁget_active_version_info__mutmut_5': xǁTfManagerǁget_active_version_info__mutmut_5, 
        'xǁTfManagerǁget_active_version_info__mutmut_6': xǁTfManagerǁget_active_version_info__mutmut_6, 
        'xǁTfManagerǁget_active_version_info__mutmut_7': xǁTfManagerǁget_active_version_info__mutmut_7, 
        'xǁTfManagerǁget_active_version_info__mutmut_8': xǁTfManagerǁget_active_version_info__mutmut_8, 
        'xǁTfManagerǁget_active_version_info__mutmut_9': xǁTfManagerǁget_active_version_info__mutmut_9, 
        'xǁTfManagerǁget_active_version_info__mutmut_10': xǁTfManagerǁget_active_version_info__mutmut_10, 
        'xǁTfManagerǁget_active_version_info__mutmut_11': xǁTfManagerǁget_active_version_info__mutmut_11, 
        'xǁTfManagerǁget_active_version_info__mutmut_12': xǁTfManagerǁget_active_version_info__mutmut_12
    }
    
    def get_active_version_info(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁget_active_version_info__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁget_active_version_info__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_active_version_info.__signature__ = _mutmut_signature(xǁTfManagerǁget_active_version_info__mutmut_orig)
    xǁTfManagerǁget_active_version_info__mutmut_orig.__name__ = 'xǁTfManagerǁget_active_version_info'

    def xǁTfManagerǁ_get_current_profile__mutmut_orig(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_1(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_2(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_3(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_4(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_5(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_6(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_7(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_8(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_9(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_10(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_11(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_12(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_13(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_14(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_15(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_16(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_17(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_18(self) -> str:
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

    def xǁTfManagerǁ_get_current_profile__mutmut_19(self) -> str:
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
    
    xǁTfManagerǁ_get_current_profile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁ_get_current_profile__mutmut_1': xǁTfManagerǁ_get_current_profile__mutmut_1, 
        'xǁTfManagerǁ_get_current_profile__mutmut_2': xǁTfManagerǁ_get_current_profile__mutmut_2, 
        'xǁTfManagerǁ_get_current_profile__mutmut_3': xǁTfManagerǁ_get_current_profile__mutmut_3, 
        'xǁTfManagerǁ_get_current_profile__mutmut_4': xǁTfManagerǁ_get_current_profile__mutmut_4, 
        'xǁTfManagerǁ_get_current_profile__mutmut_5': xǁTfManagerǁ_get_current_profile__mutmut_5, 
        'xǁTfManagerǁ_get_current_profile__mutmut_6': xǁTfManagerǁ_get_current_profile__mutmut_6, 
        'xǁTfManagerǁ_get_current_profile__mutmut_7': xǁTfManagerǁ_get_current_profile__mutmut_7, 
        'xǁTfManagerǁ_get_current_profile__mutmut_8': xǁTfManagerǁ_get_current_profile__mutmut_8, 
        'xǁTfManagerǁ_get_current_profile__mutmut_9': xǁTfManagerǁ_get_current_profile__mutmut_9, 
        'xǁTfManagerǁ_get_current_profile__mutmut_10': xǁTfManagerǁ_get_current_profile__mutmut_10, 
        'xǁTfManagerǁ_get_current_profile__mutmut_11': xǁTfManagerǁ_get_current_profile__mutmut_11, 
        'xǁTfManagerǁ_get_current_profile__mutmut_12': xǁTfManagerǁ_get_current_profile__mutmut_12, 
        'xǁTfManagerǁ_get_current_profile__mutmut_13': xǁTfManagerǁ_get_current_profile__mutmut_13, 
        'xǁTfManagerǁ_get_current_profile__mutmut_14': xǁTfManagerǁ_get_current_profile__mutmut_14, 
        'xǁTfManagerǁ_get_current_profile__mutmut_15': xǁTfManagerǁ_get_current_profile__mutmut_15, 
        'xǁTfManagerǁ_get_current_profile__mutmut_16': xǁTfManagerǁ_get_current_profile__mutmut_16, 
        'xǁTfManagerǁ_get_current_profile__mutmut_17': xǁTfManagerǁ_get_current_profile__mutmut_17, 
        'xǁTfManagerǁ_get_current_profile__mutmut_18': xǁTfManagerǁ_get_current_profile__mutmut_18, 
        'xǁTfManagerǁ_get_current_profile__mutmut_19': xǁTfManagerǁ_get_current_profile__mutmut_19
    }
    
    def _get_current_profile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁ_get_current_profile__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁ_get_current_profile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_current_profile.__signature__ = _mutmut_signature(xǁTfManagerǁ_get_current_profile__mutmut_orig)
    xǁTfManagerǁ_get_current_profile__mutmut_orig.__name__ = 'xǁTfManagerǁ_get_current_profile'

    def xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_orig(self) -> None:
        """Copy all active tf binaries to workenv bin directory."""
        copy_tf_binaries_to_workenv(self.workenv_bin_dir, self.config)

    def xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_1(self) -> None:
        """Copy all active tf binaries to workenv bin directory."""
        copy_tf_binaries_to_workenv(None, self.config)

    def xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_2(self) -> None:
        """Copy all active tf binaries to workenv bin directory."""
        copy_tf_binaries_to_workenv(self.workenv_bin_dir, None)

    def xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_3(self) -> None:
        """Copy all active tf binaries to workenv bin directory."""
        copy_tf_binaries_to_workenv(self.config)

    def xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_4(self) -> None:
        """Copy all active tf binaries to workenv bin directory."""
        copy_tf_binaries_to_workenv(self.workenv_bin_dir, )
    
    xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_1': xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_1, 
        'xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_2': xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_2, 
        'xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_3': xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_3, 
        'xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_4': xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_4
    }
    
    def _copy_active_binaries_to_venv(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _copy_active_binaries_to_venv.__signature__ = _mutmut_signature(xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_orig)
    xǁTfManagerǁ_copy_active_binaries_to_venv__mutmut_orig.__name__ = 'xǁTfManagerǁ_copy_active_binaries_to_venv'

    def xǁTfManagerǁswitch_version__mutmut_orig(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_1(self, version: str, dry_run: bool = True) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_2(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(None)
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_3(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_4(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(None).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_5(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(None)
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_6(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_7(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(None).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_8(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(None)
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_9(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(None, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_10(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=None)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_11(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_12(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, )

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_13(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=True)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_14(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(None)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_15(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = None
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_16(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists() and (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_17(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists() and (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_18(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir * "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_19(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "XXpyproject.tomlXX").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_20(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "PYPROJECT.TOML").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_21(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir * "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_22(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "XXwrknv.tomlXX").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_23(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "WRKNV.TOML").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_24(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir * ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_25(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / "XX.wrknv.tomlXX").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_26(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".WRKNV.TOML").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_27(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(None)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_28(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug(None)
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_29(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("XXRegenerated env.sh with new versionXX")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_30(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_31(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("REGENERATED ENV.SH WITH NEW VERSION")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_32(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(None)

        logger.info(f"Switched to {self.tool_name} {version}")

    def xǁTfManagerǁswitch_version__mutmut_33(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv by copying binaries to venv bin
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.tool_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.tool_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.tool_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Activate in workenv (copies binaries to venv bin)
        self.create_symlink(version)

        # 3. Regenerate env script
        try:
            from wrknv.wenv.env_generator import create_project_env_scripts

            project_dir = pathlib.Path.cwd()
            # Only regenerate if we're in a project directory
            if (
                (project_dir / "pyproject.toml").exists()
                or (project_dir / "wrknv.toml").exists()
                or (project_dir / ".wrknv.toml").exists()
            ):
                create_project_env_scripts(project_dir)
                logger.debug("Regenerated env.sh with new version")
        except Exception as e:
            if logger.is_debug_enabled():
                logger.debug(f"Could not regenerate env.sh: {e}")

        logger.info(None)
    
    xǁTfManagerǁswitch_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTfManagerǁswitch_version__mutmut_1': xǁTfManagerǁswitch_version__mutmut_1, 
        'xǁTfManagerǁswitch_version__mutmut_2': xǁTfManagerǁswitch_version__mutmut_2, 
        'xǁTfManagerǁswitch_version__mutmut_3': xǁTfManagerǁswitch_version__mutmut_3, 
        'xǁTfManagerǁswitch_version__mutmut_4': xǁTfManagerǁswitch_version__mutmut_4, 
        'xǁTfManagerǁswitch_version__mutmut_5': xǁTfManagerǁswitch_version__mutmut_5, 
        'xǁTfManagerǁswitch_version__mutmut_6': xǁTfManagerǁswitch_version__mutmut_6, 
        'xǁTfManagerǁswitch_version__mutmut_7': xǁTfManagerǁswitch_version__mutmut_7, 
        'xǁTfManagerǁswitch_version__mutmut_8': xǁTfManagerǁswitch_version__mutmut_8, 
        'xǁTfManagerǁswitch_version__mutmut_9': xǁTfManagerǁswitch_version__mutmut_9, 
        'xǁTfManagerǁswitch_version__mutmut_10': xǁTfManagerǁswitch_version__mutmut_10, 
        'xǁTfManagerǁswitch_version__mutmut_11': xǁTfManagerǁswitch_version__mutmut_11, 
        'xǁTfManagerǁswitch_version__mutmut_12': xǁTfManagerǁswitch_version__mutmut_12, 
        'xǁTfManagerǁswitch_version__mutmut_13': xǁTfManagerǁswitch_version__mutmut_13, 
        'xǁTfManagerǁswitch_version__mutmut_14': xǁTfManagerǁswitch_version__mutmut_14, 
        'xǁTfManagerǁswitch_version__mutmut_15': xǁTfManagerǁswitch_version__mutmut_15, 
        'xǁTfManagerǁswitch_version__mutmut_16': xǁTfManagerǁswitch_version__mutmut_16, 
        'xǁTfManagerǁswitch_version__mutmut_17': xǁTfManagerǁswitch_version__mutmut_17, 
        'xǁTfManagerǁswitch_version__mutmut_18': xǁTfManagerǁswitch_version__mutmut_18, 
        'xǁTfManagerǁswitch_version__mutmut_19': xǁTfManagerǁswitch_version__mutmut_19, 
        'xǁTfManagerǁswitch_version__mutmut_20': xǁTfManagerǁswitch_version__mutmut_20, 
        'xǁTfManagerǁswitch_version__mutmut_21': xǁTfManagerǁswitch_version__mutmut_21, 
        'xǁTfManagerǁswitch_version__mutmut_22': xǁTfManagerǁswitch_version__mutmut_22, 
        'xǁTfManagerǁswitch_version__mutmut_23': xǁTfManagerǁswitch_version__mutmut_23, 
        'xǁTfManagerǁswitch_version__mutmut_24': xǁTfManagerǁswitch_version__mutmut_24, 
        'xǁTfManagerǁswitch_version__mutmut_25': xǁTfManagerǁswitch_version__mutmut_25, 
        'xǁTfManagerǁswitch_version__mutmut_26': xǁTfManagerǁswitch_version__mutmut_26, 
        'xǁTfManagerǁswitch_version__mutmut_27': xǁTfManagerǁswitch_version__mutmut_27, 
        'xǁTfManagerǁswitch_version__mutmut_28': xǁTfManagerǁswitch_version__mutmut_28, 
        'xǁTfManagerǁswitch_version__mutmut_29': xǁTfManagerǁswitch_version__mutmut_29, 
        'xǁTfManagerǁswitch_version__mutmut_30': xǁTfManagerǁswitch_version__mutmut_30, 
        'xǁTfManagerǁswitch_version__mutmut_31': xǁTfManagerǁswitch_version__mutmut_31, 
        'xǁTfManagerǁswitch_version__mutmut_32': xǁTfManagerǁswitch_version__mutmut_32, 
        'xǁTfManagerǁswitch_version__mutmut_33': xǁTfManagerǁswitch_version__mutmut_33
    }
    
    def switch_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTfManagerǁswitch_version__mutmut_orig"), object.__getattribute__(self, "xǁTfManagerǁswitch_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    switch_version.__signature__ = _mutmut_signature(xǁTfManagerǁswitch_version__mutmut_orig)
    xǁTfManagerǁswitch_version__mutmut_orig.__name__ = 'xǁTfManagerǁswitch_version'


# 🧰🌍🔚
