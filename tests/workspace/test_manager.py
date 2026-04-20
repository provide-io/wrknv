#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for WorkspaceManager."""

from __future__ import annotations

import asyncio
from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.workspace.manager import WorkspaceManager
from wrknv.workspace.schema import WorkspaceConfig


class TestWorkspaceManagerLoadConfig(FoundationTestCase):
    """Tests for WorkspaceManager.load_config."""

    def test_returns_none_when_config_file_missing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)
        result = mgr.load_config()
        assert result is None

    def test_returns_none_when_toml_empty(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)
        mgr.config_dir.mkdir(exist_ok=True)
        mgr.config_path.write_text("")
        with mock.patch("wrknv.workspace.manager.read_toml", return_value={}):
            result = mgr.load_config()
        assert result is None

    def test_returns_none_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)
        mgr.config_dir.mkdir(exist_ok=True)
        mgr.config_path.write_text("[workspace]\nroot = '/tmp'")
        with mock.patch("wrknv.workspace.manager.read_toml", side_effect=Exception("parse error")):
            result = mgr.load_config()
        assert result is None

    def test_returns_config_when_valid(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)
        mgr.config_dir.mkdir(exist_ok=True)
        mgr.config_path.write_text("")

        mock_config = mock.Mock(spec=WorkspaceConfig)
        with (
            mock.patch("wrknv.workspace.manager.read_toml", return_value={"root": str(tmp)}),
            mock.patch("wrknv.workspace.manager.WorkspaceConfig.from_dict", return_value=mock_config),
        ):
            result = mgr.load_config()
        assert result is mock_config


class TestWorkspaceManagerSaveConfig(FoundationTestCase):
    """Tests for WorkspaceManager.save_config."""

    def test_raises_on_write_failure(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)
        config = mock.Mock(spec=WorkspaceConfig)
        config.to_dict.return_value = {}

        with (
            mock.patch("wrknv.workspace.manager.write_toml", side_effect=OSError("disk full")),
            pytest.raises(OSError),
        ):
            mgr.save_config(config)

    def test_saves_successfully(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)
        mgr.config_dir.mkdir(exist_ok=True)
        config = mock.Mock(spec=WorkspaceConfig)
        config.to_dict.return_value = {}

        with mock.patch("wrknv.workspace.manager.write_toml") as mock_write:
            mgr.save_config(config)
        mock_write.assert_called_once()


class TestWorkspaceManagerAddRepo(FoundationTestCase):
    """Tests for WorkspaceManager.add_repo."""

    def test_raises_when_repo_path_missing(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)
        with pytest.raises(FileNotFoundError):
            mgr.add_repo(tmp / "nonexistent")

    def test_creates_workspace_when_none_exists(self) -> None:
        tmp = self.create_temp_dir()
        repo_dir = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)

        mock_info = mock.Mock()
        mock_info.name = "myrepo"
        mock_info.detected_type = "generic"

        mock_config = mock.Mock(spec=WorkspaceConfig)
        mock_updated = mock.Mock(spec=WorkspaceConfig)
        mock_config.add_repo.return_value = mock_updated

        with (
            mock.patch.object(mgr.discovery, "analyze_repo", return_value=mock_info),
            mock.patch.object(mgr, "load_config", return_value=None),
            mock.patch.object(mgr, "init_workspace", return_value=mock_config) as mock_init,
            mock.patch.object(mgr, "save_config"),
        ):
            result = mgr.add_repo(repo_dir)

        mock_init.assert_called_once_with(auto_discover=False)
        assert result is mock_updated


class TestWorkspaceManagerSyncAll(FoundationTestCase):
    """Tests for WorkspaceManager.sync_all."""

    def test_raises_when_no_config(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)

        with (
            mock.patch.object(mgr, "load_config", return_value=None),
            pytest.raises(RuntimeError, match="No workspace configuration found"),
        ):
            asyncio.run(mgr.sync_all())


