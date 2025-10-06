from __future__ import annotations

import pytest

#!/usr/bin/env python3
"""
Debug container volume mounting
"""

import sys
import time
from pathlib import Path

from provide.foundation.process import run_command

sys.path.insert(0, "src")

from wrknv.container.manager import ContainerManager
from wrknv.wenv.schema import ContainerConfig, WorkenvConfig


@pytest.mark.container
def test_volume_debug():
    """Debug volume mounting issues."""
    # Use a path that Docker Desktop can access (not /tmp which may be virtualized)
    storage_path = Path.home() / ".wrknv_debug_test"
    storage_path.mkdir(exist_ok=True)

    config = WorkenvConfig(
        project_name="debug-test",
        container=ContainerConfig(
            enabled=True,
            storage_path=str(storage_path),
            python_version="3.11",
            base_image="python:3.11-slim",
        ),
    )

    manager = ContainerManager(config)
    # Storage is now automatically set up in __attrs_post_init__

    # Check paths
    print(f"Storage path: {storage_path}")
    print(f"Container name: {manager.container_name}")

    workspace_path = manager.get_container_path("volumes/workspace")
    print(f"Workspace path: {workspace_path}")
    print(f"Workspace exists: {workspace_path.exists()}")

    # Build and start container
    if not manager.build_image():
        print("Failed to build image")
        return False

    if not manager.start():
        print("Failed to start container")
        return False

    time.sleep(2)

    # Check container is running
    result = run_command(
        ["docker", "ps", "--filter", f"name={manager.container_name}"], capture_output=True, text=True
    )
    print(f"Container status:\n{result.stdout}")

    # Check volume mounts
    result = run_command(
        ["docker", "inspect", manager.container_name, "--format", "{{json .Mounts}}"],
        capture_output=True,
        text=True,
    )
    print(f"Volume mounts:\n{result.stdout}")

    # Try to write a file
    test_file = "test_debug.txt"
    cmd = [
        "docker",
        "exec",
        manager.container_name,
        "sh",
        "-c",
        f"echo 'Debug test' > /workspace/{test_file} && ls -la /workspace/",
    ]

    result = run_command(cmd, capture_output=True, text=True)
    print(f"Write command result: {result.returncode}")
    print(f"Stdout: {result.stdout}")
    print(f"Stderr: {result.stderr}")

    # Check if file exists on host
    host_file = workspace_path / test_file
    print(f"Host file path: {host_file}")
    print(f"Host file exists: {host_file.exists()}")

    if host_file.exists():
        print(f"Host file content: {host_file.read_text()}")

    # List workspace directory on host
    if workspace_path.exists():
        files = list(workspace_path.iterdir())
        print(f"Files in workspace: {files}")

    # Cleanup
    run_command(["docker", "stop", manager.container_name], capture_output=True)
    run_command(["docker", "rm", manager.container_name], capture_output=True)

    return host_file.exists()


if __name__ == "__main__":
    success = test_volume_debug()
    print(f"\nTest {'PASSED' if success else 'FAILED'}")
    sys.exit(0 if success else 1)
