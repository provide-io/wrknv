#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.tasks.environment — uncovered branches."""

from __future__ import annotations

import sys
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.tasks.environment import ExecutionEnvironment


class TestArchNormalization(FoundationTestCase):
    """Lines 141, 145: architecture normalization branches in _find_venv_path."""

    def test_x86_64_normalizes_to_amd64(self) -> None:
        """Line 141: machine 'x86_64' → arch normalized to 'amd64'."""
        tmp = self.create_temp_dir()
        with (
            mock.patch("platform.machine", return_value="x86_64"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            ExecutionEnvironment(tmp, "testpkg")
            # Build the expected workenv path with amd64 arch
            expected_workenv = tmp / "workenv" / "testpkg_linux_amd64"
            expected_workenv.mkdir(parents=True)
            (expected_workenv / "pyvenv.cfg").write_text("[virtualenv]\n")
            # Re-evaluate to pick up the dir we just created
            env2 = ExecutionEnvironment(tmp, "testpkg")
        assert env2.venv_path == expected_workenv

    def test_unknown_arch_passes_through(self) -> None:
        """Line 145: machine 'ppc64le' → arch passed through unchanged."""
        tmp = self.create_temp_dir()
        with (
            mock.patch("platform.machine", return_value="ppc64le"),
            mock.patch("platform.system", return_value="Linux"),
        ):
            ExecutionEnvironment(tmp, "testpkg")
            expected_workenv = tmp / "workenv" / "testpkg_linux_ppc64le"
            expected_workenv.mkdir(parents=True)
            (expected_workenv / "pyvenv.cfg").write_text("[virtualenv]\n")
            env2 = ExecutionEnvironment(tmp, "testpkg")
        assert env2.venv_path == expected_workenv


class TestVenvNotFound(FoundationTestCase):
    """Line 171: _find_venv_path returns None when no venv found outside virtual env."""

    def test_returns_none_when_no_venv_and_not_in_venv(self) -> None:
        """Line 171: no venv dirs found, not in virtual env → returns None."""
        tmp = self.create_temp_dir()
        # Simulate not being in a virtual environment
        original_base = sys.base_prefix
        try:
            sys.base_prefix = sys.prefix  # make base_prefix == prefix → not in venv
            if hasattr(sys, "real_prefix"):
                real_prefix = sys.real_prefix
                del sys.real_prefix
            else:
                real_prefix = None
            env = ExecutionEnvironment(tmp, "testpkg")
            result = env.venv_path
        finally:
            sys.base_prefix = original_base
            if real_prefix is not None:
                sys.real_prefix = real_prefix  # type: ignore[attr-defined]
        assert result is None


class TestUVProjectReadTomlException(FoundationTestCase):
    """Line 196: except Exception when read_toml fails in _is_uv_project."""

    def test_corrupt_pyproject_does_not_raise(self) -> None:
        """Line 196: read_toml raises → exception caught → returns False."""
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text("{ not valid toml !!!")

        env = ExecutionEnvironment(tmp, "testpkg")
        # Should not raise; corrupt pyproject.toml → not uv project
        assert env.is_uv_project is False


# 🧰🌍🔚
