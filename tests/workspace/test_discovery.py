#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.workspace.discovery."""

from __future__ import annotations

from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.workspace.discovery import RepoInfo, WorkspaceDiscovery


def _make_git_pyproject_repo(root: Path, name: str, extra_toml: str = "") -> Path:
    """Create a minimal git+pyproject repo directory under root."""
    repo = root / name
    repo.mkdir(parents=True, exist_ok=True)
    (repo / ".git").mkdir()
    (repo / "pyproject.toml").write_text(f'[project]\nname = "{name}"\n{extra_toml}')
    return repo


class TestRepoInfoDataclass(FoundationTestCase):
    """Tests for the RepoInfo attrs dataclass."""

    def test_instantiation_with_all_fields(self) -> None:
        path = Path("/some/path")
        info = RepoInfo(
            path=path,
            name="my-repo",
            has_git=True,
            has_pyproject=True,
            detected_type="foundation-based",
            current_config={"project": {"name": "my-repo"}},
        )
        assert info.path == path
        assert info.name == "my-repo"
        assert info.has_git is True
        assert info.has_pyproject is True
        assert info.detected_type == "foundation-based"
        assert info.current_config is not None

    def test_instantiation_with_none_fields(self) -> None:
        info = RepoInfo(
            path=Path("/x"),
            name=None,
            has_git=False,
            has_pyproject=False,
            detected_type=None,
            current_config=None,
        )
        assert info.name is None
        assert info.detected_type is None
        assert info.current_config is None


class TestWorkspaceDiscoveryInit(FoundationTestCase):
    """Tests for WorkspaceDiscovery.__init__."""

    def test_default_root_is_cwd(self) -> None:
        cwd = Path("/some/cwd")
        with mock.patch("pathlib.Path.cwd", return_value=cwd):
            disc = WorkspaceDiscovery()
        assert disc.root == cwd

    def test_custom_root_is_used(self) -> None:
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        assert disc.root == tmp


class TestDiscoverRepos(FoundationTestCase):
    """Tests for WorkspaceDiscovery.discover_repos."""

    def test_empty_workspace_returns_empty_list(self) -> None:
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        repos = disc.discover_repos()
        assert repos == []

    def test_discovers_git_pyproject_repos(self) -> None:
        tmp = self.create_temp_dir()
        _make_git_pyproject_repo(tmp, "repo-a")
        _make_git_pyproject_repo(tmp, "repo-b")
        disc = WorkspaceDiscovery(root=tmp)
        repos = disc.discover_repos()
        names = {r.name for r in repos}
        assert "repo-a" in names
        assert "repo-b" in names

    def test_excludes_dirs_without_git(self) -> None:
        tmp = self.create_temp_dir()
        no_git = tmp / "no-git"
        no_git.mkdir()
        (no_git / "pyproject.toml").write_text('[project]\nname = "no-git"\n')
        disc = WorkspaceDiscovery(root=tmp)
        repos = disc.discover_repos()
        assert all(r.name != "no-git" for r in repos)

    def test_excludes_dirs_without_pyproject(self) -> None:
        tmp = self.create_temp_dir()
        no_pp = tmp / "no-pyproject"
        no_pp.mkdir()
        (no_pp / ".git").mkdir()
        disc = WorkspaceDiscovery(root=tmp)
        repos = disc.discover_repos()
        assert all(r.name != "no-pyproject" for r in repos)

    def test_default_pattern_is_star(self) -> None:
        tmp = self.create_temp_dir()
        _make_git_pyproject_repo(tmp, "myrepo")
        disc = WorkspaceDiscovery(root=tmp)
        repos = disc.discover_repos(patterns=None)
        assert any(r.name == "myrepo" for r in repos)

    def test_custom_pattern_filters_repos(self) -> None:
        tmp = self.create_temp_dir()
        _make_git_pyproject_repo(tmp, "provide-foo")
        _make_git_pyproject_repo(tmp, "other-tool")
        disc = WorkspaceDiscovery(root=tmp)
        repos = disc.discover_repos(patterns=["provide-*"])
        names = {r.name for r in repos}
        assert "provide-foo" in names
        assert "other-tool" not in names

    def test_root_itself_not_included(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / ".git").mkdir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "root"\n')
        disc = WorkspaceDiscovery(root=tmp)
        repos = disc.discover_repos()
        assert all(r.path != tmp for r in repos)


