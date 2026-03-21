#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tf Bin Operations
=================
Tf-specific binary operations for workenv bin directory."""

from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

from provide.foundation import logger

from wrknv.wenv.bin_manager import copy_tool_binary

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


def x_copy_tf_binaries_to_workenv__mutmut_orig(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_1(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_2(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning(None)
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_3(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("XXNo bin directory available for tf binary copyingXX")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_4(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("no bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_5(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("NO BIN DIRECTORY AVAILABLE FOR TF BINARY COPYING")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_6(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["XXtofuXX", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_7(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["TOFU", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_8(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "XXibmtfXX"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_9(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "IBMTF"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_10(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name != "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_11(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "XXtofuXX":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_12(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "TOFU":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_13(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = None
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_14(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(None)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_15(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = None

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_16(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(None)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_17(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = None
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_18(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = None
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_19(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(None)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_20(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = None

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_21(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) or logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_22(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(None, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_23(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, None, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_24(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, None) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_25(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_26(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_27(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, ) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_28(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(None)

        except Exception as e:
            logger.warning(f"Failed to copy {tool_name} binary: {e}")


def x_copy_tf_binaries_to_workenv__mutmut_29(bin_dir: pathlib.Path, config: WorkenvConfig | None) -> None:
    """Copy all active tf binaries to workenv bin directory.

    Args:
        bin_dir: Target bin directory
        config: Workenv configuration
    """
    if not bin_dir:
        logger.warning("No bin directory available for tf binary copying")
        return

    # Get active versions for both tf variants
    for tool_name in ["tofu", "ibmtf"]:
        try:
            # Create a temporary manager instance to get active version
            if tool_name == "tofu":
                from wrknv.managers.tf.tofu import TofuTfVariant

                temp_manager = TofuTfVariant(config)
            else:
                from wrknv.managers.tf.ibm import IbmTfVariant

                temp_manager = IbmTfVariant(config)

            active_version = temp_manager.get_installed_version()
            if active_version:
                source_path = temp_manager.get_binary_path(active_version)
                target_name = temp_manager.executable_name

                if copy_tool_binary(source_path, target_name, bin_dir) and logger.is_debug_enabled():
                    logger.debug(f"Copied {tool_name} {active_version} to {bin_dir}")

        except Exception as e:
            logger.warning(None)

x_copy_tf_binaries_to_workenv__mutmut_mutants : ClassVar[MutantDict] = {
'x_copy_tf_binaries_to_workenv__mutmut_1': x_copy_tf_binaries_to_workenv__mutmut_1, 
    'x_copy_tf_binaries_to_workenv__mutmut_2': x_copy_tf_binaries_to_workenv__mutmut_2, 
    'x_copy_tf_binaries_to_workenv__mutmut_3': x_copy_tf_binaries_to_workenv__mutmut_3, 
    'x_copy_tf_binaries_to_workenv__mutmut_4': x_copy_tf_binaries_to_workenv__mutmut_4, 
    'x_copy_tf_binaries_to_workenv__mutmut_5': x_copy_tf_binaries_to_workenv__mutmut_5, 
    'x_copy_tf_binaries_to_workenv__mutmut_6': x_copy_tf_binaries_to_workenv__mutmut_6, 
    'x_copy_tf_binaries_to_workenv__mutmut_7': x_copy_tf_binaries_to_workenv__mutmut_7, 
    'x_copy_tf_binaries_to_workenv__mutmut_8': x_copy_tf_binaries_to_workenv__mutmut_8, 
    'x_copy_tf_binaries_to_workenv__mutmut_9': x_copy_tf_binaries_to_workenv__mutmut_9, 
    'x_copy_tf_binaries_to_workenv__mutmut_10': x_copy_tf_binaries_to_workenv__mutmut_10, 
    'x_copy_tf_binaries_to_workenv__mutmut_11': x_copy_tf_binaries_to_workenv__mutmut_11, 
    'x_copy_tf_binaries_to_workenv__mutmut_12': x_copy_tf_binaries_to_workenv__mutmut_12, 
    'x_copy_tf_binaries_to_workenv__mutmut_13': x_copy_tf_binaries_to_workenv__mutmut_13, 
    'x_copy_tf_binaries_to_workenv__mutmut_14': x_copy_tf_binaries_to_workenv__mutmut_14, 
    'x_copy_tf_binaries_to_workenv__mutmut_15': x_copy_tf_binaries_to_workenv__mutmut_15, 
    'x_copy_tf_binaries_to_workenv__mutmut_16': x_copy_tf_binaries_to_workenv__mutmut_16, 
    'x_copy_tf_binaries_to_workenv__mutmut_17': x_copy_tf_binaries_to_workenv__mutmut_17, 
    'x_copy_tf_binaries_to_workenv__mutmut_18': x_copy_tf_binaries_to_workenv__mutmut_18, 
    'x_copy_tf_binaries_to_workenv__mutmut_19': x_copy_tf_binaries_to_workenv__mutmut_19, 
    'x_copy_tf_binaries_to_workenv__mutmut_20': x_copy_tf_binaries_to_workenv__mutmut_20, 
    'x_copy_tf_binaries_to_workenv__mutmut_21': x_copy_tf_binaries_to_workenv__mutmut_21, 
    'x_copy_tf_binaries_to_workenv__mutmut_22': x_copy_tf_binaries_to_workenv__mutmut_22, 
    'x_copy_tf_binaries_to_workenv__mutmut_23': x_copy_tf_binaries_to_workenv__mutmut_23, 
    'x_copy_tf_binaries_to_workenv__mutmut_24': x_copy_tf_binaries_to_workenv__mutmut_24, 
    'x_copy_tf_binaries_to_workenv__mutmut_25': x_copy_tf_binaries_to_workenv__mutmut_25, 
    'x_copy_tf_binaries_to_workenv__mutmut_26': x_copy_tf_binaries_to_workenv__mutmut_26, 
    'x_copy_tf_binaries_to_workenv__mutmut_27': x_copy_tf_binaries_to_workenv__mutmut_27, 
    'x_copy_tf_binaries_to_workenv__mutmut_28': x_copy_tf_binaries_to_workenv__mutmut_28, 
    'x_copy_tf_binaries_to_workenv__mutmut_29': x_copy_tf_binaries_to_workenv__mutmut_29
}

def copy_tf_binaries_to_workenv(*args, **kwargs):
    result = _mutmut_trampoline(x_copy_tf_binaries_to_workenv__mutmut_orig, x_copy_tf_binaries_to_workenv__mutmut_mutants, args, kwargs)
    return result 

copy_tf_binaries_to_workenv.__signature__ = _mutmut_signature(x_copy_tf_binaries_to_workenv__mutmut_orig)
x_copy_tf_binaries_to_workenv__mutmut_orig.__name__ = 'x_copy_tf_binaries_to_workenv'


# 🧰🌍🔚
