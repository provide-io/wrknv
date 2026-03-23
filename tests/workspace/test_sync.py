#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for WorkspaceSync."""

from __future__ import annotations

import asyncio
from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.workspace.schema import RepoConfig, WorkspaceConfig
from wrknv.workspace.sync import WorkspaceSync


def _make_repo(name: str = "myrepo", path: Path | None = None, repo_type: str = "generic") -> RepoConfig:
    return RepoConfig(
        name=name,
        path=path or Path("/tmp/fake_repo"),
        type=repo_type,
        features=[],
        template_profile="default",
        custom_values={},
    )


def _make_workspace(*repos: RepoConfig) -> WorkspaceConfig:
    return WorkspaceConfig(root=Path("/tmp/workspace"), repos=list(repos), global_standards={})


class TestWorkspaceSyncBuildTemplateContext(FoundationTestCase):
    """Tests for _build_template_context."""

    def test_basic_context(self) -> None:
        repo = _make_repo(name="myrepo", repo_type="generic")
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)
        ctx = sync._build_template_context(repo)
        assert ctx["project_name"] == "myrepo"
        assert ctx["package_type"] == "generic"
        assert ctx["version"] == "1.0.0"
        assert ctx["python_version"] == "3.11"

    def test_custom_values_override_defaults(self) -> None:
        repo = _make_repo()
        repo = RepoConfig(
            name="myrepo",
            path=Path("/tmp/fake"),
            type="generic",
            features=[],
            template_profile="default",
            custom_values={"version": "2.0.0"},
        )
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)
        ctx = sync._build_template_context(repo)
        assert ctx["version"] == "2.0.0"

    def test_global_standards_included(self) -> None:
        repo = _make_repo()
        ws = WorkspaceConfig(root=Path("/tmp/workspace"), repos=[repo], global_standards={"company": "acme"})
        sync = WorkspaceSync(ws)
        ctx = sync._build_template_context(repo)
        assert ctx["company"] == "acme"

    def test_foundation_based_type_sets_workspace_sources(self) -> None:
        repo = _make_repo(repo_type="foundation-based")
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)
        ctx = sync._build_template_context(repo)
        assert "workspace_sources" in ctx
        assert "provide-foundation" in ctx["workspace_sources"]

    def test_pyvider_plugin_type_sets_workspace_sources(self) -> None:
        repo = _make_repo(repo_type="pyvider-plugin")
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)
        ctx = sync._build_template_context(repo)
        assert "workspace_sources" in ctx
        assert "pyvider" in ctx["workspace_sources"]

    def test_features_included_in_context(self) -> None:
        repo = RepoConfig(
            name="myrepo",
            path=Path("/tmp/fake"),
            type="generic",
            features=["docker", "terraform"],
            template_profile="default",
            custom_values={},
        )
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)
        ctx = sync._build_template_context(repo)
        assert ctx["features"] == ["docker", "terraform"]


class TestWorkspaceSyncApplyConfigChange(FoundationTestCase):
    """Tests for _apply_config_change."""

    def setup_method(self) -> None:
        super().setup_method()
        self.temp_dir = self.create_temp_dir()

    def _run(self, coro: object) -> object:
        return asyncio.run(coro)  # type: ignore[arg-type]

    def test_no_change_when_content_same(self) -> None:
        file_path = self.temp_dir / "config.txt"
        file_path.write_text("same content")
        sync = WorkspaceSync(_make_workspace())
        result = self._run(sync._apply_config_change(file_path, "same content", dry_run=False))
        assert not result["changed"]
        assert result["diff"] is None

    def test_writes_new_file(self) -> None:
        file_path = self.temp_dir / "new.txt"
        sync = WorkspaceSync(_make_workspace())
        result = self._run(sync._apply_config_change(file_path, "new content", dry_run=False))
        assert result["changed"]
        assert file_path.read_text() == "new content"

    def test_updates_existing_file(self) -> None:
        file_path = self.temp_dir / "existing.txt"
        file_path.write_text("old content")
        sync = WorkspaceSync(_make_workspace())
        result = self._run(sync._apply_config_change(file_path, "new content", dry_run=False))
        assert result["changed"]
        assert file_path.read_text() == "new content"

    def test_dry_run_does_not_write(self) -> None:
        file_path = self.temp_dir / "dry.txt"
        file_path.write_text("original")
        sync = WorkspaceSync(_make_workspace())
        result = self._run(sync._apply_config_change(file_path, "changed", dry_run=True))
        assert result["changed"]
        assert file_path.read_text() == "original"  # Not written

    def test_diff_generated_on_change(self) -> None:
        file_path = self.temp_dir / "diff.txt"
        file_path.write_text("old line\n")
        sync = WorkspaceSync(_make_workspace())
        result = self._run(sync._apply_config_change(file_path, "new line\n", dry_run=True))
        assert result["diff"] is not None
        assert "old line" in result["diff"] or "new line" in result["diff"]

    def test_creates_parent_directory(self) -> None:
        nested = self.temp_dir / "subdir" / "deep" / "file.txt"
        sync = WorkspaceSync(_make_workspace())
        self._run(sync._apply_config_change(nested, "content", dry_run=False))
        assert nested.exists()

    def test_read_error_returns_error_info(self) -> None:
        """Test that read errors return error info without crashing."""
        # Create a directory where the file should be (can't be read as text)
        file_path = self.temp_dir / "notreadable"
        file_path.mkdir()
        sync = WorkspaceSync(_make_workspace())
        result = self._run(sync._apply_config_change(file_path, "content", dry_run=False))
        assert "error" in result


