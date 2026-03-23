#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.wenv.operations.verify — uncovered branches."""

from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from typing import Any
from unittest.mock import patch

from provide.foundation.process import ProcessError
from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.operations.verify import (
    check_binary_compatibility,
    parse_go_version,
    run_version_check,
)


@contextmanager
def _fast_retry(func: Any) -> Generator[None, None, None]:
    """Temporarily zero out the retry sleep on a @retry-decorated function."""
    executor = func.__closure__[0].cell_contents
    original = executor._sleep
    executor._sleep = lambda t: None
    try:
        yield
    finally:
        executor._sleep = original


class TestRunVersionCheckProcessError(FoundationTestCase):
    """Lines 75-79: except ProcessError branches in run_version_check."""

    def test_process_error_with_timeout_true(self) -> None:
        """Line 75->76: ProcessError.timeout=True → 'timed out' log + re-raise."""
        tmp = self.create_temp_dir()
        binary_path = tmp / "terraform"
        binary_path.write_text("#!/bin/sh")

        with (
            _fast_retry(run_version_check),
            patch(
                "wrknv.wenv.operations.verify.run",
                side_effect=ProcessError("timeout", timeout=True),
            ),
            pytest.raises(ProcessError),
        ):
            run_version_check(binary_path, "terraform")

    def test_process_error_with_timeout_false(self) -> None:
        """Lines 77-79: ProcessError.timeout=False → 'failed' log + re-raise."""
        tmp = self.create_temp_dir()
        binary_path = tmp / "terraform"
        binary_path.write_text("#!/bin/sh")

        with (
            _fast_retry(run_version_check),
            patch(
                "wrknv.wenv.operations.verify.run",
                side_effect=ProcessError("cmd failed", timeout=False),
            ),
            pytest.raises(ProcessError),
        ):
            run_version_check(binary_path, "terraform")


class TestCheckBinaryCompatibilityProcessError(FoundationTestCase):
    """Lines 124-127: except ProcessError branches in check_binary_compatibility."""

    def test_process_error_timeout_returns_timed_out(self) -> None:
        """Line 124->125: ProcessError.timeout=True → 'timed out' error result."""
        tmp = self.create_temp_dir()
        binary_path = tmp / "terraform"
        binary_path.write_text("#!/bin/sh")

        with patch(
            "wrknv.wenv.operations.verify.run",
            side_effect=ProcessError("timeout", timeout=True),
        ):
            result = check_binary_compatibility(binary_path)

        assert result["compatible"] is False
        assert "timed out" in str(result["error"])

    def test_process_error_non_timeout_returns_error_str(self) -> None:
        """Lines 126-127: ProcessError.timeout=False → str(e) in error result."""
        tmp = self.create_temp_dir()
        binary_path = tmp / "terraform"
        binary_path.write_text("#!/bin/sh")

        with patch(
            "wrknv.wenv.operations.verify.run",
            side_effect=ProcessError("exec failed", timeout=False),
        ):
            result = check_binary_compatibility(binary_path)

        assert result["compatible"] is False
        assert "exec failed" in str(result["error"])


class TestParseGoVersionNoGoPrefixBranch(FoundationTestCase):
    """Branch 237->240: version_part.startswith('go') is False → skip version extraction."""

    def test_non_go_prefix_in_version_part(self) -> None:
        """237->240: parts[2] doesn't start with 'go' → info has no 'version' key."""
        # "go version 1.21.0" → parts[2]="1.21.0" doesn't start with "go"
        result = parse_go_version("go version 1.21.0")

        assert result["tool"] == "go"
        # version key is NOT set because parts[2] doesn't start with "go"
        assert "version" not in result

    def test_non_go_prefix_with_platform_part(self) -> None:
        """237->240 + 240->241: no 'go' prefix + 4 parts → platform extracted."""
        # parts[2]="1.21.0" (no "go" prefix), parts[3]="linux/amd64"
        result = parse_go_version("go version 1.21.0 linux/amd64")

        assert result["tool"] == "go"
        assert "version" not in result
        assert result["platform"] == "linux/amd64"


# 🧰🌍🔚
