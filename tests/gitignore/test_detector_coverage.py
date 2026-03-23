#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for gitignore.detector - uncovered branches."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from wrknv.gitignore.detector import ProjectDetector


@pytest.mark.unit
class TestRequirementsTxtException:
    """Cover exception handler in _check_directory (line 216)."""

    def test_unreadable_requirements_txt_logs_debug(self, tmp_path: Path) -> None:
        """Line 216: exception reading requirements.txt is silently caught."""
        (tmp_path / "requirements.txt").write_text("flask\n")
        detector = ProjectDetector()

        with patch("pathlib.Path.read_text", side_effect=OSError("permission denied")):
            # Should not raise
            detector.detect_project_types(tmp_path)


@pytest.mark.unit
class TestScanRecursiveSkipsNonFileNonDir:
    """Cover line 137->127: items that are neither file nor non-hidden dir are skipped."""

    def test_broken_symlink_is_skipped(self, tmp_path: Path) -> None:
        """Line 137->127: broken symlink is neither is_file() nor is_dir() → loop continues."""
        # Create a broken symlink (points to non-existent target)
        broken = tmp_path / "broken_link"
        broken.symlink_to(tmp_path / "nonexistent_target")
        # Also create a real file so the scan has something to process
        (tmp_path / "setup.py").write_text("# setup")

        detector = ProjectDetector()
        # Should not raise - broken symlink is silently skipped
        detector.detect_project_types(tmp_path)


# 🧰🌍🔚
