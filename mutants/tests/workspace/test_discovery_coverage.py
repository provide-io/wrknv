#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.workspace.discovery — uncovered branches."""

from __future__ import annotations

from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.workspace.discovery import RepoInfo, WorkspaceDiscovery


def _make_repo_info(
    path: Path,
    name: str,
    has_git: bool = True,
    has_pyproject: bool = True,
    detected_type: str | None = "foundation-based",
) -> RepoInfo:
    return RepoInfo(
        path=path,
        name=name,
        has_git=has_git,
        has_pyproject=has_pyproject,
        detected_type=detected_type,
        current_config=None,
    )


class TestClassifierLoopBranch(FoundationTestCase):
    """Line 125->122: elif classifier False → loop continues (non-matching classifier)."""

    def test_unrecognized_classifier_loops_back(self) -> None:
        """Line 125->122: classifier matches neither logging nor build tools → continue."""
        tmp = self.create_temp_dir()
        repo = tmp / "mypkg"
        repo.mkdir()
        (repo / ".git").mkdir()
        # pyproject with classifiers that match neither known topic
        (repo / "pyproject.toml").write_text(
            '[project]\nname = "mypkg"\n'
            'classifiers = ["Topic :: Internet :: WWW/HTTP", "Topic :: Utilities"]\n'
        )
        disc = WorkspaceDiscovery(root=tmp)
        info = disc.discover_repos()
        # repo should be discovered; detected_type will be "unknown" since classifiers don't match
        repo_infos = [r for r in info if r.name == "mypkg"]
        assert len(repo_infos) == 1
        assert repo_infos[0].detected_type == "unknown"


class TestValidateWorkspaceStructureBranches(FoundationTestCase):
    """Lines 208, 211, 213->206: validate branches with no-git and no-pyproject repos."""

    def test_repo_without_git_adds_issue(self) -> None:
        """Line 208: repo.has_git is False → issue appended."""
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        fake_repo = _make_repo_info(tmp / "mypkg", "mypkg", has_git=False)
        with mock.patch.object(disc, "discover_repos", return_value=[fake_repo]):
            issues = disc.validate_workspace_structure(tmp)
        assert any("not a git repository" in i for i in issues)

    def test_repo_without_pyproject_adds_issue(self) -> None:
        """Line 211: repo.has_pyproject is False → issue appended."""
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        fake_repo = _make_repo_info(tmp / "mypkg", "mypkg", has_pyproject=False)
        with mock.patch.object(disc, "discover_repos", return_value=[fake_repo]):
            issues = disc.validate_workspace_structure(tmp)
        assert any("no pyproject.toml" in i for i in issues)

    def test_multiple_repos_loop_continues(self) -> None:
        """Line 213->206: for loop iterates beyond first repo (backward branch)."""
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        repo1 = _make_repo_info(tmp / "pkg1", "pkg1", detected_type="unknown")
        repo2 = _make_repo_info(tmp / "pkg2", "pkg2", detected_type="foundation-based")
        with mock.patch.object(disc, "discover_repos", return_value=[repo1, repo2]):
            issues = disc.validate_workspace_structure(tmp)
        # pkg1 had unknown type → issue added; pkg2 didn't → loop continued after pkg1
        assert any("pkg1" in i for i in issues)


class TestGetGitStatusSuccess(FoundationTestCase):
    """Lines 172-180: _get_git_status successful path."""

    def test_get_git_status_returns_branch_and_dirty(self) -> None:
        """Lines 172-180: git commands succeed → returns branch and dirty flag."""
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)

        clean_result = mock.Mock()
        clean_result.stdout = "main\n"
        dirty_result = mock.Mock()
        dirty_result.stdout = " M file.py\n"

        with mock.patch("provide.foundation.process.run", side_effect=[clean_result, dirty_result]):
            result = disc._get_git_status(tmp)

        assert result is not None
        assert result["branch"] == "main"
        assert result["dirty"] is True
        assert result["files_changed"] == 1


# 🧰🌍🔚
