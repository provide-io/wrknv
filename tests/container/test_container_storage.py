import pytest
#
# tests/container/test_container_storage.py
#
"""
Test Container Storage Management
==================================
Tests for container storage structure under ~/.wrknv
"""

import json
import shutil
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import pytest

from wrknv.container.manager import ContainerManager
from wrknv.wenv.schema import ContainerConfig, WorkenvConfig


@pytest.mark.container
class TestContainerStorageStructure:
    """Test container storage directory structure."""

    @pytest.fixture
    def test_storage_path(self, tmp_path):
        """Create a test storage path."""
        storage_path = tmp_path / "test_wrknv_containers"
        return str(storage_path)

    @pytest.fixture
    def container_manager(self, test_storage_path):
        """Create a ContainerManager instance with test config."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(
                enabled=True,
                storage_path=test_storage_path
            ),
        )
        return ContainerManager(config)

    def test_storage_directory_exists(self, container_manager, test_storage_path):
        """Test that storage directory is created."""
        # The directory should be created during __init__
        storage_dir = Path(test_storage_path)
        assert storage_dir.exists()
        assert storage_dir.is_dir()

    def test_containers_directory_structure(self, container_manager, test_storage_path):
        """Test that containers directory structure is created correctly."""
        storage_dir = Path(test_storage_path)
        
        # Check for shared directory
        shared_dir = storage_dir / "shared"
        assert shared_dir.exists()
        assert (shared_dir / "downloads").exists()

    def test_container_specific_directories(self, container_manager, test_storage_path):
        """Test that container-specific directories are created."""
        container_name = container_manager.CONTAINER_NAME
        storage_dir = Path(test_storage_path)
        
        container_dir = storage_dir / container_name
        assert container_dir.exists()
        
        # Check all required subdirectories
        assert (container_dir / "volumes").exists()
        assert (container_dir / "volumes" / "workspace").exists()
        assert (container_dir / "volumes" / "cache").exists()
        assert (container_dir / "volumes" / "config").exists()
        assert (container_dir / "build").exists()
        assert (container_dir / "logs").exists()
        assert (container_dir / "backups").exists()

    def test_get_container_path(self, container_manager, test_storage_path):
        """Test getting container-specific paths."""
        container_manager._setup_storage()
        
        # Test various path types
        workspace_path = container_manager.get_container_path("volumes/workspace")
        assert workspace_path.exists()
        assert "test-project-dev" in str(workspace_path)
        assert workspace_path.name == "workspace"
        
        build_path = container_manager.get_container_path("build")
        assert build_path.exists()
        assert build_path.name == "build"
        
        # Test root container path
        root_path = container_manager.get_container_path()
        assert root_path.exists()
        assert root_path.name == container_manager.CONTAINER_NAME


@pytest.mark.container
class TestContainerMetadata:
    """Test container metadata management."""

    @pytest.fixture
    def test_storage_path(self, tmp_path):
        """Create a test storage path."""
        storage_path = tmp_path / "test_wrknv_containers"
        return str(storage_path)

    @pytest.fixture
    def container_manager(self, test_storage_path):
        """Create a ContainerManager instance."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(
                enabled=True,
                python_version="3.11",
                additional_packages=["git", "curl"],
                storage_path=test_storage_path
            ),
        )
        manager = ContainerManager(config)
        manager._setup_storage()
        return manager

    def test_save_metadata(self, container_manager, test_storage_path):
        """Test saving container metadata."""
        container_manager.save_metadata()
        
        metadata_file = container_manager.get_container_path("metadata.json")
        assert metadata_file.exists()
        
        with open(metadata_file) as f:
            metadata = json.load(f)
        
        assert "created" in metadata
        assert "config" in metadata
        assert metadata["config"]["python_version"] == "3.11"
        assert "git" in metadata["config"]["additional_packages"]
        assert metadata["image"] == f"{container_manager.IMAGE_NAME}:{container_manager.IMAGE_TAG}"

    def test_load_metadata(self, container_manager, test_storage_path):
        """Test loading container metadata."""
        # Save metadata first
        container_manager.save_metadata()
        
        # Load it back
        metadata = container_manager.load_metadata()
        
        assert metadata is not None
        assert "created" in metadata
        assert "config" in metadata
        assert metadata["config"]["python_version"] == "3.11"

    def test_update_metadata(self, container_manager, test_storage_path):
        """Test updating container metadata."""
        # Save initial metadata
        container_manager.save_metadata()
        
        # Update metadata
        container_manager.update_metadata({"last_started": "2025-08-31T15:00:00"})
        
        # Load and verify
        metadata = container_manager.load_metadata()
        assert metadata["last_started"] == "2025-08-31T15:00:00"
        assert "created" in metadata  # Original field still exists

    def test_metadata_not_found(self, container_manager):
        """Test loading metadata when file doesn't exist."""
        metadata = container_manager.load_metadata()
        assert metadata is None


