#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Template Handler for Gitignore Files
=====================================
Manages gitignore templates from GitHub's collection."""

from __future__ import annotations

from pathlib import Path
import tempfile

from provide.foundation import logger
from provide.foundation.archive.operations import ArchiveOperations
from provide.foundation.file import safe_move, safe_rmtree
from provide.foundation.resilience import retry
from provide.foundation.transport import get
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


class TemplateHandler:
    """Handles gitignore template operations including caching and GitHub sync."""

    GITHUB_REPO = "https://github.com/github/gitignore"
    GITHUB_ARCHIVE = "https://github.com/github/gitignore/archive/refs/heads/main.tar.gz"
    GITHUB_API = "https://api.github.com/repos/github/gitignore"

    def xǁTemplateHandlerǁ__init____mutmut_orig(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_1(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = None
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_2(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir and Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_3(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" * "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_4(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() * ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_5(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / "XX.wrknvXX" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_6(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".WRKNV" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_7(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "XXgitignore-templatesXX"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_8(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "GITIGNORE-TEMPLATES"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_9(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = None
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_10(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(None)

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_11(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_12(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(None)
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_13(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=None, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_14(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=None)

    def xǁTemplateHandlerǁ__init____mutmut_15(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_16(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, )

    def xǁTemplateHandlerǁ__init____mutmut_17(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=False, exist_ok=True)

    def xǁTemplateHandlerǁ__init____mutmut_18(self, cache_dir: Path | None = None) -> None:
        """
        Initialize template handler.

        Args:
            cache_dir: Directory for caching templates (default: ~/.wrknv/gitignore-templates)
        """
        self.cache_dir = cache_dir or Path.home() / ".wrknv" / "gitignore-templates"
        self.cache_dir = self.cache_dir.expanduser()
        if logger.is_debug_enabled():
            logger.debug(f"TemplateHandler initialized with cache_dir: {self.cache_dir}")

        # Create cache directory if it doesn't exist
        if not self.cache_dir.exists():
            logger.info(f"Creating gitignore template cache directory: {self.cache_dir}")
            self.cache_dir.mkdir(parents=True, exist_ok=False)
    
    xǁTemplateHandlerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTemplateHandlerǁ__init____mutmut_1': xǁTemplateHandlerǁ__init____mutmut_1, 
        'xǁTemplateHandlerǁ__init____mutmut_2': xǁTemplateHandlerǁ__init____mutmut_2, 
        'xǁTemplateHandlerǁ__init____mutmut_3': xǁTemplateHandlerǁ__init____mutmut_3, 
        'xǁTemplateHandlerǁ__init____mutmut_4': xǁTemplateHandlerǁ__init____mutmut_4, 
        'xǁTemplateHandlerǁ__init____mutmut_5': xǁTemplateHandlerǁ__init____mutmut_5, 
        'xǁTemplateHandlerǁ__init____mutmut_6': xǁTemplateHandlerǁ__init____mutmut_6, 
        'xǁTemplateHandlerǁ__init____mutmut_7': xǁTemplateHandlerǁ__init____mutmut_7, 
        'xǁTemplateHandlerǁ__init____mutmut_8': xǁTemplateHandlerǁ__init____mutmut_8, 
        'xǁTemplateHandlerǁ__init____mutmut_9': xǁTemplateHandlerǁ__init____mutmut_9, 
        'xǁTemplateHandlerǁ__init____mutmut_10': xǁTemplateHandlerǁ__init____mutmut_10, 
        'xǁTemplateHandlerǁ__init____mutmut_11': xǁTemplateHandlerǁ__init____mutmut_11, 
        'xǁTemplateHandlerǁ__init____mutmut_12': xǁTemplateHandlerǁ__init____mutmut_12, 
        'xǁTemplateHandlerǁ__init____mutmut_13': xǁTemplateHandlerǁ__init____mutmut_13, 
        'xǁTemplateHandlerǁ__init____mutmut_14': xǁTemplateHandlerǁ__init____mutmut_14, 
        'xǁTemplateHandlerǁ__init____mutmut_15': xǁTemplateHandlerǁ__init____mutmut_15, 
        'xǁTemplateHandlerǁ__init____mutmut_16': xǁTemplateHandlerǁ__init____mutmut_16, 
        'xǁTemplateHandlerǁ__init____mutmut_17': xǁTemplateHandlerǁ__init____mutmut_17, 
        'xǁTemplateHandlerǁ__init____mutmut_18': xǁTemplateHandlerǁ__init____mutmut_18
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTemplateHandlerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTemplateHandlerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTemplateHandlerǁ__init____mutmut_orig)
    xǁTemplateHandlerǁ__init____mutmut_orig.__name__ = 'xǁTemplateHandlerǁ__init__'

    def xǁTemplateHandlerǁupdate_cache__mutmut_orig(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_1(self, force: bool = True) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_2(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir * ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_3(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / "XX.versionXX"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_4(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".VERSION"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_5(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force or self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_6(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_7(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug(None)
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_8(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("XXTemplate cache is valid, skipping updateXX")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_9(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_10(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("TEMPLATE CACHE IS VALID, SKIPPING UPDATE")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_11(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return True

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_12(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info(None)

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_13(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("XXUpdating gitignore templates from GitHub...XX")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_14(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("updating gitignore templates from github...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_15(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("UPDATING GITIGNORE TEMPLATES FROM GITHUB...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_16(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=None, delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_17(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=None) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_18(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_19(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", ) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_20(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix="XX.tar.gzXX", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_21(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".TAR.GZ", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_22(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=True) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_23(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = None

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_24(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(None)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_25(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(None)
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_26(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(None, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_27(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, None, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_28(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=None)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_29(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_30(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_31(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, )

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_32(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=True)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_33(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug(None)
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_34(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("XXExtracting templates archiveXX")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_35(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_36(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("EXTRACTING TEMPLATES ARCHIVE")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_37(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(None, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_38(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, None)

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_39(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_40(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, )

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_41(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(None))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_42(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = None
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_43(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(None)
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_44(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(None).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_45(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_46(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError(None)

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_47(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("XXArchive is emptyXX")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_48(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_49(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("ARCHIVE IS EMPTY")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_50(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = None

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_51(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[1] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_52(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) != 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_53(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 2 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_54(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(None)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_55(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug(None)
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_56(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("XXClearing existing cacheXX")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_57(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_58(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("CLEARING EXISTING CACHE")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_59(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(None)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_60(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(None, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_61(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, None)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_62(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_63(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, )

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_64(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(None)
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_65(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return False

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_66(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(None)
            return False

    def xǁTemplateHandlerǁupdate_cache__mutmut_67(self, force: bool = False) -> bool:
        """
        Update the template cache from GitHub.

        Args:
            force: Force update even if cache exists

        Returns:
            True if cache was updated, False otherwise
        """
        self.cache_dir / ".version"

        # Check if update is needed
        if not force and self._is_cache_valid():
            logger.debug("Template cache is valid, skipping update")
            return False

        logger.info("Updating gitignore templates from GitHub...")

        try:
            # Download archive to temp file using foundation download
            from wrknv.wenv.operations.download import download_file

            # Use NamedTemporaryFile but don't delete automatically
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            if logger.is_debug_enabled():
                logger.debug(f"Downloading templates archive to {tmp_path}")
            download_file(self.GITHUB_ARCHIVE, tmp_path, show_progress=False)

            # Extract archive using foundation utilities
            logger.debug("Extracting templates archive")
            with tempfile.TemporaryDirectory() as extract_dir:
                # Extract with security validation (path traversal protection)
                ArchiveOperations.extract_tar_gz(tmp_path, Path(extract_dir))

                # Find root directory (usually gitignore-main)
                extracted_items = list(Path(extract_dir).iterdir())
                if not extracted_items:
                    raise ValueError("Archive is empty")

                source_dir = extracted_items[0] if len(extracted_items) == 1 else Path(extract_dir)

                # Clear existing cache
                if self.cache_dir.exists():
                    logger.debug("Clearing existing cache")
                    safe_rmtree(self.cache_dir)

                # Move extracted files to cache
                safe_move(source_dir, self.cache_dir)

            # Clean up temp file
            tmp_path.unlink()

            # Update version file with current commit
            self._update_version_file()

            logger.info(f"Successfully updated templates in {self.cache_dir}")
            return True

        except Exception as e:
            logger.error(f"Failed to update template cache: {e}")
            return True
    
    xǁTemplateHandlerǁupdate_cache__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTemplateHandlerǁupdate_cache__mutmut_1': xǁTemplateHandlerǁupdate_cache__mutmut_1, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_2': xǁTemplateHandlerǁupdate_cache__mutmut_2, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_3': xǁTemplateHandlerǁupdate_cache__mutmut_3, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_4': xǁTemplateHandlerǁupdate_cache__mutmut_4, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_5': xǁTemplateHandlerǁupdate_cache__mutmut_5, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_6': xǁTemplateHandlerǁupdate_cache__mutmut_6, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_7': xǁTemplateHandlerǁupdate_cache__mutmut_7, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_8': xǁTemplateHandlerǁupdate_cache__mutmut_8, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_9': xǁTemplateHandlerǁupdate_cache__mutmut_9, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_10': xǁTemplateHandlerǁupdate_cache__mutmut_10, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_11': xǁTemplateHandlerǁupdate_cache__mutmut_11, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_12': xǁTemplateHandlerǁupdate_cache__mutmut_12, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_13': xǁTemplateHandlerǁupdate_cache__mutmut_13, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_14': xǁTemplateHandlerǁupdate_cache__mutmut_14, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_15': xǁTemplateHandlerǁupdate_cache__mutmut_15, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_16': xǁTemplateHandlerǁupdate_cache__mutmut_16, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_17': xǁTemplateHandlerǁupdate_cache__mutmut_17, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_18': xǁTemplateHandlerǁupdate_cache__mutmut_18, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_19': xǁTemplateHandlerǁupdate_cache__mutmut_19, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_20': xǁTemplateHandlerǁupdate_cache__mutmut_20, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_21': xǁTemplateHandlerǁupdate_cache__mutmut_21, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_22': xǁTemplateHandlerǁupdate_cache__mutmut_22, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_23': xǁTemplateHandlerǁupdate_cache__mutmut_23, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_24': xǁTemplateHandlerǁupdate_cache__mutmut_24, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_25': xǁTemplateHandlerǁupdate_cache__mutmut_25, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_26': xǁTemplateHandlerǁupdate_cache__mutmut_26, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_27': xǁTemplateHandlerǁupdate_cache__mutmut_27, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_28': xǁTemplateHandlerǁupdate_cache__mutmut_28, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_29': xǁTemplateHandlerǁupdate_cache__mutmut_29, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_30': xǁTemplateHandlerǁupdate_cache__mutmut_30, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_31': xǁTemplateHandlerǁupdate_cache__mutmut_31, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_32': xǁTemplateHandlerǁupdate_cache__mutmut_32, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_33': xǁTemplateHandlerǁupdate_cache__mutmut_33, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_34': xǁTemplateHandlerǁupdate_cache__mutmut_34, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_35': xǁTemplateHandlerǁupdate_cache__mutmut_35, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_36': xǁTemplateHandlerǁupdate_cache__mutmut_36, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_37': xǁTemplateHandlerǁupdate_cache__mutmut_37, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_38': xǁTemplateHandlerǁupdate_cache__mutmut_38, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_39': xǁTemplateHandlerǁupdate_cache__mutmut_39, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_40': xǁTemplateHandlerǁupdate_cache__mutmut_40, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_41': xǁTemplateHandlerǁupdate_cache__mutmut_41, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_42': xǁTemplateHandlerǁupdate_cache__mutmut_42, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_43': xǁTemplateHandlerǁupdate_cache__mutmut_43, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_44': xǁTemplateHandlerǁupdate_cache__mutmut_44, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_45': xǁTemplateHandlerǁupdate_cache__mutmut_45, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_46': xǁTemplateHandlerǁupdate_cache__mutmut_46, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_47': xǁTemplateHandlerǁupdate_cache__mutmut_47, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_48': xǁTemplateHandlerǁupdate_cache__mutmut_48, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_49': xǁTemplateHandlerǁupdate_cache__mutmut_49, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_50': xǁTemplateHandlerǁupdate_cache__mutmut_50, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_51': xǁTemplateHandlerǁupdate_cache__mutmut_51, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_52': xǁTemplateHandlerǁupdate_cache__mutmut_52, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_53': xǁTemplateHandlerǁupdate_cache__mutmut_53, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_54': xǁTemplateHandlerǁupdate_cache__mutmut_54, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_55': xǁTemplateHandlerǁupdate_cache__mutmut_55, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_56': xǁTemplateHandlerǁupdate_cache__mutmut_56, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_57': xǁTemplateHandlerǁupdate_cache__mutmut_57, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_58': xǁTemplateHandlerǁupdate_cache__mutmut_58, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_59': xǁTemplateHandlerǁupdate_cache__mutmut_59, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_60': xǁTemplateHandlerǁupdate_cache__mutmut_60, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_61': xǁTemplateHandlerǁupdate_cache__mutmut_61, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_62': xǁTemplateHandlerǁupdate_cache__mutmut_62, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_63': xǁTemplateHandlerǁupdate_cache__mutmut_63, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_64': xǁTemplateHandlerǁupdate_cache__mutmut_64, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_65': xǁTemplateHandlerǁupdate_cache__mutmut_65, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_66': xǁTemplateHandlerǁupdate_cache__mutmut_66, 
        'xǁTemplateHandlerǁupdate_cache__mutmut_67': xǁTemplateHandlerǁupdate_cache__mutmut_67
    }
    
    def update_cache(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTemplateHandlerǁupdate_cache__mutmut_orig"), object.__getattribute__(self, "xǁTemplateHandlerǁupdate_cache__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_cache.__signature__ = _mutmut_signature(xǁTemplateHandlerǁupdate_cache__mutmut_orig)
    xǁTemplateHandlerǁupdate_cache__mutmut_orig.__name__ = 'xǁTemplateHandlerǁupdate_cache'

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_orig(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_1(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = None

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_2(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir * ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_3(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / "XX.versionXX"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_4(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".VERSION"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_5(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_6(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug(None)
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_7(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("XXNo version file found, cache invalidXX")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_8(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("no version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_9(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("NO VERSION FILE FOUND, CACHE INVALID")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_10(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return True

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_11(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = None
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_12(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["XXPython.gitignoreXX", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_13(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_14(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["PYTHON.GITIGNORE", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_15(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "XXNode.gitignoreXX", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_16(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_17(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "NODE.GITIGNORE", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_18(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "XXGo.gitignoreXX"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_19(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_20(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "GO.GITIGNORE"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_21(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_22(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir * template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_23(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(None)
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_24(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return True

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_25(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug(None)
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_26(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("XXCache validation passedXX")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_27(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("cache validation passed")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_28(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("CACHE VALIDATION PASSED")
        return True

    def xǁTemplateHandlerǁ_is_cache_valid__mutmut_29(self) -> bool:
        """Check if the cache is valid and recent enough."""
        version_file = self.cache_dir / ".version"

        if not version_file.exists():
            logger.debug("No version file found, cache invalid")
            return False

        # Check if basic templates exist
        essential_templates = ["Python.gitignore", "Node.gitignore", "Go.gitignore"]
        for template in essential_templates:
            if not (self.cache_dir / template).exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Essential template {template} missing, cache invalid")
                return False

        # Cache is considered valid if version file exists and essential templates are present
        logger.debug("Cache validation passed")
        return False
    
    xǁTemplateHandlerǁ_is_cache_valid__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTemplateHandlerǁ_is_cache_valid__mutmut_1': xǁTemplateHandlerǁ_is_cache_valid__mutmut_1, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_2': xǁTemplateHandlerǁ_is_cache_valid__mutmut_2, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_3': xǁTemplateHandlerǁ_is_cache_valid__mutmut_3, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_4': xǁTemplateHandlerǁ_is_cache_valid__mutmut_4, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_5': xǁTemplateHandlerǁ_is_cache_valid__mutmut_5, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_6': xǁTemplateHandlerǁ_is_cache_valid__mutmut_6, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_7': xǁTemplateHandlerǁ_is_cache_valid__mutmut_7, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_8': xǁTemplateHandlerǁ_is_cache_valid__mutmut_8, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_9': xǁTemplateHandlerǁ_is_cache_valid__mutmut_9, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_10': xǁTemplateHandlerǁ_is_cache_valid__mutmut_10, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_11': xǁTemplateHandlerǁ_is_cache_valid__mutmut_11, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_12': xǁTemplateHandlerǁ_is_cache_valid__mutmut_12, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_13': xǁTemplateHandlerǁ_is_cache_valid__mutmut_13, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_14': xǁTemplateHandlerǁ_is_cache_valid__mutmut_14, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_15': xǁTemplateHandlerǁ_is_cache_valid__mutmut_15, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_16': xǁTemplateHandlerǁ_is_cache_valid__mutmut_16, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_17': xǁTemplateHandlerǁ_is_cache_valid__mutmut_17, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_18': xǁTemplateHandlerǁ_is_cache_valid__mutmut_18, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_19': xǁTemplateHandlerǁ_is_cache_valid__mutmut_19, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_20': xǁTemplateHandlerǁ_is_cache_valid__mutmut_20, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_21': xǁTemplateHandlerǁ_is_cache_valid__mutmut_21, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_22': xǁTemplateHandlerǁ_is_cache_valid__mutmut_22, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_23': xǁTemplateHandlerǁ_is_cache_valid__mutmut_23, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_24': xǁTemplateHandlerǁ_is_cache_valid__mutmut_24, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_25': xǁTemplateHandlerǁ_is_cache_valid__mutmut_25, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_26': xǁTemplateHandlerǁ_is_cache_valid__mutmut_26, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_27': xǁTemplateHandlerǁ_is_cache_valid__mutmut_27, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_28': xǁTemplateHandlerǁ_is_cache_valid__mutmut_28, 
        'xǁTemplateHandlerǁ_is_cache_valid__mutmut_29': xǁTemplateHandlerǁ_is_cache_valid__mutmut_29
    }
    
    def _is_cache_valid(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTemplateHandlerǁ_is_cache_valid__mutmut_orig"), object.__getattribute__(self, "xǁTemplateHandlerǁ_is_cache_valid__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_cache_valid.__signature__ = _mutmut_signature(xǁTemplateHandlerǁ_is_cache_valid__mutmut_orig)
    xǁTemplateHandlerǁ_is_cache_valid__mutmut_orig.__name__ = 'xǁTemplateHandlerǁ_is_cache_valid'

    @retry(Exception, max_attempts=3, base_delay=1.0)
    def _fetch_commit_sha(self) -> str:
        """Fetch latest commit SHA from GitHub API with retry."""
        import asyncio

        logger.debug("Fetching latest commit SHA from GitHub API")
        response = asyncio.run(get(f"{self.GITHUB_API}/commits/main"))
        data = response.json()
        sha: str = data["sha"]
        return sha[:8]

    def _fallback_version(self) -> str:
        """Fallback version identifier using timestamp."""
        from provide.foundation.time import provide_now

        return provide_now().isoformat()

    def xǁTemplateHandlerǁ_update_version_file__mutmut_orig(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / ".version"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_1(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = None

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_2(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir * ".version"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_3(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / "XX.versionXX"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_4(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / ".VERSION"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_5(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / ".version"

        try:
            commit_sha = None
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_6(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / ".version"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(None)
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_7(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / ".version"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = None

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_8(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / ".version"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(None)
        if logger.is_debug_enabled():
            logger.debug(f"Updated version file with: {commit_sha}")

    def xǁTemplateHandlerǁ_update_version_file__mutmut_9(self) -> None:
        """Update the version file with current information.

        Uses GitHub API with retry, falls back to timestamp if unavailable.
        """
        version_file = self.cache_dir / ".version"

        try:
            commit_sha = self._fetch_commit_sha()
        except Exception as e:
            logger.warning(f"Could not fetch commit SHA after retries: {e}, using timestamp fallback")
            commit_sha = self._fallback_version()

        version_file.write_text(commit_sha)
        if logger.is_debug_enabled():
            logger.debug(None)
    
    xǁTemplateHandlerǁ_update_version_file__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTemplateHandlerǁ_update_version_file__mutmut_1': xǁTemplateHandlerǁ_update_version_file__mutmut_1, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_2': xǁTemplateHandlerǁ_update_version_file__mutmut_2, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_3': xǁTemplateHandlerǁ_update_version_file__mutmut_3, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_4': xǁTemplateHandlerǁ_update_version_file__mutmut_4, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_5': xǁTemplateHandlerǁ_update_version_file__mutmut_5, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_6': xǁTemplateHandlerǁ_update_version_file__mutmut_6, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_7': xǁTemplateHandlerǁ_update_version_file__mutmut_7, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_8': xǁTemplateHandlerǁ_update_version_file__mutmut_8, 
        'xǁTemplateHandlerǁ_update_version_file__mutmut_9': xǁTemplateHandlerǁ_update_version_file__mutmut_9
    }
    
    def _update_version_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTemplateHandlerǁ_update_version_file__mutmut_orig"), object.__getattribute__(self, "xǁTemplateHandlerǁ_update_version_file__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_version_file.__signature__ = _mutmut_signature(xǁTemplateHandlerǁ_update_version_file__mutmut_orig)
    xǁTemplateHandlerǁ_update_version_file__mutmut_orig.__name__ = 'xǁTemplateHandlerǁ_update_version_file'

    def xǁTemplateHandlerǁget_template__mutmut_orig(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_1(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_2(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info(None)
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_3(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("XXCache invalid, updating templates...XX")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_4(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_5(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("CACHE INVALID, UPDATING TEMPLATES...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_6(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = None

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_7(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir * f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_8(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" * f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_9(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir * "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_10(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "XXGlobalXX" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_11(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_12(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "GLOBAL" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_13(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" * f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_14(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir * "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_15(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "XXcommunityXX" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_16(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "COMMUNITY" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_17(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(None)
                return path.read_text()

        logger.warning(f"Template '{name}' not found in cache")
        return None

    def xǁTemplateHandlerǁget_template__mutmut_18(self, name: str) -> str | None:
        """
        Get the content of a gitignore template.

        Args:
            name: Template name (e.g., "Python", "Node")

        Returns:
            Template content or None if not found
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        # Try different locations for the template
        possible_paths = [
            self.cache_dir / f"{name}.gitignore",
            self.cache_dir / "Global" / f"{name}.gitignore",
            self.cache_dir / "community" / f"{name}.gitignore",
        ]

        for path in possible_paths:
            if path.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Found template at {path}")
                return path.read_text()

        logger.warning(None)
        return None
    
    xǁTemplateHandlerǁget_template__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTemplateHandlerǁget_template__mutmut_1': xǁTemplateHandlerǁget_template__mutmut_1, 
        'xǁTemplateHandlerǁget_template__mutmut_2': xǁTemplateHandlerǁget_template__mutmut_2, 
        'xǁTemplateHandlerǁget_template__mutmut_3': xǁTemplateHandlerǁget_template__mutmut_3, 
        'xǁTemplateHandlerǁget_template__mutmut_4': xǁTemplateHandlerǁget_template__mutmut_4, 
        'xǁTemplateHandlerǁget_template__mutmut_5': xǁTemplateHandlerǁget_template__mutmut_5, 
        'xǁTemplateHandlerǁget_template__mutmut_6': xǁTemplateHandlerǁget_template__mutmut_6, 
        'xǁTemplateHandlerǁget_template__mutmut_7': xǁTemplateHandlerǁget_template__mutmut_7, 
        'xǁTemplateHandlerǁget_template__mutmut_8': xǁTemplateHandlerǁget_template__mutmut_8, 
        'xǁTemplateHandlerǁget_template__mutmut_9': xǁTemplateHandlerǁget_template__mutmut_9, 
        'xǁTemplateHandlerǁget_template__mutmut_10': xǁTemplateHandlerǁget_template__mutmut_10, 
        'xǁTemplateHandlerǁget_template__mutmut_11': xǁTemplateHandlerǁget_template__mutmut_11, 
        'xǁTemplateHandlerǁget_template__mutmut_12': xǁTemplateHandlerǁget_template__mutmut_12, 
        'xǁTemplateHandlerǁget_template__mutmut_13': xǁTemplateHandlerǁget_template__mutmut_13, 
        'xǁTemplateHandlerǁget_template__mutmut_14': xǁTemplateHandlerǁget_template__mutmut_14, 
        'xǁTemplateHandlerǁget_template__mutmut_15': xǁTemplateHandlerǁget_template__mutmut_15, 
        'xǁTemplateHandlerǁget_template__mutmut_16': xǁTemplateHandlerǁget_template__mutmut_16, 
        'xǁTemplateHandlerǁget_template__mutmut_17': xǁTemplateHandlerǁget_template__mutmut_17, 
        'xǁTemplateHandlerǁget_template__mutmut_18': xǁTemplateHandlerǁget_template__mutmut_18
    }
    
    def get_template(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTemplateHandlerǁget_template__mutmut_orig"), object.__getattribute__(self, "xǁTemplateHandlerǁget_template__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_template.__signature__ = _mutmut_signature(xǁTemplateHandlerǁget_template__mutmut_orig)
    xǁTemplateHandlerǁget_template__mutmut_orig.__name__ = 'xǁTemplateHandlerǁget_template'

    def xǁTemplateHandlerǁlist_templates__mutmut_orig(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_1(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_2(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info(None)
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_3(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("XXCache invalid, updating templates...XX")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_4(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_5(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("CACHE INVALID, UPDATING TEMPLATES...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_6(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = None

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_7(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = None
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_8(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir * category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_9(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(None)
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_10(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob(None):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_11(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("XX*.gitignoreXX"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_12(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.GITIGNORE"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_13(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(None)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_14(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug(None)

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_15(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("XXListing all templatesXX")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_16(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_17(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("LISTING ALL TEMPLATES")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_18(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob(None):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_19(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("XX*.gitignoreXX"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_20(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.GITIGNORE"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_21(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(None)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_22(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = None
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_23(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir * "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_24(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "XXGlobalXX"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_25(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_26(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "GLOBAL"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_27(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob(None):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_28(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("XX*.gitignoreXX"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_29(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.GITIGNORE"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_30(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(None)

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_31(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = None
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_32(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir * "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_33(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "XXcommunityXX"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_34(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "COMMUNITY"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_35(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob(None):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_36(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("XX*.gitignoreXX"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_37(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.GITIGNORE"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_38(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = None
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_39(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(None)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_40(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(None)

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_41(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix(None).as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_42(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('XXXX').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_43(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(None)
        return sorted(templates)

    def xǁTemplateHandlerǁlist_templates__mutmut_44(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter (e.g., "Global", "community")

        Returns:
            List of template names
        """
        # Ensure cache is populated
        if not self._is_cache_valid():
            logger.info("Cache invalid, updating templates...")
            self.update_cache()

        templates = []

        if category:
            # List templates in specific category
            category_dir = self.cache_dir / category
            if category_dir.exists():
                if logger.is_debug_enabled():
                    logger.debug(f"Listing templates in category: {category}")
                for file in category_dir.glob("*.gitignore"):
                    templates.append(file.stem)
        else:
            # List all templates
            logger.debug("Listing all templates")

            # Root level templates
            for file in self.cache_dir.glob("*.gitignore"):
                templates.append(file.stem)

            # Global templates
            global_dir = self.cache_dir / "Global"
            if global_dir.exists():
                for file in global_dir.glob("*.gitignore"):
                    templates.append(f"Global/{file.stem}")

            # Community templates
            community_dir = self.cache_dir / "community"
            if community_dir.exists():
                for file in community_dir.rglob("*.gitignore"):
                    relative = file.relative_to(community_dir)
                    templates.append(f"community/{relative.with_suffix('').as_posix()}")

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(templates)} templates")
        return sorted(None)
    
    xǁTemplateHandlerǁlist_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTemplateHandlerǁlist_templates__mutmut_1': xǁTemplateHandlerǁlist_templates__mutmut_1, 
        'xǁTemplateHandlerǁlist_templates__mutmut_2': xǁTemplateHandlerǁlist_templates__mutmut_2, 
        'xǁTemplateHandlerǁlist_templates__mutmut_3': xǁTemplateHandlerǁlist_templates__mutmut_3, 
        'xǁTemplateHandlerǁlist_templates__mutmut_4': xǁTemplateHandlerǁlist_templates__mutmut_4, 
        'xǁTemplateHandlerǁlist_templates__mutmut_5': xǁTemplateHandlerǁlist_templates__mutmut_5, 
        'xǁTemplateHandlerǁlist_templates__mutmut_6': xǁTemplateHandlerǁlist_templates__mutmut_6, 
        'xǁTemplateHandlerǁlist_templates__mutmut_7': xǁTemplateHandlerǁlist_templates__mutmut_7, 
        'xǁTemplateHandlerǁlist_templates__mutmut_8': xǁTemplateHandlerǁlist_templates__mutmut_8, 
        'xǁTemplateHandlerǁlist_templates__mutmut_9': xǁTemplateHandlerǁlist_templates__mutmut_9, 
        'xǁTemplateHandlerǁlist_templates__mutmut_10': xǁTemplateHandlerǁlist_templates__mutmut_10, 
        'xǁTemplateHandlerǁlist_templates__mutmut_11': xǁTemplateHandlerǁlist_templates__mutmut_11, 
        'xǁTemplateHandlerǁlist_templates__mutmut_12': xǁTemplateHandlerǁlist_templates__mutmut_12, 
        'xǁTemplateHandlerǁlist_templates__mutmut_13': xǁTemplateHandlerǁlist_templates__mutmut_13, 
        'xǁTemplateHandlerǁlist_templates__mutmut_14': xǁTemplateHandlerǁlist_templates__mutmut_14, 
        'xǁTemplateHandlerǁlist_templates__mutmut_15': xǁTemplateHandlerǁlist_templates__mutmut_15, 
        'xǁTemplateHandlerǁlist_templates__mutmut_16': xǁTemplateHandlerǁlist_templates__mutmut_16, 
        'xǁTemplateHandlerǁlist_templates__mutmut_17': xǁTemplateHandlerǁlist_templates__mutmut_17, 
        'xǁTemplateHandlerǁlist_templates__mutmut_18': xǁTemplateHandlerǁlist_templates__mutmut_18, 
        'xǁTemplateHandlerǁlist_templates__mutmut_19': xǁTemplateHandlerǁlist_templates__mutmut_19, 
        'xǁTemplateHandlerǁlist_templates__mutmut_20': xǁTemplateHandlerǁlist_templates__mutmut_20, 
        'xǁTemplateHandlerǁlist_templates__mutmut_21': xǁTemplateHandlerǁlist_templates__mutmut_21, 
        'xǁTemplateHandlerǁlist_templates__mutmut_22': xǁTemplateHandlerǁlist_templates__mutmut_22, 
        'xǁTemplateHandlerǁlist_templates__mutmut_23': xǁTemplateHandlerǁlist_templates__mutmut_23, 
        'xǁTemplateHandlerǁlist_templates__mutmut_24': xǁTemplateHandlerǁlist_templates__mutmut_24, 
        'xǁTemplateHandlerǁlist_templates__mutmut_25': xǁTemplateHandlerǁlist_templates__mutmut_25, 
        'xǁTemplateHandlerǁlist_templates__mutmut_26': xǁTemplateHandlerǁlist_templates__mutmut_26, 
        'xǁTemplateHandlerǁlist_templates__mutmut_27': xǁTemplateHandlerǁlist_templates__mutmut_27, 
        'xǁTemplateHandlerǁlist_templates__mutmut_28': xǁTemplateHandlerǁlist_templates__mutmut_28, 
        'xǁTemplateHandlerǁlist_templates__mutmut_29': xǁTemplateHandlerǁlist_templates__mutmut_29, 
        'xǁTemplateHandlerǁlist_templates__mutmut_30': xǁTemplateHandlerǁlist_templates__mutmut_30, 
        'xǁTemplateHandlerǁlist_templates__mutmut_31': xǁTemplateHandlerǁlist_templates__mutmut_31, 
        'xǁTemplateHandlerǁlist_templates__mutmut_32': xǁTemplateHandlerǁlist_templates__mutmut_32, 
        'xǁTemplateHandlerǁlist_templates__mutmut_33': xǁTemplateHandlerǁlist_templates__mutmut_33, 
        'xǁTemplateHandlerǁlist_templates__mutmut_34': xǁTemplateHandlerǁlist_templates__mutmut_34, 
        'xǁTemplateHandlerǁlist_templates__mutmut_35': xǁTemplateHandlerǁlist_templates__mutmut_35, 
        'xǁTemplateHandlerǁlist_templates__mutmut_36': xǁTemplateHandlerǁlist_templates__mutmut_36, 
        'xǁTemplateHandlerǁlist_templates__mutmut_37': xǁTemplateHandlerǁlist_templates__mutmut_37, 
        'xǁTemplateHandlerǁlist_templates__mutmut_38': xǁTemplateHandlerǁlist_templates__mutmut_38, 
        'xǁTemplateHandlerǁlist_templates__mutmut_39': xǁTemplateHandlerǁlist_templates__mutmut_39, 
        'xǁTemplateHandlerǁlist_templates__mutmut_40': xǁTemplateHandlerǁlist_templates__mutmut_40, 
        'xǁTemplateHandlerǁlist_templates__mutmut_41': xǁTemplateHandlerǁlist_templates__mutmut_41, 
        'xǁTemplateHandlerǁlist_templates__mutmut_42': xǁTemplateHandlerǁlist_templates__mutmut_42, 
        'xǁTemplateHandlerǁlist_templates__mutmut_43': xǁTemplateHandlerǁlist_templates__mutmut_43, 
        'xǁTemplateHandlerǁlist_templates__mutmut_44': xǁTemplateHandlerǁlist_templates__mutmut_44
    }
    
    def list_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTemplateHandlerǁlist_templates__mutmut_orig"), object.__getattribute__(self, "xǁTemplateHandlerǁlist_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_templates.__signature__ = _mutmut_signature(xǁTemplateHandlerǁlist_templates__mutmut_orig)
    xǁTemplateHandlerǁlist_templates__mutmut_orig.__name__ = 'xǁTemplateHandlerǁlist_templates'

    def xǁTemplateHandlerǁsearch_templates__mutmut_orig(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = pattern.lower()
        all_templates = self.list_templates()

        matches = [t for t in all_templates if pattern_lower in t.lower()]
        if logger.is_debug_enabled():
            logger.debug(f"Found {len(matches)} templates matching '{pattern}'")

        return matches

    def xǁTemplateHandlerǁsearch_templates__mutmut_1(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = None
        all_templates = self.list_templates()

        matches = [t for t in all_templates if pattern_lower in t.lower()]
        if logger.is_debug_enabled():
            logger.debug(f"Found {len(matches)} templates matching '{pattern}'")

        return matches

    def xǁTemplateHandlerǁsearch_templates__mutmut_2(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = pattern.upper()
        all_templates = self.list_templates()

        matches = [t for t in all_templates if pattern_lower in t.lower()]
        if logger.is_debug_enabled():
            logger.debug(f"Found {len(matches)} templates matching '{pattern}'")

        return matches

    def xǁTemplateHandlerǁsearch_templates__mutmut_3(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = pattern.lower()
        all_templates = None

        matches = [t for t in all_templates if pattern_lower in t.lower()]
        if logger.is_debug_enabled():
            logger.debug(f"Found {len(matches)} templates matching '{pattern}'")

        return matches

    def xǁTemplateHandlerǁsearch_templates__mutmut_4(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = pattern.lower()
        all_templates = self.list_templates()

        matches = None
        if logger.is_debug_enabled():
            logger.debug(f"Found {len(matches)} templates matching '{pattern}'")

        return matches

    def xǁTemplateHandlerǁsearch_templates__mutmut_5(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = pattern.lower()
        all_templates = self.list_templates()

        matches = [t for t in all_templates if pattern_lower not in t.lower()]
        if logger.is_debug_enabled():
            logger.debug(f"Found {len(matches)} templates matching '{pattern}'")

        return matches

    def xǁTemplateHandlerǁsearch_templates__mutmut_6(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = pattern.lower()
        all_templates = self.list_templates()

        matches = [t for t in all_templates if pattern_lower in t.upper()]
        if logger.is_debug_enabled():
            logger.debug(f"Found {len(matches)} templates matching '{pattern}'")

        return matches

    def xǁTemplateHandlerǁsearch_templates__mutmut_7(self, pattern: str) -> list[str]:
        """
        Search for templates matching a pattern.

        Args:
            pattern: Search pattern (case-insensitive)

        Returns:
            List of matching template names
        """
        pattern_lower = pattern.lower()
        all_templates = self.list_templates()

        matches = [t for t in all_templates if pattern_lower in t.lower()]
        if logger.is_debug_enabled():
            logger.debug(None)

        return matches
    
    xǁTemplateHandlerǁsearch_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTemplateHandlerǁsearch_templates__mutmut_1': xǁTemplateHandlerǁsearch_templates__mutmut_1, 
        'xǁTemplateHandlerǁsearch_templates__mutmut_2': xǁTemplateHandlerǁsearch_templates__mutmut_2, 
        'xǁTemplateHandlerǁsearch_templates__mutmut_3': xǁTemplateHandlerǁsearch_templates__mutmut_3, 
        'xǁTemplateHandlerǁsearch_templates__mutmut_4': xǁTemplateHandlerǁsearch_templates__mutmut_4, 
        'xǁTemplateHandlerǁsearch_templates__mutmut_5': xǁTemplateHandlerǁsearch_templates__mutmut_5, 
        'xǁTemplateHandlerǁsearch_templates__mutmut_6': xǁTemplateHandlerǁsearch_templates__mutmut_6, 
        'xǁTemplateHandlerǁsearch_templates__mutmut_7': xǁTemplateHandlerǁsearch_templates__mutmut_7
    }
    
    def search_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTemplateHandlerǁsearch_templates__mutmut_orig"), object.__getattribute__(self, "xǁTemplateHandlerǁsearch_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    search_templates.__signature__ = _mutmut_signature(xǁTemplateHandlerǁsearch_templates__mutmut_orig)
    xǁTemplateHandlerǁsearch_templates__mutmut_orig.__name__ = 'xǁTemplateHandlerǁsearch_templates'


# 🧰🌍🔚
