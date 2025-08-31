#
# tests/container/test_container_migration.py
#
"""
Test Container Storage Migration
================================
Tests for migrating from old to new container storage structure.
"""

import shutil
import tarfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from wrknv.container.manager import ContainerManager
from wrknv.container.migration import migrate_container_storage
from wrknv.wenv.schema import ContainerConfig, WorkenvConfig


class TestContainerStorageMigration:
    """Test container storage migration functionality."""

    @pytest.fixture
    def mock_home(self, tmp_path):
        """Mock home directory with old structure."""
        mock_home = tmp_path / "home"
        mock_home.mkdir()
        
        # Create old structure
        old_wrknv = mock_home / ".wrknv"
        old_wrknv.mkdir()
        
        # Old container-build directory
        old_build = old_wrknv / "container-build"
        old_build.mkdir()
        (old_build / "Dockerfile").write_text("FROM ubuntu:22.04\nRUN apt-get update")
        (old_build / "requirements.txt").write_text("flask==2.0.0\nrequests==2.28.0")
        
        # Existing cache and tools directories
        (old_wrknv / "cache").mkdir()
        (old_wrknv / "tools").mkdir()
        
        with patch("pathlib.Path.home", return_value=mock_home):
            yield mock_home

    @pytest.fixture
    def container_manager(self, mock_home):
        """Create ContainerManager instance."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(enabled=True),
        )
        return ContainerManager(config)

    def test_detect_old_structure(self, mock_home):
        """Test detection of old container structure."""
        assert migrate_container_storage.needs_migration()
        
        # Check what needs migration
        old_build = mock_home / ".wrknv" / "container-build"
        assert old_build.exists()
        
        # New structure shouldn't exist yet
        new_containers = mock_home / ".wrknv" / "containers"
        assert not new_containers.exists()

    def test_migrate_build_directory(self, container_manager, mock_home):
        """Test migration of old build directory."""
        # Run migration
        result = migrate_container_storage.migrate(container_manager)
        
        assert result is True
        
        # Old directory should be moved/removed
        old_build = mock_home / ".wrknv" / "container-build"
        assert not old_build.exists()
        
        # New directory should exist with content
        new_build = container_manager.get_container_path("build")
        assert new_build.exists()
        assert (new_build / "Dockerfile").exists()
        assert (new_build / "Dockerfile").read_text() == "FROM ubuntu:22.04\nRUN apt-get update"
        assert (new_build / "requirements.txt").exists()

    def test_migrate_preserves_other_directories(self, container_manager, mock_home):
        """Test that migration preserves cache and tools directories."""
        # Add content to cache and tools
        cache_dir = mock_home / ".wrknv" / "cache"
        (cache_dir / "package.tar").write_text("cached")
        
        tools_dir = mock_home / ".wrknv" / "tools"
        (tools_dir / "tool.sh").write_text("#!/bin/bash")
        
        # Run migration
        migrate_container_storage.migrate(container_manager)
        
        # Cache and tools should be untouched
        assert cache_dir.exists()
        assert (cache_dir / "package.tar").read_text() == "cached"
        assert tools_dir.exists()
        assert (tools_dir / "tool.sh").read_text() == "#!/bin/bash"

    def test_migrate_creates_new_structure(self, container_manager, mock_home):
        """Test that migration creates complete new structure."""
        # Run migration
        migrate_container_storage.migrate(container_manager)
        
        # Check new structure
        containers_dir = mock_home / ".wrknv" / "containers"
        assert containers_dir.exists()
        
        # Shared directory
        assert (containers_dir / "shared").exists()
        assert (containers_dir / "shared" / "downloads").exists()
        
        # Container-specific directories
        container_dir = containers_dir / container_manager.CONTAINER_NAME
        assert container_dir.exists()
        assert (container_dir / "volumes").exists()
        assert (container_dir / "volumes" / "workspace").exists()
        assert (container_dir / "volumes" / "cache").exists()
        assert (container_dir / "volumes" / "config").exists()
        assert (container_dir / "logs").exists()
        assert (container_dir / "backups").exists()

    def test_migrate_with_existing_new_structure(self, container_manager, mock_home):
        """Test migration when new structure partially exists."""
        # Create partial new structure
        new_containers = mock_home / ".wrknv" / "containers"
        new_containers.mkdir(parents=True)
        container_dir = new_containers / container_manager.CONTAINER_NAME
        container_dir.mkdir()
        (container_dir / "existing.txt").write_text("keep this")
        
        # Run migration
        result = migrate_container_storage.migrate(container_manager)
        
        assert result is True
        
        # Existing files should be preserved
        assert (container_dir / "existing.txt").read_text() == "keep this"
        
        # Old build content should be migrated
        new_build = container_dir / "build"
        assert new_build.exists()
        assert (new_build / "Dockerfile").exists()

    def test_migrate_handles_no_old_structure(self, mock_home):
        """Test migration when no old structure exists."""
        # Remove old structure
        old_build = mock_home / ".wrknv" / "container-build"
        shutil.rmtree(old_build)
        
        # Should not need migration
        assert not migrate_container_storage.needs_migration()
        
        # Migration should be a no-op
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(enabled=True),
        )
        manager = ContainerManager(config)
        
        result = migrate_container_storage.migrate(manager)
        assert result is True  # Success but no action needed

    def test_migrate_creates_backup(self, container_manager, mock_home):
        """Test that migration creates a backup of old structure."""
        # Run migration with backup
        result = migrate_container_storage.migrate(
            container_manager,
            create_backup=True
        )
        
        assert result is True
        
        # Check for backup
        backup_dir = mock_home / ".wrknv" / "migration-backups"
        assert backup_dir.exists()
        
        # Should have a timestamped backup file
        backups = list(backup_dir.glob("container-build-*.tar.gz"))
        assert len(backups) == 1
        
        # Verify backup contents
        with tarfile.open(backups[0], "r:gz") as tar:
            members = tar.getnames()
            assert "Dockerfile" in members
            assert "requirements.txt" in members

    def test_migrate_rollback_on_error(self, container_manager, mock_home):
        """Test rollback on migration error."""
        # Make migration fail partway through
        with patch.object(
            container_manager,
            "get_container_path",
            side_effect=Exception("Migration failed")
        ):
            result = migrate_container_storage.migrate(container_manager)
        
        assert result is False
        
        # Old structure should still exist
        old_build = mock_home / ".wrknv" / "container-build"
        assert old_build.exists()
        assert (old_build / "Dockerfile").exists()

    def test_migration_status_report(self, container_manager, mock_home, capsys):
        """Test migration status reporting."""
        # Run migration with verbose output
        result = migrate_container_storage.migrate(
            container_manager,
            verbose=True
        )
        
        captured = capsys.readouterr()
        
        assert "Starting container storage migration" in captured.out
        assert "Migrating from old structure" in captured.out
        assert "Creating new directory structure" in captured.out
        assert "Migration completed successfully" in captured.out

    def test_dry_run_migration(self, container_manager, mock_home, capsys):
        """Test dry-run migration mode."""
        # Run migration in dry-run mode
        result = migrate_container_storage.migrate(
            container_manager,
            dry_run=True
        )
        
        assert result is True  # Dry run "succeeds"
        
        # Old structure should still exist
        old_build = mock_home / ".wrknv" / "container-build"
        assert old_build.exists()
        
        # New structure should NOT be created
        new_containers = mock_home / ".wrknv" / "containers"
        assert not new_containers.exists()
        
        captured = capsys.readouterr()
        assert "DRY RUN" in captured.out
        assert "Would migrate" in captured.out


class TestMigrationUtilities:
    """Test migration utility functions."""

    def test_backup_directory(self, tmp_path):
        """Test backing up a directory."""
        # Create test directory
        test_dir = tmp_path / "test"
        test_dir.mkdir()
        (test_dir / "file1.txt").write_text("content1")
        (test_dir / "subdir").mkdir()
        (test_dir / "subdir" / "file2.txt").write_text("content2")
        
        # Backup
        backup_path = migrate_container_storage.backup_directory(
            test_dir,
            tmp_path / "backup.tar.gz"
        )
        
        assert backup_path.exists()
        
        # Verify backup
        with tarfile.open(backup_path, "r:gz") as tar:
            members = tar.getnames()
            assert "file1.txt" in members
            assert "subdir/file2.txt" in members

    def test_copy_directory_contents(self, tmp_path):
        """Test copying directory contents."""
        # Create source
        src = tmp_path / "source"
        src.mkdir()
        (src / "file.txt").write_text("content")
        (src / "subdir").mkdir()
        (src / "subdir" / "nested.txt").write_text("nested")
        
        # Create destination
        dst = tmp_path / "dest"
        dst.mkdir()
        
        # Copy contents
        migrate_container_storage.copy_directory_contents(src, dst)
        
        # Verify
        assert (dst / "file.txt").exists()
        assert (dst / "file.txt").read_text() == "content"
        assert (dst / "subdir" / "nested.txt").exists()
        assert (dst / "subdir" / "nested.txt").read_text() == "nested"

    def test_safe_move_directory(self, tmp_path):
        """Test safe directory moving."""
        # Create source
        src = tmp_path / "source"
        src.mkdir()
        (src / "file.txt").write_text("content")
        
        dst = tmp_path / "dest"
        
        # Safe move
        result = migrate_container_storage.safe_move_directory(src, dst)
        
        assert result is True
        assert not src.exists()
        assert dst.exists()
        assert (dst / "file.txt").read_text() == "content"

    def test_safe_move_with_existing_destination(self, tmp_path):
        """Test safe move when destination exists."""
        # Create source and destination
        src = tmp_path / "source"
        src.mkdir()
        (src / "new.txt").write_text("new")
        
        dst = tmp_path / "dest"
        dst.mkdir()
        (dst / "existing.txt").write_text("existing")
        
        # Safe move should merge
        result = migrate_container_storage.safe_move_directory(
            src, dst,
            merge=True
        )
        
        assert result is True
        assert not src.exists()
        assert (dst / "existing.txt").read_text() == "existing"
        assert (dst / "new.txt").read_text() == "new"