#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.cli.commands.security — uncovered branches."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from provide.testkit import FoundationTestCase


class TestSecurityScanNoGenerate(FoundationTestCase):
    """Line 170->180: security_scan with generate=False skips config block."""

    def test_scan_with_no_generate_skips_config(self) -> None:
        """Line 170->180: when generate=False, config load/write block is skipped."""
        from wrknv.cli.commands.security import security_scan

        with (
            patch("wrknv.cli.commands.security._run_trufflehog", return_value=True),
            patch("wrknv.cli.commands.security._run_gitleaks", return_value=True),
            patch("wrknv.cli.commands.security.load_security_config") as mock_load,
        ):
            security_scan(generate=False)
        mock_load.assert_not_called()


class TestRunTrufflehogExcludeFile(FoundationTestCase):
    """Line 219->222: _run_trufflehog adds --exclude-paths when exclude file exists."""

    def test_exclude_file_extends_cmd(self) -> None:
        """Line 219->222: exclude file exists → cmd extended with --exclude-paths."""
        from wrknv.cli.commands.security import _run_trufflehog

        tmp = self.create_temp_dir()
        exclude_file = tmp / ".trufflehog-exclude-paths.txt"
        exclude_file.write_text("tests/\n")

        mock_result = MagicMock()
        mock_result.returncode = 0

        with (
            patch("shutil.which", return_value="/usr/local/bin/trufflehog"),
            patch("pathlib.Path.cwd", return_value=tmp),
            patch("subprocess.run", return_value=mock_result) as mock_run,
        ):
            result = _run_trufflehog()

        assert result is True
        call_args = mock_run.call_args[0][0]
        assert "--exclude-paths" in call_args


class TestRunTrufflehogFailureNoStdout(FoundationTestCase):
    """Line 229->231: _run_trufflehog failure with empty stdout (False branch)."""

    def test_failure_with_no_stdout_skips_stdout_echo(self) -> None:
        """Line 229->231: scan fails and stdout is empty → stdout echo skipped."""
        from wrknv.cli.commands.security import _run_trufflehog

        tmp = self.create_temp_dir()
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "error message\n"

        with (
            patch("shutil.which", return_value="/usr/local/bin/trufflehog"),
            patch("pathlib.Path.cwd", return_value=tmp),
            patch("subprocess.run", return_value=mock_result),
        ):
            result = _run_trufflehog()

        assert result is False


class TestRunGitleaksConfigFile(FoundationTestCase):
    """Line 252->255: _run_gitleaks adds --config when config file exists."""

    def test_config_file_extends_cmd(self) -> None:
        """Line 252->255: config file exists → cmd extended with --config."""
        from wrknv.cli.commands.security import _run_gitleaks

        tmp = self.create_temp_dir()
        config_file = tmp / ".gitleaks.toml"
        config_file.write_text("[allowlist]\n")

        mock_result = MagicMock()
        mock_result.returncode = 0

        with (
            patch("shutil.which", return_value="/usr/local/bin/gitleaks"),
            patch("pathlib.Path.cwd", return_value=tmp),
            patch("subprocess.run", return_value=mock_result) as mock_run,
        ):
            result = _run_gitleaks()

        assert result is True
        call_args = mock_run.call_args[0][0]
        assert "--config" in call_args


class TestRunGitleaksFailureNoStdout(FoundationTestCase):
    """Line 262->264: _run_gitleaks failure with empty stdout (False branch)."""

    def test_failure_with_no_stdout_skips_stdout_echo(self) -> None:
        """Line 262->264: scan fails and stdout is empty → stdout echo skipped."""
        from wrknv.cli.commands.security import _run_gitleaks

        tmp = self.create_temp_dir()
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "error detail\n"

        with (
            patch("shutil.which", return_value="/usr/local/bin/gitleaks"),
            patch("pathlib.Path.cwd", return_value=tmp),
            patch("subprocess.run", return_value=mock_result),
        ):
            result = _run_gitleaks()

        assert result is False


# 🧰🌍🔚