class TestWorkspaceManagerSyncRepo(FoundationTestCase):
    """Tests for WorkspaceManager.sync_repo."""

    def test_raises_when_no_config(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)

        with (
            mock.patch.object(mgr, "load_config", return_value=None),
            pytest.raises(RuntimeError, match="No workspace configuration found"),
        ):
            asyncio.run(mgr.sync_repo("myrepo"))


class TestWorkspaceManagerCheckDrift(FoundationTestCase):
    """Tests for WorkspaceManager.check_drift."""

    def test_raises_when_no_config(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)

        with (
            mock.patch.object(mgr, "load_config", return_value=None),
            pytest.raises(RuntimeError, match="No workspace configuration found"),
        ):
            mgr.check_drift()


class TestWorkspaceManagerSetupWorkspace(FoundationTestCase):
    """Tests for WorkspaceManager.setup_workspace."""

    def test_raises_when_no_config(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)

        with (
            mock.patch.object(mgr, "load_config", return_value=None),
            pytest.raises(RuntimeError, match="No workspace configuration found"),
        ):
            mgr.setup_workspace()

    def test_skips_repo_with_missing_path(self) -> None:
        tmp = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)

        mock_path = mock.Mock(spec=Path)
        mock_path.is_absolute.return_value = True
        mock_path.exists.return_value = False

        mock_repo = mock.Mock()
        mock_repo.name = "ghost_repo"
        mock_repo.path = mock_path

        mock_config = mock.Mock(spec=WorkspaceConfig)
        mock_config.repos = [mock_repo]

        with mock.patch.object(mgr, "load_config", return_value=mock_config):
            result = mgr.setup_workspace()

        assert "ghost_repo" in result["failures"]

    def test_skips_repo_without_pyproject(self) -> None:
        tmp = self.create_temp_dir()
        repo_dir = self.create_temp_dir()
        mgr = WorkspaceManager(root=tmp)

        mock_repo = mock.Mock()
        mock_repo.name = "nopyproject"
        mock_repo.path = repo_dir

        mock_config = mock.Mock(spec=WorkspaceConfig)
        mock_config.repos = [mock_repo]

        with mock.patch.object(mgr, "load_config", return_value=mock_config):
            result = mgr.setup_workspace()

        assert "nopyproject" in result["failures"]

    def test_succeeds_for_valid_repo(self) -> None:
        tmp = self.create_temp_dir()
        repo_dir = self.create_temp_dir()
        (repo_dir / "pyproject.toml").write_text("[project]\nname = 'test'")
        mgr = WorkspaceManager(root=tmp)

        mock_repo = mock.Mock()
        mock_repo.name = "goodrepo"
        mock_repo.path = repo_dir

        mock_config = mock.Mock(spec=WorkspaceConfig)
        mock_config.repos = [mock_repo]

        with (
            mock.patch.object(mgr, "load_config", return_value=mock_config),
            mock.patch(
                "wrknv.wenv.env_generator.create_project_env_scripts",
                return_value=(repo_dir / "env.sh", repo_dir / "env.ps1"),
            ),
        ):
            result = mgr.setup_workspace()

        assert result["success_count"] == 1
        assert "goodrepo" not in result["failures"]

    def test_catches_exception_during_env_script_generation(self) -> None:
        tmp = self.create_temp_dir()
        repo_dir = self.create_temp_dir()
        (repo_dir / "pyproject.toml").write_text("[project]\nname = 'test'")
        mgr = WorkspaceManager(root=tmp)

        mock_repo = mock.Mock()
        mock_repo.name = "badrepo"
        mock_repo.path = repo_dir

        mock_config = mock.Mock(spec=WorkspaceConfig)
        mock_config.repos = [mock_repo]

        with (
            mock.patch.object(mgr, "load_config", return_value=mock_config),
            mock.patch(
                "wrknv.wenv.env_generator.create_project_env_scripts",
                side_effect=RuntimeError("generation failed"),
            ),
        ):
            result = mgr.setup_workspace()

        assert "badrepo" in result["failures"]
        assert result["success_count"] == 0


# 🧰🌍🔚
