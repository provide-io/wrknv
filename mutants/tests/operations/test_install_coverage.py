#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wenv/operations/install.py and platform.py — uncovered branches."""

from __future__ import annotations

from unittest.mock import patch

from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.operations.install import clean_directory, create_symlink, make_executable
from wrknv.wenv.operations.platform import get_workenv_platform


class TestGetWorkenvPlatform(FoundationTestCase):
    """Line 54 in platform.py: get_workenv_platform() was never called."""

    def test_get_workenv_platform_returns_string(self) -> None:
        """Line 54: get_workenv_platform() delegates to get_platform_string()."""
        result = get_workenv_platform()
        assert isinstance(result, str)
        assert len(result) > 0


class TestMakeExecutableChmodFailure(FoundationTestCase):
    """Lines 88-89 in install.py: except Exception in make_executable."""

    def test_chmod_failure_logs_warning(self) -> None:
        """Line 88-89: chmod raises → warning logged, no exception propagated."""
        tmp = self.create_temp_dir()
        target = tmp / "binary"
        target.write_text("#!/bin/sh")

        with (
            patch("platform.system", return_value="Linux"),
            patch("pathlib.Path.chmod", side_effect=OSError("chmod failed")),
        ):
            # Should not raise — exception is caught and logged
            make_executable(target)


class TestCreateSymlinkNonWindowsRaises(FoundationTestCase):
    """Line 120 in install.py: raise in create_symlink when not Windows."""

    def test_symlink_oserror_re_raises_on_non_windows(self) -> None:
        """Line 120: OSError from symlink_to + not Windows → re-raise."""
        tmp = self.create_temp_dir()
        target = tmp / "target.txt"
        target.write_text("content")
        link = tmp / "link.txt"

        with (
            patch("pathlib.Path.symlink_to", side_effect=OSError("Permission denied")),
            patch("platform.system", return_value="Linux"),
            pytest.raises(OSError),
        ):
            create_symlink(target, link)


class TestCleanDirectoryItemRemovalFails(FoundationTestCase):
    """Line 155-156 in install.py: except Exception in clean_directory."""

    def test_item_removal_failure_logs_warning(self) -> None:
        """Lines 155-156: safe_delete raises → warning logged, continues."""
        tmp = self.create_temp_dir()
        test_dir = tmp / "to_clean"
        test_dir.mkdir()
        (test_dir / "file.txt").write_text("content")

        with patch(
            "wrknv.wenv.operations.install.safe_delete",
            side_effect=OSError("permission denied"),
        ):
            # Should not raise — exception is caught and logged
            clean_directory(test_dir)


# 🧰🌍🔚
