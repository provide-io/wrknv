#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for container.storage - uncovered branches."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from wrknv.container.storage import ContainerStorage
from wrknv.wenv.schema import ContainerConfig


def _make_storage(tmp_path: Path) -> ContainerStorage:
    config = ContainerConfig(enabled=True, storage_path=str(tmp_path / "storage"))
    return ContainerStorage(container_name="test-project-dev", container_config=config)


@pytest.mark.container
class TestSaveMetadataException:
    """Cover exception handler in save_metadata (line 113)."""

    def test_write_error_logs_warning(self, tmp_path: Path) -> None:
        """Line 113: exception during save_metadata logs warning and doesn't raise."""
        storage = _make_storage(tmp_path)
        # Patch json.dump (inside try block) to trigger except Exception branch
        with patch("json.dump", side_effect=OSError("disk full")):
            storage.save_metadata({"key": "value"})  # Should not raise


@pytest.mark.container
class TestLoadMetadataException:
    """Cover exception handler in load_metadata (lines 127-129)."""

    def test_corrupt_json_logs_warning(self, tmp_path: Path) -> None:
        """Lines 127-129: corrupt JSON in load_metadata logs warning and returns None."""
        storage = _make_storage(tmp_path)
        # Create the metadata file with corrupt JSON
        metadata_path = storage.get_container_path("metadata.json")
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text("{ not valid json }")

        result = storage.load_metadata()
        assert result is None


@pytest.mark.container
class TestGetBackupPath:
    """Cover auto-generated backup name (lines 143-144)."""

    def test_auto_generated_name(self, tmp_path: Path) -> None:
        """Lines 143-144: when backup_name is None, auto-generates timestamped name."""
        storage = _make_storage(tmp_path)
        # Must create parent dirs so backup_dir.mkdir(exist_ok=True) can run
        storage.get_container_path().mkdir(parents=True, exist_ok=True)
        path = storage.get_backup_path()
        assert path.name.startswith("volumes_backup_")
        assert path.name.endswith(".tar.gz")

    def test_explicit_name(self, tmp_path: Path) -> None:
        """Explicit backup_name is used as-is."""
        storage = _make_storage(tmp_path)
        storage.get_container_path().mkdir(parents=True, exist_ok=True)
        path = storage.get_backup_path("my_backup.tar.gz")
        assert path.name == "my_backup.tar.gz"


@pytest.mark.container
class TestGetLatestBackup:
    """Cover get_latest_backup (lines 150-161)."""

    def test_no_backup_dir_returns_none(self, tmp_path: Path) -> None:
        """Lines 150-153: returns None when backup dir doesn't exist."""
        storage = _make_storage(tmp_path)
        result = storage.get_latest_backup()
        assert result is None

    def test_empty_backup_dir_returns_none(self, tmp_path: Path) -> None:
        """Lines 155-157: returns None when no backup files found."""
        storage = _make_storage(tmp_path)
        backup_dir = storage.get_container_path("backups")
        backup_dir.mkdir(parents=True)
        result = storage.get_latest_backup()
        assert result is None

    def test_returns_latest_backup(self, tmp_path: Path) -> None:
        """Lines 159-161: returns the most recently modified backup file."""
        storage = _make_storage(tmp_path)
        backup_dir = storage.get_container_path("backups")
        backup_dir.mkdir(parents=True)
        # Create two backup files with different mtimes
        older = backup_dir / "volumes_backup_20240101_000000.tar.gz"
        newer = backup_dir / "volumes_backup_20240102_000000.tar.gz"
        older.write_bytes(b"old")
        newer.write_bytes(b"new")
        import os
        import time

        os.utime(older, (time.time() - 100, time.time() - 100))
        os.utime(newer, (time.time(), time.time()))

        result = storage.get_latest_backup()
        assert result == newer