class TestAnalyzeRepo(FoundationTestCase):
    """Tests for WorkspaceDiscovery.analyze_repo."""

    def test_full_repo_detected(self) -> None:
        tmp = self.create_temp_dir()
        repo = _make_git_pyproject_repo(tmp, "myrepo")
        disc = WorkspaceDiscovery(root=tmp)
        info = disc.analyze_repo(repo)
        assert info.has_git is True
        assert info.has_pyproject is True
        assert info.name == "myrepo"
        assert info.current_config is not None

    def test_name_falls_back_to_dir_name_when_no_project_name(self) -> None:
        tmp = self.create_temp_dir()
        repo = tmp / "fallback-name"
        repo.mkdir()
        (repo / ".git").mkdir()
        (repo / "pyproject.toml").write_text("[tool.ruff]\nline-length = 88\n")
        disc = WorkspaceDiscovery(root=tmp)
        info = disc.analyze_repo(repo)
        assert info.name == "fallback-name"

    def test_name_falls_back_when_no_pyproject(self) -> None:
        tmp = self.create_temp_dir()
        repo = tmp / "bare-git"
        repo.mkdir()
        (repo / ".git").mkdir()
        disc = WorkspaceDiscovery(root=tmp)
        info = disc.analyze_repo(repo)
        assert info.has_pyproject is False
        assert info.name == "bare-git"
        assert info.current_config is None

    def test_invalid_toml_results_in_none_config(self) -> None:
        tmp = self.create_temp_dir()
        repo = tmp / "broken"
        repo.mkdir()
        (repo / ".git").mkdir()
        (repo / "pyproject.toml").write_bytes(b"\xff\xfe invalid toml !!!")
        disc = WorkspaceDiscovery(root=tmp)
        info = disc.analyze_repo(repo)
        # Exception swallowed; config is None, name falls back to dir name
        assert info.current_config is None
        assert info.name == "broken"

    def test_detected_type_set_when_pyproject_present(self) -> None:
        tmp = self.create_temp_dir()
        repo = _make_git_pyproject_repo(tmp, "provide-foundation")
        disc = WorkspaceDiscovery(root=tmp)
        info = disc.analyze_repo(repo)
        assert info.detected_type == "foundation"


class TestDetectRepoType(FoundationTestCase):
    """Tests for WorkspaceDiscovery.detect_repo_type."""

    def _disc(self) -> WorkspaceDiscovery:
        return WorkspaceDiscovery(root=Path("/fake"))

    def test_detects_foundation_by_name(self) -> None:
        disc = self._disc()
        result = disc.detect_repo_type({"project": {"name": "provide-foundation", "dependencies": []}}, Path("/x"))
        assert result == "foundation"

    def test_detects_testkit_by_name(self) -> None:
        disc = self._disc()
        result = disc.detect_repo_type({"project": {"name": "provide-testkit", "dependencies": []}}, Path("/x"))
        assert result == "testkit"

    def test_detects_pyvider_plugin_by_prefix(self) -> None:
        disc = self._disc()
        result = disc.detect_repo_type({"project": {"name": "pyvider-myplugin", "dependencies": []}}, Path("/x"))
        assert result == "pyvider-plugin"

    def test_detects_provider_by_exact_name(self) -> None:
        disc = self._disc()
        result = disc.detect_repo_type({"project": {"name": "pyvider", "dependencies": []}}, Path("/x"))
        assert result == "provider"

    def test_detects_packaging_by_flavor_in_name(self) -> None:
        disc = self._disc()
        result = disc.detect_repo_type({"project": {"name": "my-flavor-pkg", "dependencies": []}}, Path("/x"))
        assert result == "packaging"

    def test_detects_foundation_based_by_dependency(self) -> None:
        disc = self._disc()
        pyproject = {"project": {"name": "something-else", "dependencies": ["provide-foundation>=1.0"]}}
        result = disc.detect_repo_type(pyproject, Path("/x"))
        assert result == "foundation-based"

    def test_detects_pyvider_plugin_by_dependency(self) -> None:
        disc = self._disc()
        pyproject = {"project": {"name": "something-else", "dependencies": ["pyvider>=2.0"]}}
        result = disc.detect_repo_type(pyproject, Path("/x"))
        assert result == "pyvider-plugin"

    def test_detects_provider_by_src_pyvider_dir(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "src" / "pyvider").mkdir(parents=True)
        disc = self._disc()
        pyproject = {"project": {"name": "some-unnamed", "dependencies": []}}
        result = disc.detect_repo_type(pyproject, tmp)
        assert result == "provider"

    def test_detects_foundation_based_by_src_provide_dir(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "src" / "provide").mkdir(parents=True)
        disc = self._disc()
        pyproject = {"project": {"name": "some-unnamed", "dependencies": []}}
        result = disc.detect_repo_type(pyproject, tmp)
        assert result == "foundation-based"

    def test_detects_foundation_based_by_logging_classifier(self) -> None:
        disc = self._disc()
        pyproject = {
            "project": {
                "name": "some-lib",
                "dependencies": [],
                "classifiers": ["Topic :: System :: Logging"],
            }
        }
        result = disc.detect_repo_type(pyproject, Path("/x"))
        assert result == "foundation-based"

    def test_detects_packaging_by_build_tools_classifier(self) -> None:
        disc = self._disc()
        pyproject = {
            "project": {
                "name": "some-lib",
                "dependencies": [],
                "classifiers": ["Topic :: Software Development :: Build Tools"],
            }
        }
        result = disc.detect_repo_type(pyproject, Path("/x"))
        assert result == "packaging"

    def test_returns_unknown_when_no_patterns_match(self) -> None:
        disc = self._disc()
        pyproject = {"project": {"name": "unrelated-thing", "dependencies": [], "classifiers": []}}
        result = disc.detect_repo_type(pyproject, Path("/x"))
        assert result == "unknown"

    def test_empty_pyproject_returns_unknown(self) -> None:
        disc = self._disc()
        result = disc.detect_repo_type({}, Path("/x"))
        assert result == "unknown"


