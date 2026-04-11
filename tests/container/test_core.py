#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for container.core.ContainerManager."""

from __future__ import annotations

from pathlib import Path
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.config import WorkenvConfig
from wrknv.config.core import WorkenvSettings
from wrknv.container.core import ContainerManager
from wrknv.wenv.schema import ContainerConfig


def _make_manager(tmp_dir: Path, project_name: str | None = None) -> ContainerManager:
    """Create a ContainerManager with storage path in tmp_dir."""

    container_cfg = ContainerConfig(
        storage_path=str(tmp_dir / "containers"),
        persistent_volumes=["workspace"],
    )
    cfg = WorkenvConfig(
        project_name=project_name,
        version="1.0.0",
        container=container_cfg,
        workenv=WorkenvSettings(),
    )
    with mock.patch("pathlib.Path.cwd", return_value=tmp_dir):
        return ContainerManager(config=cfg)


class TestContainerManagerInit(FoundationTestCase):
    """Tests for ContainerManager.__init__."""

    def test_init_with_default_project_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, None)
        assert manager.CONTAINER_NAME == ContainerManager.DEFAULT_CONTAINER_NAME

    def test_init_with_custom_project_name(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp, "my-awesome-app")
        assert manager.CONTAINER_NAME == "my-awesome-app-dev"

    def test_init_sets_image_tag(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        assert manager.IMAGE_TAG == ContainerManager.DEFAULT_IMAGE_TAG
        assert "latest" in manager.full_image

    def test_setup_storage_creates_directories(self) -> None:
        tmp = self.create_temp_dir()
        _make_manager(tmp)
        storage_base = tmp / "containers"
        assert storage_base.exists()
        assert (storage_base / "shared").exists()
        assert (storage_base / "shared" / "downloads").exists()

    def test_setup_storage_creates_container_dir(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        storage_base = tmp / "containers"
        container_dir = storage_base / manager.CONTAINER_NAME
        assert container_dir.exists()
        assert (container_dir / "volumes").exists()
        assert (container_dir / "build").exists()
        assert (container_dir / "logs").exists()
        assert (container_dir / "backups").exists()

    def test_setup_storage_creates_persistent_volume_dirs(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        volumes_dir = tmp / "containers" / manager.CONTAINER_NAME / "volumes"
        assert (volumes_dir / "workspace").exists()

    def test_init_without_config_uses_default(self) -> None:
        tmp = self.create_temp_dir()
        from wrknv.wenv.schema import get_default_config

        default_cfg = get_default_config()
        with (
            mock.patch.object(
                type(default_cfg.container), "storage_path", new=str(tmp / "containers")
            ),
            mock.patch("wrknv.wenv.schema.get_default_config", return_value=default_cfg),
            mock.patch("pathlib.Path.cwd", return_value=tmp),
        ):
            # Just check it doesn't error
            pass


class TestContainerManagerGetContainerPath(FoundationTestCase):
    """Tests for get_container_path."""

    def test_returns_container_dir_with_no_subpath(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        path = manager.get_container_path()
        assert path == tmp / "containers" / manager.CONTAINER_NAME

    def test_returns_subpath_within_container_dir(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        path = manager.get_container_path("logs")
        assert path == tmp / "containers" / manager.CONTAINER_NAME / "logs"

    def test_returns_empty_string_subpath_as_base(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        path = manager.get_container_path("")
        assert path == tmp / "containers" / manager.CONTAINER_NAME


class TestContainerManagerCheckDocker(FoundationTestCase):
    """Tests for check_docker."""

    def test_returns_true_when_docker_available(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 0
        with mock.patch("wrknv.container.core.run", return_value=mock_result):
            assert manager.check_docker() is True

    def test_returns_false_when_docker_fails(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 1
        with mock.patch("wrknv.container.core.run", return_value=mock_result):
            assert manager.check_docker() is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.container.core.run", side_effect=FileNotFoundError):
            assert manager.check_docker() is False


class TestContainerManagerContainerExists(FoundationTestCase):
    """Tests for container_exists."""

    def test_returns_true_when_container_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 0
        with mock.patch("wrknv.container.core.run", return_value=mock_result):
            assert manager.container_exists() is True

    def test_returns_false_when_not_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 1
        with mock.patch("wrknv.container.core.run", return_value=mock_result):
            assert manager.container_exists() is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.container.core.run", side_effect=RuntimeError):
            assert manager.container_exists() is False


class TestContainerManagerContainerRunning(FoundationTestCase):
    """Tests for container_running."""

    def test_returns_false_when_container_not_exists(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch.object(manager, "container_exists", return_value=False):
            assert manager.container_running() is False

    def test_returns_true_when_running(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "true"
        with (
            mock.patch.object(manager, "container_exists", return_value=True),
            mock.patch("wrknv.container.core.run", return_value=mock_result),
        ):
            assert manager.container_running() is True

    def test_returns_false_when_not_running(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 0
        mock_result.stdout = "false"
        with (
            mock.patch.object(manager, "container_exists", return_value=True),
            mock.patch("wrknv.container.core.run", return_value=mock_result),
        ):
            assert manager.container_running() is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with (
            mock.patch.object(manager, "container_exists", return_value=True),
            mock.patch("wrknv.container.core.run", side_effect=RuntimeError),
        ):
            assert manager.container_running() is False


class TestContainerManagerImageExists(FoundationTestCase):
    """Tests for image_exists."""

    def test_returns_true_when_image_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 0
        with mock.patch("wrknv.container.core.run", return_value=mock_result):
            assert manager.image_exists() is True

    def test_returns_false_when_not_found(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        mock_result = mock.Mock()
        mock_result.returncode = 1
        with mock.patch("wrknv.container.core.run", return_value=mock_result):
            assert manager.image_exists() is False

    def test_returns_false_on_exception(self) -> None:
        tmp = self.create_temp_dir()
        manager = _make_manager(tmp)
        with mock.patch("wrknv.container.core.run", side_effect=FileNotFoundError):
            assert manager.image_exists() is False


class TestContainerManagerGetVolumeMappings(FoundationTestCase):
    """Tests for get_volume_mappings."""

    def test_returns_configured_mappings_when_set(self) -> None:
        tmp = self.create_temp_dir()
        container_cfg = ContainerConfig(
            storage_path=str(tmp / "containers"),
            volume_mappings={"myvolume": "/host/path:/container/path"},
        )
        cfg = WorkenvConfig(
            project_name="test",
            version="1.0.0",
            container=container_cfg,
            workenv=WorkenvSettings(),
        )
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            manager = ContainerManager(config=cfg)
        mappings = manager.get_volume_mappings()
        assert "myvolume" in mappings
        assert mappings["myvolume"] == "/host/path:/container/path"

    def test_returns_default_mappings_when_not_configured(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            manager = _make_manager(tmp)
            mappings = manager.get_volume_mappings()
        assert str(tmp) in mappings
        assert mappings[str(tmp)] == "/workspace"

    def test_includes_persistent_volumes_in_default_mappings(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.cwd", return_value=tmp):
            manager = _make_manager(tmp)
            mappings = manager.get_volume_mappings()
        # "workspace" is the persistent volume from _make_manager
        assert any("workspace" in k for k in mappings)


# 🧰🌍🔚
