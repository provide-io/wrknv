#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for config.persistence module (WorkenvConfigPersistence)."""

from __future__ import annotations

import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config.core import WorkenvConfig
from wrknv.config.persistence import WorkenvConfigPersistence


def _make_config(config_path: pathlib.Path | None = None) -> WorkenvConfig:
    """Create a WorkenvConfig with mocked _find_config_file."""
    path = config_path or pathlib.Path("/nonexistent/wrknv.toml")
    with mock.patch.object(WorkenvConfig, "_find_config_file", return_value=path):
        cfg = WorkenvConfig.load()
    return cfg


class TestEnsureConfigPath(FoundationTestCase):
    """Test _ensure_config_path."""

    def test_raises_when_config_path_is_none(self) -> None:
        cfg = _make_config()
        cfg.config_path = None
        persistence = WorkenvConfigPersistence(config=cfg)
        with pytest.raises(RuntimeError, match="Configuration path is not set"):
            persistence._ensure_config_path()

    def test_returns_config_path_when_set(self) -> None:
        path = pathlib.Path("/some/wrknv.toml")
        cfg = _make_config(config_path=path)
        persistence = WorkenvConfigPersistence(config=cfg)
        assert persistence._ensure_config_path() == path


class TestLoadConfig(FoundationTestCase):
    """Test load_config branches."""

    def test_load_config_with_all_fields(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        config_path.write_text("")  # file must exist
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        config_data = {
            "project_name": "loaded-project",
            "version": "2.0",
            "tools": {"uv": "0.5.0"},
            "profiles": {"default": {}},
            "gitignore": {"templates": ["Python"]},
            "workenv": {
                "auto_install": True,
                "use_cache": False,
                "env": {"siblings": []},
            },
        }

        with mock.patch("wrknv.config.persistence.read_toml", return_value=config_data):
            persistence.load_config()

        assert cfg.project_name == "loaded-project"
        assert cfg.version == "2.0"
        assert cfg.tools == {"uv": "0.5.0"}
        assert cfg.profiles == {"default": {}}
        assert cfg.gitignore == {"templates": ["Python"]}
        assert cfg.env == {"siblings": []}
        assert cfg.workenv.auto_install is True

    def test_load_config_exception_is_swallowed(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        config_path.write_text("")  # file must exist
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        with mock.patch("wrknv.config.persistence.read_toml", side_effect=Exception("parse error")):
            # Should not raise
            persistence.load_config()

    def test_load_config_no_file(self) -> None:
        """load_config is a no-op when config_path doesn't exist."""
        cfg = _make_config()
        cfg.config_path = pathlib.Path("/no/such/file.toml")
        persistence = WorkenvConfigPersistence(config=cfg)
        # Should not raise
        persistence.load_config()

    def test_load_config_workenv_unknown_key_ignored(self) -> None:
        """workenv keys not on WorkenvSettings are silently ignored."""
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        config_path.write_text("")  # file must exist
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        config_data = {"workenv": {"unknown_key": "value"}}

        with mock.patch("wrknv.config.persistence.read_toml", return_value=config_data):
            persistence.load_config()


class TestToDict(FoundationTestCase):
    """Test to_dict branches."""

    def test_to_dict_includes_env_when_set(self) -> None:
        cfg = _make_config()
        cfg.env = {"siblings": ["../other"]}
        persistence = WorkenvConfigPersistence(config=cfg)
        result = persistence.to_dict()
        assert "env" in result["workenv"]
        assert result["workenv"]["env"] == {"siblings": ["../other"]}

    def test_to_dict_excludes_env_when_empty(self) -> None:
        cfg = _make_config()
        cfg.env = {}
        persistence = WorkenvConfigPersistence(config=cfg)
        result = persistence.to_dict()
        assert "env" not in result["workenv"]

    def test_to_dict_includes_gitignore_when_set(self) -> None:
        cfg = _make_config()
        cfg.gitignore = {"templates": ["Python", "Node"]}
        persistence = WorkenvConfigPersistence(config=cfg)
        result = persistence.to_dict()
        assert result["gitignore"] == {"templates": ["Python", "Node"]}

    def test_to_dict_excludes_gitignore_when_empty(self) -> None:
        cfg = _make_config()
        cfg.gitignore = {}
        persistence = WorkenvConfigPersistence(config=cfg)
        result = persistence.to_dict()
        assert "gitignore" not in result


class TestWriteConfig(FoundationTestCase):
    """Test write_config branches."""

    def test_write_config_updates_all_fields(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        new_data = {
            "project_name": "new-name",
            "version": "3.0",
            "tools": {"go": "1.21"},
            "profiles": {"prod": {}},
            "gitignore": {"templates": ["Go"]},
            "workenv": {
                "auto_install": False,
                "env": {"siblings": ["../sibling"]},
            },
        }

        with mock.patch("wrknv.config.persistence.write_toml"):
            persistence.write_config(new_data)

        assert cfg.project_name == "new-name"
        assert cfg.version == "3.0"
        assert cfg.tools == {"go": "1.21"}
        assert cfg.profiles == {"prod": {}}
        assert cfg.gitignore == {"templates": ["Go"]}
        assert cfg.env == {"siblings": ["../sibling"]}

    def test_write_config_partial_data(self) -> None:
        """write_config handles dict with only some fields."""
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        cfg = _make_config(config_path=config_path)
        cfg.project_name = "original"
        persistence = WorkenvConfigPersistence(config=cfg)

        with mock.patch("wrknv.config.persistence.write_toml"):
            persistence.write_config({"version": "5.0"})

        assert cfg.project_name == "original"  # unchanged
        assert cfg.version == "5.0"


class TestEditConfig(FoundationTestCase):
    """Test edit_config branches."""

    def test_edit_config_raises_when_no_editor(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        config_path.write_text("")
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        with (
            mock.patch.dict("os.environ", {"EDITOR": "", "VISUAL": ""}),
            pytest.raises(RuntimeError, match="No editor configured"),
        ):
            persistence.edit_config()

    def test_edit_config_creates_file_if_missing(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        mock_result = mock.MagicMock()
        mock_result.returncode = 0

        with (
            mock.patch.dict("os.environ", {"EDITOR": "vim"}),
            mock.patch("wrknv.config.persistence.run", return_value=mock_result),
            mock.patch("wrknv.config.persistence.write_toml"),
        ):
            persistence.edit_config()

    def test_edit_config_raises_on_nonzero_exit(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        config_path.write_text("")
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        mock_result = mock.MagicMock()
        mock_result.returncode = 1

        with (
            mock.patch.dict("os.environ", {"EDITOR": "vim"}),
            mock.patch("wrknv.config.persistence.run", return_value=mock_result),
            pytest.raises(RuntimeError, match="Editor exited with error code"),
        ):
            persistence.edit_config()

    def test_edit_config_reloads_after_edit(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        config_path.write_text("")
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)

        mock_result = mock.MagicMock()
        mock_result.returncode = 0

        with (
            mock.patch.dict("os.environ", {"EDITOR": "vim"}),
            mock.patch("wrknv.config.persistence.run", return_value=mock_result),
            mock.patch.object(persistence, "load_config") as mock_load,
        ):
            persistence.edit_config()
        mock_load.assert_called_once()


class TestConfigExistsAndGetPath(FoundationTestCase):
    """Test config_exists and get_config_path."""

    def test_config_exists_returns_false_when_no_path(self) -> None:
        cfg = _make_config()
        cfg.config_path = None
        persistence = WorkenvConfigPersistence(config=cfg)
        assert persistence.config_exists() is False

    def test_config_exists_returns_true_when_file_present(self) -> None:
        tmp = self.create_temp_dir()
        config_path = tmp / "wrknv.toml"
        config_path.write_text("")
        cfg = _make_config(config_path=config_path)
        persistence = WorkenvConfigPersistence(config=cfg)
        assert persistence.config_exists() is True

    def test_config_exists_returns_false_when_file_missing(self) -> None:
        cfg = _make_config(config_path=pathlib.Path("/no/such/file.toml"))
        persistence = WorkenvConfigPersistence(config=cfg)
        assert persistence.config_exists() is False

    def test_get_config_path_returns_path(self) -> None:
        path = pathlib.Path("/my/wrknv.toml")
        cfg = _make_config(config_path=path)
        persistence = WorkenvConfigPersistence(config=cfg)
        assert persistence.get_config_path() == path


# 🧰🌍🔚
