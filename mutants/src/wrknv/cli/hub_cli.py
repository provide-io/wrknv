#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Hub-based CLI Entry Point
=========================
Main CLI using provide.foundation.hub for command registration."""

from __future__ import annotations

import asyncio
import importlib
from pathlib import Path
import sys
from typing import TYPE_CHECKING

import click
from provide.foundation.cli import echo_error, echo_info, echo_success
from provide.foundation.console.output import perr, pout
from provide.foundation.hub import get_hub
from provide.foundation.logger import get_logger

from wrknv.config import WorkenvConfig

if TYPE_CHECKING:
    from wrknv.tasks.registry import TaskRegistry

logger = get_logger(__name__)
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


class WrknvContext:
    """Shared context for wrknv CLI commands."""

    _config = None

    @classmethod
    def get_config(cls) -> WorkenvConfig:
        """Get or load the WorkenvConfig singleton."""
        if cls._config is None:
            cls._config = WorkenvConfig.load()
        return cls._config

    @classmethod
    def reset(cls) -> None:
        """Reset config cache (for testing)."""
        cls._config = None


def x_load_commands__mutmut_orig() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_1() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = None

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_2() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "XXwrknv.cli.commands.checkXX",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_3() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "WRKNV.CLI.COMMANDS.CHECK",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_4() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "XXwrknv.cli.commands.configXX",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_5() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "WRKNV.CLI.COMMANDS.CONFIG",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_6() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "XXwrknv.cli.commands.containerXX",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_7() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "WRKNV.CLI.COMMANDS.CONTAINER",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_8() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "XXwrknv.cli.commands.doctorXX",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_9() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "WRKNV.CLI.COMMANDS.DOCTOR",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_10() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "XXwrknv.cli.commands.gitignoreXX",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_11() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "WRKNV.CLI.COMMANDS.GITIGNORE",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_12() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "XXwrknv.cli.commands.lockXX",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_13() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "WRKNV.CLI.COMMANDS.LOCK",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_14() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "XXwrknv.cli.commands.profileXX",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_15() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "WRKNV.CLI.COMMANDS.PROFILE",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_16() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "XXwrknv.cli.commands.runXX",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_17() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "WRKNV.CLI.COMMANDS.RUN",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_18() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "XXwrknv.cli.commands.secretsXX",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_19() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "WRKNV.CLI.COMMANDS.SECRETS",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_20() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "XXwrknv.cli.commands.securityXX",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_21() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "WRKNV.CLI.COMMANDS.SECURITY",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_22() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "XXwrknv.cli.commands.setupXX",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_23() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "WRKNV.CLI.COMMANDS.SETUP",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_24() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "XXwrknv.cli.commands.terraformXX",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_25() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "WRKNV.CLI.COMMANDS.TERRAFORM",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_26() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "XXwrknv.cli.commands.toolsXX",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_27() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "WRKNV.CLI.COMMANDS.TOOLS",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_28() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "XXwrknv.cli.commands.workspaceXX",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_29() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "WRKNV.CLI.COMMANDS.WORKSPACE",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_30() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "XXwrknv.cli.commands.memrayXX",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_31() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "WRKNV.CLI.COMMANDS.MEMRAY",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_32() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name not in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_33() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(None)
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_34() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(None)

    logger.debug("Loaded wrknv command modules")


def x_load_commands__mutmut_35() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug(None)


def x_load_commands__mutmut_36() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("XXLoaded wrknv command modulesXX")


def x_load_commands__mutmut_37() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("loaded wrknv command modules")


def x_load_commands__mutmut_38() -> None:
    """Import all command modules to trigger registration."""
    # List of command modules to load
    command_modules = [
        "wrknv.cli.commands.check",
        "wrknv.cli.commands.config",
        "wrknv.cli.commands.container",
        "wrknv.cli.commands.doctor",
        "wrknv.cli.commands.gitignore",
        "wrknv.cli.commands.lock",
        "wrknv.cli.commands.profile",
        "wrknv.cli.commands.run",
        "wrknv.cli.commands.secrets",
        "wrknv.cli.commands.security",
        "wrknv.cli.commands.setup",
        "wrknv.cli.commands.terraform",
        "wrknv.cli.commands.tools",
        "wrknv.cli.commands.workspace",
        "wrknv.cli.commands.memray",
    ]

    # Import or reload command modules to trigger @register_command decorators
    # Reload is needed when Foundation clears the registry between tests
    for module_name in command_modules:
        if module_name in sys.modules:
            # Module already imported - reload to re-run decorators
            importlib.reload(sys.modules[module_name])
        else:
            # First import
            importlib.import_module(module_name)

    logger.debug("LOADED WRKNV COMMAND MODULES")

x_load_commands__mutmut_mutants : ClassVar[MutantDict] = {
'x_load_commands__mutmut_1': x_load_commands__mutmut_1, 
    'x_load_commands__mutmut_2': x_load_commands__mutmut_2, 
    'x_load_commands__mutmut_3': x_load_commands__mutmut_3, 
    'x_load_commands__mutmut_4': x_load_commands__mutmut_4, 
    'x_load_commands__mutmut_5': x_load_commands__mutmut_5, 
    'x_load_commands__mutmut_6': x_load_commands__mutmut_6, 
    'x_load_commands__mutmut_7': x_load_commands__mutmut_7, 
    'x_load_commands__mutmut_8': x_load_commands__mutmut_8, 
    'x_load_commands__mutmut_9': x_load_commands__mutmut_9, 
    'x_load_commands__mutmut_10': x_load_commands__mutmut_10, 
    'x_load_commands__mutmut_11': x_load_commands__mutmut_11, 
    'x_load_commands__mutmut_12': x_load_commands__mutmut_12, 
    'x_load_commands__mutmut_13': x_load_commands__mutmut_13, 
    'x_load_commands__mutmut_14': x_load_commands__mutmut_14, 
    'x_load_commands__mutmut_15': x_load_commands__mutmut_15, 
    'x_load_commands__mutmut_16': x_load_commands__mutmut_16, 
    'x_load_commands__mutmut_17': x_load_commands__mutmut_17, 
    'x_load_commands__mutmut_18': x_load_commands__mutmut_18, 
    'x_load_commands__mutmut_19': x_load_commands__mutmut_19, 
    'x_load_commands__mutmut_20': x_load_commands__mutmut_20, 
    'x_load_commands__mutmut_21': x_load_commands__mutmut_21, 
    'x_load_commands__mutmut_22': x_load_commands__mutmut_22, 
    'x_load_commands__mutmut_23': x_load_commands__mutmut_23, 
    'x_load_commands__mutmut_24': x_load_commands__mutmut_24, 
    'x_load_commands__mutmut_25': x_load_commands__mutmut_25, 
    'x_load_commands__mutmut_26': x_load_commands__mutmut_26, 
    'x_load_commands__mutmut_27': x_load_commands__mutmut_27, 
    'x_load_commands__mutmut_28': x_load_commands__mutmut_28, 
    'x_load_commands__mutmut_29': x_load_commands__mutmut_29, 
    'x_load_commands__mutmut_30': x_load_commands__mutmut_30, 
    'x_load_commands__mutmut_31': x_load_commands__mutmut_31, 
    'x_load_commands__mutmut_32': x_load_commands__mutmut_32, 
    'x_load_commands__mutmut_33': x_load_commands__mutmut_33, 
    'x_load_commands__mutmut_34': x_load_commands__mutmut_34, 
    'x_load_commands__mutmut_35': x_load_commands__mutmut_35, 
    'x_load_commands__mutmut_36': x_load_commands__mutmut_36, 
    'x_load_commands__mutmut_37': x_load_commands__mutmut_37, 
    'x_load_commands__mutmut_38': x_load_commands__mutmut_38
}

def load_commands(*args, **kwargs):
    result = _mutmut_trampoline(x_load_commands__mutmut_orig, x_load_commands__mutmut_mutants, args, kwargs)
    return result 

load_commands.__signature__ = _mutmut_signature(x_load_commands__mutmut_orig)
x_load_commands__mutmut_orig.__name__ = 'x_load_commands'


def x_create_cli__mutmut_orig() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_1() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = None

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_2() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=None)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_3() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = None

    return cli


def x_create_cli__mutmut_4() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name=None,
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_5() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version=None,
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_6() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help=None,
    )

    return cli


def x_create_cli__mutmut_7() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_8() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_9() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        )

    return cli


def x_create_cli__mutmut_10() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="XXwrknvXX",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_11() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="WRKNV",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_12() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="XX0.3.0XX",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_13() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="XXwrknv provides cross-platform tool installation and version management XX"
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_14() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="WRKNV PROVIDES CROSS-PLATFORM TOOL INSTALLATION AND VERSION MANAGEMENT "
        "for development environments, including Terraform, OpenTofu, Go, UV, and more.",
    )

    return cli


def x_create_cli__mutmut_15() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "XXfor development environments, including Terraform, OpenTofu, Go, UV, and more.XX",
    )

    return cli


def x_create_cli__mutmut_16() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "for development environments, including terraform, opentofu, go, uv, and more.",
    )

    return cli


def x_create_cli__mutmut_17() -> click.Group:
    """Create the main CLI application using the hub."""
    # Get or create hub
    hub = get_hub()

    # Clear existing command registrations to allow re-creation in tests
    # This prevents AlreadyExistsError when create_cli() is called multiple times
    from provide.foundation.hub.categories import ComponentCategory

    hub.clear(dimension=ComponentCategory.COMMAND.value)

    # Reset config cache when creating CLI (for test isolation)
    WrknvContext.reset()

    # Load all commands (this will register them in the cleared registry)
    load_commands()

    # Create CLI with standard options
    cli = hub.create_cli(
        name="wrknv",
        version="0.3.0",
        help="wrknv provides cross-platform tool installation and version management "
        "FOR DEVELOPMENT ENVIRONMENTS, INCLUDING TERRAFORM, OPENTOFU, GO, UV, AND MORE.",
    )

    return cli

x_create_cli__mutmut_mutants : ClassVar[MutantDict] = {
'x_create_cli__mutmut_1': x_create_cli__mutmut_1, 
    'x_create_cli__mutmut_2': x_create_cli__mutmut_2, 
    'x_create_cli__mutmut_3': x_create_cli__mutmut_3, 
    'x_create_cli__mutmut_4': x_create_cli__mutmut_4, 
    'x_create_cli__mutmut_5': x_create_cli__mutmut_5, 
    'x_create_cli__mutmut_6': x_create_cli__mutmut_6, 
    'x_create_cli__mutmut_7': x_create_cli__mutmut_7, 
    'x_create_cli__mutmut_8': x_create_cli__mutmut_8, 
    'x_create_cli__mutmut_9': x_create_cli__mutmut_9, 
    'x_create_cli__mutmut_10': x_create_cli__mutmut_10, 
    'x_create_cli__mutmut_11': x_create_cli__mutmut_11, 
    'x_create_cli__mutmut_12': x_create_cli__mutmut_12, 
    'x_create_cli__mutmut_13': x_create_cli__mutmut_13, 
    'x_create_cli__mutmut_14': x_create_cli__mutmut_14, 
    'x_create_cli__mutmut_15': x_create_cli__mutmut_15, 
    'x_create_cli__mutmut_16': x_create_cli__mutmut_16, 
    'x_create_cli__mutmut_17': x_create_cli__mutmut_17
}

def create_cli(*args, **kwargs):
    result = _mutmut_trampoline(x_create_cli__mutmut_orig, x_create_cli__mutmut_mutants, args, kwargs)
    return result 

create_cli.__signature__ = _mutmut_signature(x_create_cli__mutmut_orig)
x_create_cli__mutmut_orig.__name__ = 'x_create_cli'


def x_intercept_task_command__mutmut_orig() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_1() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = None

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_2() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "XXcheckXX",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_3() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "CHECK",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_4() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "XXconfigXX",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_5() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "CONFIG",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_6() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "XXcontainerXX",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_7() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "CONTAINER",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_8() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "XXdoctorXX",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_9() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "DOCTOR",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_10() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "XXgitignoreXX",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_11() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "GITIGNORE",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_12() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "XXlockXX",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_13() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "LOCK",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_14() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "XXprofileXX",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_15() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "PROFILE",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_16() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "XXrunXX",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_17() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "RUN",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_18() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "XXsecretsXX",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_19() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "SECRETS",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_20() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "XXsecurityXX",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_21() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "SECURITY",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_22() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "XXselftestXX",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_23() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "SELFTEST",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_24() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "XXsetupXX",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_25() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "SETUP",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_26() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "XXterraformXX",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_27() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "TERRAFORM",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_28() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "XXtoolsXX",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_29() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "TOOLS",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_30() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "XXworkspaceXX",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_31() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "WORKSPACE",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_32() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "XXtasksXX",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_33() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "TASKS",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_34() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "XX--helpXX",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_35() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--HELP",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_36() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "XX-hXX",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_37() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-H",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_38() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "XX--versionXX",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_39() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--VERSION",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_40() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "XX-vXX",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_41() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-V",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_42() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = None

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_43() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[2:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_44() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args and args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_45() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_46() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[1] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_47() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] not in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_48() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return True

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_49() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = None
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_50() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = None

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_51() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(None)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_52() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = None
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_53() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(None, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_54() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, None)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_55() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_56() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, )
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_57() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_58() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return True

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_59() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = None

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_60() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(None)
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_61() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(None, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_62() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, None, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_63() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, None))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_64() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_65() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_66() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, ))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_67() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return False

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return False


def x_intercept_task_command__mutmut_68() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(None)
        return False


def x_intercept_task_command__mutmut_69() -> bool:
    """Intercept and run task commands before Click processes them.

    Enables running tasks without the 'run' subcommand (e.g., `we test` instead of `we run test`).

    Returns:
        True if a task was intercepted and executed, False to continue with normal CLI flow
    """
    # Built-in commands that should not be intercepted
    BUILT_IN_COMMANDS = {
        "check",
        "config",
        "container",
        "doctor",
        "gitignore",
        "lock",
        "profile",
        "run",
        "secrets",
        "security",
        "selftest",
        "setup",
        "terraform",
        "tools",
        "workspace",
        "tasks",
        "--help",
        "-h",
        "--version",
        "-v",
    }

    # Get command line args (skip program name)
    args = sys.argv[1:]

    if not args or args[0] in BUILT_IN_COMMANDS:
        return False

    # Try to resolve as a task
    try:
        repo_path = Path.cwd()
        from wrknv.tasks.registry import TaskRegistry

        registry = TaskRegistry.from_repo(repo_path)

        # Try to match task name from args (greedy matching)
        match = _try_resolve_task_from_args(registry, args)
        if not match:
            return False

        task_name, remaining_args = match

        # Run the task
        asyncio.run(_run_task_for_intercept(registry, task_name, remaining_args))
        return True

    except Exception as e:
        # If anything goes wrong, let Click handle it
        logger.debug(f"Task intercept failed: {e}")
        return True

x_intercept_task_command__mutmut_mutants : ClassVar[MutantDict] = {
'x_intercept_task_command__mutmut_1': x_intercept_task_command__mutmut_1, 
    'x_intercept_task_command__mutmut_2': x_intercept_task_command__mutmut_2, 
    'x_intercept_task_command__mutmut_3': x_intercept_task_command__mutmut_3, 
    'x_intercept_task_command__mutmut_4': x_intercept_task_command__mutmut_4, 
    'x_intercept_task_command__mutmut_5': x_intercept_task_command__mutmut_5, 
    'x_intercept_task_command__mutmut_6': x_intercept_task_command__mutmut_6, 
    'x_intercept_task_command__mutmut_7': x_intercept_task_command__mutmut_7, 
    'x_intercept_task_command__mutmut_8': x_intercept_task_command__mutmut_8, 
    'x_intercept_task_command__mutmut_9': x_intercept_task_command__mutmut_9, 
    'x_intercept_task_command__mutmut_10': x_intercept_task_command__mutmut_10, 
    'x_intercept_task_command__mutmut_11': x_intercept_task_command__mutmut_11, 
    'x_intercept_task_command__mutmut_12': x_intercept_task_command__mutmut_12, 
    'x_intercept_task_command__mutmut_13': x_intercept_task_command__mutmut_13, 
    'x_intercept_task_command__mutmut_14': x_intercept_task_command__mutmut_14, 
    'x_intercept_task_command__mutmut_15': x_intercept_task_command__mutmut_15, 
    'x_intercept_task_command__mutmut_16': x_intercept_task_command__mutmut_16, 
    'x_intercept_task_command__mutmut_17': x_intercept_task_command__mutmut_17, 
    'x_intercept_task_command__mutmut_18': x_intercept_task_command__mutmut_18, 
    'x_intercept_task_command__mutmut_19': x_intercept_task_command__mutmut_19, 
    'x_intercept_task_command__mutmut_20': x_intercept_task_command__mutmut_20, 
    'x_intercept_task_command__mutmut_21': x_intercept_task_command__mutmut_21, 
    'x_intercept_task_command__mutmut_22': x_intercept_task_command__mutmut_22, 
    'x_intercept_task_command__mutmut_23': x_intercept_task_command__mutmut_23, 
    'x_intercept_task_command__mutmut_24': x_intercept_task_command__mutmut_24, 
    'x_intercept_task_command__mutmut_25': x_intercept_task_command__mutmut_25, 
    'x_intercept_task_command__mutmut_26': x_intercept_task_command__mutmut_26, 
    'x_intercept_task_command__mutmut_27': x_intercept_task_command__mutmut_27, 
    'x_intercept_task_command__mutmut_28': x_intercept_task_command__mutmut_28, 
    'x_intercept_task_command__mutmut_29': x_intercept_task_command__mutmut_29, 
    'x_intercept_task_command__mutmut_30': x_intercept_task_command__mutmut_30, 
    'x_intercept_task_command__mutmut_31': x_intercept_task_command__mutmut_31, 
    'x_intercept_task_command__mutmut_32': x_intercept_task_command__mutmut_32, 
    'x_intercept_task_command__mutmut_33': x_intercept_task_command__mutmut_33, 
    'x_intercept_task_command__mutmut_34': x_intercept_task_command__mutmut_34, 
    'x_intercept_task_command__mutmut_35': x_intercept_task_command__mutmut_35, 
    'x_intercept_task_command__mutmut_36': x_intercept_task_command__mutmut_36, 
    'x_intercept_task_command__mutmut_37': x_intercept_task_command__mutmut_37, 
    'x_intercept_task_command__mutmut_38': x_intercept_task_command__mutmut_38, 
    'x_intercept_task_command__mutmut_39': x_intercept_task_command__mutmut_39, 
    'x_intercept_task_command__mutmut_40': x_intercept_task_command__mutmut_40, 
    'x_intercept_task_command__mutmut_41': x_intercept_task_command__mutmut_41, 
    'x_intercept_task_command__mutmut_42': x_intercept_task_command__mutmut_42, 
    'x_intercept_task_command__mutmut_43': x_intercept_task_command__mutmut_43, 
    'x_intercept_task_command__mutmut_44': x_intercept_task_command__mutmut_44, 
    'x_intercept_task_command__mutmut_45': x_intercept_task_command__mutmut_45, 
    'x_intercept_task_command__mutmut_46': x_intercept_task_command__mutmut_46, 
    'x_intercept_task_command__mutmut_47': x_intercept_task_command__mutmut_47, 
    'x_intercept_task_command__mutmut_48': x_intercept_task_command__mutmut_48, 
    'x_intercept_task_command__mutmut_49': x_intercept_task_command__mutmut_49, 
    'x_intercept_task_command__mutmut_50': x_intercept_task_command__mutmut_50, 
    'x_intercept_task_command__mutmut_51': x_intercept_task_command__mutmut_51, 
    'x_intercept_task_command__mutmut_52': x_intercept_task_command__mutmut_52, 
    'x_intercept_task_command__mutmut_53': x_intercept_task_command__mutmut_53, 
    'x_intercept_task_command__mutmut_54': x_intercept_task_command__mutmut_54, 
    'x_intercept_task_command__mutmut_55': x_intercept_task_command__mutmut_55, 
    'x_intercept_task_command__mutmut_56': x_intercept_task_command__mutmut_56, 
    'x_intercept_task_command__mutmut_57': x_intercept_task_command__mutmut_57, 
    'x_intercept_task_command__mutmut_58': x_intercept_task_command__mutmut_58, 
    'x_intercept_task_command__mutmut_59': x_intercept_task_command__mutmut_59, 
    'x_intercept_task_command__mutmut_60': x_intercept_task_command__mutmut_60, 
    'x_intercept_task_command__mutmut_61': x_intercept_task_command__mutmut_61, 
    'x_intercept_task_command__mutmut_62': x_intercept_task_command__mutmut_62, 
    'x_intercept_task_command__mutmut_63': x_intercept_task_command__mutmut_63, 
    'x_intercept_task_command__mutmut_64': x_intercept_task_command__mutmut_64, 
    'x_intercept_task_command__mutmut_65': x_intercept_task_command__mutmut_65, 
    'x_intercept_task_command__mutmut_66': x_intercept_task_command__mutmut_66, 
    'x_intercept_task_command__mutmut_67': x_intercept_task_command__mutmut_67, 
    'x_intercept_task_command__mutmut_68': x_intercept_task_command__mutmut_68, 
    'x_intercept_task_command__mutmut_69': x_intercept_task_command__mutmut_69
}

def intercept_task_command(*args, **kwargs):
    result = _mutmut_trampoline(x_intercept_task_command__mutmut_orig, x_intercept_task_command__mutmut_mutants, args, kwargs)
    return result 

intercept_task_command.__signature__ = _mutmut_signature(x_intercept_task_command__mutmut_orig)
x_intercept_task_command__mutmut_orig.__name__ = 'x_intercept_task_command'


def x__try_resolve_task_from_args__mutmut_orig(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_1(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(None, 0, -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_2(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), None, -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_3(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, None):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_4(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(0, -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_5(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_6(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, ):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_7(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 1, -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_8(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, +1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_9(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -2):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_10(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -1):
        task_parts = None
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_11(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -1):
        task_parts = args[:i]
        task_name = None
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_12(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -1):
        task_parts = args[:i]
        task_name = ".".join(None)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_13(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -1):
        task_parts = args[:i]
        task_name = "XX.XX".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_14(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = None

        if registry.get_task(task_name):
            return (task_name, remaining_args)

    return None


def x__try_resolve_task_from_args__mutmut_15(
    registry: TaskRegistry,
    args: list[str],
) -> tuple[str, list[str]] | None:
    """Try to resolve a task name from command args using greedy matching.

    Tries progressively longer task names from left to right until a match is found.

    Args:
        registry: Task registry to search
        args: Command line arguments

    Returns:
        (task_name, remaining_args) if task found, None otherwise

    Examples:
        ["test", "unit", "--verbose"] -> ("test.unit", ["--verbose"])
        ["test", "--verbose"] -> ("test", ["--verbose"])
    """
    # Try progressively longer task names (greedy matching from longest to shortest)
    for i in range(len(args), 0, -1):
        task_parts = args[:i]
        task_name = ".".join(task_parts)
        remaining_args = args[i:]

        if registry.get_task(None):
            return (task_name, remaining_args)

    return None

x__try_resolve_task_from_args__mutmut_mutants : ClassVar[MutantDict] = {
'x__try_resolve_task_from_args__mutmut_1': x__try_resolve_task_from_args__mutmut_1, 
    'x__try_resolve_task_from_args__mutmut_2': x__try_resolve_task_from_args__mutmut_2, 
    'x__try_resolve_task_from_args__mutmut_3': x__try_resolve_task_from_args__mutmut_3, 
    'x__try_resolve_task_from_args__mutmut_4': x__try_resolve_task_from_args__mutmut_4, 
    'x__try_resolve_task_from_args__mutmut_5': x__try_resolve_task_from_args__mutmut_5, 
    'x__try_resolve_task_from_args__mutmut_6': x__try_resolve_task_from_args__mutmut_6, 
    'x__try_resolve_task_from_args__mutmut_7': x__try_resolve_task_from_args__mutmut_7, 
    'x__try_resolve_task_from_args__mutmut_8': x__try_resolve_task_from_args__mutmut_8, 
    'x__try_resolve_task_from_args__mutmut_9': x__try_resolve_task_from_args__mutmut_9, 
    'x__try_resolve_task_from_args__mutmut_10': x__try_resolve_task_from_args__mutmut_10, 
    'x__try_resolve_task_from_args__mutmut_11': x__try_resolve_task_from_args__mutmut_11, 
    'x__try_resolve_task_from_args__mutmut_12': x__try_resolve_task_from_args__mutmut_12, 
    'x__try_resolve_task_from_args__mutmut_13': x__try_resolve_task_from_args__mutmut_13, 
    'x__try_resolve_task_from_args__mutmut_14': x__try_resolve_task_from_args__mutmut_14, 
    'x__try_resolve_task_from_args__mutmut_15': x__try_resolve_task_from_args__mutmut_15
}

def _try_resolve_task_from_args(*args, **kwargs):
    result = _mutmut_trampoline(x__try_resolve_task_from_args__mutmut_orig, x__try_resolve_task_from_args__mutmut_mutants, args, kwargs)
    return result 

_try_resolve_task_from_args.__signature__ = _mutmut_signature(x__try_resolve_task_from_args__mutmut_orig)
x__try_resolve_task_from_args__mutmut_orig.__name__ = 'x__try_resolve_task_from_args'


async def x__run_task_for_intercept__mutmut_orig(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_1(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(None)

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_2(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(None)

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_3(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = None

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_4(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(None, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_5(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=None, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_6(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=None, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_7(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_8(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_9(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_10(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, )

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_11(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=True, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_12(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(None, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_13(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end=None)
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_14(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_15(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, )
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_16(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="XXXX")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_17(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(None, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_18(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end=None)

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_19(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_20(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, )

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_21(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="XXXX")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_22(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(None)
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_23(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(None)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_24(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(1)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_25(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(None)
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_26(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(None)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_27(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(None)
        sys.exit(1)


async def x__run_task_for_intercept__mutmut_28(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(None)


async def x__run_task_for_intercept__mutmut_29(
    registry: TaskRegistry,
    task_name: str,
    args: list[str],
) -> None:
    """Run a task for auto-detection (simplified version of run command).

    Args:
        registry: Task registry
        task_name: Task name to run
        args: Arguments to pass to the task
    """
    from provide.foundation.process import set_process_title

    # Set process title for the task
    set_process_title(f"we: {task_name}")

    echo_info(f"\n▶ Running task: {task_name}")

    try:
        result = await registry.run_task(task_name, args=args, dry_run=False, env=None)

        if result.stdout:
            pout(result.stdout, end="")
        if result.stderr:
            perr(result.stderr, end="")

        if result.success:
            echo_success(f"✓ Task {task_name} completed in {result.duration:.2f}s")
            sys.exit(0)
        else:
            echo_error(f"✗ Task {task_name} failed (exit code {result.exit_code})")
            sys.exit(result.exit_code)

    except Exception as e:
        echo_error(f"Error running task: {e}")
        sys.exit(2)

x__run_task_for_intercept__mutmut_mutants : ClassVar[MutantDict] = {
'x__run_task_for_intercept__mutmut_1': x__run_task_for_intercept__mutmut_1, 
    'x__run_task_for_intercept__mutmut_2': x__run_task_for_intercept__mutmut_2, 
    'x__run_task_for_intercept__mutmut_3': x__run_task_for_intercept__mutmut_3, 
    'x__run_task_for_intercept__mutmut_4': x__run_task_for_intercept__mutmut_4, 
    'x__run_task_for_intercept__mutmut_5': x__run_task_for_intercept__mutmut_5, 
    'x__run_task_for_intercept__mutmut_6': x__run_task_for_intercept__mutmut_6, 
    'x__run_task_for_intercept__mutmut_7': x__run_task_for_intercept__mutmut_7, 
    'x__run_task_for_intercept__mutmut_8': x__run_task_for_intercept__mutmut_8, 
    'x__run_task_for_intercept__mutmut_9': x__run_task_for_intercept__mutmut_9, 
    'x__run_task_for_intercept__mutmut_10': x__run_task_for_intercept__mutmut_10, 
    'x__run_task_for_intercept__mutmut_11': x__run_task_for_intercept__mutmut_11, 
    'x__run_task_for_intercept__mutmut_12': x__run_task_for_intercept__mutmut_12, 
    'x__run_task_for_intercept__mutmut_13': x__run_task_for_intercept__mutmut_13, 
    'x__run_task_for_intercept__mutmut_14': x__run_task_for_intercept__mutmut_14, 
    'x__run_task_for_intercept__mutmut_15': x__run_task_for_intercept__mutmut_15, 
    'x__run_task_for_intercept__mutmut_16': x__run_task_for_intercept__mutmut_16, 
    'x__run_task_for_intercept__mutmut_17': x__run_task_for_intercept__mutmut_17, 
    'x__run_task_for_intercept__mutmut_18': x__run_task_for_intercept__mutmut_18, 
    'x__run_task_for_intercept__mutmut_19': x__run_task_for_intercept__mutmut_19, 
    'x__run_task_for_intercept__mutmut_20': x__run_task_for_intercept__mutmut_20, 
    'x__run_task_for_intercept__mutmut_21': x__run_task_for_intercept__mutmut_21, 
    'x__run_task_for_intercept__mutmut_22': x__run_task_for_intercept__mutmut_22, 
    'x__run_task_for_intercept__mutmut_23': x__run_task_for_intercept__mutmut_23, 
    'x__run_task_for_intercept__mutmut_24': x__run_task_for_intercept__mutmut_24, 
    'x__run_task_for_intercept__mutmut_25': x__run_task_for_intercept__mutmut_25, 
    'x__run_task_for_intercept__mutmut_26': x__run_task_for_intercept__mutmut_26, 
    'x__run_task_for_intercept__mutmut_27': x__run_task_for_intercept__mutmut_27, 
    'x__run_task_for_intercept__mutmut_28': x__run_task_for_intercept__mutmut_28, 
    'x__run_task_for_intercept__mutmut_29': x__run_task_for_intercept__mutmut_29
}

def _run_task_for_intercept(*args, **kwargs):
    result = _mutmut_trampoline(x__run_task_for_intercept__mutmut_orig, x__run_task_for_intercept__mutmut_mutants, args, kwargs)
    return result 

_run_task_for_intercept.__signature__ = _mutmut_signature(x__run_task_for_intercept__mutmut_orig)
x__run_task_for_intercept__mutmut_orig.__name__ = 'x__run_task_for_intercept'


def x_main__mutmut_orig() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_1() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = None

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_2() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = None

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_3() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = None

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_4() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        None,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_5() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name=None,
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_6() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=None,
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_7() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_8() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_9() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_10() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="XXwrknvXX",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_11() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="WRKNV",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_12() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            None,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_13() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=None,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_14() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_15() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_16() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = None
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_17() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(None)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_18() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title(None)

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_19() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("XXweXX")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_20() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("WE")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = create_cli()
    cli()


def x_main__mutmut_21() -> None:
    """Main entry point for the CLI."""
    from attrs import evolve
    from provide.foundation import TelemetryConfig
    from provide.foundation.process import set_process_title

    # Load wrknv configuration to get log level
    from wrknv.config import WorkenvConfig

    wrknv_config = WorkenvConfig.from_env()

    # Get base telemetry config from environment
    base_telemetry = TelemetryConfig.from_env()

    # Merge with wrknv-specific settings
    telemetry_config = evolve(
        base_telemetry,
        service_name="wrknv",
        logging=evolve(
            base_telemetry.logging,
            default_level=wrknv_config.workenv.log_level,
        ),
    )

    # Initialize Foundation with merged config
    hub = get_hub()
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")

    # Try to intercept and run task commands directly (auto-detection)
    if intercept_task_command():
        return  # Task was run, exit

    # Fall through to normal CLI if not a task
    cli = None
    cli()

x_main__mutmut_mutants : ClassVar[MutantDict] = {
'x_main__mutmut_1': x_main__mutmut_1, 
    'x_main__mutmut_2': x_main__mutmut_2, 
    'x_main__mutmut_3': x_main__mutmut_3, 
    'x_main__mutmut_4': x_main__mutmut_4, 
    'x_main__mutmut_5': x_main__mutmut_5, 
    'x_main__mutmut_6': x_main__mutmut_6, 
    'x_main__mutmut_7': x_main__mutmut_7, 
    'x_main__mutmut_8': x_main__mutmut_8, 
    'x_main__mutmut_9': x_main__mutmut_9, 
    'x_main__mutmut_10': x_main__mutmut_10, 
    'x_main__mutmut_11': x_main__mutmut_11, 
    'x_main__mutmut_12': x_main__mutmut_12, 
    'x_main__mutmut_13': x_main__mutmut_13, 
    'x_main__mutmut_14': x_main__mutmut_14, 
    'x_main__mutmut_15': x_main__mutmut_15, 
    'x_main__mutmut_16': x_main__mutmut_16, 
    'x_main__mutmut_17': x_main__mutmut_17, 
    'x_main__mutmut_18': x_main__mutmut_18, 
    'x_main__mutmut_19': x_main__mutmut_19, 
    'x_main__mutmut_20': x_main__mutmut_20, 
    'x_main__mutmut_21': x_main__mutmut_21
}

def main(*args, **kwargs):
    result = _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs)
    return result 

main.__signature__ = _mutmut_signature(x_main__mutmut_orig)
x_main__mutmut_orig.__name__ = 'x_main'


if __name__ == "__main__":
    main()

# 🧰🌍🔚