class TestWorkspaceSyncSyncRepo(FoundationTestCase):
    """Tests for sync_repo with mocked config generation."""

    def _run(self, coro: object) -> object:
        return asyncio.run(coro)  # type: ignore[arg-type]

    def test_sync_repo_with_generated_config_applies_changes(self) -> None:
        tmp = self.create_temp_dir()
        repo = _make_repo(name="mocked_repo", path=tmp)
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)

        with mock.patch.object(sync, "_generate_configs", return_value={"config.txt": "new content"}):
            result = self._run(sync.sync_repo(repo, dry_run=False))

        assert result["repo"] == "mocked_repo"
        assert "config.txt" in result["changes"]
        assert result["files_updated"] == 1
        assert (tmp / "config.txt").read_text() == "new content"

    def test_sync_repo_dry_run_does_not_write(self) -> None:
        tmp = self.create_temp_dir()
        repo = _make_repo(name="dryrun_repo", path=tmp)
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)

        with mock.patch.object(sync, "_generate_configs", return_value={"config.txt": "content"}):
            result = self._run(sync.sync_repo(repo, dry_run=True))

        assert result["files_updated"] == 1
        assert not (tmp / "config.txt").exists()


class TestWorkspaceSyncWriteError(FoundationTestCase):
    """Tests for _apply_config_change write error handling."""

    def _run(self, coro: object) -> object:
        return asyncio.run(coro)  # type: ignore[arg-type]

    def test_write_error_sets_error_key(self) -> None:
        tmp = self.create_temp_dir()
        file_path = tmp / "existing.txt"
        file_path.write_text("original content")
        sync = WorkspaceSync(_make_workspace())

        with mock.patch.object(Path, "write_text", side_effect=OSError("permission denied")):
            result = self._run(sync._apply_config_change(file_path, "new content", dry_run=False))

        assert "error" in result
        assert result["changed"] is True


class TestWorkspaceSyncCheckDrift(FoundationTestCase):
    """Tests for check_drift."""

    def test_no_repos_no_drift(self) -> None:
        ws = _make_workspace()
        sync = WorkspaceSync(ws)
        report = sync.check_drift()
        assert not report["drift_detected"]
        assert report["repos_checked"] == 0

    def test_drift_detected_when_generates_configs(self) -> None:
        """Since _generate_configs returns {}, there's never any drift."""
        repo = _make_repo()
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)
        report = sync.check_drift()
        # No configs generated → no drift (empty expected_configs loop)
        assert not report["drift_detected"]

    def test_drift_detected_when_file_missing(self) -> None:
        tmp = self.create_temp_dir()
        repo = _make_repo(path=tmp)
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)

        with mock.patch.object(sync, "_generate_configs", return_value={"missing.txt": "content"}):
            report = sync.check_drift()

        assert report["drift_detected"] is True

    def test_drift_detected_when_file_differs(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "file.txt").write_text("old content")
        repo = _make_repo(path=tmp)
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)

        with mock.patch.object(sync, "_generate_configs", return_value={"file.txt": "new content"}):
            report = sync.check_drift()

        assert report["drift_detected"] is True

    def test_no_drift_when_file_matches(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "file.txt").write_text("same content")
        repo = _make_repo(path=tmp)
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)

        with mock.patch.object(sync, "_generate_configs", return_value={"file.txt": "same content"}):
            report = sync.check_drift()

        assert report["drift_detected"] is False

    def test_drift_on_read_error(self) -> None:
        tmp = self.create_temp_dir()
        trouble = tmp / "trouble.txt"
        trouble.mkdir()  # directory where file expected, causing read error
        repo = _make_repo(path=tmp)
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)

        with mock.patch.object(sync, "_generate_configs", return_value={"trouble.txt": "content"}):
            report = sync.check_drift()

        assert report["drift_detected"] is True

    def test_drift_report_structure(self) -> None:
        repo = _make_repo()
        ws = _make_workspace(repo)
        sync = WorkspaceSync(ws)
        report = sync.check_drift()
        assert "repos_checked" in report
        assert "drift_detected" in report
        assert "repo_drifts" in report


class TestWorkspaceSyncAll(FoundationTestCase):
    """Tests for sync_all."""

    def _run(self, coro: object) -> object:
        return asyncio.run(coro)  # type: ignore[arg-type]

    def test_sync_all_empty_workspace(self) -> None:
        ws = _make_workspace()
        sync = WorkspaceSync(ws)
        results = self._run(sync.sync_all())
        assert results == {}

    def test_sync_all_returns_results_per_repo(self) -> None:
        repo1 = _make_repo(name="repo1")
        repo2 = _make_repo(name="repo2")
        ws = _make_workspace(repo1, repo2)
        sync = WorkspaceSync(ws)
        results = self._run(sync.sync_all(dry_run=True))
        assert "repo1" in results
        assert "repo2" in results

    def test_sync_all_handles_repo_exception(self) -> None:
        """Test that exceptions in individual repos don't stop the whole sync."""
        repo1 = _make_repo(name="failing_repo")
        ws = _make_workspace(repo1)
        sync = WorkspaceSync(ws)

        # Make sync_repo raise
        from unittest import mock

        with mock.patch.object(sync, "sync_repo", side_effect=RuntimeError("boom")):
            results = self._run(sync.sync_all())

        assert "failing_repo" in results
        assert "error" in results["failing_repo"]


class TestWorkspaceSyncValidateTemplates(FoundationTestCase):
    """Tests for validate_templates."""

    def test_validate_templates_always_true(self) -> None:
        ws = _make_workspace()
        sync = WorkspaceSync(ws)
        assert sync.validate_templates() is True


# 🧰🌍🔚
