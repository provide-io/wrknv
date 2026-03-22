#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for container.manager - uncovered branches."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from wrknv.config import WorkenvConfig
from wrknv.container.manager import ContainerManager


def _make_manager(tmp_path: Path) -> ContainerManager:
    from wrknv.wenv.schema import ContainerConfig

    config = WorkenvConfig(
        project_name="test-project",
        container=ContainerConfig(enabled=True, storage_path=str(tmp_path / "storage")),
    )
    return ContainerManager(config)


def _make_manager_with_env(tmp_path: Path, env: dict) -> ContainerManager:
    from wrknv.wenv.schema import ContainerConfig

    config = WorkenvConfig(
        project_name="test-project",
        container=ContainerConfig(enabled=True, storage_path=str(tmp_path / "storage"), environment=env),
    )
    return ContainerManager(config)


@pytest.mark.container
class TestBuildImageWithEnvironment:
    """Cover line 164: build_args.update when environment is non-empty."""

    def test_environment_vars_passed_to_builder(self, tmp_path: Path) -> None:
        """Line 164: non-empty environment → build_args.update(environment)."""
        from provide.testkit.mocking import Mock

        mgr = _make_manager_with_env(tmp_path, {"MYVAR": "value"})
        mock_builder = Mock()
        mock_builder.generate_dockerfile.return_value = "FROM ubuntu:22.04\n"
        mock_builder.build.return_value = True
        mgr.builder = mock_builder

        with patch("pathlib.Path.write_text"):
            result = mgr.build_image()

        assert result is True
        _, kwargs = mock_builder.build.call_args
        assert kwargs.get("build_args") == {"MYVAR": "value"}


@pytest.mark.container
class TestCheckDockerRuntimeError:
    """Cover lines 124-125: RuntimeError from runtime.is_available() returns False."""

    def test_runtime_error_returns_false(self, tmp_path: Path) -> None:
        """Lines 124-125: RuntimeError → returns False."""
        mgr = _make_manager(tmp_path)
        with patch.object(mgr.runtime.__class__, "is_available", side_effect=RuntimeError("no docker")):
            result = mgr.check_docker()
        assert result is False


@pytest.mark.container
class TestStatusRuntimeError:
    """Cover lines 218-219: RuntimeError from runtime.is_available() in status()."""

    def test_runtime_error_sets_false(self, tmp_path: Path) -> None:
        """Lines 218-219: RuntimeError → docker_available=False in status dict."""
        mgr = _make_manager(tmp_path)
        with (
            patch.object(mgr.runtime.__class__, "is_available", side_effect=RuntimeError("no docker")),
            patch.object(mgr.lifecycle.__class__, "status", return_value={}),
        ):
            result = mgr.status()
        assert result["docker_available"] is False


@pytest.mark.container
class TestBackupVolumes:
    """Cover lines 247->251, 256, 263-265 in backup_volumes."""

    def test_exception_returns_none(self, tmp_path: Path) -> None:
        """Lines 263-265: exception during backup returns None."""
        mgr = _make_manager(tmp_path)
        container_dir = mgr.storage.get_container_path()
        container_dir.mkdir(parents=True, exist_ok=True)
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir(exist_ok=True)
        (volumes_dir / "data").mkdir(exist_ok=True)

        backup_dest = tmp_path / "backup.tar.gz"
        with patch("tarfile.open", side_effect=OSError("disk full")):
            result = mgr.backup_volumes(backup_path=backup_dest)
        assert result is None

    def test_auto_generates_backup_path(self, tmp_path: Path) -> None:
        """Line 247->251: backup_path is None → auto-generate timestamped path."""
        mgr = _make_manager(tmp_path)
        result = mgr.backup_volumes()  # backup_path=None, volumes_dir already created by setup
        # volumes_dir exists and is empty → backup succeeds with auto-generated name
        assert result is not None
        assert result.name.startswith("volumes_backup_")