@pytest.mark.container
class TestCleanStorage:
    """Cover clean_storage method (lines 165-209)."""

    def test_no_container_dir_returns_true(self, tmp_path: Path) -> None:
        """Lines 165-168: returns True when container dir doesn't exist."""
        storage = _make_storage(tmp_path)
        result = storage.clean_storage()
        assert result is True

    def test_clean_with_volumes(self, tmp_path: Path) -> None:
        """Lines 172-179: cleans up volumes directory."""
        storage = _make_storage(tmp_path)
        container_dir = storage.get_container_path()
        container_dir.mkdir(parents=True)
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir()
        vol = volumes_dir / "my_volume"
        vol.mkdir()
        (vol / "data.txt").write_text("data")

        result = storage.clean_storage()
        assert result is True
        assert not vol.exists()

    def test_clean_with_file_in_volumes_skips_it(self, tmp_path: Path) -> None:
        """Line 175->174: volume entry that is a file (not dir) → if volume_path.is_dir() False → loop continues."""
        storage = _make_storage(tmp_path)
        container_dir = storage.get_container_path()
        container_dir.mkdir(parents=True)
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir()
        # Create a file inside volumes/ (not a directory)
        (volumes_dir / "not_a_dir.txt").write_text("metadata")

        result = storage.clean_storage()
        assert result is True
        assert (volumes_dir / "not_a_dir.txt").exists()  # file was NOT removed

    def test_clean_with_build_dir(self, tmp_path: Path) -> None:
        """Lines 181-187: cleans up build directory."""
        storage = _make_storage(tmp_path)
        container_dir = storage.get_container_path()
        container_dir.mkdir(parents=True)
        build_dir = container_dir / "build"
        build_dir.mkdir()
        (build_dir / "artifact").write_text("artifact")

        result = storage.clean_storage()
        assert result is True
        assert build_dir.exists()  # Recreated empty

    def test_clean_with_logs(self, tmp_path: Path) -> None:
        """Lines 190-193: removes .log files from logs directory."""
        storage = _make_storage(tmp_path)
        container_dir = storage.get_container_path()
        container_dir.mkdir(parents=True)
        logs_dir = container_dir / "logs"
        logs_dir.mkdir()
        log_file = logs_dir / "app.log"
        log_file.write_text("log content")

        result = storage.clean_storage()
        assert result is True
        assert not log_file.exists()

    def test_clean_preserves_backups_by_default(self, tmp_path: Path) -> None:
        """Lines 195-196: backups are preserved when preserve_backups=True."""
        storage = _make_storage(tmp_path)
        container_dir = storage.get_container_path()
        container_dir.mkdir(parents=True)
        backups_dir = container_dir / "backups"
        backups_dir.mkdir()
        backup = backups_dir / "volumes_backup_20240101_000000.tar.gz"
        backup.write_bytes(b"backup")

        result = storage.clean_storage(preserve_backups=True)
        assert result is True
        assert backup.exists()

    def test_clean_removes_backups_when_not_preserved(self, tmp_path: Path) -> None:
        """Lines 196-202: backups removed when preserve_backups=False."""
        storage = _make_storage(tmp_path)
        container_dir = storage.get_container_path()
        container_dir.mkdir(parents=True)
        backups_dir = container_dir / "backups"
        backups_dir.mkdir()
        backup = backups_dir / "volumes_backup_20240101_000000.tar.gz"
        backup.write_bytes(b"backup")

        result = storage.clean_storage(preserve_backups=False)
        assert result is True
        assert not backup.exists()

    def test_exception_returns_false(self, tmp_path: Path) -> None:
        """Lines 207-209: exception during clean returns False."""
        storage = _make_storage(tmp_path)
        container_dir = storage.get_container_path()
        container_dir.mkdir(parents=True)
        volumes_dir = container_dir / "volumes"
        volumes_dir.mkdir()
        vol = volumes_dir / "my_volume"
        vol.mkdir()

        with patch("shutil.rmtree", side_effect=OSError("permission denied")):
            result = storage.clean_storage()
        assert result is False


# 🧰🌍🔚
