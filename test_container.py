#!/usr/bin/env python3
"""Test container functionality without Docker."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from wrkenv.container import commands
from wrkenv.container.manager import ContainerManager
from wrkenv.env.config import WorkenvConfig

def test_container_imports():
    """Test that container module can be imported."""
    print("✅ Container module imported successfully")
    
    # Test that all commands exist
    commands_to_test = [
        "build_container",
        "start_container",
        "enter_container",
        "stop_container",
        "restart_container",
        "container_status",
        "view_logs",
        "clean_container",
        "rebuild_container",
    ]
    
    for cmd in commands_to_test:
        if hasattr(commands, cmd):
            print(f"✅ Command '{cmd}' exists")
        else:
            print(f"❌ Command '{cmd}' missing")
    
    # Test ContainerManager initialization
    try:
        config = WorkenvConfig()
        manager = ContainerManager(config)
        print("✅ ContainerManager initialized successfully")
        
        # Test that manager has expected methods
        methods = ["build_image", "start", "stop", "restart", "enter", "status", "logs", "clean"]
        for method in methods:
            if hasattr(manager, method):
                print(f"✅ ContainerManager.{method} exists")
            else:
                print(f"❌ ContainerManager.{method} missing")
                
    except Exception as e:
        print(f"❌ ContainerManager initialization failed: {e}")

if __name__ == "__main__":
    test_container_imports()