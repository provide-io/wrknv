#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.tf.bin_ops module."""

from __future__ import annotations

from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.managers.tf.bin_ops import copy_tf_binaries_to_workenv


class TestCopyTfBinariesToWorkenv(FoundationTestCase):
    """Tests for copy_tf_binaries_to_workenv."""

    def test_does_nothing_when_no_bin_dir(self) -> None:
        # Passing None as bin_dir should return early
        with mock.patch("wrknv.managers.tf.bin_ops.copy_tool_binary") as mock_copy:
            copy_tf_binaries_to_workenv(None, None)  # type: ignore[arg-type]
        mock_copy.assert_not_called()

    def test_copies_when_versions_active(self) -> None:
        tmp = self.create_temp_dir()
        mock_tofu = mock.Mock()
        mock_tofu.get_installed_version.return_value = "1.5.0"
        mock_tofu.get_binary_path.return_value = tmp / "tofu"
        mock_tofu.executable_name = "tofu"

        mock_ibm = mock.Mock()
        mock_ibm.get_installed_version.return_value = "1.7.0"
        mock_ibm.get_binary_path.return_value = tmp / "ibmtf"
        mock_ibm.executable_name = "ibmtf"

        def make_manager(config):
            return mock_tofu if "Tofu" in str(type(config)) else mock_ibm

        with (
            mock.patch("wrknv.managers.tf.bin_ops.copy_tool_binary", return_value=True) as mock_copy,
            mock.patch("wrknv.managers.tf.tofu.TofuTfVariant", return_value=mock_tofu),
            mock.patch("wrknv.managers.tf.ibm.IbmTfVariant", return_value=mock_ibm),
        ):
            copy_tf_binaries_to_workenv(tmp / "bin", None)
        assert mock_copy.call_count >= 1

    def test_handles_exception_gracefully(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("wrknv.managers.tf.tofu.TofuTfVariant", side_effect=RuntimeError("fail")):
            # Should not raise
            copy_tf_binaries_to_workenv(tmp / "bin", None)

    def test_skips_when_no_active_version(self) -> None:
        tmp = self.create_temp_dir()
        mock_tofu = mock.Mock()
        mock_tofu.get_installed_version.return_value = None

        mock_ibm = mock.Mock()
        mock_ibm.get_installed_version.return_value = None

        with (
            mock.patch("wrknv.managers.tf.bin_ops.copy_tool_binary") as mock_copy,
            mock.patch("wrknv.managers.tf.tofu.TofuTfVariant", return_value=mock_tofu),
            mock.patch("wrknv.managers.tf.ibm.IbmTfVariant", return_value=mock_ibm),
        ):
            copy_tf_binaries_to_workenv(tmp / "bin", None)
        mock_copy.assert_not_called()


# 🧰🌍🔚