@pytest.mark.container
class TestVolumeManagement:
    """Test container volume management."""

    @pytest.fixture
    def test_storage_path(self, tmp_path):
        """Create a test storage path."""
        storage_path = tmp_path / "test_wrknv_containers"
        return str(storage_path)

    @pytest.fixture
    def container_manager(self, test_storage_path):
        """Create a ContainerManager instance."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(
                enabled=True,
                storage_path=test_storage_path
            ),
        )
        manager = ContainerManager(config)
        manager._setup_storage()
        return manager

    def test_get_volume_mappings(self, container_manager):
        """Test getting volume mappings for container."""
        mappings = container_manager.get_volume_mappings()
        
        assert "workspace" in mappings
        assert "cache" in mappings
        assert "config" in mappings
        assert "shared_downloads" in mappings
        
        # Check format of mappings
        workspace_mapping = mappings["workspace"]
        assert "/test_wrknv_containers/" in workspace_mapping
        assert ":/workspace" in workspace_mapping
        
        # Shared downloads should be read-only
        assert mappings["shared_downloads"].endswith(":ro")

    def test_custom_volume_mappings(self, test_storage_path):
        """Test custom volume mappings from config."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(
                enabled=True,
                volume_mappings={
                    "data": "/host/data:/container/data",
                    "logs": "/host/logs:/container/logs:ro",
                }
            ),
        )
        manager = ContainerManager(config)
        manager._setup_storage()
        
        mappings = manager.get_volume_mappings()
        
        # Default mappings still exist
        assert "workspace" in mappings
        
        # Custom mappings added
        assert "data" in mappings
        assert mappings["data"] == "/host/data:/container/data"
        assert "logs" in mappings
        assert mappings["logs"] == "/host/logs:/container/logs:ro"

    def test_list_volumes(self, container_manager, test_storage_path):
        """Test listing container volumes."""
        # Create some test files in volumes
        workspace = container_manager.get_container_path("volumes/workspace")
        (workspace / "test.txt").write_text("test")
        
        cache = container_manager.get_container_path("volumes/cache")
        (cache / "packages").mkdir()
        
        volumes = container_manager.list_volumes()
        
        assert len(volumes) > 0
        assert any(v["name"] == "workspace" for v in volumes)
        assert any(v["name"] == "cache" for v in volumes)
        
        # Check volume info
        workspace_vol = next(v for v in volumes if v["name"] == "workspace")
        assert workspace_vol["path"] == str(workspace)
        assert workspace_vol["exists"] is True
        assert workspace_vol["size"] > 0

    def test_backup_volumes(self, container_manager, test_storage_path):
        """Test backing up container volumes."""
        # Create test data
        workspace = container_manager.get_container_path("volumes/workspace")
        (workspace / "project.txt").write_text("project data")
        
        # Backup volumes
        backup_path = container_manager.backup_volumes()
        
        assert backup_path.exists()
        assert backup_path.suffix == ".gz" or backup_path.name.endswith(".tar.gz")
        assert "backup-" in backup_path.name  # Default backup naming
        
        # Check backup location
        backups_dir = Path(test_storage_path) / container_manager.CONTAINER_NAME / "backups"
        assert backups_dir.exists()
        assert backup_path.parent == backups_dir

    def test_restore_volumes(self, container_manager, test_storage_path):
        """Test restoring container volumes from backup."""
        # Create and backup test data
        workspace = container_manager.get_container_path("volumes/workspace")
        test_file = workspace / "original.txt"
        test_file.write_text("original data")
        
        backup_path = container_manager.backup_volumes()
        
        # Modify data
        test_file.write_text("modified data")
        
        # Restore from backup with force=True
        container_manager.restore_volumes(backup_path, force=True)
        
        # Check restoration
        assert test_file.read_text() == "original data"

    def test_clean_volumes(self, container_manager, test_storage_path):
        """Test cleaning container volumes."""
        # Create test data
        workspace = container_manager.get_container_path("volumes/workspace")
        (workspace / "test.txt").write_text("test")
        
        cache = container_manager.get_container_path("volumes/cache")
        (cache / "package.tar").write_text("package")
        
        # Clean volumes
        container_manager.clean_volumes()
        
        # Volumes directory should be empty but exist
        volumes_dir = container_manager.get_container_path("volumes")
        assert volumes_dir.exists()
        assert not (workspace / "test.txt").exists()
        assert not (cache / "package.tar").exists()

    def test_clean_volumes_with_preserve(self, container_manager, test_storage_path):
        """Test cleaning volumes with preservation of specific volumes."""
        # Create test data
        workspace = container_manager.get_container_path("volumes/workspace")
        (workspace / "important.txt").write_text("keep this")
        
        cache = container_manager.get_container_path("volumes/cache")
        (cache / "temp.txt").write_text("delete this")
        
        # Clean volumes but preserve workspace
        container_manager.clean_volumes(preserve=["workspace"])
        
        # Workspace preserved, cache cleaned
        assert (workspace / "important.txt").exists()
        assert not (cache / "temp.txt").exists()



