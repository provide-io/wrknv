#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Task execution environment detection and management.

This module provides auto-detection of virtual environments, UV projects,
and editable installs to determine the optimal task execution strategy.

Patterns adopted from pyvider's launch-context for robust detection.
"""

from __future__ import annotations

from importlib.metadata import Distribution, PackageNotFoundError
import json
import os
from pathlib import Path
import platform
import sys
from typing import Literal

from provide.foundation import logger
from provide.foundation.file.formats import read_toml

ExecutionMode = Literal["auto", "uv_run", "direct", "system"]
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


class ExecutionEnvironment:
    """Manages environment detection for task execution.

    This class detects the optimal execution strategy by checking:
    1. Environment variable overrides (WRKNV_TASK_RUNNER)
    2. Whether package is editable installed
    3. Whether project uses UV
    4. Available virtual environments

    Example:
        >>> env = ExecutionEnvironment(Path("/project"), "mypackage")
        >>> command = env.prepare_command("pytest tests/")
        >>> exec_env = env.prepare_environment({"FOO": "bar"})
    """

    def xǁExecutionEnvironmentǁ__init____mutmut_orig(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_1(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "XXautoXX",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_2(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "AUTO",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_3(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = None
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_4(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = None
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_5(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name and project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_6(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = None

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_7(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = ""
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_8(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = None
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_9(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = True
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_10(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = None
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_11(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = True
        self.use_uv_run: bool = False
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_12(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = None
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_13(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = True
        self.override_from_env: str | None = None

        # Run detection
        self._detect()

    def xǁExecutionEnvironmentǁ__init____mutmut_14(
        self,
        project_dir: Path,
        package_name: str | None = None,
        mode: ExecutionMode = "auto",
    ) -> None:
        """Initialize environment detection.

        Args:
            project_dir: Project root directory
            package_name: Package name to check for editable install
            mode: Execution mode override ("auto", "uv_run", "direct", "system")
        """
        self.project_dir = project_dir
        self.package_name = package_name or project_dir.name
        self.mode = mode

        # Detection results (cached)
        self.venv_path: Path | None = None
        self.is_uv_project: bool = False
        self.package_is_editable: bool = False
        self.use_uv_run: bool = False
        self.override_from_env: str | None = ""

        # Run detection
        self._detect()
    
    xǁExecutionEnvironmentǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁExecutionEnvironmentǁ__init____mutmut_1': xǁExecutionEnvironmentǁ__init____mutmut_1, 
        'xǁExecutionEnvironmentǁ__init____mutmut_2': xǁExecutionEnvironmentǁ__init____mutmut_2, 
        'xǁExecutionEnvironmentǁ__init____mutmut_3': xǁExecutionEnvironmentǁ__init____mutmut_3, 
        'xǁExecutionEnvironmentǁ__init____mutmut_4': xǁExecutionEnvironmentǁ__init____mutmut_4, 
        'xǁExecutionEnvironmentǁ__init____mutmut_5': xǁExecutionEnvironmentǁ__init____mutmut_5, 
        'xǁExecutionEnvironmentǁ__init____mutmut_6': xǁExecutionEnvironmentǁ__init____mutmut_6, 
        'xǁExecutionEnvironmentǁ__init____mutmut_7': xǁExecutionEnvironmentǁ__init____mutmut_7, 
        'xǁExecutionEnvironmentǁ__init____mutmut_8': xǁExecutionEnvironmentǁ__init____mutmut_8, 
        'xǁExecutionEnvironmentǁ__init____mutmut_9': xǁExecutionEnvironmentǁ__init____mutmut_9, 
        'xǁExecutionEnvironmentǁ__init____mutmut_10': xǁExecutionEnvironmentǁ__init____mutmut_10, 
        'xǁExecutionEnvironmentǁ__init____mutmut_11': xǁExecutionEnvironmentǁ__init____mutmut_11, 
        'xǁExecutionEnvironmentǁ__init____mutmut_12': xǁExecutionEnvironmentǁ__init____mutmut_12, 
        'xǁExecutionEnvironmentǁ__init____mutmut_13': xǁExecutionEnvironmentǁ__init____mutmut_13, 
        'xǁExecutionEnvironmentǁ__init____mutmut_14': xǁExecutionEnvironmentǁ__init____mutmut_14
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁExecutionEnvironmentǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁExecutionEnvironmentǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁExecutionEnvironmentǁ__init____mutmut_orig)
    xǁExecutionEnvironmentǁ__init____mutmut_orig.__name__ = 'xǁExecutionEnvironmentǁ__init__'

    def xǁExecutionEnvironmentǁ_detect__mutmut_orig(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_1(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = None
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_2(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get(None)
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_3(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("XXWRKNV_TASK_RUNNERXX")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_4(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("wrknv_task_runner")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_5(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                None,
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_6(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=None,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_7(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_8(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_9(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "XXTask runner override from environmentXX",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_10(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_11(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "TASK RUNNER OVERRIDE FROM ENVIRONMENT",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_12(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = None
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_13(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env != "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_14(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "XXuv runXX"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_15(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "UV RUN"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_16(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = None
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_17(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = None
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_18(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = None

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_19(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode != "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_20(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "XXuv_runXX":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_21(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "UV_RUN":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_22(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = None
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_23(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = False
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_24(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode != "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_25(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "XXdirectXX":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_26(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "DIRECT":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_27(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = None
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_28(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = True
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_29(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode != "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_30(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "XXsystemXX":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_31(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "SYSTEM":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_32(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = None
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_33(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = True
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_34(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = ""  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_35(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = None
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_36(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = True
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_37(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                None,
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_38(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=None,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_39(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_40(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_41(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "XXEditable install detected - using direct executionXX",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_42(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_43(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "EDITABLE INSTALL DETECTED - USING DIRECT EXECUTION",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_44(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = None
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_45(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = False
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_46(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug(None)
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_47(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("XXUV project detected - using uv runXX")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_48(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("uv project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_49(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV PROJECT DETECTED - USING UV RUN")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_50(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = None
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_51(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = True
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_52(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug(None)

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_53(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("XXUsing direct execution with PATH modificationXX")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_54(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("using direct execution with path modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_55(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("USING DIRECT EXECUTION WITH PATH MODIFICATION")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_56(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            None,
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_57(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_58(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=None,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_59(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=None,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_60(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=None,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_61(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=None,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_62(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_63(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_64(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_65(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_66(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_67(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            )

    def xǁExecutionEnvironmentǁ_detect__mutmut_68(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "XXEnvironment detection completeXX",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_69(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "environment detection complete",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_70(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "ENVIRONMENT DETECTION COMPLETE",
            venv_path=str(self.venv_path) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )

    def xǁExecutionEnvironmentǁ_detect__mutmut_71(self) -> None:
        """Run all detection checks and determine execution strategy."""
        # Priority 1: Check for environment variable override
        self.override_from_env = os.environ.get("WRKNV_TASK_RUNNER")
        if self.override_from_env:
            logger.debug(
                "Task runner override from environment",
                runner=self.override_from_env,
            )
            self.use_uv_run = self.override_from_env == "uv run"
            return

        # Priority 2: Detect environment components
        self.venv_path = self._detect_venv()
        self.is_uv_project = self._is_uv_project()
        self.package_is_editable = self._is_editable_install()

        # Priority 3: Apply mode-specific logic
        if self.mode == "uv_run":
            self.use_uv_run = True
        elif self.mode == "direct":
            self.use_uv_run = False
        elif self.mode == "system":
            self.use_uv_run = False
            self.venv_path = None  # Ignore venv
        # Auto-detection logic:
        # If editable install detected -> use direct (PATH) to preserve it
        # If UV project but not editable -> use uv run
        # Otherwise -> use direct with PATH modification
        elif self.package_is_editable:
            self.use_uv_run = False
            logger.debug(
                "Editable install detected - using direct execution",
                package=self.package_name,
            )
        elif self.is_uv_project:
            self.use_uv_run = True
            logger.debug("UV project detected - using uv run")
        else:
            self.use_uv_run = False
            logger.debug("Using direct execution with PATH modification")

        logger.debug(
            "Environment detection complete",
            venv_path=str(None) if self.venv_path else None,
            is_uv_project=self.is_uv_project,
            package_is_editable=self.package_is_editable,
            use_uv_run=self.use_uv_run,
            mode=self.mode,
        )
    
    xǁExecutionEnvironmentǁ_detect__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁExecutionEnvironmentǁ_detect__mutmut_1': xǁExecutionEnvironmentǁ_detect__mutmut_1, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_2': xǁExecutionEnvironmentǁ_detect__mutmut_2, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_3': xǁExecutionEnvironmentǁ_detect__mutmut_3, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_4': xǁExecutionEnvironmentǁ_detect__mutmut_4, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_5': xǁExecutionEnvironmentǁ_detect__mutmut_5, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_6': xǁExecutionEnvironmentǁ_detect__mutmut_6, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_7': xǁExecutionEnvironmentǁ_detect__mutmut_7, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_8': xǁExecutionEnvironmentǁ_detect__mutmut_8, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_9': xǁExecutionEnvironmentǁ_detect__mutmut_9, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_10': xǁExecutionEnvironmentǁ_detect__mutmut_10, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_11': xǁExecutionEnvironmentǁ_detect__mutmut_11, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_12': xǁExecutionEnvironmentǁ_detect__mutmut_12, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_13': xǁExecutionEnvironmentǁ_detect__mutmut_13, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_14': xǁExecutionEnvironmentǁ_detect__mutmut_14, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_15': xǁExecutionEnvironmentǁ_detect__mutmut_15, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_16': xǁExecutionEnvironmentǁ_detect__mutmut_16, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_17': xǁExecutionEnvironmentǁ_detect__mutmut_17, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_18': xǁExecutionEnvironmentǁ_detect__mutmut_18, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_19': xǁExecutionEnvironmentǁ_detect__mutmut_19, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_20': xǁExecutionEnvironmentǁ_detect__mutmut_20, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_21': xǁExecutionEnvironmentǁ_detect__mutmut_21, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_22': xǁExecutionEnvironmentǁ_detect__mutmut_22, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_23': xǁExecutionEnvironmentǁ_detect__mutmut_23, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_24': xǁExecutionEnvironmentǁ_detect__mutmut_24, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_25': xǁExecutionEnvironmentǁ_detect__mutmut_25, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_26': xǁExecutionEnvironmentǁ_detect__mutmut_26, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_27': xǁExecutionEnvironmentǁ_detect__mutmut_27, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_28': xǁExecutionEnvironmentǁ_detect__mutmut_28, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_29': xǁExecutionEnvironmentǁ_detect__mutmut_29, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_30': xǁExecutionEnvironmentǁ_detect__mutmut_30, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_31': xǁExecutionEnvironmentǁ_detect__mutmut_31, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_32': xǁExecutionEnvironmentǁ_detect__mutmut_32, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_33': xǁExecutionEnvironmentǁ_detect__mutmut_33, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_34': xǁExecutionEnvironmentǁ_detect__mutmut_34, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_35': xǁExecutionEnvironmentǁ_detect__mutmut_35, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_36': xǁExecutionEnvironmentǁ_detect__mutmut_36, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_37': xǁExecutionEnvironmentǁ_detect__mutmut_37, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_38': xǁExecutionEnvironmentǁ_detect__mutmut_38, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_39': xǁExecutionEnvironmentǁ_detect__mutmut_39, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_40': xǁExecutionEnvironmentǁ_detect__mutmut_40, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_41': xǁExecutionEnvironmentǁ_detect__mutmut_41, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_42': xǁExecutionEnvironmentǁ_detect__mutmut_42, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_43': xǁExecutionEnvironmentǁ_detect__mutmut_43, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_44': xǁExecutionEnvironmentǁ_detect__mutmut_44, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_45': xǁExecutionEnvironmentǁ_detect__mutmut_45, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_46': xǁExecutionEnvironmentǁ_detect__mutmut_46, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_47': xǁExecutionEnvironmentǁ_detect__mutmut_47, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_48': xǁExecutionEnvironmentǁ_detect__mutmut_48, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_49': xǁExecutionEnvironmentǁ_detect__mutmut_49, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_50': xǁExecutionEnvironmentǁ_detect__mutmut_50, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_51': xǁExecutionEnvironmentǁ_detect__mutmut_51, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_52': xǁExecutionEnvironmentǁ_detect__mutmut_52, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_53': xǁExecutionEnvironmentǁ_detect__mutmut_53, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_54': xǁExecutionEnvironmentǁ_detect__mutmut_54, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_55': xǁExecutionEnvironmentǁ_detect__mutmut_55, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_56': xǁExecutionEnvironmentǁ_detect__mutmut_56, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_57': xǁExecutionEnvironmentǁ_detect__mutmut_57, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_58': xǁExecutionEnvironmentǁ_detect__mutmut_58, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_59': xǁExecutionEnvironmentǁ_detect__mutmut_59, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_60': xǁExecutionEnvironmentǁ_detect__mutmut_60, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_61': xǁExecutionEnvironmentǁ_detect__mutmut_61, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_62': xǁExecutionEnvironmentǁ_detect__mutmut_62, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_63': xǁExecutionEnvironmentǁ_detect__mutmut_63, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_64': xǁExecutionEnvironmentǁ_detect__mutmut_64, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_65': xǁExecutionEnvironmentǁ_detect__mutmut_65, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_66': xǁExecutionEnvironmentǁ_detect__mutmut_66, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_67': xǁExecutionEnvironmentǁ_detect__mutmut_67, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_68': xǁExecutionEnvironmentǁ_detect__mutmut_68, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_69': xǁExecutionEnvironmentǁ_detect__mutmut_69, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_70': xǁExecutionEnvironmentǁ_detect__mutmut_70, 
        'xǁExecutionEnvironmentǁ_detect__mutmut_71': xǁExecutionEnvironmentǁ_detect__mutmut_71
    }
    
    def _detect(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁExecutionEnvironmentǁ_detect__mutmut_orig"), object.__getattribute__(self, "xǁExecutionEnvironmentǁ_detect__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _detect.__signature__ = _mutmut_signature(xǁExecutionEnvironmentǁ_detect__mutmut_orig)
    xǁExecutionEnvironmentǁ_detect__mutmut_orig.__name__ = 'xǁExecutionEnvironmentǁ_detect'

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_orig(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_1(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = None
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_2(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().upper()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_3(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = None

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_4(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().upper()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_5(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine not in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_6(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["XXx86_64XX", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_7(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["X86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_8(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "XXamd64XX"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_9(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "AMD64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_10(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = None
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_11(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "XXamd64XX"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_12(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "AMD64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_13(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine not in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_14(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["XXarm64XX", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_15(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["ARM64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_16(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "XXaarch64XX"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_17(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "AARCH64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_18(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = None
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_19(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "XXarm64XX"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_20(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "ARM64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_21(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = None

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_22(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = None
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_23(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" * f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_24(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir * "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_25(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "XXworkenvXX" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_26(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "WORKENV" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_27(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() or (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_28(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path * "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_29(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "XXpyvenv.cfgXX").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_30(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "PYVENV.CFG").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_31(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace(None, path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_32(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=None)
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_33(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace(path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_34(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", )
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_35(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("XXFound workenv venvXX", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_36(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_37(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("FOUND WORKENV VENV", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_38(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(None))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_39(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = None
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_40(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir * ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_41(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / "XX.venvXX"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_42(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".VENV"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_43(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() or (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_44(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path * "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_45(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "XXpyvenv.cfgXX").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_46(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "PYVENV.CFG").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_47(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace(None, path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_48(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=None)
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_49(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace(path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_50(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", )
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_51(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("XXFound .venvXX", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_52(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_53(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("FOUND .VENV", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_54(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(None))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_55(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = None
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_56(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir * "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_57(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "XXvenvXX"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_58(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "VENV"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_59(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() or (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_60(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path * "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_61(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "XXpyvenv.cfgXX").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_62(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "PYVENV.CFG").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_63(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace(None, path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_64(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=None)
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_65(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace(path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_66(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", )
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_67(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("XXFound venvXX", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_68(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_69(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("FOUND VENV", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_70(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(None))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_71(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") and (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_72(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(None, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_73(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, None) or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_74(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr("real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_75(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, ) or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_76(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "XXreal_prefixXX") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_77(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "REAL_PREFIX") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_78(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") or sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_79(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(None, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_80(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, None) and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_81(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr("base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_82(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, ) and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_83(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "XXbase_prefixXX") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_84(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "BASE_PREFIX") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_85(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix == sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_86(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = None
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_87(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(None)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_88(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace(None, path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_89(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=None)
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_90(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace(path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_91(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", )
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_92(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("XXUsing current venvXX", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_93(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("using current venv", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_94(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("USING CURRENT VENV", path=str(current_venv))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_95(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(None))
            return current_venv

        logger.trace("No venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_96(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace(None)
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_97(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("XXNo venv foundXX")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_98(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("no venv found")
        return None

    def xǁExecutionEnvironmentǁ_detect_venv__mutmut_99(self) -> Path | None:
        """Find virtual environment using priority order.

        Priority:
        1. workenv/{package}_{os}_{arch}/ (wrknv pattern)
        2. .venv/ (standard)
        3. venv/ (fallback)
        4. Current Python's venv (if running in one)

        Returns:
            Path to venv if found, None otherwise
        """
        # Priority 1: workenv pattern
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Normalize architecture
        if machine in ["x86_64", "amd64"]:
            arch = "amd64"
        elif machine in ["arm64", "aarch64"]:
            arch = "arm64"
        else:
            arch = machine

        workenv_path = self.project_dir / "workenv" / f"{self.package_name}_{system}_{arch}"
        if workenv_path.exists() and (workenv_path / "pyvenv.cfg").exists():
            logger.trace("Found workenv venv", path=str(workenv_path))
            return workenv_path

        # Priority 2: .venv
        venv_path = self.project_dir / ".venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found .venv", path=str(venv_path))
            return venv_path

        # Priority 3: venv
        venv_path = self.project_dir / "venv"
        if venv_path.exists() and (venv_path / "pyvenv.cfg").exists():
            logger.trace("Found venv", path=str(venv_path))
            return venv_path

        # Priority 4: Check if we're currently in a venv
        if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
            current_venv = Path(sys.prefix)
            logger.trace("Using current venv", path=str(current_venv))
            return current_venv

        logger.trace("NO VENV FOUND")
        return None
    
    xǁExecutionEnvironmentǁ_detect_venv__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁExecutionEnvironmentǁ_detect_venv__mutmut_1': xǁExecutionEnvironmentǁ_detect_venv__mutmut_1, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_2': xǁExecutionEnvironmentǁ_detect_venv__mutmut_2, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_3': xǁExecutionEnvironmentǁ_detect_venv__mutmut_3, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_4': xǁExecutionEnvironmentǁ_detect_venv__mutmut_4, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_5': xǁExecutionEnvironmentǁ_detect_venv__mutmut_5, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_6': xǁExecutionEnvironmentǁ_detect_venv__mutmut_6, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_7': xǁExecutionEnvironmentǁ_detect_venv__mutmut_7, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_8': xǁExecutionEnvironmentǁ_detect_venv__mutmut_8, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_9': xǁExecutionEnvironmentǁ_detect_venv__mutmut_9, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_10': xǁExecutionEnvironmentǁ_detect_venv__mutmut_10, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_11': xǁExecutionEnvironmentǁ_detect_venv__mutmut_11, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_12': xǁExecutionEnvironmentǁ_detect_venv__mutmut_12, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_13': xǁExecutionEnvironmentǁ_detect_venv__mutmut_13, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_14': xǁExecutionEnvironmentǁ_detect_venv__mutmut_14, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_15': xǁExecutionEnvironmentǁ_detect_venv__mutmut_15, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_16': xǁExecutionEnvironmentǁ_detect_venv__mutmut_16, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_17': xǁExecutionEnvironmentǁ_detect_venv__mutmut_17, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_18': xǁExecutionEnvironmentǁ_detect_venv__mutmut_18, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_19': xǁExecutionEnvironmentǁ_detect_venv__mutmut_19, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_20': xǁExecutionEnvironmentǁ_detect_venv__mutmut_20, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_21': xǁExecutionEnvironmentǁ_detect_venv__mutmut_21, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_22': xǁExecutionEnvironmentǁ_detect_venv__mutmut_22, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_23': xǁExecutionEnvironmentǁ_detect_venv__mutmut_23, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_24': xǁExecutionEnvironmentǁ_detect_venv__mutmut_24, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_25': xǁExecutionEnvironmentǁ_detect_venv__mutmut_25, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_26': xǁExecutionEnvironmentǁ_detect_venv__mutmut_26, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_27': xǁExecutionEnvironmentǁ_detect_venv__mutmut_27, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_28': xǁExecutionEnvironmentǁ_detect_venv__mutmut_28, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_29': xǁExecutionEnvironmentǁ_detect_venv__mutmut_29, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_30': xǁExecutionEnvironmentǁ_detect_venv__mutmut_30, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_31': xǁExecutionEnvironmentǁ_detect_venv__mutmut_31, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_32': xǁExecutionEnvironmentǁ_detect_venv__mutmut_32, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_33': xǁExecutionEnvironmentǁ_detect_venv__mutmut_33, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_34': xǁExecutionEnvironmentǁ_detect_venv__mutmut_34, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_35': xǁExecutionEnvironmentǁ_detect_venv__mutmut_35, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_36': xǁExecutionEnvironmentǁ_detect_venv__mutmut_36, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_37': xǁExecutionEnvironmentǁ_detect_venv__mutmut_37, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_38': xǁExecutionEnvironmentǁ_detect_venv__mutmut_38, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_39': xǁExecutionEnvironmentǁ_detect_venv__mutmut_39, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_40': xǁExecutionEnvironmentǁ_detect_venv__mutmut_40, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_41': xǁExecutionEnvironmentǁ_detect_venv__mutmut_41, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_42': xǁExecutionEnvironmentǁ_detect_venv__mutmut_42, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_43': xǁExecutionEnvironmentǁ_detect_venv__mutmut_43, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_44': xǁExecutionEnvironmentǁ_detect_venv__mutmut_44, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_45': xǁExecutionEnvironmentǁ_detect_venv__mutmut_45, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_46': xǁExecutionEnvironmentǁ_detect_venv__mutmut_46, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_47': xǁExecutionEnvironmentǁ_detect_venv__mutmut_47, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_48': xǁExecutionEnvironmentǁ_detect_venv__mutmut_48, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_49': xǁExecutionEnvironmentǁ_detect_venv__mutmut_49, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_50': xǁExecutionEnvironmentǁ_detect_venv__mutmut_50, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_51': xǁExecutionEnvironmentǁ_detect_venv__mutmut_51, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_52': xǁExecutionEnvironmentǁ_detect_venv__mutmut_52, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_53': xǁExecutionEnvironmentǁ_detect_venv__mutmut_53, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_54': xǁExecutionEnvironmentǁ_detect_venv__mutmut_54, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_55': xǁExecutionEnvironmentǁ_detect_venv__mutmut_55, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_56': xǁExecutionEnvironmentǁ_detect_venv__mutmut_56, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_57': xǁExecutionEnvironmentǁ_detect_venv__mutmut_57, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_58': xǁExecutionEnvironmentǁ_detect_venv__mutmut_58, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_59': xǁExecutionEnvironmentǁ_detect_venv__mutmut_59, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_60': xǁExecutionEnvironmentǁ_detect_venv__mutmut_60, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_61': xǁExecutionEnvironmentǁ_detect_venv__mutmut_61, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_62': xǁExecutionEnvironmentǁ_detect_venv__mutmut_62, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_63': xǁExecutionEnvironmentǁ_detect_venv__mutmut_63, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_64': xǁExecutionEnvironmentǁ_detect_venv__mutmut_64, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_65': xǁExecutionEnvironmentǁ_detect_venv__mutmut_65, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_66': xǁExecutionEnvironmentǁ_detect_venv__mutmut_66, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_67': xǁExecutionEnvironmentǁ_detect_venv__mutmut_67, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_68': xǁExecutionEnvironmentǁ_detect_venv__mutmut_68, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_69': xǁExecutionEnvironmentǁ_detect_venv__mutmut_69, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_70': xǁExecutionEnvironmentǁ_detect_venv__mutmut_70, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_71': xǁExecutionEnvironmentǁ_detect_venv__mutmut_71, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_72': xǁExecutionEnvironmentǁ_detect_venv__mutmut_72, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_73': xǁExecutionEnvironmentǁ_detect_venv__mutmut_73, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_74': xǁExecutionEnvironmentǁ_detect_venv__mutmut_74, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_75': xǁExecutionEnvironmentǁ_detect_venv__mutmut_75, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_76': xǁExecutionEnvironmentǁ_detect_venv__mutmut_76, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_77': xǁExecutionEnvironmentǁ_detect_venv__mutmut_77, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_78': xǁExecutionEnvironmentǁ_detect_venv__mutmut_78, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_79': xǁExecutionEnvironmentǁ_detect_venv__mutmut_79, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_80': xǁExecutionEnvironmentǁ_detect_venv__mutmut_80, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_81': xǁExecutionEnvironmentǁ_detect_venv__mutmut_81, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_82': xǁExecutionEnvironmentǁ_detect_venv__mutmut_82, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_83': xǁExecutionEnvironmentǁ_detect_venv__mutmut_83, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_84': xǁExecutionEnvironmentǁ_detect_venv__mutmut_84, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_85': xǁExecutionEnvironmentǁ_detect_venv__mutmut_85, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_86': xǁExecutionEnvironmentǁ_detect_venv__mutmut_86, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_87': xǁExecutionEnvironmentǁ_detect_venv__mutmut_87, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_88': xǁExecutionEnvironmentǁ_detect_venv__mutmut_88, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_89': xǁExecutionEnvironmentǁ_detect_venv__mutmut_89, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_90': xǁExecutionEnvironmentǁ_detect_venv__mutmut_90, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_91': xǁExecutionEnvironmentǁ_detect_venv__mutmut_91, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_92': xǁExecutionEnvironmentǁ_detect_venv__mutmut_92, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_93': xǁExecutionEnvironmentǁ_detect_venv__mutmut_93, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_94': xǁExecutionEnvironmentǁ_detect_venv__mutmut_94, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_95': xǁExecutionEnvironmentǁ_detect_venv__mutmut_95, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_96': xǁExecutionEnvironmentǁ_detect_venv__mutmut_96, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_97': xǁExecutionEnvironmentǁ_detect_venv__mutmut_97, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_98': xǁExecutionEnvironmentǁ_detect_venv__mutmut_98, 
        'xǁExecutionEnvironmentǁ_detect_venv__mutmut_99': xǁExecutionEnvironmentǁ_detect_venv__mutmut_99
    }
    
    def _detect_venv(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁExecutionEnvironmentǁ_detect_venv__mutmut_orig"), object.__getattribute__(self, "xǁExecutionEnvironmentǁ_detect_venv__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _detect_venv.__signature__ = _mutmut_signature(xǁExecutionEnvironmentǁ_detect_venv__mutmut_orig)
    xǁExecutionEnvironmentǁ_detect_venv__mutmut_orig.__name__ = 'xǁExecutionEnvironmentǁ_detect_venv'

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_orig(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_1(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir * "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_2(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "XXuv.lockXX").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_3(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "UV.LOCK").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_4(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace(None)
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_5(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("XXUV project detected via uv.lockXX")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_6(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("uv project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_7(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV PROJECT DETECTED VIA UV.LOCK")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_8(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return False

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_9(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = None
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_10(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir * "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_11(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "XXpyproject.tomlXX"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_12(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "PYPROJECT.TOML"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_13(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = None
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_14(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(None, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_15(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default=None)
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_16(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_17(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, )
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_18(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data or "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_19(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data or "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_20(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "XXtoolXX" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_21(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "TOOL" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_22(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" not in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_23(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "XXuvXX" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_24(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "UV" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_25(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" not in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_26(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["XXtoolXX"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_27(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["TOOL"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_28(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace(None)
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_29(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("XXUV project detected via pyproject.toml [tool.uv]XX")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_30(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("uv project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_31(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV PROJECT DETECTED VIA PYPROJECT.TOML [TOOL.UV]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_32(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return False
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return False

    def xǁExecutionEnvironmentǁ_is_uv_project__mutmut_33(self) -> bool:
        """Check if project uses UV package manager.

        Checks for:
        1. uv.lock file (strongest indicator)
        2. [tool.uv] section in pyproject.toml

        Returns:
            True if UV project, False otherwise
        """
        # Check for uv.lock (strongest indicator)
        if (self.project_dir / "uv.lock").exists():
            logger.trace("UV project detected via uv.lock")
            return True

        # Check for [tool.uv] in pyproject.toml
        pyproject = self.project_dir / "pyproject.toml"
        if pyproject.exists():
            try:
                data = read_toml(pyproject, default={})
                if data and "tool" in data and "uv" in data["tool"]:
                    logger.trace("UV project detected via pyproject.toml [tool.uv]")
                    return True
            except Exception:
                pass  # nosec B110 - Fallback if pyproject.toml parsing fails

        return True
    
    xǁExecutionEnvironmentǁ_is_uv_project__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_1': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_1, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_2': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_2, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_3': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_3, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_4': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_4, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_5': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_5, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_6': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_6, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_7': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_7, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_8': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_8, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_9': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_9, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_10': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_10, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_11': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_11, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_12': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_12, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_13': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_13, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_14': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_14, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_15': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_15, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_16': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_16, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_17': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_17, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_18': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_18, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_19': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_19, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_20': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_20, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_21': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_21, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_22': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_22, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_23': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_23, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_24': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_24, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_25': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_25, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_26': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_26, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_27': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_27, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_28': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_28, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_29': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_29, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_30': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_30, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_31': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_31, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_32': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_32, 
        'xǁExecutionEnvironmentǁ_is_uv_project__mutmut_33': xǁExecutionEnvironmentǁ_is_uv_project__mutmut_33
    }
    
    def _is_uv_project(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁExecutionEnvironmentǁ_is_uv_project__mutmut_orig"), object.__getattribute__(self, "xǁExecutionEnvironmentǁ_is_uv_project__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_uv_project.__signature__ = _mutmut_signature(xǁExecutionEnvironmentǁ_is_uv_project__mutmut_orig)
    xǁExecutionEnvironmentǁ_is_uv_project__mutmut_orig.__name__ = 'xǁExecutionEnvironmentǁ_is_uv_project'

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_orig(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_1(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = None
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_2(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(None)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_3(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = None
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_4(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text(None)
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_5(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("XXdirect_url.jsonXX")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_6(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("DIRECT_URL.JSON")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_7(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = None
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_8(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(None)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_9(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get(None, False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_10(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", None):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_11(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get(False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_12(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", ):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_13(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get(None, {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_14(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", None).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_15(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get({}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_16(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", ).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_17(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("XXdir_infoXX", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_18(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("DIR_INFO", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_19(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("XXeditableXX", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_20(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("EDITABLE", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_21(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", True):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_22(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        None,
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_23(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=None,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_24(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_25(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_26(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "XXEditable install detected via direct_url.jsonXX",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_27(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_28(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "EDITABLE INSTALL DETECTED VIA DIRECT_URL.JSON",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_29(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return False
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_30(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = None
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_31(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(None)
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_32(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace(None, "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_33(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", None))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_34(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_35(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", ))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_36(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("XX-XX", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_37(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "XX_XX"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_38(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_39(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = None

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_40(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(None).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_41(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name != "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_42(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "XXsrcXX":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_43(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "SRC":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_44(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        None,
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_45(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=None,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_46(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=None,
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_47(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_48(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_49(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_50(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "XXEditable install detected via src/ structureXX",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_51(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_52(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "EDITABLE INSTALL DETECTED VIA SRC/ STRUCTURE",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_53(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(None),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_54(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return False
        except (ImportError, AttributeError, TypeError):
            pass

        return False

    def xǁExecutionEnvironmentǁ_is_editable_install__mutmut_55(self) -> bool:
        """Check if package is installed in editable mode.

        Uses two detection methods:
        1. Modern: direct_url.json with editable flag (Python 3.11+)
        2. Legacy: src/ directory structure pattern (adopted from pyvider)

        Returns:
            True if package is editable install, False otherwise
        """
        # Method 1: Modern detection via direct_url.json
        try:
            dist = Distribution.from_name(self.package_name)
            direct_url_text = dist.read_text("direct_url.json")
            if direct_url_text:
                direct_url = json.loads(direct_url_text)
                if direct_url.get("dir_info", {}).get("editable", False):
                    logger.trace(
                        "Editable install detected via direct_url.json",
                        package=self.package_name,
                    )
                    return True
        except (PackageNotFoundError, FileNotFoundError, json.JSONDecodeError):
            pass

        # Method 2: Legacy detection via src/ structure (pyvider pattern)
        # Check if package module is in src/ directory structure
        try:
            import importlib

            module = importlib.import_module(self.package_name.replace("-", "_"))
            if module.__file__ is not None:
                module_path = Path(module.__file__).parent

                # Check if module is in src/ directory structure
                if module_path.parent.name == "src":
                    logger.trace(
                        "Editable install detected via src/ structure",
                        package=self.package_name,
                        path=str(module_path),
                    )
                    return True
        except (ImportError, AttributeError, TypeError):
            pass

        return True
    
    xǁExecutionEnvironmentǁ_is_editable_install__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_1': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_1, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_2': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_2, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_3': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_3, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_4': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_4, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_5': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_5, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_6': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_6, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_7': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_7, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_8': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_8, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_9': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_9, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_10': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_10, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_11': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_11, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_12': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_12, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_13': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_13, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_14': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_14, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_15': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_15, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_16': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_16, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_17': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_17, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_18': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_18, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_19': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_19, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_20': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_20, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_21': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_21, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_22': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_22, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_23': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_23, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_24': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_24, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_25': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_25, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_26': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_26, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_27': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_27, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_28': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_28, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_29': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_29, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_30': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_30, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_31': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_31, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_32': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_32, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_33': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_33, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_34': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_34, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_35': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_35, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_36': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_36, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_37': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_37, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_38': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_38, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_39': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_39, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_40': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_40, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_41': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_41, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_42': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_42, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_43': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_43, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_44': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_44, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_45': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_45, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_46': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_46, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_47': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_47, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_48': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_48, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_49': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_49, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_50': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_50, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_51': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_51, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_52': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_52, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_53': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_53, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_54': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_54, 
        'xǁExecutionEnvironmentǁ_is_editable_install__mutmut_55': xǁExecutionEnvironmentǁ_is_editable_install__mutmut_55
    }
    
    def _is_editable_install(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁExecutionEnvironmentǁ_is_editable_install__mutmut_orig"), object.__getattribute__(self, "xǁExecutionEnvironmentǁ_is_editable_install__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _is_editable_install.__signature__ = _mutmut_signature(xǁExecutionEnvironmentǁ_is_editable_install__mutmut_orig)
    xǁExecutionEnvironmentǁ_is_editable_install__mutmut_orig.__name__ = 'xǁExecutionEnvironmentǁ_is_editable_install'

    def xǁExecutionEnvironmentǁprepare_command__mutmut_orig(self, command: str, prefix_override: str | None = None) -> str:
        """Prepare command with uv run prefix if needed.

        Args:
            command: Original command string
            prefix_override: Per-task prefix override (takes precedence)

        Returns:
            Modified command (may have 'uv run' or custom prefix prepended)
        """
        # Per-task override takes precedence
        if prefix_override is not None:
            if prefix_override:  # Non-empty string
                return f"{prefix_override} {command}"
            return command  # Empty string = explicitly no prefix

        # Environment variable override
        if self.override_from_env:
            return f"{self.override_from_env} {command}"

        # Auto-detected behavior
        if self.use_uv_run:
            return f"uv run {command}"

        return command

    def xǁExecutionEnvironmentǁprepare_command__mutmut_1(self, command: str, prefix_override: str | None = None) -> str:
        """Prepare command with uv run prefix if needed.

        Args:
            command: Original command string
            prefix_override: Per-task prefix override (takes precedence)

        Returns:
            Modified command (may have 'uv run' or custom prefix prepended)
        """
        # Per-task override takes precedence
        if prefix_override is None:
            if prefix_override:  # Non-empty string
                return f"{prefix_override} {command}"
            return command  # Empty string = explicitly no prefix

        # Environment variable override
        if self.override_from_env:
            return f"{self.override_from_env} {command}"

        # Auto-detected behavior
        if self.use_uv_run:
            return f"uv run {command}"

        return command
    
    xǁExecutionEnvironmentǁprepare_command__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁExecutionEnvironmentǁprepare_command__mutmut_1': xǁExecutionEnvironmentǁprepare_command__mutmut_1
    }
    
    def prepare_command(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁExecutionEnvironmentǁprepare_command__mutmut_orig"), object.__getattribute__(self, "xǁExecutionEnvironmentǁprepare_command__mutmut_mutants"), args, kwargs, self)
        return result 
    
    prepare_command.__signature__ = _mutmut_signature(xǁExecutionEnvironmentǁprepare_command__mutmut_orig)
    xǁExecutionEnvironmentǁprepare_command__mutmut_orig.__name__ = 'xǁExecutionEnvironmentǁprepare_command'

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_orig(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_1(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = None

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_2(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_3(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = None
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_4(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(None)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_5(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = None
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_6(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = "XX;XX" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_7(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() != "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_8(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "XXWindowsXX" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_9(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_10(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "WINDOWS" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_11(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else "XX:XX"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_12(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = None
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_13(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get(None, os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_14(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", None)
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_15(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get(os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_16(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", )
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_17(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("XXPATHXX", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_18(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("path", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_19(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get(None, ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_20(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", None))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_21(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get(""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_22(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_23(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("XXPATHXX", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_24(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("path", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_25(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", "XXXX"))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_26(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = None
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_27(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["XXPATHXX"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_28(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["path"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_29(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace(None, bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_30(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=None)

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_31(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace(bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_32(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", )

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_33(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("XXPrepended venv bin to PATHXX", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_34(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("prepended venv bin to path", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_35(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("PREPENDED VENV BIN TO PATH", bin_dir=str(bin_dir))

        return env

    def xǁExecutionEnvironmentǁprepare_environment__mutmut_36(self, base_env: dict[str, str] | None = None) -> dict[str, str]:
        """Prepare environment dictionary with PATH modifications.

        Args:
            base_env: Base environment to extend

        Returns:
            Environment dictionary with PATH modifications if needed
        """
        env = base_env.copy() if base_env else {}

        # If using uv run, don't modify PATH (uv handles it)
        if self.use_uv_run:
            return env

        # If no venv, return as-is
        if not self.venv_path:
            return env

        # Prepend venv bin to PATH for direct execution
        bin_dir = self._get_bin_dir(self.venv_path)
        if bin_dir.exists():
            separator = ";" if platform.system() == "Windows" else ":"
            current_path = env.get("PATH", os.environ.get("PATH", ""))
            env["PATH"] = f"{bin_dir}{separator}{current_path}"
            logger.trace("Prepended venv bin to PATH", bin_dir=str(None))

        return env
    
    xǁExecutionEnvironmentǁprepare_environment__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁExecutionEnvironmentǁprepare_environment__mutmut_1': xǁExecutionEnvironmentǁprepare_environment__mutmut_1, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_2': xǁExecutionEnvironmentǁprepare_environment__mutmut_2, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_3': xǁExecutionEnvironmentǁprepare_environment__mutmut_3, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_4': xǁExecutionEnvironmentǁprepare_environment__mutmut_4, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_5': xǁExecutionEnvironmentǁprepare_environment__mutmut_5, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_6': xǁExecutionEnvironmentǁprepare_environment__mutmut_6, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_7': xǁExecutionEnvironmentǁprepare_environment__mutmut_7, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_8': xǁExecutionEnvironmentǁprepare_environment__mutmut_8, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_9': xǁExecutionEnvironmentǁprepare_environment__mutmut_9, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_10': xǁExecutionEnvironmentǁprepare_environment__mutmut_10, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_11': xǁExecutionEnvironmentǁprepare_environment__mutmut_11, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_12': xǁExecutionEnvironmentǁprepare_environment__mutmut_12, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_13': xǁExecutionEnvironmentǁprepare_environment__mutmut_13, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_14': xǁExecutionEnvironmentǁprepare_environment__mutmut_14, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_15': xǁExecutionEnvironmentǁprepare_environment__mutmut_15, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_16': xǁExecutionEnvironmentǁprepare_environment__mutmut_16, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_17': xǁExecutionEnvironmentǁprepare_environment__mutmut_17, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_18': xǁExecutionEnvironmentǁprepare_environment__mutmut_18, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_19': xǁExecutionEnvironmentǁprepare_environment__mutmut_19, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_20': xǁExecutionEnvironmentǁprepare_environment__mutmut_20, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_21': xǁExecutionEnvironmentǁprepare_environment__mutmut_21, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_22': xǁExecutionEnvironmentǁprepare_environment__mutmut_22, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_23': xǁExecutionEnvironmentǁprepare_environment__mutmut_23, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_24': xǁExecutionEnvironmentǁprepare_environment__mutmut_24, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_25': xǁExecutionEnvironmentǁprepare_environment__mutmut_25, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_26': xǁExecutionEnvironmentǁprepare_environment__mutmut_26, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_27': xǁExecutionEnvironmentǁprepare_environment__mutmut_27, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_28': xǁExecutionEnvironmentǁprepare_environment__mutmut_28, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_29': xǁExecutionEnvironmentǁprepare_environment__mutmut_29, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_30': xǁExecutionEnvironmentǁprepare_environment__mutmut_30, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_31': xǁExecutionEnvironmentǁprepare_environment__mutmut_31, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_32': xǁExecutionEnvironmentǁprepare_environment__mutmut_32, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_33': xǁExecutionEnvironmentǁprepare_environment__mutmut_33, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_34': xǁExecutionEnvironmentǁprepare_environment__mutmut_34, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_35': xǁExecutionEnvironmentǁprepare_environment__mutmut_35, 
        'xǁExecutionEnvironmentǁprepare_environment__mutmut_36': xǁExecutionEnvironmentǁprepare_environment__mutmut_36
    }
    
    def prepare_environment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁExecutionEnvironmentǁprepare_environment__mutmut_orig"), object.__getattribute__(self, "xǁExecutionEnvironmentǁprepare_environment__mutmut_mutants"), args, kwargs, self)
        return result 
    
    prepare_environment.__signature__ = _mutmut_signature(xǁExecutionEnvironmentǁprepare_environment__mutmut_orig)
    xǁExecutionEnvironmentǁprepare_environment__mutmut_orig.__name__ = 'xǁExecutionEnvironmentǁprepare_environment'

    @staticmethod
    def _get_bin_dir(venv_path: Path) -> Path:
        """Get bin/Scripts directory for venv.

        Args:
            venv_path: Path to virtual environment

        Returns:
            Path to bin directory (Windows: Scripts/, Unix: bin/)
        """
        if platform.system() == "Windows":
            return venv_path / "Scripts"
        return venv_path / "bin"


# 🧰🌍🔚
