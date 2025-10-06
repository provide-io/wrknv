from __future__ import annotations

#
# tests/container/test_container_integration.py
#
"""
Container Integration Tests
===========================
Integration tests that actually run containers and verify file system interactions.
These tests require Docker to be installed and running.
"""

import json
from pathlib import Path
import shutil
import time

import pytest
from provide.foundation.process import run_command
from provide.testkit import FoundationTestCase

from wrknv.container.manager import ContainerManager
from wrknv.wenv.schema import ContainerConfig, WorkenvConfig


def docker_available():
    """Check if Docker is available."""
    return shutil.which("docker") is not None


@pytest.mark.integration
@pytest.mark.skipif(not docker_available(), reason="Docker not available")
@pytest.mark.container
class TestContainerVolumeIntegration(FoundationTestCase):
    """Test actual container volume interactions with the host filesystem."""

    @pytest.fixture
    def test_project_dir(self, tmp_path):
        """Create a temporary project directory."""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()
        return project_dir

    @pytest.fixture
    def test_config(self) -> None:
        """Create test configuration with custom storage path."""
        # Use home directory for Docker Desktop compatibility
        storage_path = Path.home() / ".wrknv_test_containers"
        storage_path.mkdir(exist_ok=True)
        return WorkenvConfig(
            project_name="integration-test",
            container=ContainerConfig(
                enabled=True,
                storage_path=str(storage_path),
                python_version="3.11",
                base_image="python:3.11-slim",
            ),
        )

    @pytest.fixture
    def container_manager(self, test_config):
        """Create a real ContainerManager instance."""
        manager = ContainerManager(test_config)
        # Storage is now automatically set up in __attrs_post_init__
        yield manager
        # Cleanup: stop and remove container
        try:
            run_command(["docker", "stop", manager.CONTAINER_NAME], capture_output=True, timeout=10)
            run_command(["docker", "rm", manager.CONTAINER_NAME], capture_output=True, timeout=10)
        except:
            pass

    def test_shared_storage_write_from_container(self, container_manager):
        """Test writing to shared storage from within a container."""
        # Ensure container is built
        assert container_manager.build_image(), "Failed to build container image"

        # Start container
        assert container_manager.start(), "Failed to start container"

        # Give container time to start
        time.sleep(2)

        # Write a file to shared downloads from within the container
        test_content = "Hello from container!"
        test_file = "test_from_container.txt"

        # Execute command in container to write to shared downloads
        # Note: shared downloads is mounted as read-only, so we'll use workspace
        cmd = [
            "docker",
            "exec",
            container_manager.CONTAINER_NAME,
            "sh",
            "-c",
            f"echo '{test_content}' > /workspace/{test_file}",
        ]

        result = run_command(cmd, capture_output=True, text=True)
        assert result.returncode == 0, f"Failed to write file in container: {result.stderr}"

        # Verify file exists on host
        workspace_path = container_manager.get_container_path("volumes/workspace")
        host_file = workspace_path / test_file

        assert host_file.exists(), "File not found on host filesystem"
        assert host_file.read_text().strip() == test_content, "File content mismatch"

    def test_volume_persistence_across_restarts(self, container_manager):
        """Test that volume data persists across container restarts."""
        # Build and start container
        assert container_manager.build_image()
        assert container_manager.start()

        time.sleep(2)

        # Write data to volumes
        test_data = {"test": "persistence", "timestamp": time.time()}

        # Write to workspace volume
        cmd = [
            "docker",
            "exec",
            container_manager.CONTAINER_NAME,
            "sh",
            "-c",
            f"echo '{json.dumps(test_data)}' > /workspace/persistent.json",
        ]
        result = run_command(cmd, capture_output=True)
        assert result.returncode == 0

        # Write to cache volume
        cmd = [
            "docker",
            "exec",
            container_manager.CONTAINER_NAME,
            "sh",
            "-c",
            "echo 'cached data' > /home/user/.cache/data.txt",
        ]
        result = run_command(cmd, capture_output=True)
        assert result.returncode == 0

        # Stop container
        assert container_manager.stop()

        # Verify data still exists on host
        workspace_file = container_manager.get_container_path("volumes/workspace/persistent.json")
        cache_file = container_manager.get_container_path("volumes/cache/data.txt")

        assert workspace_file.exists()
        assert cache_file.exists()

        # Restart container
        assert container_manager.start()
        time.sleep(2)

        # Read data from restarted container
        cmd = ["docker", "exec", container_manager.CONTAINER_NAME, "cat", "/workspace/persistent.json"]
        result = run_command(cmd, capture_output=True, text=True)
        assert result.returncode == 0

        # Verify data matches
        retrieved_data = json.loads(result.stdout)
        assert retrieved_data == test_data

    def test_shared_downloads_readonly(self, container_manager):
        """Test that shared downloads is mounted as read-only."""
        # Build and start container
        assert container_manager.build_image()
        assert container_manager.start()

        time.sleep(2)

        # Create a file in shared downloads on host
        shared_downloads = Path(container_manager.config.container.storage_path).expanduser()
        shared_downloads = shared_downloads / "shared" / "downloads"
        shared_downloads.mkdir(parents=True, exist_ok=True)

        test_file = shared_downloads / "readonly_test.txt"
        test_file.write_text("This is read-only")

        # Try to read the file from container (should work)
        cmd = ["docker", "exec", container_manager.CONTAINER_NAME, "cat", "/downloads/readonly_test.txt"]
        result = run_command(cmd, capture_output=True, text=True)
        assert result.returncode == 0
        assert "This is read-only" in result.stdout

        # Try to write to shared downloads from container (should fail)
        cmd = [
            "docker",
            "exec",
            container_manager.CONTAINER_NAME,
            "sh",
            "-c",
            "echo 'trying to write' > /downloads/should_fail.txt",
        ]
        result = run_command(cmd, capture_output=True, text=True)
        assert result.returncode != 0, "Should not be able to write to read-only mount"
        assert "Read-only file system" in result.stderr or "Permission denied" in result.stderr

    def test_volume_backup_restore_with_real_data(self, container_manager):
        """Test backup and restore with actual container data."""
        # Build and start container
        assert container_manager.build_image()
        assert container_manager.start()

        time.sleep(2)

        # Create various files in different volumes
        files_to_create = [
            ("/workspace/project.py", "print('Hello World')"),
            ("/workspace/data/config.json", '{"setting": "value"}'),
            ("/home/user/.cache/package.tar.gz", "binary data here"),
            ("/home/user/.config/settings.ini", "[section]\nkey=value"),
        ]

        for filepath, content in files_to_create:
            # Create directories if needed
            dir_path = str(Path(filepath).parent)
            if dir_path != "/":
                mkdir_cmd = ["docker", "exec", container_manager.CONTAINER_NAME, "mkdir", "-p", dir_path]
                run_command(mkdir_cmd, capture_output=True)

            # Create file
            cmd = [
                "docker",
                "exec",
                container_manager.CONTAINER_NAME,
                "sh",
                "-c",
                f"echo '{content}' > {filepath}",
            ]
            result = run_command(cmd, capture_output=True)
            assert result.returncode == 0, f"Failed to create {filepath}"

        # Stop container for backup
        assert container_manager.stop()

        # Create backup
        backup_path = container_manager.backup_volumes()
        assert backup_path.exists()
        assert backup_path.stat().st_size > 0

        # Clear volumes
        container_manager.clean_volumes()

        # Verify files are gone
        workspace_file = container_manager.get_container_path("volumes/workspace/project.py")
        assert not workspace_file.exists()

        # Restore from backup
        assert container_manager.restore_volumes(backup_path, force=True)

        # Verify files are restored
        assert workspace_file.exists()
        assert workspace_file.read_text().strip() == "print('Hello World')"

        # Start container and verify from inside
        assert container_manager.start()
        time.sleep(2)

        cmd = ["docker", "exec", container_manager.CONTAINER_NAME, "python", "/workspace/project.py"]
        result = run_command(cmd, capture_output=True, text=True)
        assert result.returncode == 0
        assert "Hello World" in result.stdout

    def test_multiple_containers_shared_downloads(self) -> None:
        """Test that multiple containers can share the downloads directory."""
        # Use home directory for Docker Desktop compatibility
        storage_path = Path.home() / ".wrknv_test_multi_containers"
        storage_path.mkdir(exist_ok=True)

        # Create two container configurations
        config1 = WorkenvConfig(
            project_name="project-one",
            container=ContainerConfig(
                enabled=True,
                storage_path=str(storage_path),
                python_version="3.11",
                base_image="python:3.11-slim",
            ),
        )

        config2 = WorkenvConfig(
            project_name="project-two",
            container=ContainerConfig(
                enabled=True,
                storage_path=str(storage_path),
                python_version="3.11",
                base_image="python:3.11-slim",
            ),
        )

        manager1 = ContainerManager(config1)
        manager2 = ContainerManager(config2)

        try:
            # Storage is now automatically set up in __attrs_post_init__
            # Create a file in shared downloads
            shared_downloads = storage_path / "shared" / "downloads"
            shared_file = shared_downloads / "shared_resource.txt"
            shared_file.write_text("Shared between containers")

            # Build and start both containers
            assert manager1.build_image()
            assert manager2.build_image()

            assert manager1.start()
            assert manager2.start()

            time.sleep(2)

            # Verify both containers can read the shared file
            for manager in [manager1, manager2]:
                cmd = ["docker", "exec", manager.CONTAINER_NAME, "cat", "/downloads/shared_resource.txt"]
                result = run_command(cmd, capture_output=True, text=True)
                assert result.returncode == 0
                assert "Shared between containers" in result.stdout

            # Verify containers have separate workspace volumes
            cmd1 = [
                "docker",
                "exec",
                manager1.CONTAINER_NAME,
                "sh",
                "-c",
                "echo 'project1 data' > /workspace/project1.txt",
            ]
            run_command(cmd1, capture_output=True)

            cmd2 = [
                "docker",
                "exec",
                manager2.CONTAINER_NAME,
                "sh",
                "-c",
                "echo 'project2 data' > /workspace/project2.txt",
            ]
            run_command(cmd2, capture_output=True)

            # Verify isolation - project1 file should not exist in project2
            cmd = ["docker", "exec", manager2.CONTAINER_NAME, "ls", "/workspace/project1.txt"]
            result = run_command(cmd, capture_output=True)
            assert result.returncode != 0, "Workspaces should be isolated"

        finally:
            # Cleanup
            for manager in [manager1, manager2]:
                try:
                    run_command(["docker", "stop", manager.CONTAINER_NAME], capture_output=True, timeout=10)
                    run_command(["docker", "rm", manager.CONTAINER_NAME], capture_output=True, timeout=10)
                except:
                    pass

    def test_metadata_persistence(self, container_manager):
        """Test that container metadata is saved and persisted correctly."""
        # Build container
        assert container_manager.build_image()

        # Metadata should be saved after build
        metadata = container_manager.load_metadata()
        assert metadata is not None
        assert "created" in metadata
        assert metadata["config"]["python_version"] == "3.11"

        # Start container
        assert container_manager.start()
        time.sleep(2)

        # Update metadata with runtime info
        container_manager.update_metadata({"last_started": time.time()})

        # Create a new manager instance and verify metadata persists
        new_manager = ContainerManager(container_manager.config)
        loaded_metadata = new_manager.load_metadata()

        assert loaded_metadata is not None
        assert "last_started" in loaded_metadata
        assert loaded_metadata["config"]["python_version"] == "3.11"

    def test_volume_permissions(self, container_manager):
        """Test that volume permissions allow container to read/write properly."""
        # Build and start container
        assert container_manager.build_image()
        assert container_manager.start()

        time.sleep(2)

        # Test writing as the container user
        volumes_to_test = ["/workspace", "/home/user/.cache", "/home/user/.config"]

        for volume in volumes_to_test:
            test_file = f"{volume}/permission_test.txt"
            cmd = [
                "docker",
                "exec",
                container_manager.CONTAINER_NAME,
                "sh",
                "-c",
                f"echo 'test' > {test_file} && echo 'success'",
            ]
            result = run_command(cmd, capture_output=True, text=True)
            assert result.returncode == 0, f"Failed to write to {volume}: {result.stderr}"
            assert "success" in result.stdout

    def test_large_file_handling(self, container_manager):
        """Test handling of large files in volumes."""
        # Build and start container
        assert container_manager.build_image()
        assert container_manager.start()

        time.sleep(2)

        # Create a 10MB file in workspace
        cmd = [
            "docker",
            "exec",
            container_manager.CONTAINER_NAME,
            "dd",
            "if=/dev/zero",
            "of=/workspace/large_file.bin",
            "bs=1M",
            "count=10",
        ]
        result = run_command(cmd, capture_output=True)
        assert result.returncode == 0

        # Verify file exists on host
        large_file = container_manager.get_container_path("volumes/workspace/large_file.bin")
        assert large_file.exists()
        assert large_file.stat().st_size == 10 * 1024 * 1024  # 10MB

        # Test backup with large file
        backup_path = container_manager.backup_volumes()
        assert backup_path.exists()
        assert backup_path.stat().st_size > 0  # Should be compressed

        # Clean and restore
        container_manager.clean_volumes()
        assert not large_file.exists()

        assert container_manager.restore_volumes(backup_path, force=True)
        assert large_file.exists()
        assert large_file.stat().st_size == 10 * 1024 * 1024
