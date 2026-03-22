#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""SubRosaManager Base Class
=========================
Base class for sub rosa (secret) management tools.

'Sub rosa' - under the rose - in confidence.
Manages secret management tool variants (OpenBao, HashiCorp Vault, etc.)"""

from __future__ import annotations

from abc import abstractmethod
import json
import pathlib
from typing import TYPE_CHECKING

from provide.foundation import logger
from provide.foundation.file import safe_copy, safe_delete, safe_rmtree

from wrknv.managers.base import BaseToolManager, ToolManagerError
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


class SubRosaManager(BaseToolManager):
    """
    Base class for secret management tool managers.

    Provides common functionality for managing secret management tools
    like OpenBao and HashiCorp Vault, with version switching and
    workenv integration.
    """

    def xǁSubRosaManagerǁ__init____mutmut_orig(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_1(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(None)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_2(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = None
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_3(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path(None).expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_4(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("XX~/.wrknv/subrosaXX").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_5(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.WRKNV/SUBROSA").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_6(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=None, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_7(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=None)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_8(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_9(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, )

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_10(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=False, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_11(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=False)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_12(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = None

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_13(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(None)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_14(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = None
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_15(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path * "metadata.json"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_16(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "XXmetadata.jsonXX"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_17(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "METADATA.JSON"
        self.metadata = self._load_metadata()

    def xǁSubRosaManagerǁ__init____mutmut_18(self, config: WorkenvConfig | None = None) -> None:
        super().__init__(config)

        # Override install path to use subrosa directory
        self.install_path = pathlib.Path("~/.wrknv/subrosa").expanduser()
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Get workenv bin directory for symlinking active version
        self.workenv_bin_dir = get_workenv_bin_dir(config)

        # Metadata file for tracking active versions
        self.metadata_file = self.install_path / "metadata.json"
        self.metadata = None
    
    xǁSubRosaManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁ__init____mutmut_1': xǁSubRosaManagerǁ__init____mutmut_1, 
        'xǁSubRosaManagerǁ__init____mutmut_2': xǁSubRosaManagerǁ__init____mutmut_2, 
        'xǁSubRosaManagerǁ__init____mutmut_3': xǁSubRosaManagerǁ__init____mutmut_3, 
        'xǁSubRosaManagerǁ__init____mutmut_4': xǁSubRosaManagerǁ__init____mutmut_4, 
        'xǁSubRosaManagerǁ__init____mutmut_5': xǁSubRosaManagerǁ__init____mutmut_5, 
        'xǁSubRosaManagerǁ__init____mutmut_6': xǁSubRosaManagerǁ__init____mutmut_6, 
        'xǁSubRosaManagerǁ__init____mutmut_7': xǁSubRosaManagerǁ__init____mutmut_7, 
        'xǁSubRosaManagerǁ__init____mutmut_8': xǁSubRosaManagerǁ__init____mutmut_8, 
        'xǁSubRosaManagerǁ__init____mutmut_9': xǁSubRosaManagerǁ__init____mutmut_9, 
        'xǁSubRosaManagerǁ__init____mutmut_10': xǁSubRosaManagerǁ__init____mutmut_10, 
        'xǁSubRosaManagerǁ__init____mutmut_11': xǁSubRosaManagerǁ__init____mutmut_11, 
        'xǁSubRosaManagerǁ__init____mutmut_12': xǁSubRosaManagerǁ__init____mutmut_12, 
        'xǁSubRosaManagerǁ__init____mutmut_13': xǁSubRosaManagerǁ__init____mutmut_13, 
        'xǁSubRosaManagerǁ__init____mutmut_14': xǁSubRosaManagerǁ__init____mutmut_14, 
        'xǁSubRosaManagerǁ__init____mutmut_15': xǁSubRosaManagerǁ__init____mutmut_15, 
        'xǁSubRosaManagerǁ__init____mutmut_16': xǁSubRosaManagerǁ__init____mutmut_16, 
        'xǁSubRosaManagerǁ__init____mutmut_17': xǁSubRosaManagerǁ__init____mutmut_17, 
        'xǁSubRosaManagerǁ__init____mutmut_18': xǁSubRosaManagerǁ__init____mutmut_18
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSubRosaManagerǁ__init____mutmut_orig)
    xǁSubRosaManagerǁ__init____mutmut_orig.__name__ = 'xǁSubRosaManagerǁ__init__'

    @property
    @abstractmethod
    def variant_name(self) -> str:
        """Variant name (e.g., 'bao' or 'vault')."""

    @property
    def tool_name(self) -> str:
        """Tool name for CLI - all variants use 'bao'."""
        return "bao"

    @property
    def executable_name(self) -> str:
        """Executable name in PATH."""
        return "bao"

    def xǁSubRosaManagerǁ_load_metadata__mutmut_orig(self) -> dict:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load subrosa metadata: {e}")
                return {}
        return {}

    def xǁSubRosaManagerǁ_load_metadata__mutmut_1(self) -> dict:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    return json.load(None)
            except Exception as e:
                logger.warning(f"Failed to load subrosa metadata: {e}")
                return {}
        return {}

    def xǁSubRosaManagerǁ_load_metadata__mutmut_2(self) -> dict:
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with self.metadata_file.open() as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(None)
                return {}
        return {}
    
    xǁSubRosaManagerǁ_load_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁ_load_metadata__mutmut_1': xǁSubRosaManagerǁ_load_metadata__mutmut_1, 
        'xǁSubRosaManagerǁ_load_metadata__mutmut_2': xǁSubRosaManagerǁ_load_metadata__mutmut_2
    }
    
    def _load_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁ_load_metadata__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁ_load_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _load_metadata.__signature__ = _mutmut_signature(xǁSubRosaManagerǁ_load_metadata__mutmut_orig)
    xǁSubRosaManagerǁ_load_metadata__mutmut_orig.__name__ = 'xǁSubRosaManagerǁ_load_metadata'

    def xǁSubRosaManagerǁ_save_metadata__mutmut_orig(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_1(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open(None) as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_2(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("XXwXX") as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_3(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("W") as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_4(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(None, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_5(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, None, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_6(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=None)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_7(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_8(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, indent=2)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_9(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, )
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_10(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=3)
        except Exception as e:
            logger.error(f"Failed to save subrosa metadata: {e}")

    def xǁSubRosaManagerǁ_save_metadata__mutmut_11(self) -> None:
        """Save metadata to JSON file."""
        try:
            with self.metadata_file.open("w") as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            logger.error(None)
    
    xǁSubRosaManagerǁ_save_metadata__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁ_save_metadata__mutmut_1': xǁSubRosaManagerǁ_save_metadata__mutmut_1, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_2': xǁSubRosaManagerǁ_save_metadata__mutmut_2, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_3': xǁSubRosaManagerǁ_save_metadata__mutmut_3, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_4': xǁSubRosaManagerǁ_save_metadata__mutmut_4, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_5': xǁSubRosaManagerǁ_save_metadata__mutmut_5, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_6': xǁSubRosaManagerǁ_save_metadata__mutmut_6, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_7': xǁSubRosaManagerǁ_save_metadata__mutmut_7, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_8': xǁSubRosaManagerǁ_save_metadata__mutmut_8, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_9': xǁSubRosaManagerǁ_save_metadata__mutmut_9, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_10': xǁSubRosaManagerǁ_save_metadata__mutmut_10, 
        'xǁSubRosaManagerǁ_save_metadata__mutmut_11': xǁSubRosaManagerǁ_save_metadata__mutmut_11
    }
    
    def _save_metadata(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁ_save_metadata__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁ_save_metadata__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _save_metadata.__signature__ = _mutmut_signature(xǁSubRosaManagerǁ_save_metadata__mutmut_orig)
    xǁSubRosaManagerǁ_save_metadata__mutmut_orig.__name__ = 'xǁSubRosaManagerǁ_save_metadata'

    def xǁSubRosaManagerǁget_binary_path__mutmut_orig(self, version: str) -> pathlib.Path:
        """Get path to installed binary for a version.

        Format: ~/.wrknv/subrosa/{variant}_{version}
        Example: ~/.wrknv/subrosa/bao_2.1.0
        """
        binary_name = f"{self.variant_name}_{version}"
        return self.install_path / binary_name

    def xǁSubRosaManagerǁget_binary_path__mutmut_1(self, version: str) -> pathlib.Path:
        """Get path to installed binary for a version.

        Format: ~/.wrknv/subrosa/{variant}_{version}
        Example: ~/.wrknv/subrosa/bao_2.1.0
        """
        binary_name = None
        return self.install_path / binary_name

    def xǁSubRosaManagerǁget_binary_path__mutmut_2(self, version: str) -> pathlib.Path:
        """Get path to installed binary for a version.

        Format: ~/.wrknv/subrosa/{variant}_{version}
        Example: ~/.wrknv/subrosa/bao_2.1.0
        """
        binary_name = f"{self.variant_name}_{version}"
        return self.install_path * binary_name
    
    xǁSubRosaManagerǁget_binary_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁget_binary_path__mutmut_1': xǁSubRosaManagerǁget_binary_path__mutmut_1, 
        'xǁSubRosaManagerǁget_binary_path__mutmut_2': xǁSubRosaManagerǁget_binary_path__mutmut_2
    }
    
    def get_binary_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁget_binary_path__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁget_binary_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_binary_path.__signature__ = _mutmut_signature(xǁSubRosaManagerǁget_binary_path__mutmut_orig)
    xǁSubRosaManagerǁget_binary_path__mutmut_orig.__name__ = 'xǁSubRosaManagerǁget_binary_path'

    def xǁSubRosaManagerǁget_installed_versions__mutmut_orig(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_1(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = None

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_2(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = None
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_3(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() or item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_4(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(None):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_5(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = None
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_6(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(None)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_7(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=None, reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_8(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=None)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_9(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_10(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), )
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_11(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: None, reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_12(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(None), reverse=True)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_13(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=False)
        except Exception:
            versions.sort(reverse=True)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_14(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=None)

        return versions

    def xǁSubRosaManagerǁget_installed_versions__mutmut_15(self) -> list[str]:
        """Get all installed versions of this variant."""
        versions = []

        prefix = f"{self.variant_name}_"
        for item in self.install_path.iterdir():
            if item.is_file() and item.name.startswith(prefix):
                # Extract version from filename
                version = item.name[len(prefix) :]
                versions.append(version)

        # Sort by version
        try:
            from packaging.version import parse as parse_version

            versions.sort(key=lambda v: parse_version(v), reverse=True)
        except Exception:
            versions.sort(reverse=False)

        return versions
    
    xǁSubRosaManagerǁget_installed_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁget_installed_versions__mutmut_1': xǁSubRosaManagerǁget_installed_versions__mutmut_1, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_2': xǁSubRosaManagerǁget_installed_versions__mutmut_2, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_3': xǁSubRosaManagerǁget_installed_versions__mutmut_3, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_4': xǁSubRosaManagerǁget_installed_versions__mutmut_4, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_5': xǁSubRosaManagerǁget_installed_versions__mutmut_5, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_6': xǁSubRosaManagerǁget_installed_versions__mutmut_6, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_7': xǁSubRosaManagerǁget_installed_versions__mutmut_7, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_8': xǁSubRosaManagerǁget_installed_versions__mutmut_8, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_9': xǁSubRosaManagerǁget_installed_versions__mutmut_9, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_10': xǁSubRosaManagerǁget_installed_versions__mutmut_10, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_11': xǁSubRosaManagerǁget_installed_versions__mutmut_11, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_12': xǁSubRosaManagerǁget_installed_versions__mutmut_12, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_13': xǁSubRosaManagerǁget_installed_versions__mutmut_13, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_14': xǁSubRosaManagerǁget_installed_versions__mutmut_14, 
        'xǁSubRosaManagerǁget_installed_versions__mutmut_15': xǁSubRosaManagerǁget_installed_versions__mutmut_15
    }
    
    def get_installed_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁget_installed_versions__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁget_installed_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_versions.__signature__ = _mutmut_signature(xǁSubRosaManagerǁget_installed_versions__mutmut_orig)
    xǁSubRosaManagerǁget_installed_versions__mutmut_orig.__name__ = 'xǁSubRosaManagerǁget_installed_versions'

    def xǁSubRosaManagerǁget_installed_version__mutmut_orig(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get("active_versions", {})
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_1(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = None
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_2(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get(None, {})
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_3(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get("active_versions", None)
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_4(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get({})
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_5(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get("active_versions", )
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_6(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get("XXactive_versionsXX", {})
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_7(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get("ACTIVE_VERSIONS", {})
        return active_versions.get(self.variant_name)

    def xǁSubRosaManagerǁget_installed_version__mutmut_8(self) -> str | None:
        """Get currently active version from metadata."""
        active_versions = self.metadata.get("active_versions", {})
        return active_versions.get(None)
    
    xǁSubRosaManagerǁget_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁget_installed_version__mutmut_1': xǁSubRosaManagerǁget_installed_version__mutmut_1, 
        'xǁSubRosaManagerǁget_installed_version__mutmut_2': xǁSubRosaManagerǁget_installed_version__mutmut_2, 
        'xǁSubRosaManagerǁget_installed_version__mutmut_3': xǁSubRosaManagerǁget_installed_version__mutmut_3, 
        'xǁSubRosaManagerǁget_installed_version__mutmut_4': xǁSubRosaManagerǁget_installed_version__mutmut_4, 
        'xǁSubRosaManagerǁget_installed_version__mutmut_5': xǁSubRosaManagerǁget_installed_version__mutmut_5, 
        'xǁSubRosaManagerǁget_installed_version__mutmut_6': xǁSubRosaManagerǁget_installed_version__mutmut_6, 
        'xǁSubRosaManagerǁget_installed_version__mutmut_7': xǁSubRosaManagerǁget_installed_version__mutmut_7, 
        'xǁSubRosaManagerǁget_installed_version__mutmut_8': xǁSubRosaManagerǁget_installed_version__mutmut_8
    }
    
    def get_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁget_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁget_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_installed_version.__signature__ = _mutmut_signature(xǁSubRosaManagerǁget_installed_version__mutmut_orig)
    xǁSubRosaManagerǁget_installed_version__mutmut_orig.__name__ = 'xǁSubRosaManagerǁget_installed_version'

    def xǁSubRosaManagerǁset_installed_version__mutmut_orig(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_1(self, version: str) -> None:
        """Set the active version in metadata."""
        if "XXactive_versionsXX" not in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_2(self, version: str) -> None:
        """Set the active version in metadata."""
        if "ACTIVE_VERSIONS" not in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_3(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_4(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["active_versions"] = None

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_5(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["XXactive_versionsXX"] = {}

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_6(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["ACTIVE_VERSIONS"] = {}

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_7(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["active_versions"][self.variant_name] = None
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_8(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["XXactive_versionsXX"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_9(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["ACTIVE_VERSIONS"][self.variant_name] = version
        self._save_metadata()

        logger.info(f"Set {self.variant_name} active version to {version}")

    def xǁSubRosaManagerǁset_installed_version__mutmut_10(self, version: str) -> None:
        """Set the active version in metadata."""
        if "active_versions" not in self.metadata:
            self.metadata["active_versions"] = {}

        self.metadata["active_versions"][self.variant_name] = version
        self._save_metadata()

        logger.info(None)
    
    xǁSubRosaManagerǁset_installed_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁset_installed_version__mutmut_1': xǁSubRosaManagerǁset_installed_version__mutmut_1, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_2': xǁSubRosaManagerǁset_installed_version__mutmut_2, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_3': xǁSubRosaManagerǁset_installed_version__mutmut_3, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_4': xǁSubRosaManagerǁset_installed_version__mutmut_4, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_5': xǁSubRosaManagerǁset_installed_version__mutmut_5, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_6': xǁSubRosaManagerǁset_installed_version__mutmut_6, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_7': xǁSubRosaManagerǁset_installed_version__mutmut_7, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_8': xǁSubRosaManagerǁset_installed_version__mutmut_8, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_9': xǁSubRosaManagerǁset_installed_version__mutmut_9, 
        'xǁSubRosaManagerǁset_installed_version__mutmut_10': xǁSubRosaManagerǁset_installed_version__mutmut_10
    }
    
    def set_installed_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁset_installed_version__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁset_installed_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_installed_version.__signature__ = _mutmut_signature(xǁSubRosaManagerǁset_installed_version__mutmut_orig)
    xǁSubRosaManagerǁset_installed_version__mutmut_orig.__name__ = 'xǁSubRosaManagerǁset_installed_version'

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_orig(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_1(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = None

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_2(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(None)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_3(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_4(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(None)
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_5(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = None

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_6(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir * self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_7(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() and symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_8(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(None, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_9(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=None)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_10(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_11(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, )

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_12(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=False)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_13(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(None)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_14(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(None)
            except OSError as e:
                logger.warning(f"Could not create symlink: {e}")

    def xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_15(self, version: str) -> None:
        """Update workenv bin symlink to point to active version."""
        binary_path = self.get_binary_path(version)

        if not binary_path.exists():
            logger.warning(f"Binary not found at {binary_path}, cannot update symlink")
            return

        # Create symlink in workenv bin directory
        if self.workenv_bin_dir:
            symlink_path = self.workenv_bin_dir / self.executable_name

            # Remove existing symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                safe_delete(symlink_path, missing_ok=True)

            try:
                symlink_path.symlink_to(binary_path)
                logger.info(f"Updated symlink: {symlink_path} -> {binary_path}")
            except OSError as e:
                logger.warning(None)
    
    xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_1': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_1, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_2': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_2, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_3': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_3, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_4': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_4, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_5': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_5, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_6': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_6, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_7': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_7, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_8': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_8, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_9': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_9, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_10': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_10, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_11': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_11, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_12': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_12, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_13': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_13, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_14': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_14, 
        'xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_15': xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_15
    }
    
    def _update_workenv_symlink(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_workenv_symlink.__signature__ = _mutmut_signature(xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_orig)
    xǁSubRosaManagerǁ_update_workenv_symlink__mutmut_orig.__name__ = 'xǁSubRosaManagerǁ_update_workenv_symlink'

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_orig(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_1(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_2(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_3(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_4(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_5(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_6(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_7(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_8(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_9(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_10(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_11(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_12(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_13(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_14(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_15(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_16(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_17(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(f"Could not regenerate env.sh: {e}")

    def xǁSubRosaManagerǁ_regenerate_env_script__mutmut_18(self) -> None:
        """Regenerate env.sh script with updated version."""
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
            logger.debug(None)
    
    xǁSubRosaManagerǁ_regenerate_env_script__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_1': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_1, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_2': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_2, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_3': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_3, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_4': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_4, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_5': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_5, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_6': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_6, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_7': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_7, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_8': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_8, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_9': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_9, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_10': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_10, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_11': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_11, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_12': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_12, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_13': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_13, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_14': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_14, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_15': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_15, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_16': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_16, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_17': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_17, 
        'xǁSubRosaManagerǁ_regenerate_env_script__mutmut_18': xǁSubRosaManagerǁ_regenerate_env_script__mutmut_18
    }
    
    def _regenerate_env_script(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁ_regenerate_env_script__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁ_regenerate_env_script__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _regenerate_env_script.__signature__ = _mutmut_signature(xǁSubRosaManagerǁ_regenerate_env_script__mutmut_orig)
    xǁSubRosaManagerǁ_regenerate_env_script__mutmut_orig.__name__ = 'xǁSubRosaManagerǁ_regenerate_env_script'

    def xǁSubRosaManagerǁswitch_version__mutmut_orig(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_1(self, version: str, dry_run: bool = True) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_2(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(None)
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_3(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_4(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(None).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_5(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(None)
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_6(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_7(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(None).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_8(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(None)
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_9(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(None, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_10(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=None)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_11(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_12(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, )

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_13(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=True)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_14(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(None)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_15(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(None)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(f"Switched to {self.variant_name} {version}")

    def xǁSubRosaManagerǁswitch_version__mutmut_16(self, version: str, dry_run: bool = False) -> None:
        """Switch to a specific version (like nvm use, tfswitch).

        This method:
        1. Installs the version if not present
        2. Updates workenv bin symlinks
        3. Sets active version in metadata
        4. Regenerates env.sh script

        Args:
            version: Version to switch to
            dry_run: If True, show what would be done without doing it
        """
        if dry_run:
            logger.info(f"[DRY-RUN] Would switch to {self.variant_name} {version}")
            if not self.get_binary_path(version).exists():
                logger.info(f"[DRY-RUN] Would install {self.variant_name} {version}")
            return

        # 1. Install if not present
        if not self.get_binary_path(version).exists():
            logger.info(f"Installing {self.variant_name} {version}...")
            self.install_version(version, dry_run=False)

        # 2. Update workenv symlinks
        self._update_workenv_symlink(version)

        # 3. Set active version
        self.set_installed_version(version)

        # 4. Regenerate env script
        self._regenerate_env_script()

        logger.info(None)
    
    xǁSubRosaManagerǁswitch_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁswitch_version__mutmut_1': xǁSubRosaManagerǁswitch_version__mutmut_1, 
        'xǁSubRosaManagerǁswitch_version__mutmut_2': xǁSubRosaManagerǁswitch_version__mutmut_2, 
        'xǁSubRosaManagerǁswitch_version__mutmut_3': xǁSubRosaManagerǁswitch_version__mutmut_3, 
        'xǁSubRosaManagerǁswitch_version__mutmut_4': xǁSubRosaManagerǁswitch_version__mutmut_4, 
        'xǁSubRosaManagerǁswitch_version__mutmut_5': xǁSubRosaManagerǁswitch_version__mutmut_5, 
        'xǁSubRosaManagerǁswitch_version__mutmut_6': xǁSubRosaManagerǁswitch_version__mutmut_6, 
        'xǁSubRosaManagerǁswitch_version__mutmut_7': xǁSubRosaManagerǁswitch_version__mutmut_7, 
        'xǁSubRosaManagerǁswitch_version__mutmut_8': xǁSubRosaManagerǁswitch_version__mutmut_8, 
        'xǁSubRosaManagerǁswitch_version__mutmut_9': xǁSubRosaManagerǁswitch_version__mutmut_9, 
        'xǁSubRosaManagerǁswitch_version__mutmut_10': xǁSubRosaManagerǁswitch_version__mutmut_10, 
        'xǁSubRosaManagerǁswitch_version__mutmut_11': xǁSubRosaManagerǁswitch_version__mutmut_11, 
        'xǁSubRosaManagerǁswitch_version__mutmut_12': xǁSubRosaManagerǁswitch_version__mutmut_12, 
        'xǁSubRosaManagerǁswitch_version__mutmut_13': xǁSubRosaManagerǁswitch_version__mutmut_13, 
        'xǁSubRosaManagerǁswitch_version__mutmut_14': xǁSubRosaManagerǁswitch_version__mutmut_14, 
        'xǁSubRosaManagerǁswitch_version__mutmut_15': xǁSubRosaManagerǁswitch_version__mutmut_15, 
        'xǁSubRosaManagerǁswitch_version__mutmut_16': xǁSubRosaManagerǁswitch_version__mutmut_16
    }
    
    def switch_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁswitch_version__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁswitch_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    switch_version.__signature__ = _mutmut_signature(xǁSubRosaManagerǁswitch_version__mutmut_orig)
    xǁSubRosaManagerǁswitch_version__mutmut_orig.__name__ = 'xǁSubRosaManagerǁswitch_version'

    def xǁSubRosaManagerǁremove_version__mutmut_orig(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_1(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = None

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_2(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(None)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_3(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(None)

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_4(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version or (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_5(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() != version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_6(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata or self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_7(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "XXactive_versionsXX" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_8(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "ACTIVE_VERSIONS" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_9(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" not in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_10(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name not in self.metadata["active_versions"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_11(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["XXactive_versionsXX"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_12(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["ACTIVE_VERSIONS"]
            ):
                del self.metadata["active_versions"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_13(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["XXactive_versionsXX"][self.variant_name]
                self._save_metadata()

    def xǁSubRosaManagerǁremove_version__mutmut_14(self, version: str) -> None:
        """Remove a specific version of the tool."""
        binary_path = self.get_binary_path(version)

        if binary_path.exists():
            binary_path.unlink()
            logger.info(f"Removed {self.variant_name} {version}")

            # Update metadata if this was the current version
            if self.get_installed_version() == version and (
                "active_versions" in self.metadata and self.variant_name in self.metadata["active_versions"]
            ):
                del self.metadata["ACTIVE_VERSIONS"][self.variant_name]
                self._save_metadata()
    
    xǁSubRosaManagerǁremove_version__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁremove_version__mutmut_1': xǁSubRosaManagerǁremove_version__mutmut_1, 
        'xǁSubRosaManagerǁremove_version__mutmut_2': xǁSubRosaManagerǁremove_version__mutmut_2, 
        'xǁSubRosaManagerǁremove_version__mutmut_3': xǁSubRosaManagerǁremove_version__mutmut_3, 
        'xǁSubRosaManagerǁremove_version__mutmut_4': xǁSubRosaManagerǁremove_version__mutmut_4, 
        'xǁSubRosaManagerǁremove_version__mutmut_5': xǁSubRosaManagerǁremove_version__mutmut_5, 
        'xǁSubRosaManagerǁremove_version__mutmut_6': xǁSubRosaManagerǁremove_version__mutmut_6, 
        'xǁSubRosaManagerǁremove_version__mutmut_7': xǁSubRosaManagerǁremove_version__mutmut_7, 
        'xǁSubRosaManagerǁremove_version__mutmut_8': xǁSubRosaManagerǁremove_version__mutmut_8, 
        'xǁSubRosaManagerǁremove_version__mutmut_9': xǁSubRosaManagerǁremove_version__mutmut_9, 
        'xǁSubRosaManagerǁremove_version__mutmut_10': xǁSubRosaManagerǁremove_version__mutmut_10, 
        'xǁSubRosaManagerǁremove_version__mutmut_11': xǁSubRosaManagerǁremove_version__mutmut_11, 
        'xǁSubRosaManagerǁremove_version__mutmut_12': xǁSubRosaManagerǁremove_version__mutmut_12, 
        'xǁSubRosaManagerǁremove_version__mutmut_13': xǁSubRosaManagerǁremove_version__mutmut_13, 
        'xǁSubRosaManagerǁremove_version__mutmut_14': xǁSubRosaManagerǁremove_version__mutmut_14
    }
    
    def remove_version(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁremove_version__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁremove_version__mutmut_mutants"), args, kwargs, self)
        return result 
    
    remove_version.__signature__ = _mutmut_signature(xǁSubRosaManagerǁremove_version__mutmut_orig)
    xǁSubRosaManagerǁremove_version__mutmut_orig.__name__ = 'xǁSubRosaManagerǁremove_version'

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_orig(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_1(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = None
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_2(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir * f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_3(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=None)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_4(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=False)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_5(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(None, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_6(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, None)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_7(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_8(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, )

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_9(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = ""
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_10(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(None):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_11(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() or file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_12(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name not in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_13(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = None
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_14(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    return

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_15(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_16(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(None)

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_17(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = None
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_18(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(None)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_19(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(None, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_20(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, None, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_21(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=None)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_22(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_23(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_24(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, )

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_25(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=False)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_26(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(None)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_27(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(None)

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_28(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_29(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(None):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_30(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(None)

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_31(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(None, missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_32(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=None)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_33(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(missing_ok=True)

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_34(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, )

    def xǁSubRosaManagerǁ_install_from_archive__mutmut_35(self, archive_path: pathlib.Path, version: str) -> None:
        """Install tool from downloaded archive.

        Subclasses can override this for variant-specific extraction logic.
        """
        # Create extraction directory
        extract_dir = self.cache_dir / f"{self.variant_name}_{version}_extract"
        extract_dir.mkdir(exist_ok=True)

        try:
            self.extract_archive(archive_path, extract_dir)

            # Find binary in extracted files
            binary_path = None
            for file_path in extract_dir.rglob(f"{self.variant_name}*"):
                if file_path.is_file() and file_path.name in [
                    self.variant_name,
                    f"{self.variant_name}.exe",
                ]:
                    binary_path = file_path
                    break

            if not binary_path:
                raise ToolManagerError(f"{self.variant_name} binary not found in archive")

            # Copy to target location
            target_path = self.get_binary_path(version)
            safe_copy(binary_path, target_path, overwrite=True)

            # Make executable (Unix systems)
            self.make_executable(target_path)

            logger.info(f"Installed {self.variant_name} binary to: {target_path}")

            # Verify installation
            if not self.verify_installation(version):
                raise ToolManagerError(f"{self.variant_name} {version} installation verification failed")

        finally:
            # Clean up extraction directory
            safe_rmtree(extract_dir, missing_ok=False)
    
    xǁSubRosaManagerǁ_install_from_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁ_install_from_archive__mutmut_1': xǁSubRosaManagerǁ_install_from_archive__mutmut_1, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_2': xǁSubRosaManagerǁ_install_from_archive__mutmut_2, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_3': xǁSubRosaManagerǁ_install_from_archive__mutmut_3, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_4': xǁSubRosaManagerǁ_install_from_archive__mutmut_4, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_5': xǁSubRosaManagerǁ_install_from_archive__mutmut_5, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_6': xǁSubRosaManagerǁ_install_from_archive__mutmut_6, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_7': xǁSubRosaManagerǁ_install_from_archive__mutmut_7, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_8': xǁSubRosaManagerǁ_install_from_archive__mutmut_8, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_9': xǁSubRosaManagerǁ_install_from_archive__mutmut_9, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_10': xǁSubRosaManagerǁ_install_from_archive__mutmut_10, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_11': xǁSubRosaManagerǁ_install_from_archive__mutmut_11, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_12': xǁSubRosaManagerǁ_install_from_archive__mutmut_12, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_13': xǁSubRosaManagerǁ_install_from_archive__mutmut_13, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_14': xǁSubRosaManagerǁ_install_from_archive__mutmut_14, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_15': xǁSubRosaManagerǁ_install_from_archive__mutmut_15, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_16': xǁSubRosaManagerǁ_install_from_archive__mutmut_16, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_17': xǁSubRosaManagerǁ_install_from_archive__mutmut_17, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_18': xǁSubRosaManagerǁ_install_from_archive__mutmut_18, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_19': xǁSubRosaManagerǁ_install_from_archive__mutmut_19, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_20': xǁSubRosaManagerǁ_install_from_archive__mutmut_20, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_21': xǁSubRosaManagerǁ_install_from_archive__mutmut_21, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_22': xǁSubRosaManagerǁ_install_from_archive__mutmut_22, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_23': xǁSubRosaManagerǁ_install_from_archive__mutmut_23, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_24': xǁSubRosaManagerǁ_install_from_archive__mutmut_24, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_25': xǁSubRosaManagerǁ_install_from_archive__mutmut_25, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_26': xǁSubRosaManagerǁ_install_from_archive__mutmut_26, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_27': xǁSubRosaManagerǁ_install_from_archive__mutmut_27, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_28': xǁSubRosaManagerǁ_install_from_archive__mutmut_28, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_29': xǁSubRosaManagerǁ_install_from_archive__mutmut_29, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_30': xǁSubRosaManagerǁ_install_from_archive__mutmut_30, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_31': xǁSubRosaManagerǁ_install_from_archive__mutmut_31, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_32': xǁSubRosaManagerǁ_install_from_archive__mutmut_32, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_33': xǁSubRosaManagerǁ_install_from_archive__mutmut_33, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_34': xǁSubRosaManagerǁ_install_from_archive__mutmut_34, 
        'xǁSubRosaManagerǁ_install_from_archive__mutmut_35': xǁSubRosaManagerǁ_install_from_archive__mutmut_35
    }
    
    def _install_from_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁ_install_from_archive__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁ_install_from_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _install_from_archive.__signature__ = _mutmut_signature(xǁSubRosaManagerǁ_install_from_archive__mutmut_orig)
    xǁSubRosaManagerǁ_install_from_archive__mutmut_orig.__name__ = 'xǁSubRosaManagerǁ_install_from_archive'

    def xǁSubRosaManagerǁverify_installation__mutmut_orig(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_1(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = None
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_2(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(None)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_3(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_4(self, version: str) -> bool:
        """Verify that installation works and version matches."""
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_5(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_6(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = None

            if result.returncode == 0:
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_7(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_8(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_9(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_10(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_11(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_12(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_13(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_14(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
            return False

        try:
            from provide.foundation.process import run

            result = run(
                [str(binary_path), "version"],
                capture_output=True,
                text=True,
                )

            if result.returncode == 0:
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_15(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_16(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_17(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_18(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_19(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_20(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_21(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_22(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_23(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout and f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_24(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version not in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_25(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" not in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_26(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(None)
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_27(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return False
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_28(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(None)
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_29(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(None)

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_30(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return True

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_31(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(None)
            return False

    def xǁSubRosaManagerǁverify_installation__mutmut_32(self, version: str) -> bool:
        """Verify that installation works and version matches."""
        binary_path = self.get_binary_path(version)
        if not binary_path.exists():
            logger.error(f"{self.variant_name} binary not found at {binary_path}")
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
                # Check if version is in output
                if version in result.stdout or f"v{version}" in result.stdout:
                    logger.debug(f"{self.variant_name} {version} verification successful")
                    return True
                else:
                    logger.error(f"Version mismatch in {self.variant_name} output: {result.stdout}")
            else:
                logger.error(f"{self.variant_name} version command failed: {result.stderr}")

            return False

        except Exception as e:
            logger.error(f"Failed to verify {self.variant_name} installation: {e}")
            return True
    
    xǁSubRosaManagerǁverify_installation__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSubRosaManagerǁverify_installation__mutmut_1': xǁSubRosaManagerǁverify_installation__mutmut_1, 
        'xǁSubRosaManagerǁverify_installation__mutmut_2': xǁSubRosaManagerǁverify_installation__mutmut_2, 
        'xǁSubRosaManagerǁverify_installation__mutmut_3': xǁSubRosaManagerǁverify_installation__mutmut_3, 
        'xǁSubRosaManagerǁverify_installation__mutmut_4': xǁSubRosaManagerǁverify_installation__mutmut_4, 
        'xǁSubRosaManagerǁverify_installation__mutmut_5': xǁSubRosaManagerǁverify_installation__mutmut_5, 
        'xǁSubRosaManagerǁverify_installation__mutmut_6': xǁSubRosaManagerǁverify_installation__mutmut_6, 
        'xǁSubRosaManagerǁverify_installation__mutmut_7': xǁSubRosaManagerǁverify_installation__mutmut_7, 
        'xǁSubRosaManagerǁverify_installation__mutmut_8': xǁSubRosaManagerǁverify_installation__mutmut_8, 
        'xǁSubRosaManagerǁverify_installation__mutmut_9': xǁSubRosaManagerǁverify_installation__mutmut_9, 
        'xǁSubRosaManagerǁverify_installation__mutmut_10': xǁSubRosaManagerǁverify_installation__mutmut_10, 
        'xǁSubRosaManagerǁverify_installation__mutmut_11': xǁSubRosaManagerǁverify_installation__mutmut_11, 
        'xǁSubRosaManagerǁverify_installation__mutmut_12': xǁSubRosaManagerǁverify_installation__mutmut_12, 
        'xǁSubRosaManagerǁverify_installation__mutmut_13': xǁSubRosaManagerǁverify_installation__mutmut_13, 
        'xǁSubRosaManagerǁverify_installation__mutmut_14': xǁSubRosaManagerǁverify_installation__mutmut_14, 
        'xǁSubRosaManagerǁverify_installation__mutmut_15': xǁSubRosaManagerǁverify_installation__mutmut_15, 
        'xǁSubRosaManagerǁverify_installation__mutmut_16': xǁSubRosaManagerǁverify_installation__mutmut_16, 
        'xǁSubRosaManagerǁverify_installation__mutmut_17': xǁSubRosaManagerǁverify_installation__mutmut_17, 
        'xǁSubRosaManagerǁverify_installation__mutmut_18': xǁSubRosaManagerǁverify_installation__mutmut_18, 
        'xǁSubRosaManagerǁverify_installation__mutmut_19': xǁSubRosaManagerǁverify_installation__mutmut_19, 
        'xǁSubRosaManagerǁverify_installation__mutmut_20': xǁSubRosaManagerǁverify_installation__mutmut_20, 
        'xǁSubRosaManagerǁverify_installation__mutmut_21': xǁSubRosaManagerǁverify_installation__mutmut_21, 
        'xǁSubRosaManagerǁverify_installation__mutmut_22': xǁSubRosaManagerǁverify_installation__mutmut_22, 
        'xǁSubRosaManagerǁverify_installation__mutmut_23': xǁSubRosaManagerǁverify_installation__mutmut_23, 
        'xǁSubRosaManagerǁverify_installation__mutmut_24': xǁSubRosaManagerǁverify_installation__mutmut_24, 
        'xǁSubRosaManagerǁverify_installation__mutmut_25': xǁSubRosaManagerǁverify_installation__mutmut_25, 
        'xǁSubRosaManagerǁverify_installation__mutmut_26': xǁSubRosaManagerǁverify_installation__mutmut_26, 
        'xǁSubRosaManagerǁverify_installation__mutmut_27': xǁSubRosaManagerǁverify_installation__mutmut_27, 
        'xǁSubRosaManagerǁverify_installation__mutmut_28': xǁSubRosaManagerǁverify_installation__mutmut_28, 
        'xǁSubRosaManagerǁverify_installation__mutmut_29': xǁSubRosaManagerǁverify_installation__mutmut_29, 
        'xǁSubRosaManagerǁverify_installation__mutmut_30': xǁSubRosaManagerǁverify_installation__mutmut_30, 
        'xǁSubRosaManagerǁverify_installation__mutmut_31': xǁSubRosaManagerǁverify_installation__mutmut_31, 
        'xǁSubRosaManagerǁverify_installation__mutmut_32': xǁSubRosaManagerǁverify_installation__mutmut_32
    }
    
    def verify_installation(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSubRosaManagerǁverify_installation__mutmut_orig"), object.__getattribute__(self, "xǁSubRosaManagerǁverify_installation__mutmut_mutants"), args, kwargs, self)
        return result 
    
    verify_installation.__signature__ = _mutmut_signature(xǁSubRosaManagerǁverify_installation__mutmut_orig)
    xǁSubRosaManagerǁverify_installation__mutmut_orig.__name__ = 'xǁSubRosaManagerǁverify_installation'


__all__ = [
    "SubRosaManager",
]

# 🧰🌍🔚
