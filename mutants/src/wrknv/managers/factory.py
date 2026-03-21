#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tool Manager Factory for wrknv
================================
Factory for creating appropriate tool managers."""

from __future__ import annotations

from wrknv.config import WorkenvConfig

from .base import BaseToolManager
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


def x_get_tool_manager__mutmut_orig(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_1(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is not None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_2(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = None

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_3(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name != "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_4(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "XXibmtfXX":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_5(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "IBMTF":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_6(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(None)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_7(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name != "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_8(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "XXtofuXX":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_9(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "TOFU":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_10(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(None)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_11(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name != "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_12(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "XXbaoXX":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_13(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "BAO":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_14(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(None)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_15(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name != "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_16(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "XXvaultXX":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_17(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "VAULT":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_18(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(None)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_19(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name != "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_20(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "XXuvXX":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_21(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "UV":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_22(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(None)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_23(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name != "go":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_24(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "XXgoXX":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_25(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "GO":
        from .go import GoManager

        return GoManager(config)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None


def x_get_tool_manager__mutmut_26(tool_name: str, config: WorkenvConfig | None = None) -> BaseToolManager | None:
    """Get appropriate tool manager for a tool."""

    if config is None:
        config = WorkenvConfig.load()

    # Terraform ecosystem
    if tool_name == "ibmtf":
        from .tf.ibm import IbmTfVariant

        return IbmTfVariant(config)

    elif tool_name == "tofu":
        from .tf.tofu import TofuTfVariant

        return TofuTfVariant(config)

    # Secret management (sub rosa)
    elif tool_name == "bao":
        from .subrosa.bao import BaoVariant

        return BaoVariant(config)

    elif tool_name == "vault":
        from .subrosa.ibm import IbmVaultVariant

        return IbmVaultVariant(config)

    # Single-variant tools
    elif tool_name == "uv":
        from .uv import UvManager

        return UvManager(config)

    elif tool_name == "go":
        from .go import GoManager

        return GoManager(None)

    # Add more tools as needed:
    # elif tool_name == "python":
    #     from .python import PythonManager
    #     return PythonManager(config)
    #
    # elif tool_name == "node":
    #     from .node import NodeManager
    #     return NodeManager(config)

    return None

x_get_tool_manager__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_tool_manager__mutmut_1': x_get_tool_manager__mutmut_1, 
    'x_get_tool_manager__mutmut_2': x_get_tool_manager__mutmut_2, 
    'x_get_tool_manager__mutmut_3': x_get_tool_manager__mutmut_3, 
    'x_get_tool_manager__mutmut_4': x_get_tool_manager__mutmut_4, 
    'x_get_tool_manager__mutmut_5': x_get_tool_manager__mutmut_5, 
    'x_get_tool_manager__mutmut_6': x_get_tool_manager__mutmut_6, 
    'x_get_tool_manager__mutmut_7': x_get_tool_manager__mutmut_7, 
    'x_get_tool_manager__mutmut_8': x_get_tool_manager__mutmut_8, 
    'x_get_tool_manager__mutmut_9': x_get_tool_manager__mutmut_9, 
    'x_get_tool_manager__mutmut_10': x_get_tool_manager__mutmut_10, 
    'x_get_tool_manager__mutmut_11': x_get_tool_manager__mutmut_11, 
    'x_get_tool_manager__mutmut_12': x_get_tool_manager__mutmut_12, 
    'x_get_tool_manager__mutmut_13': x_get_tool_manager__mutmut_13, 
    'x_get_tool_manager__mutmut_14': x_get_tool_manager__mutmut_14, 
    'x_get_tool_manager__mutmut_15': x_get_tool_manager__mutmut_15, 
    'x_get_tool_manager__mutmut_16': x_get_tool_manager__mutmut_16, 
    'x_get_tool_manager__mutmut_17': x_get_tool_manager__mutmut_17, 
    'x_get_tool_manager__mutmut_18': x_get_tool_manager__mutmut_18, 
    'x_get_tool_manager__mutmut_19': x_get_tool_manager__mutmut_19, 
    'x_get_tool_manager__mutmut_20': x_get_tool_manager__mutmut_20, 
    'x_get_tool_manager__mutmut_21': x_get_tool_manager__mutmut_21, 
    'x_get_tool_manager__mutmut_22': x_get_tool_manager__mutmut_22, 
    'x_get_tool_manager__mutmut_23': x_get_tool_manager__mutmut_23, 
    'x_get_tool_manager__mutmut_24': x_get_tool_manager__mutmut_24, 
    'x_get_tool_manager__mutmut_25': x_get_tool_manager__mutmut_25, 
    'x_get_tool_manager__mutmut_26': x_get_tool_manager__mutmut_26
}

def get_tool_manager(*args, **kwargs):
    result = _mutmut_trampoline(x_get_tool_manager__mutmut_orig, x_get_tool_manager__mutmut_mutants, args, kwargs)
    return result 

get_tool_manager.__signature__ = _mutmut_signature(x_get_tool_manager__mutmut_orig)
x_get_tool_manager__mutmut_orig.__name__ = 'x_get_tool_manager'


def x_get_supported_tools__mutmut_orig() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "bao", "vault", "uv", "go"]


def x_get_supported_tools__mutmut_1() -> list[str]:
    """Get list of supported tools."""
    return ["XXibmtfXX", "tofu", "bao", "vault", "uv", "go"]


def x_get_supported_tools__mutmut_2() -> list[str]:
    """Get list of supported tools."""
    return ["IBMTF", "tofu", "bao", "vault", "uv", "go"]


def x_get_supported_tools__mutmut_3() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "XXtofuXX", "bao", "vault", "uv", "go"]


def x_get_supported_tools__mutmut_4() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "TOFU", "bao", "vault", "uv", "go"]


def x_get_supported_tools__mutmut_5() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "XXbaoXX", "vault", "uv", "go"]


def x_get_supported_tools__mutmut_6() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "BAO", "vault", "uv", "go"]


def x_get_supported_tools__mutmut_7() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "bao", "XXvaultXX", "uv", "go"]


def x_get_supported_tools__mutmut_8() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "bao", "VAULT", "uv", "go"]


def x_get_supported_tools__mutmut_9() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "bao", "vault", "XXuvXX", "go"]


def x_get_supported_tools__mutmut_10() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "bao", "vault", "UV", "go"]


def x_get_supported_tools__mutmut_11() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "bao", "vault", "uv", "XXgoXX"]


def x_get_supported_tools__mutmut_12() -> list[str]:
    """Get list of supported tools."""
    return ["ibmtf", "tofu", "bao", "vault", "uv", "GO"]

x_get_supported_tools__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_supported_tools__mutmut_1': x_get_supported_tools__mutmut_1, 
    'x_get_supported_tools__mutmut_2': x_get_supported_tools__mutmut_2, 
    'x_get_supported_tools__mutmut_3': x_get_supported_tools__mutmut_3, 
    'x_get_supported_tools__mutmut_4': x_get_supported_tools__mutmut_4, 
    'x_get_supported_tools__mutmut_5': x_get_supported_tools__mutmut_5, 
    'x_get_supported_tools__mutmut_6': x_get_supported_tools__mutmut_6, 
    'x_get_supported_tools__mutmut_7': x_get_supported_tools__mutmut_7, 
    'x_get_supported_tools__mutmut_8': x_get_supported_tools__mutmut_8, 
    'x_get_supported_tools__mutmut_9': x_get_supported_tools__mutmut_9, 
    'x_get_supported_tools__mutmut_10': x_get_supported_tools__mutmut_10, 
    'x_get_supported_tools__mutmut_11': x_get_supported_tools__mutmut_11, 
    'x_get_supported_tools__mutmut_12': x_get_supported_tools__mutmut_12
}

def get_supported_tools(*args, **kwargs):
    result = _mutmut_trampoline(x_get_supported_tools__mutmut_orig, x_get_supported_tools__mutmut_mutants, args, kwargs)
    return result 

get_supported_tools.__signature__ = _mutmut_signature(x_get_supported_tools__mutmut_orig)
x_get_supported_tools__mutmut_orig.__name__ = 'x_get_supported_tools'


def x_get_major_tools__mutmut_orig() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "bao", "vault", "uv", "go"]


def x_get_major_tools__mutmut_1() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["XXibmtfXX", "tofu", "bao", "vault", "uv", "go"]


def x_get_major_tools__mutmut_2() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["IBMTF", "tofu", "bao", "vault", "uv", "go"]


def x_get_major_tools__mutmut_3() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "XXtofuXX", "bao", "vault", "uv", "go"]


def x_get_major_tools__mutmut_4() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "TOFU", "bao", "vault", "uv", "go"]


def x_get_major_tools__mutmut_5() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "XXbaoXX", "vault", "uv", "go"]


def x_get_major_tools__mutmut_6() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "BAO", "vault", "uv", "go"]


def x_get_major_tools__mutmut_7() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "bao", "XXvaultXX", "uv", "go"]


def x_get_major_tools__mutmut_8() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "bao", "VAULT", "uv", "go"]


def x_get_major_tools__mutmut_9() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "bao", "vault", "XXuvXX", "go"]


def x_get_major_tools__mutmut_10() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "bao", "vault", "UV", "go"]


def x_get_major_tools__mutmut_11() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "bao", "vault", "uv", "XXgoXX"]


def x_get_major_tools__mutmut_12() -> list[str]:
    """Get list of major tools (those with direct CLI commands)."""
    return ["ibmtf", "tofu", "bao", "vault", "uv", "GO"]

x_get_major_tools__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_major_tools__mutmut_1': x_get_major_tools__mutmut_1, 
    'x_get_major_tools__mutmut_2': x_get_major_tools__mutmut_2, 
    'x_get_major_tools__mutmut_3': x_get_major_tools__mutmut_3, 
    'x_get_major_tools__mutmut_4': x_get_major_tools__mutmut_4, 
    'x_get_major_tools__mutmut_5': x_get_major_tools__mutmut_5, 
    'x_get_major_tools__mutmut_6': x_get_major_tools__mutmut_6, 
    'x_get_major_tools__mutmut_7': x_get_major_tools__mutmut_7, 
    'x_get_major_tools__mutmut_8': x_get_major_tools__mutmut_8, 
    'x_get_major_tools__mutmut_9': x_get_major_tools__mutmut_9, 
    'x_get_major_tools__mutmut_10': x_get_major_tools__mutmut_10, 
    'x_get_major_tools__mutmut_11': x_get_major_tools__mutmut_11, 
    'x_get_major_tools__mutmut_12': x_get_major_tools__mutmut_12
}

def get_major_tools(*args, **kwargs):
    result = _mutmut_trampoline(x_get_major_tools__mutmut_orig, x_get_major_tools__mutmut_mutants, args, kwargs)
    return result 

get_major_tools.__signature__ = _mutmut_signature(x_get_major_tools__mutmut_orig)
x_get_major_tools__mutmut_orig.__name__ = 'x_get_major_tools'


def get_secondary_tools() -> list[str]:
    """Get list of secondary tools (managed via set/get commands)."""
    # For now, all tools are major tools
    # This will be expanded later for tools like python, node, docker, etc.
    return []


# 🧰🌍🔚
