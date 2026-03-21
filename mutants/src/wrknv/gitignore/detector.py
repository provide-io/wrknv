#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Project Detector for Gitignore Templates
=========================================
Auto-detects project types and suggests appropriate gitignore templates."""

from __future__ import annotations

import json
from pathlib import Path
from typing import ClassVar

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


class ProjectDetector:
    """Detects project characteristics to suggest gitignore templates."""

    # File patterns for language detection
    LANGUAGE_PATTERNS: ClassVar[dict[str, list[str]]] = {
        "Python": ["*.py", "requirements.txt", "setup.py", "pyproject.toml"],
        "Node": ["*.js", "*.mjs", "*.cjs", "package.json"],
        "TypeScript": ["*.ts", "*.tsx", "tsconfig.json"],
        "Go": ["*.go", "go.mod", "go.sum"],
        "Rust": ["*.rs", "Cargo.toml", "Cargo.lock"],
        "Java": ["*.java", "pom.xml"],
        "Ruby": ["*.rb", "Gemfile", "Gemfile.lock"],
        "PHP": ["*.php", "composer.json", "composer.lock"],
        "C": ["*.c", "*.h", "Makefile"],
        "C++": ["*.cpp", "*.hpp", "*.cc", "*.cxx", "CMakeLists.txt"],
        "Swift": ["*.swift", "Package.swift"],
        "Kotlin": ["*.kt", "*.kts"],
        "Scala": ["*.scala", "build.sbt"],
        "Elixir": ["*.ex", "*.exs", "mix.exs"],
    }

    # Framework detection patterns
    FRAMEWORK_PATTERNS: ClassVar[dict[str, list[str]]] = {
        "Django": ["manage.py", "settings.py", "urls.py"],
        "Flask": ["app.py", "flask_app.py"],
        "React": ["react", "react-dom"],  # Check in package.json
        "Vue": ["vue"],  # Check in package.json
        "Angular": ["@angular/core"],  # Check in package.json
        "NextJS": ["next"],  # Check in package.json
        "Rails": ["Gemfile", "config.ru", "Rakefile"],
        "Laravel": ["artisan", "composer.json"],  # Check for laravel in composer
        "Spring": ["pom.xml", "build.gradle"],  # Check for spring deps
    }

    # Tool detection patterns
    TOOL_PATTERNS: ClassVar[dict[str, list[str]]] = {
        "Poetry": ["poetry.lock", "pyproject.toml"],
        "PDM": ["pdm.lock"],
        "Pipenv": ["Pipfile", "Pipfile.lock"],
        "Ruff": [".ruff_cache"],
        "Maven": ["pom.xml"],
        "Gradle": ["build.gradle", "build.gradle.kts"],
        "Docker": ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"],
        "Terraform": ["*.tf", "*.tfvars"],
        "Kubernetes": ["*.yaml", "*.yml"],  # Check for k8s resources
        "VisualStudioCode": [".vscode"],
        "JetBrains": [".idea"],
        "Vim": [".vimrc", ".vim"],
        "Emacs": [".emacs", ".emacs.d"],
        "Git": [".git"],
    }

    # OS detection patterns
    OS_PATTERNS: ClassVar[dict[str, list[str]]] = {
        "macOS": [".DS_Store", ".AppleDouble", ".LSOverride"],
        "Windows": ["Thumbs.db", "Desktop.ini", "ehthumbs.db"],
        "Linux": [".directory", ".Trash-*"],
    }

    def xǁProjectDetectorǁ__init____mutmut_orig(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = set()
        logger.debug("ProjectDetector initialized")

    def xǁProjectDetectorǁ__init____mutmut_1(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = None
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = set()
        logger.debug("ProjectDetector initialized")

    def xǁProjectDetectorǁ__init____mutmut_2(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = None
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = set()
        logger.debug("ProjectDetector initialized")

    def xǁProjectDetectorǁ__init____mutmut_3(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = None
        self.detected_os: set[str] = set()
        logger.debug("ProjectDetector initialized")

    def xǁProjectDetectorǁ__init____mutmut_4(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = None
        logger.debug("ProjectDetector initialized")

    def xǁProjectDetectorǁ__init____mutmut_5(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = set()
        logger.debug(None)

    def xǁProjectDetectorǁ__init____mutmut_6(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = set()
        logger.debug("XXProjectDetector initializedXX")

    def xǁProjectDetectorǁ__init____mutmut_7(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = set()
        logger.debug("projectdetector initialized")

    def xǁProjectDetectorǁ__init____mutmut_8(self) -> None:
        """Initialize the detector."""
        self.detected_languages: set[str] = set()
        self.detected_frameworks: set[str] = set()
        self.detected_tools: set[str] = set()
        self.detected_os: set[str] = set()
        logger.debug("PROJECTDETECTOR INITIALIZED")
    
    xǁProjectDetectorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁ__init____mutmut_1': xǁProjectDetectorǁ__init____mutmut_1, 
        'xǁProjectDetectorǁ__init____mutmut_2': xǁProjectDetectorǁ__init____mutmut_2, 
        'xǁProjectDetectorǁ__init____mutmut_3': xǁProjectDetectorǁ__init____mutmut_3, 
        'xǁProjectDetectorǁ__init____mutmut_4': xǁProjectDetectorǁ__init____mutmut_4, 
        'xǁProjectDetectorǁ__init____mutmut_5': xǁProjectDetectorǁ__init____mutmut_5, 
        'xǁProjectDetectorǁ__init____mutmut_6': xǁProjectDetectorǁ__init____mutmut_6, 
        'xǁProjectDetectorǁ__init____mutmut_7': xǁProjectDetectorǁ__init____mutmut_7, 
        'xǁProjectDetectorǁ__init____mutmut_8': xǁProjectDetectorǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁProjectDetectorǁ__init____mutmut_orig)
    xǁProjectDetectorǁ__init____mutmut_orig.__name__ = 'xǁProjectDetectorǁ__init__'

    def xǁProjectDetectorǁreset__mutmut_orig(self) -> None:
        """Reset detection state."""
        self.detected_languages.clear()
        self.detected_frameworks.clear()
        self.detected_tools.clear()
        self.detected_os.clear()
        logger.debug("ProjectDetector reset")

    def xǁProjectDetectorǁreset__mutmut_1(self) -> None:
        """Reset detection state."""
        self.detected_languages.clear()
        self.detected_frameworks.clear()
        self.detected_tools.clear()
        self.detected_os.clear()
        logger.debug(None)

    def xǁProjectDetectorǁreset__mutmut_2(self) -> None:
        """Reset detection state."""
        self.detected_languages.clear()
        self.detected_frameworks.clear()
        self.detected_tools.clear()
        self.detected_os.clear()
        logger.debug("XXProjectDetector resetXX")

    def xǁProjectDetectorǁreset__mutmut_3(self) -> None:
        """Reset detection state."""
        self.detected_languages.clear()
        self.detected_frameworks.clear()
        self.detected_tools.clear()
        self.detected_os.clear()
        logger.debug("projectdetector reset")

    def xǁProjectDetectorǁreset__mutmut_4(self) -> None:
        """Reset detection state."""
        self.detected_languages.clear()
        self.detected_frameworks.clear()
        self.detected_tools.clear()
        self.detected_os.clear()
        logger.debug("PROJECTDETECTOR RESET")
    
    xǁProjectDetectorǁreset__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁreset__mutmut_1': xǁProjectDetectorǁreset__mutmut_1, 
        'xǁProjectDetectorǁreset__mutmut_2': xǁProjectDetectorǁreset__mutmut_2, 
        'xǁProjectDetectorǁreset__mutmut_3': xǁProjectDetectorǁreset__mutmut_3, 
        'xǁProjectDetectorǁreset__mutmut_4': xǁProjectDetectorǁreset__mutmut_4
    }
    
    def reset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁreset__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁreset__mutmut_mutants"), args, kwargs, self)
        return result 
    
    reset.__signature__ = _mutmut_signature(xǁProjectDetectorǁreset__mutmut_orig)
    xǁProjectDetectorǁreset__mutmut_orig.__name__ = 'xǁProjectDetectorǁreset'

    def xǁProjectDetectorǁscan_directory__mutmut_orig(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_1(self, path: Path, max_depth: int = 6) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_2(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = None
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_3(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(None)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_4(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_5(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(None)
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_6(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(None)

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_7(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(None, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_8(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=None, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_9(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=None)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_10(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_11(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_12(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, )

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_13(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=1, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_14(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(None)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_15(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(None)
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_16(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(None)
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_17(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(None)
        if logger.is_debug_enabled():
            logger.debug(f"Detected OS: {self.detected_os}")

    def xǁProjectDetectorǁscan_directory__mutmut_18(self, path: Path, max_depth: int = 5) -> None:
        """
        Scan a directory to detect project characteristics.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse
        """
        path = Path(path)
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return

        logger.info(f"Scanning directory: {path}")

        # Scan for files recursively
        self._scan_recursive(path, current_depth=0, max_depth=max_depth)

        # Check for framework-specific files
        self._detect_frameworks_from_configs(path)

        # Log results
        if logger.is_debug_enabled():
            logger.debug(f"Detected languages: {self.detected_languages}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected frameworks: {self.detected_frameworks}")
        if logger.is_debug_enabled():
            logger.debug(f"Detected tools: {self.detected_tools}")
        if logger.is_debug_enabled():
            logger.debug(None)
    
    xǁProjectDetectorǁscan_directory__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁscan_directory__mutmut_1': xǁProjectDetectorǁscan_directory__mutmut_1, 
        'xǁProjectDetectorǁscan_directory__mutmut_2': xǁProjectDetectorǁscan_directory__mutmut_2, 
        'xǁProjectDetectorǁscan_directory__mutmut_3': xǁProjectDetectorǁscan_directory__mutmut_3, 
        'xǁProjectDetectorǁscan_directory__mutmut_4': xǁProjectDetectorǁscan_directory__mutmut_4, 
        'xǁProjectDetectorǁscan_directory__mutmut_5': xǁProjectDetectorǁscan_directory__mutmut_5, 
        'xǁProjectDetectorǁscan_directory__mutmut_6': xǁProjectDetectorǁscan_directory__mutmut_6, 
        'xǁProjectDetectorǁscan_directory__mutmut_7': xǁProjectDetectorǁscan_directory__mutmut_7, 
        'xǁProjectDetectorǁscan_directory__mutmut_8': xǁProjectDetectorǁscan_directory__mutmut_8, 
        'xǁProjectDetectorǁscan_directory__mutmut_9': xǁProjectDetectorǁscan_directory__mutmut_9, 
        'xǁProjectDetectorǁscan_directory__mutmut_10': xǁProjectDetectorǁscan_directory__mutmut_10, 
        'xǁProjectDetectorǁscan_directory__mutmut_11': xǁProjectDetectorǁscan_directory__mutmut_11, 
        'xǁProjectDetectorǁscan_directory__mutmut_12': xǁProjectDetectorǁscan_directory__mutmut_12, 
        'xǁProjectDetectorǁscan_directory__mutmut_13': xǁProjectDetectorǁscan_directory__mutmut_13, 
        'xǁProjectDetectorǁscan_directory__mutmut_14': xǁProjectDetectorǁscan_directory__mutmut_14, 
        'xǁProjectDetectorǁscan_directory__mutmut_15': xǁProjectDetectorǁscan_directory__mutmut_15, 
        'xǁProjectDetectorǁscan_directory__mutmut_16': xǁProjectDetectorǁscan_directory__mutmut_16, 
        'xǁProjectDetectorǁscan_directory__mutmut_17': xǁProjectDetectorǁscan_directory__mutmut_17, 
        'xǁProjectDetectorǁscan_directory__mutmut_18': xǁProjectDetectorǁscan_directory__mutmut_18
    }
    
    def scan_directory(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁscan_directory__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁscan_directory__mutmut_mutants"), args, kwargs, self)
        return result 
    
    scan_directory.__signature__ = _mutmut_signature(xǁProjectDetectorǁscan_directory__mutmut_orig)
    xǁProjectDetectorǁscan_directory__mutmut_orig.__name__ = 'xǁProjectDetectorǁscan_directory'

    def xǁProjectDetectorǁ_scan_recursive__mutmut_orig(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_1(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth >= max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_2(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() or item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_3(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith(None):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_4(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("XX.XX"):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_5(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name not in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_6(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in ["XX.vscodeXX", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_7(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".VSCODE", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_8(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", "XX.ideaXX", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_9(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".IDEA", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_10(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", "XX.vimXX", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_11(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".VIM", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_12(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", "XX.emacs.dXX", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_13(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".EMACS.D", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_14(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", "XX.ruff_cacheXX"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_15(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".RUFF_CACHE"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_16(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(None, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_17(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=None)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_18(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_19(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, )
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_20(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=False)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_21(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    break

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_22(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(None, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_23(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=None)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_24(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_25(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, )
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_26(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=True)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_27(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() or not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_28(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_29(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith(None):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_30(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("XX.XX"):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_31(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(None, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_32(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, None, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_33(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, None)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_34(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_35(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_36(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, )
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_37(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth - 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_38(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 2, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing: {path}")

    def xǁProjectDetectorǁ_scan_recursive__mutmut_39(self, path: Path, current_depth: int, max_depth: int) -> None:
        """Recursively scan directory."""
        if current_depth > max_depth:
            return

        try:
            for item in path.iterdir():
                # Skip hidden directories (except IDE/tool directories)
                if item.is_dir() and item.name.startswith("."):
                    # Check for IDE/tool directories
                    if item.name in [".vscode", ".idea", ".vim", ".emacs.d", ".ruff_cache"]:
                        self._check_pattern(item.name, is_dir=True)
                    continue

                if item.is_file():
                    self._check_pattern(item.name, is_dir=False)
                elif item.is_dir() and not item.name.startswith("."):
                    self._scan_recursive(item, current_depth + 1, max_depth)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(None)
    
    xǁProjectDetectorǁ_scan_recursive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁ_scan_recursive__mutmut_1': xǁProjectDetectorǁ_scan_recursive__mutmut_1, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_2': xǁProjectDetectorǁ_scan_recursive__mutmut_2, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_3': xǁProjectDetectorǁ_scan_recursive__mutmut_3, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_4': xǁProjectDetectorǁ_scan_recursive__mutmut_4, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_5': xǁProjectDetectorǁ_scan_recursive__mutmut_5, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_6': xǁProjectDetectorǁ_scan_recursive__mutmut_6, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_7': xǁProjectDetectorǁ_scan_recursive__mutmut_7, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_8': xǁProjectDetectorǁ_scan_recursive__mutmut_8, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_9': xǁProjectDetectorǁ_scan_recursive__mutmut_9, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_10': xǁProjectDetectorǁ_scan_recursive__mutmut_10, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_11': xǁProjectDetectorǁ_scan_recursive__mutmut_11, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_12': xǁProjectDetectorǁ_scan_recursive__mutmut_12, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_13': xǁProjectDetectorǁ_scan_recursive__mutmut_13, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_14': xǁProjectDetectorǁ_scan_recursive__mutmut_14, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_15': xǁProjectDetectorǁ_scan_recursive__mutmut_15, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_16': xǁProjectDetectorǁ_scan_recursive__mutmut_16, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_17': xǁProjectDetectorǁ_scan_recursive__mutmut_17, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_18': xǁProjectDetectorǁ_scan_recursive__mutmut_18, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_19': xǁProjectDetectorǁ_scan_recursive__mutmut_19, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_20': xǁProjectDetectorǁ_scan_recursive__mutmut_20, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_21': xǁProjectDetectorǁ_scan_recursive__mutmut_21, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_22': xǁProjectDetectorǁ_scan_recursive__mutmut_22, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_23': xǁProjectDetectorǁ_scan_recursive__mutmut_23, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_24': xǁProjectDetectorǁ_scan_recursive__mutmut_24, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_25': xǁProjectDetectorǁ_scan_recursive__mutmut_25, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_26': xǁProjectDetectorǁ_scan_recursive__mutmut_26, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_27': xǁProjectDetectorǁ_scan_recursive__mutmut_27, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_28': xǁProjectDetectorǁ_scan_recursive__mutmut_28, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_29': xǁProjectDetectorǁ_scan_recursive__mutmut_29, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_30': xǁProjectDetectorǁ_scan_recursive__mutmut_30, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_31': xǁProjectDetectorǁ_scan_recursive__mutmut_31, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_32': xǁProjectDetectorǁ_scan_recursive__mutmut_32, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_33': xǁProjectDetectorǁ_scan_recursive__mutmut_33, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_34': xǁProjectDetectorǁ_scan_recursive__mutmut_34, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_35': xǁProjectDetectorǁ_scan_recursive__mutmut_35, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_36': xǁProjectDetectorǁ_scan_recursive__mutmut_36, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_37': xǁProjectDetectorǁ_scan_recursive__mutmut_37, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_38': xǁProjectDetectorǁ_scan_recursive__mutmut_38, 
        'xǁProjectDetectorǁ_scan_recursive__mutmut_39': xǁProjectDetectorǁ_scan_recursive__mutmut_39
    }
    
    def _scan_recursive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁ_scan_recursive__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁ_scan_recursive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _scan_recursive.__signature__ = _mutmut_signature(xǁProjectDetectorǁ_scan_recursive__mutmut_orig)
    xǁProjectDetectorǁ_scan_recursive__mutmut_orig.__name__ = 'xǁProjectDetectorǁ_scan_recursive'

    def xǁProjectDetectorǁ_check_pattern__mutmut_orig(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_1(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(None, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_2(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, None, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_3(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, None):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_4(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_5(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_6(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, ):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_7(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_8(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(None)

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_9(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(None, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_10(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, None, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_11(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, None):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_12(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_13(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_14(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, ):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_15(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_16(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(None)

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_17(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(None, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_18(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, None, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_19(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, None):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_20(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_21(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_22(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, ):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_23(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_24(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(None)

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_25(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework not in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_26(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["XXReactXX", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_27(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["react", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_28(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["REACT", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_29(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "XXVueXX", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_30(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_31(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "VUE", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_32(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "XXAngularXX", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_33(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_34(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "ANGULAR", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_35(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "XXNextJSXX"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_36(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "nextjs"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_37(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NEXTJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_38(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                break  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_39(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(None, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_40(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, None, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_41(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, None):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_42(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_43(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_44(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, ):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_45(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected framework {framework} from {filename}")

    def xǁProjectDetectorǁ_check_pattern__mutmut_46(self, filename: str, is_dir: bool) -> None:
        """Check if a filename matches any detection patterns."""
        # Check language patterns
        for lang, patterns in self.LANGUAGE_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_languages.add(lang)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected language {lang} from {filename}")

        # Check tool patterns
        for tool, patterns in self.TOOL_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_tools.add(tool)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected tool {tool} from {filename}")

        # Check OS patterns
        for os_name, patterns in self.OS_PATTERNS.items():
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_os.add(os_name)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected OS {os_name} from {filename}")

        # Check basic framework patterns
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if framework in ["React", "Vue", "Angular", "NextJS"]:
                continue  # These are checked in package.json
            for pattern in patterns:
                if self._matches_pattern(filename, pattern, is_dir):
                    self.detected_frameworks.add(framework)
                    if logger.is_trace_enabled():
                        logger.trace(None)
    
    xǁProjectDetectorǁ_check_pattern__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁ_check_pattern__mutmut_1': xǁProjectDetectorǁ_check_pattern__mutmut_1, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_2': xǁProjectDetectorǁ_check_pattern__mutmut_2, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_3': xǁProjectDetectorǁ_check_pattern__mutmut_3, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_4': xǁProjectDetectorǁ_check_pattern__mutmut_4, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_5': xǁProjectDetectorǁ_check_pattern__mutmut_5, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_6': xǁProjectDetectorǁ_check_pattern__mutmut_6, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_7': xǁProjectDetectorǁ_check_pattern__mutmut_7, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_8': xǁProjectDetectorǁ_check_pattern__mutmut_8, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_9': xǁProjectDetectorǁ_check_pattern__mutmut_9, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_10': xǁProjectDetectorǁ_check_pattern__mutmut_10, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_11': xǁProjectDetectorǁ_check_pattern__mutmut_11, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_12': xǁProjectDetectorǁ_check_pattern__mutmut_12, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_13': xǁProjectDetectorǁ_check_pattern__mutmut_13, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_14': xǁProjectDetectorǁ_check_pattern__mutmut_14, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_15': xǁProjectDetectorǁ_check_pattern__mutmut_15, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_16': xǁProjectDetectorǁ_check_pattern__mutmut_16, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_17': xǁProjectDetectorǁ_check_pattern__mutmut_17, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_18': xǁProjectDetectorǁ_check_pattern__mutmut_18, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_19': xǁProjectDetectorǁ_check_pattern__mutmut_19, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_20': xǁProjectDetectorǁ_check_pattern__mutmut_20, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_21': xǁProjectDetectorǁ_check_pattern__mutmut_21, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_22': xǁProjectDetectorǁ_check_pattern__mutmut_22, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_23': xǁProjectDetectorǁ_check_pattern__mutmut_23, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_24': xǁProjectDetectorǁ_check_pattern__mutmut_24, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_25': xǁProjectDetectorǁ_check_pattern__mutmut_25, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_26': xǁProjectDetectorǁ_check_pattern__mutmut_26, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_27': xǁProjectDetectorǁ_check_pattern__mutmut_27, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_28': xǁProjectDetectorǁ_check_pattern__mutmut_28, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_29': xǁProjectDetectorǁ_check_pattern__mutmut_29, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_30': xǁProjectDetectorǁ_check_pattern__mutmut_30, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_31': xǁProjectDetectorǁ_check_pattern__mutmut_31, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_32': xǁProjectDetectorǁ_check_pattern__mutmut_32, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_33': xǁProjectDetectorǁ_check_pattern__mutmut_33, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_34': xǁProjectDetectorǁ_check_pattern__mutmut_34, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_35': xǁProjectDetectorǁ_check_pattern__mutmut_35, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_36': xǁProjectDetectorǁ_check_pattern__mutmut_36, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_37': xǁProjectDetectorǁ_check_pattern__mutmut_37, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_38': xǁProjectDetectorǁ_check_pattern__mutmut_38, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_39': xǁProjectDetectorǁ_check_pattern__mutmut_39, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_40': xǁProjectDetectorǁ_check_pattern__mutmut_40, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_41': xǁProjectDetectorǁ_check_pattern__mutmut_41, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_42': xǁProjectDetectorǁ_check_pattern__mutmut_42, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_43': xǁProjectDetectorǁ_check_pattern__mutmut_43, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_44': xǁProjectDetectorǁ_check_pattern__mutmut_44, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_45': xǁProjectDetectorǁ_check_pattern__mutmut_45, 
        'xǁProjectDetectorǁ_check_pattern__mutmut_46': xǁProjectDetectorǁ_check_pattern__mutmut_46
    }
    
    def _check_pattern(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁ_check_pattern__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁ_check_pattern__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_pattern.__signature__ = _mutmut_signature(xǁProjectDetectorǁ_check_pattern__mutmut_orig)
    xǁProjectDetectorǁ_check_pattern__mutmut_orig.__name__ = 'xǁProjectDetectorǁ_check_pattern'

    def xǁProjectDetectorǁ_matches_pattern__mutmut_orig(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_1(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") or not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_2(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(None) and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_3(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith("XX.XX") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_4(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_5(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith(None):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_6(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("XX*.XX"):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_7(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename != pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_8(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_9(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) and filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_10(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(None, pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_11(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, None) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_12(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(pattern) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_13(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, ) or filename == pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_14(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename != pattern

        return False

    def xǁProjectDetectorǁ_matches_pattern__mutmut_15(self, filename: str, pattern: str, is_dir: bool) -> bool:
        """Check if filename matches a pattern."""
        from fnmatch import fnmatch

        # Handle directory patterns (directories starting with .)
        if pattern.startswith(".") and not pattern.startswith("*."):
            # Match exact name for both files and directories
            return filename == pattern

        # Handle wildcard file patterns
        if not is_dir:
            return fnmatch(filename, pattern) or filename == pattern

        return True
    
    xǁProjectDetectorǁ_matches_pattern__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁ_matches_pattern__mutmut_1': xǁProjectDetectorǁ_matches_pattern__mutmut_1, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_2': xǁProjectDetectorǁ_matches_pattern__mutmut_2, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_3': xǁProjectDetectorǁ_matches_pattern__mutmut_3, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_4': xǁProjectDetectorǁ_matches_pattern__mutmut_4, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_5': xǁProjectDetectorǁ_matches_pattern__mutmut_5, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_6': xǁProjectDetectorǁ_matches_pattern__mutmut_6, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_7': xǁProjectDetectorǁ_matches_pattern__mutmut_7, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_8': xǁProjectDetectorǁ_matches_pattern__mutmut_8, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_9': xǁProjectDetectorǁ_matches_pattern__mutmut_9, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_10': xǁProjectDetectorǁ_matches_pattern__mutmut_10, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_11': xǁProjectDetectorǁ_matches_pattern__mutmut_11, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_12': xǁProjectDetectorǁ_matches_pattern__mutmut_12, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_13': xǁProjectDetectorǁ_matches_pattern__mutmut_13, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_14': xǁProjectDetectorǁ_matches_pattern__mutmut_14, 
        'xǁProjectDetectorǁ_matches_pattern__mutmut_15': xǁProjectDetectorǁ_matches_pattern__mutmut_15
    }
    
    def _matches_pattern(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁ_matches_pattern__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁ_matches_pattern__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _matches_pattern.__signature__ = _mutmut_signature(xǁProjectDetectorǁ_matches_pattern__mutmut_orig)
    xǁProjectDetectorǁ_matches_pattern__mutmut_orig.__name__ = 'xǁProjectDetectorǁ_matches_pattern'

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_orig(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_1(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(None)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_2(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() or not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_3(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_4(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith(None):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_5(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("XX.XX"):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_6(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(None)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_7(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(None)

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_8(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = None
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_9(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path * "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_10(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "XXrequirements.txtXX"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_11(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "REQUIREMENTS.TXT"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_12(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = None
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_13(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().upper()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_14(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "XXflaskXX" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_15(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "FLASK" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_16(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" not in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_17(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add(None)
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_18(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("XXFlaskXX")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_19(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_20(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("FLASK")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_21(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace(None)
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_22(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("XXDetected Flask from requirements.txtXX")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_23(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("detected flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_24(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("DETECTED FLASK FROM REQUIREMENTS.TXT")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_25(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "XXdjangoXX" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_26(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "DJANGO" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_27(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" not in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_28(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add(None)
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_29(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("XXDjangoXX")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_30(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_31(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("DJANGO")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_32(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace(None)
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_33(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("XXDetected Django from requirements.txtXX")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_34(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("detected django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_35(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("DETECTED DJANGO FROM REQUIREMENTS.TXT")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_36(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "XXfastapiXX" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_37(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "FASTAPI" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_38(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" not in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_39(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add(None)
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_40(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("XXFastAPIXX")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_41(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("fastapi")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_42(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FASTAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_43(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace(None)
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_44(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("XXDetected FastAPI from requirements.txtXX")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_45(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("detected fastapi from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_46(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("DETECTED FASTAPI FROM REQUIREMENTS.TXT")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_47(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug(None)

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_48(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("XXCould not parse requirements.txtXX")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_49(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_50(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("COULD NOT PARSE REQUIREMENTS.TXT")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_51(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "XXTypeScriptXX" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_52(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "typescript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_53(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TYPESCRIPT" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_54(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" not in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_55(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add(None)
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_56(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("XXNodeXX")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_57(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("node")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_58(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("NODE")
            logger.trace("Added Node due to TypeScript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_59(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace(None)

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_60(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("XXAdded Node due to TypeScript detectionXX")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_61(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("added node due to typescript detection")

    def xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_62(self, path: Path) -> None:
        """Detect frameworks from configuration files."""
        # Check package.json for JavaScript frameworks (root and subdirectories)
        self._check_package_json(path)

        # Also check common subdirectories (frontend, backend, client, server, etc.)
        try:
            for subdir in path.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    self._check_package_json(subdir)
        except PermissionError:
            if logger.is_debug_enabled():
                logger.debug(f"Permission denied accessing subdirectories of: {path}")

        # Check requirements.txt for Python frameworks
        requirements_txt = path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "flask" in content:
                    self.detected_frameworks.add("Flask")
                    logger.trace("Detected Flask from requirements.txt")
                if "django" in content:
                    self.detected_frameworks.add("Django")
                    logger.trace("Detected Django from requirements.txt")
                if "fastapi" in content:
                    self.detected_frameworks.add("FastAPI")
                    logger.trace("Detected FastAPI from requirements.txt")
            except Exception:
                logger.debug("Could not parse requirements.txt")

        # TypeScript implies Node
        if "TypeScript" in self.detected_languages:
            self.detected_languages.add("Node")
            logger.trace("ADDED NODE DUE TO TYPESCRIPT DETECTION")
    
    xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_1': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_1, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_2': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_2, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_3': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_3, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_4': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_4, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_5': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_5, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_6': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_6, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_7': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_7, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_8': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_8, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_9': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_9, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_10': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_10, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_11': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_11, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_12': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_12, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_13': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_13, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_14': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_14, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_15': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_15, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_16': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_16, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_17': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_17, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_18': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_18, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_19': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_19, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_20': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_20, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_21': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_21, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_22': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_22, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_23': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_23, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_24': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_24, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_25': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_25, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_26': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_26, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_27': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_27, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_28': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_28, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_29': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_29, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_30': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_30, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_31': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_31, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_32': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_32, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_33': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_33, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_34': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_34, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_35': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_35, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_36': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_36, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_37': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_37, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_38': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_38, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_39': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_39, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_40': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_40, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_41': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_41, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_42': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_42, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_43': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_43, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_44': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_44, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_45': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_45, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_46': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_46, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_47': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_47, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_48': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_48, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_49': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_49, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_50': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_50, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_51': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_51, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_52': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_52, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_53': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_53, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_54': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_54, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_55': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_55, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_56': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_56, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_57': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_57, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_58': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_58, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_59': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_59, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_60': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_60, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_61': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_61, 
        'xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_62': xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_62
    }
    
    def _detect_frameworks_from_configs(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _detect_frameworks_from_configs.__signature__ = _mutmut_signature(xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_orig)
    xǁProjectDetectorǁ_detect_frameworks_from_configs__mutmut_orig.__name__ = 'xǁProjectDetectorǁ_detect_frameworks_from_configs'

    def xǁProjectDetectorǁ_check_package_json__mutmut_orig(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_1(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = None
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_2(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path * "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_3(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "XXpackage.jsonXX"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_4(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "PACKAGE.JSON"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_5(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = None
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_6(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(None)
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_7(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = None

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_8(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get(None, {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_9(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", None), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_10(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get({}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_11(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", ), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_12(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("XXdependenciesXX", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_13(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("DEPENDENCIES", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_14(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get(None, {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_15(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", None)}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_16(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get({})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_17(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", )}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_18(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("XXdevDependenciesXX", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_19(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devdependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_20(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("DEVDEPENDENCIES", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_21(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "XXreactXX" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_22(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "REACT" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_23(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" not in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_24(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_25(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("XXReactXX")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_26(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("react")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_27(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("REACT")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_28(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(None)

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_29(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "XXvueXX" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_30(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "VUE" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_31(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" not in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_32(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_33(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("XXVueXX")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_34(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_35(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("VUE")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_36(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(None)

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_37(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "XX@angular/coreXX" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_38(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@ANGULAR/CORE" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_39(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" not in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_40(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_41(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("XXAngularXX")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_42(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_43(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("ANGULAR")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_44(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(None)

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_45(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "XXnextXX" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_46(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "NEXT" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_47(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" not in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_48(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add(None)
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_49(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("XXNextJSXX")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_50(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("nextjs")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_51(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NEXTJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_52(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(None)

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(f"Could not parse {package_json}")

    def xǁProjectDetectorǁ_check_package_json__mutmut_53(self, path: Path) -> None:
        """Check a specific directory for package.json and detect frameworks."""
        package_json = path / "package.json"
        if package_json.exists():
            try:
                content = json.loads(package_json.read_text())
                deps = {**content.get("dependencies", {}), **content.get("devDependencies", {})}

                # Check for React
                if "react" in deps:
                    self.detected_frameworks.add("React")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected React from {package_json}")

                # Check for Vue
                if "vue" in deps:
                    self.detected_frameworks.add("Vue")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Vue from {package_json}")

                # Check for Angular
                if "@angular/core" in deps:
                    self.detected_frameworks.add("Angular")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Angular from {package_json}")

                # Check for Next.js
                if "next" in deps:
                    self.detected_frameworks.add("NextJS")
                    if logger.is_trace_enabled():
                        logger.trace(f"Detected Next.js from {package_json}")

            except (json.JSONDecodeError, KeyError):
                if logger.is_debug_enabled():
                    logger.debug(None)
    
    xǁProjectDetectorǁ_check_package_json__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁ_check_package_json__mutmut_1': xǁProjectDetectorǁ_check_package_json__mutmut_1, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_2': xǁProjectDetectorǁ_check_package_json__mutmut_2, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_3': xǁProjectDetectorǁ_check_package_json__mutmut_3, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_4': xǁProjectDetectorǁ_check_package_json__mutmut_4, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_5': xǁProjectDetectorǁ_check_package_json__mutmut_5, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_6': xǁProjectDetectorǁ_check_package_json__mutmut_6, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_7': xǁProjectDetectorǁ_check_package_json__mutmut_7, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_8': xǁProjectDetectorǁ_check_package_json__mutmut_8, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_9': xǁProjectDetectorǁ_check_package_json__mutmut_9, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_10': xǁProjectDetectorǁ_check_package_json__mutmut_10, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_11': xǁProjectDetectorǁ_check_package_json__mutmut_11, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_12': xǁProjectDetectorǁ_check_package_json__mutmut_12, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_13': xǁProjectDetectorǁ_check_package_json__mutmut_13, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_14': xǁProjectDetectorǁ_check_package_json__mutmut_14, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_15': xǁProjectDetectorǁ_check_package_json__mutmut_15, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_16': xǁProjectDetectorǁ_check_package_json__mutmut_16, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_17': xǁProjectDetectorǁ_check_package_json__mutmut_17, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_18': xǁProjectDetectorǁ_check_package_json__mutmut_18, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_19': xǁProjectDetectorǁ_check_package_json__mutmut_19, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_20': xǁProjectDetectorǁ_check_package_json__mutmut_20, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_21': xǁProjectDetectorǁ_check_package_json__mutmut_21, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_22': xǁProjectDetectorǁ_check_package_json__mutmut_22, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_23': xǁProjectDetectorǁ_check_package_json__mutmut_23, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_24': xǁProjectDetectorǁ_check_package_json__mutmut_24, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_25': xǁProjectDetectorǁ_check_package_json__mutmut_25, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_26': xǁProjectDetectorǁ_check_package_json__mutmut_26, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_27': xǁProjectDetectorǁ_check_package_json__mutmut_27, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_28': xǁProjectDetectorǁ_check_package_json__mutmut_28, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_29': xǁProjectDetectorǁ_check_package_json__mutmut_29, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_30': xǁProjectDetectorǁ_check_package_json__mutmut_30, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_31': xǁProjectDetectorǁ_check_package_json__mutmut_31, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_32': xǁProjectDetectorǁ_check_package_json__mutmut_32, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_33': xǁProjectDetectorǁ_check_package_json__mutmut_33, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_34': xǁProjectDetectorǁ_check_package_json__mutmut_34, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_35': xǁProjectDetectorǁ_check_package_json__mutmut_35, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_36': xǁProjectDetectorǁ_check_package_json__mutmut_36, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_37': xǁProjectDetectorǁ_check_package_json__mutmut_37, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_38': xǁProjectDetectorǁ_check_package_json__mutmut_38, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_39': xǁProjectDetectorǁ_check_package_json__mutmut_39, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_40': xǁProjectDetectorǁ_check_package_json__mutmut_40, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_41': xǁProjectDetectorǁ_check_package_json__mutmut_41, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_42': xǁProjectDetectorǁ_check_package_json__mutmut_42, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_43': xǁProjectDetectorǁ_check_package_json__mutmut_43, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_44': xǁProjectDetectorǁ_check_package_json__mutmut_44, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_45': xǁProjectDetectorǁ_check_package_json__mutmut_45, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_46': xǁProjectDetectorǁ_check_package_json__mutmut_46, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_47': xǁProjectDetectorǁ_check_package_json__mutmut_47, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_48': xǁProjectDetectorǁ_check_package_json__mutmut_48, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_49': xǁProjectDetectorǁ_check_package_json__mutmut_49, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_50': xǁProjectDetectorǁ_check_package_json__mutmut_50, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_51': xǁProjectDetectorǁ_check_package_json__mutmut_51, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_52': xǁProjectDetectorǁ_check_package_json__mutmut_52, 
        'xǁProjectDetectorǁ_check_package_json__mutmut_53': xǁProjectDetectorǁ_check_package_json__mutmut_53
    }
    
    def _check_package_json(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁ_check_package_json__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁ_check_package_json__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_package_json.__signature__ = _mutmut_signature(xǁProjectDetectorǁ_check_package_json__mutmut_orig)
    xǁProjectDetectorǁ_check_package_json__mutmut_orig.__name__ = 'xǁProjectDetectorǁ_check_package_json'

    def xǁProjectDetectorǁdetect_project_types__mutmut_orig(self, path: Path, max_depth: int = 5) -> list[str]:
        """
        Detect project types by scanning directory and suggesting templates.

        This is a convenience method that combines scan_directory and suggest_templates.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse

        Returns:
            List of suggested template names, ordered by priority
        """
        self.reset()
        self.scan_directory(path, max_depth)
        return self.suggest_templates()

    def xǁProjectDetectorǁdetect_project_types__mutmut_1(self, path: Path, max_depth: int = 6) -> list[str]:
        """
        Detect project types by scanning directory and suggesting templates.

        This is a convenience method that combines scan_directory and suggest_templates.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse

        Returns:
            List of suggested template names, ordered by priority
        """
        self.reset()
        self.scan_directory(path, max_depth)
        return self.suggest_templates()

    def xǁProjectDetectorǁdetect_project_types__mutmut_2(self, path: Path, max_depth: int = 5) -> list[str]:
        """
        Detect project types by scanning directory and suggesting templates.

        This is a convenience method that combines scan_directory and suggest_templates.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse

        Returns:
            List of suggested template names, ordered by priority
        """
        self.reset()
        self.scan_directory(None, max_depth)
        return self.suggest_templates()

    def xǁProjectDetectorǁdetect_project_types__mutmut_3(self, path: Path, max_depth: int = 5) -> list[str]:
        """
        Detect project types by scanning directory and suggesting templates.

        This is a convenience method that combines scan_directory and suggest_templates.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse

        Returns:
            List of suggested template names, ordered by priority
        """
        self.reset()
        self.scan_directory(path, None)
        return self.suggest_templates()

    def xǁProjectDetectorǁdetect_project_types__mutmut_4(self, path: Path, max_depth: int = 5) -> list[str]:
        """
        Detect project types by scanning directory and suggesting templates.

        This is a convenience method that combines scan_directory and suggest_templates.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse

        Returns:
            List of suggested template names, ordered by priority
        """
        self.reset()
        self.scan_directory(max_depth)
        return self.suggest_templates()

    def xǁProjectDetectorǁdetect_project_types__mutmut_5(self, path: Path, max_depth: int = 5) -> list[str]:
        """
        Detect project types by scanning directory and suggesting templates.

        This is a convenience method that combines scan_directory and suggest_templates.

        Args:
            path: Directory path to scan
            max_depth: Maximum depth to recurse

        Returns:
            List of suggested template names, ordered by priority
        """
        self.reset()
        self.scan_directory(path, )
        return self.suggest_templates()
    
    xǁProjectDetectorǁdetect_project_types__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁdetect_project_types__mutmut_1': xǁProjectDetectorǁdetect_project_types__mutmut_1, 
        'xǁProjectDetectorǁdetect_project_types__mutmut_2': xǁProjectDetectorǁdetect_project_types__mutmut_2, 
        'xǁProjectDetectorǁdetect_project_types__mutmut_3': xǁProjectDetectorǁdetect_project_types__mutmut_3, 
        'xǁProjectDetectorǁdetect_project_types__mutmut_4': xǁProjectDetectorǁdetect_project_types__mutmut_4, 
        'xǁProjectDetectorǁdetect_project_types__mutmut_5': xǁProjectDetectorǁdetect_project_types__mutmut_5
    }
    
    def detect_project_types(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁdetect_project_types__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁdetect_project_types__mutmut_mutants"), args, kwargs, self)
        return result 
    
    detect_project_types.__signature__ = _mutmut_signature(xǁProjectDetectorǁdetect_project_types__mutmut_orig)
    xǁProjectDetectorǁdetect_project_types__mutmut_orig.__name__ = 'xǁProjectDetectorǁdetect_project_types'

    def xǁProjectDetectorǁsuggest_templates__mutmut_orig(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_1(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = None

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_2(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(None)

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_3(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(None))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_4(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(None)

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_5(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(None))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_6(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = None
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_7(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["XXDockerXX", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_8(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_9(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["DOCKER", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_10(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "XXTerraformXX", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_11(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_12(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "TERRAFORM", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_13(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "XXPoetryXX", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_14(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_15(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "POETRY", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_16(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "XXPDMXX", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_17(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "pdm", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_18(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "XXPipenvXX"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_19(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_20(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "PIPENV"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_21(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = None
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_22(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t not in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_23(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = None
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_24(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(None)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_25(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_26(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(None)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_27(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools - other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_28(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(None)

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_29(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(None))

        logger.info(f"Suggested templates: {suggestions}")
        return suggestions

    def xǁProjectDetectorǁsuggest_templates__mutmut_30(self) -> list[str]:
        """
        Suggest gitignore templates based on detection.

        Returns:
            List of suggested template names, ordered by priority
        """
        suggestions = []

        # Add languages first (highest priority)
        suggestions.extend(sorted(self.detected_languages))

        # Add frameworks
        suggestions.extend(sorted(self.detected_frameworks))

        # Add tools
        tool_priority = ["Docker", "Terraform", "Poetry", "PDM", "Pipenv"]
        priority_tools = [t for t in tool_priority if t in self.detected_tools]
        other_tools = sorted(t for t in self.detected_tools if t not in tool_priority)
        suggestions.extend(priority_tools + other_tools)

        # Add OS last
        suggestions.extend(sorted(self.detected_os))

        logger.info(None)
        return suggestions
    
    xǁProjectDetectorǁsuggest_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProjectDetectorǁsuggest_templates__mutmut_1': xǁProjectDetectorǁsuggest_templates__mutmut_1, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_2': xǁProjectDetectorǁsuggest_templates__mutmut_2, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_3': xǁProjectDetectorǁsuggest_templates__mutmut_3, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_4': xǁProjectDetectorǁsuggest_templates__mutmut_4, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_5': xǁProjectDetectorǁsuggest_templates__mutmut_5, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_6': xǁProjectDetectorǁsuggest_templates__mutmut_6, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_7': xǁProjectDetectorǁsuggest_templates__mutmut_7, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_8': xǁProjectDetectorǁsuggest_templates__mutmut_8, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_9': xǁProjectDetectorǁsuggest_templates__mutmut_9, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_10': xǁProjectDetectorǁsuggest_templates__mutmut_10, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_11': xǁProjectDetectorǁsuggest_templates__mutmut_11, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_12': xǁProjectDetectorǁsuggest_templates__mutmut_12, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_13': xǁProjectDetectorǁsuggest_templates__mutmut_13, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_14': xǁProjectDetectorǁsuggest_templates__mutmut_14, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_15': xǁProjectDetectorǁsuggest_templates__mutmut_15, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_16': xǁProjectDetectorǁsuggest_templates__mutmut_16, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_17': xǁProjectDetectorǁsuggest_templates__mutmut_17, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_18': xǁProjectDetectorǁsuggest_templates__mutmut_18, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_19': xǁProjectDetectorǁsuggest_templates__mutmut_19, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_20': xǁProjectDetectorǁsuggest_templates__mutmut_20, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_21': xǁProjectDetectorǁsuggest_templates__mutmut_21, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_22': xǁProjectDetectorǁsuggest_templates__mutmut_22, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_23': xǁProjectDetectorǁsuggest_templates__mutmut_23, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_24': xǁProjectDetectorǁsuggest_templates__mutmut_24, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_25': xǁProjectDetectorǁsuggest_templates__mutmut_25, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_26': xǁProjectDetectorǁsuggest_templates__mutmut_26, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_27': xǁProjectDetectorǁsuggest_templates__mutmut_27, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_28': xǁProjectDetectorǁsuggest_templates__mutmut_28, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_29': xǁProjectDetectorǁsuggest_templates__mutmut_29, 
        'xǁProjectDetectorǁsuggest_templates__mutmut_30': xǁProjectDetectorǁsuggest_templates__mutmut_30
    }
    
    def suggest_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProjectDetectorǁsuggest_templates__mutmut_orig"), object.__getattribute__(self, "xǁProjectDetectorǁsuggest_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    suggest_templates.__signature__ = _mutmut_signature(xǁProjectDetectorǁsuggest_templates__mutmut_orig)
    xǁProjectDetectorǁsuggest_templates__mutmut_orig.__name__ = 'xǁProjectDetectorǁsuggest_templates'


# 🧰🌍🔚