@pytest.mark.container
class TestDockerIntegration:
    """Test Docker integration with new storage structure."""

    @pytest.fixture
    def test_storage_path(self, tmp_path):
        """Create a test storage path."""
        storage_path = tmp_path / "test_wrknv_containers"
        return str(storage_path)

    @pytest.fixture
    def container_manager(self, test_storage_path):
        """Create a ContainerManager instance."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(
                enabled=True,
                storage_path=test_storage_path
            ),
        )
        manager = ContainerManager(config)
        manager._setup_storage()
        return manager

    @patch("provide.foundation.process.run_command")
    def test_build_uses_new_path(self, mock_run, container_manager, test_storage_path):
        """Test that Docker build uses new build directory."""
        mock_run.return_value = Mock(returncode=0)
        
        container_manager.build_image()
        
        # Check that docker build was called with correct path
        build_path = container_manager.get_container_path("build")
        mock_run.assert_called()
        
        call_args = mock_run.call_args[0][0]
        assert "docker" in call_args[0]
        assert "build" in call_args[1]
        assert str(build_path) in call_args

    @patch("provide.foundation.process.run_command")
    def test_start_mounts_persistent_volumes(self, mock_run, container_manager, test_storage_path):
        """Test that Docker start mounts persistent volumes."""
        mock_run.return_value = Mock(returncode=0)
        
        # Mock container state checks
        container_manager.check_docker = Mock(return_value=True)
        container_manager.image_exists = Mock(return_value=True)
        container_manager.container_running = Mock(return_value=False)
        container_manager.container_exists = Mock(return_value=False)
        
        container_manager.start()
        
        # Check that docker run was called with volume mounts
        call_args = mock_run.call_args[0][0]
        
        # Check for workspace volume
        workspace_path = container_manager.get_container_path("volumes/workspace")
        workspace_mount = f"{workspace_path}:/workspace"
        assert any(workspace_mount in arg for arg in call_args)
        
        # Check for cache volume
        cache_path = container_manager.get_container_path("volumes/cache")
        cache_mount_prefix = str(cache_path)
        assert any(cache_mount_prefix in arg for arg in call_args)
        
        # Check for shared downloads (read-only)
        shared_path = Path(test_storage_path) / "shared" / "downloads"
        shared_mount = f"{shared_path}:/downloads:ro"
        assert any(shared_mount in arg for arg in call_args)

    @patch("provide.foundation.process.run_command")
    def test_clean_preserves_volumes_optionally(self, mock_run, container_manager):
        """Test that clean can optionally preserve volumes."""
        mock_run.return_value = Mock(returncode=0)
        
        # Create test volumes
        workspace = container_manager.get_container_path("volumes/workspace")
        (workspace / "data.txt").write_text("important")
        
        # Mock container state
        container_manager.container_running = Mock(return_value=False)
        container_manager.container_exists = Mock(return_value=True)
        container_manager.image_exists = Mock(return_value=True)
        
        # Clean without preserving volumes
        container_manager.clean(preserve_volumes=False)
        assert not (workspace / "data.txt").exists()
        
        # Recreate data
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / "data.txt").write_text("important")
        
        # Clean with preserving volumes
        container_manager.clean(preserve_volumes=True)
        assert (workspace / "data.txt").exists()


@pytest.mark.container
class TestContainerStorageConfig:
    """Test container storage configuration."""

    def test_default_storage_path(self):
        """Test default storage path configuration."""
        config = ContainerConfig()
        assert config.storage_path == "~/.wrknv/containers"

    def test_custom_storage_path(self):
        """Test custom storage path configuration."""
        config = ContainerConfig(storage_path="/custom/path/containers")
        assert config.storage_path == "/custom/path/containers"

    def test_persistent_volumes_config(self):
        """Test persistent volumes configuration."""
        config = ContainerConfig(
            persistent_volumes=["workspace", "cache", "config", "data"]
        )
        assert "workspace" in config.persistent_volumes
        assert "data" in config.persistent_volumes
        assert len(config.persistent_volumes) == 4

    def test_volume_mappings_config(self):
        """Test volume mappings configuration."""
        config = ContainerConfig(
            volume_mappings={
                "project": "/host/project:/container/project",
                "readonly": "/host/data:/container/data:ro",
            }
        )
        assert config.volume_mappings["project"] == "/host/project:/container/project"
        assert config.volume_mappings["readonly"] == "/host/data:/container/data:ro"


# Integration test placeholder
@pytest.mark.integration
@pytest.mark.container
class TestContainerStorageIntegration:
    """Integration tests for container storage (requires Docker)."""

    @pytest.mark.skipif(
        not shutil.which("docker"),
        reason="Docker not available"
    )
    def test_full_container_lifecycle_with_volumes(self):
        """Test full container lifecycle with persistent volumes."""
        # This would be a full integration test
        # Requires Docker to be installed and running
        pass