@pytest.mark.container
class TestRestoreVolumes:
    """Cover lines 277, 284, 286->289, 304-306 in restore_volumes."""

    def test_missing_backup_returns_false(self, tmp_path: Path) -> None:
        """Line 277: backup file doesn't exist → returns False."""
        mgr = _make_manager(tmp_path)
        result = mgr.restore_volumes(backup_path=tmp_path / "nonexistent.tar.gz")
        assert result is False

    def test_volumes_exist_no_force_returns_false(self, tmp_path: Path) -> None:
        """Line 284: volumes exist and force=False → returns False."""
        mgr = _make_manager(tmp_path)
        # volumes dir already created by setup_storage
        backup = tmp_path / "backup.tar.gz"
        backup.write_bytes(b"dummy")

        result = mgr.restore_volumes(backup_path=backup, force=False)
        assert result is False

    def test_force_with_invalid_tar_covers_rmtree_and_exception(self, tmp_path: Path) -> None:
        """Lines 286->289 and 304-306: force=True + existing volumes + invalid tar."""
        mgr = _make_manager(tmp_path)
        # volumes dir exists from setup_storage; force=True → rmtree branch (286->289)
        backup = tmp_path / "backup.tar.gz"
        backup.write_bytes(b"not a valid tar")

        result = mgr.restore_volumes(backup_path=backup, force=True)
        # tarfile.open fails with invalid data → exception handler (304-306)
        assert result is False


@pytest.mark.container
class TestCleanVolumes:
    """Cover lines 319->318, 330-332 in clean_volumes."""

    def test_exception_returns_false(self, tmp_path: Path) -> None:
        """Lines 330-332: exception during clean_volumes returns False."""
        mgr = _make_manager(tmp_path)
        volumes_dir = mgr.storage.get_container_path("volumes")
        vol = volumes_dir / "my_vol"
        vol.mkdir(exist_ok=True)

        with patch("shutil.rmtree", side_effect=OSError("permission denied")):
            result = mgr.clean_volumes()
        assert result is False

    def test_skips_non_directory_entries(self, tmp_path: Path) -> None:
        """Line 319->318: file entries in volumes_dir are skipped (not directories)."""
        mgr = _make_manager(tmp_path)
        volumes_dir = mgr.storage.get_container_path("volumes")
        # Create a file (not dir) and a dir in volumes_dir
        (volumes_dir / "notes.txt").write_text("log")
        (volumes_dir / "data").mkdir(exist_ok=True)

        result = mgr.clean_volumes()
        assert result is True


@pytest.mark.container
class TestClean:
    """Cover lines 351->356, 353, 356->359 in clean()."""

    def test_clean_stops_running_container(self, tmp_path: Path) -> None:
        """Line 353: container is running → stop() is called before remove."""
        mgr = _make_manager(tmp_path)
        with (
            patch.object(mgr.__class__, "container_exists", return_value=True),
            patch.object(mgr.__class__, "container_running", return_value=True),
            patch.object(mgr.__class__, "stop", return_value=True) as mock_stop,
            patch.object(mgr.lifecycle.__class__, "remove", return_value=True),
            patch.object(mgr.__class__, "clean_volumes", return_value=True),
            patch.object(mgr.storage.__class__, "clean_storage", return_value=True),
        ):
            result = mgr.clean()
        assert result is True
        mock_stop.assert_called_once()

    def test_clean_with_preserve_volumes_skips_clean_volumes(self, tmp_path: Path) -> None:
        """Line 356->359: preserve_volumes=True skips clean_volumes."""
        mgr = _make_manager(tmp_path)
        with (
            patch.object(mgr.__class__, "container_exists", return_value=False),
            patch.object(mgr.__class__, "clean_volumes", return_value=True) as mock_clean_volumes,
            patch.object(mgr.storage.__class__, "clean_storage", return_value=True),
        ):
            result = mgr.clean(preserve_volumes=True)
        assert result is True
        mock_clean_volumes.assert_not_called()


# 🧰🌍🔚