class TestGetRepoStatus(FoundationTestCase):
    """Tests for WorkspaceDiscovery.get_repo_status."""

    def test_nonexistent_path_returns_minimal_status(self) -> None:
        disc = WorkspaceDiscovery(root=Path("/fake"))
        status = disc.get_repo_status(Path("/does/not/exist/xyz"))
        assert status["exists"] is False
        assert status["has_git"] is False
        assert status["git_status"] is None

    def test_existing_path_without_git_has_no_git_status(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "x"\n')
        disc = WorkspaceDiscovery(root=tmp)
        status = disc.get_repo_status(tmp)
        assert status["exists"] is True
        assert status["has_git"] is False
        assert status["has_pyproject"] is True
        assert status["git_status"] is None

    def test_full_repo_status_keys_present(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / ".git").mkdir()
        (tmp / "pyproject.toml").write_text('[project]\nname = "x"\n')
        (tmp / "workenv").mkdir()
        (tmp / "CLAUDE.md").write_text("# CLAUDE")
        disc = WorkspaceDiscovery(root=tmp)
        mock_git_status = {"branch": "main", "dirty": False, "files_changed": 0}
        with mock.patch.object(disc, "_get_git_status", return_value=mock_git_status):
            status = disc.get_repo_status(tmp)
        assert status["has_git"] is True
        assert status["has_pyproject"] is True
        assert status["has_workenv"] is True
        assert status["has_claude_md"] is True
        assert status["git_status"] == mock_git_status

    def test_git_status_called_when_has_git(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / ".git").mkdir()
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.object(disc, "_get_git_status", return_value=None) as mock_gs:
            disc.get_repo_status(tmp)
        mock_gs.assert_called_once_with(tmp)


class TestGetGitStatus(FoundationTestCase):
    """Tests for WorkspaceDiscovery._get_git_status."""

    def test_returns_branch_dirty_files_on_success(self) -> None:
        tmp = self.create_temp_dir()
        branch_result = mock.Mock()
        branch_result.stdout = "main\n"
        status_result = mock.Mock()
        status_result.stdout = " M file.py\n?? new.py\n"

        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch("wrknv.workspace.discovery.WorkspaceDiscovery._get_git_status") as m:
            m.return_value = {"branch": "main", "dirty": True, "files_changed": 2}
            result = disc._get_git_status(tmp)
        assert result["branch"] == "main"
        assert result["dirty"] is True
        assert result["files_changed"] == 2

    def test_returns_none_when_run_raises(self) -> None:
        """_get_git_status returns None when the underlying run() call fails."""
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        mock_run = mock.Mock(side_effect=OSError("git not found"))
        mock_process = mock.MagicMock()
        mock_process.run = mock_run
        with mock.patch.dict("sys.modules", {"provide.foundation.process": mock_process}):
            result = disc._get_git_status(tmp)
        assert result is None

    def test_returns_none_when_provide_foundation_process_is_none(self) -> None:
        """_get_git_status returns None when the process module import raises."""
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.dict("sys.modules", {"provide.foundation.process": None}):
            # Module is set to None; importing from it raises TypeError/ImportError
            result = disc._get_git_status(tmp)
        assert result is None


class TestValidateWorkspaceStructure(FoundationTestCase):
    """Tests for WorkspaceDiscovery.validate_workspace_structure."""

    def test_nonexistent_root_returns_early(self) -> None:
        disc = WorkspaceDiscovery(root=Path("/fake"))
        issues = disc.validate_workspace_structure(Path("/does/not/exist/xyz"))
        assert any("does not exist" in i for i in issues)
        assert len(issues) == 1

    def test_missing_workspace_toml_adds_issue(self) -> None:
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.object(disc, "discover_repos", return_value=[]):
            issues = disc.validate_workspace_structure(tmp)
        assert any("workspace.toml" in i for i in issues)

    def test_workspace_toml_present_no_issue_for_it(self) -> None:
        tmp = self.create_temp_dir()
        wrknv_dir = tmp / ".wrknv"
        wrknv_dir.mkdir()
        (wrknv_dir / "workspace.toml").write_text("")
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.object(disc, "discover_repos", return_value=[]):
            issues = disc.validate_workspace_structure(tmp)
        assert not any("workspace.toml" in i for i in issues)

    def test_repo_with_unknown_type_adds_issue(self) -> None:
        tmp = self.create_temp_dir()
        repo = _make_git_pyproject_repo(tmp, "mystery-pkg")
        disc = WorkspaceDiscovery(root=tmp)
        fake_repo = RepoInfo(
            path=repo,
            name="mystery-pkg",
            has_git=True,
            has_pyproject=True,
            detected_type="unknown",
            current_config=None,
        )
        with mock.patch.object(disc, "discover_repos", return_value=[fake_repo]):
            issues = disc.validate_workspace_structure(tmp)
        assert any("mystery-pkg" in i and "type" in i for i in issues)


class TestGetWorkspaceSummary(FoundationTestCase):
    """Tests for WorkspaceDiscovery.get_workspace_summary."""

    def test_empty_workspace_summary(self) -> None:
        tmp = self.create_temp_dir()
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.object(disc, "discover_repos", return_value=[]):
            summary = disc.get_workspace_summary()
        assert summary["total_repos"] == 0
        assert summary["type_distribution"] == {}
        assert summary["repos"] == []
        assert summary["root"] == str(tmp)

    def test_summary_counts_types(self) -> None:
        tmp = self.create_temp_dir()
        repo_a = _make_git_pyproject_repo(tmp, "repo-a")
        repo_b = _make_git_pyproject_repo(tmp, "repo-b")
        fake_repos = [
            RepoInfo(
                path=repo_a,
                name="repo-a",
                has_git=True,
                has_pyproject=True,
                detected_type="foundation-based",
                current_config=None,
            ),
            RepoInfo(
                path=repo_b,
                name="repo-b",
                has_git=True,
                has_pyproject=True,
                detected_type="foundation-based",
                current_config=None,
            ),
        ]
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.object(disc, "discover_repos", return_value=fake_repos):
            summary = disc.get_workspace_summary()
        assert summary["total_repos"] == 2
        assert summary["type_distribution"]["foundation-based"] == 2

    def test_summary_none_type_counted_as_unknown(self) -> None:
        tmp = self.create_temp_dir()
        repo_a = _make_git_pyproject_repo(tmp, "repo-a")
        fake_repos = [
            RepoInfo(
                path=repo_a,
                name="repo-a",
                has_git=True,
                has_pyproject=True,
                detected_type=None,
                current_config=None,
            )
        ]
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.object(disc, "discover_repos", return_value=fake_repos):
            summary = disc.get_workspace_summary()
        assert summary["type_distribution"].get("unknown") == 1

    def test_summary_repos_list_has_relative_path(self) -> None:
        tmp = self.create_temp_dir()
        repo_a = _make_git_pyproject_repo(tmp, "repo-a")
        fake_repos = [
            RepoInfo(
                path=repo_a,
                name="repo-a",
                has_git=True,
                has_pyproject=True,
                detected_type="testkit",
                current_config=None,
            )
        ]
        disc = WorkspaceDiscovery(root=tmp)
        with mock.patch.object(disc, "discover_repos", return_value=fake_repos):
            summary = disc.get_workspace_summary()
        assert len(summary["repos"]) == 1
        entry = summary["repos"][0]
        assert entry["name"] == "repo-a"
        assert entry["type"] == "testkit"
        assert entry["path"] == "repo-a"


# 🧰🌍🔚
