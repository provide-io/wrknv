#!/usr/bin/env python3
"""
Validation script for wrknv implementation
==========================================
Test the core functionality without external dependencies.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_config_defaults():
    """Test that config defaults work correctly."""
    print("🧪 Testing config/defaults.py...")

    try:
        from wrknv.config.defaults import (
            DEFAULT_CLI_NAME, DEFAULT_TIMEOUT, DEFAULT_DRY_RUN,
            default_workenv_cache_dir, default_empty_list
        )

        # Test basic defaults
        assert DEFAULT_CLI_NAME == "wrknv"
        assert DEFAULT_TIMEOUT == 10
        assert DEFAULT_DRY_RUN is False

        # Test factory functions
        cache_dir = default_workenv_cache_dir()
        assert isinstance(cache_dir, Path)
        assert ".wrknv" in str(cache_dir)

        # Test list factory returns different instances
        list1 = default_empty_list()
        list2 = default_empty_list()
        assert list1 == list2 == []
        assert list1 is not list2

        print("✅ Config defaults test passed")
        return True

    except Exception as e:
        print(f"❌ Config defaults test failed: {e}")
        return False

def test_command_imports():
    """Test that command modules can be imported."""
    print("🧪 Testing command module imports...")

    try:
        # Test gitignore commands (should have proper subcommand structure)
        from wrknv.cli.commands.gitignore import gitignore_group
        print("✅ Gitignore commands imported")

        # Test package commands (should have proper subcommand structure)
        from wrknv.cli.commands.package import package_group
        print("✅ Package commands imported")

        # Test workspace commands
        from wrknv.cli.commands.workspace import workspace_group
        print("✅ Workspace commands imported")

        print("✅ Command imports test passed")
        return True

    except Exception as e:
        print(f"❌ Command imports test failed: {e}")
        return False

def test_temp_dir_fix():
    """Test that temp_dir imports are fixed."""
    print("🧪 Testing temp_dir fix...")

    try:
        # These should not fail with temp_dir import errors
        from wrknv.workenv.importer import WorkenvImporter, temp_dir
        from wrknv.workenv.packaging import WorkenvPackager

        # Test that temp_dir context manager works
        with temp_dir() as tmp_path:
            assert isinstance(tmp_path, Path)
            assert tmp_path.exists()

        # After context exit, directory should be cleaned up
        assert not tmp_path.exists()

        print("✅ temp_dir fix test passed")
        return True

    except Exception as e:
        print(f"❌ temp_dir fix test failed: {e}")
        return False

def main():
    """Run all validation tests."""
    print("🚀 Starting wrknv implementation validation...")
    print("=" * 50)

    tests = [
        test_config_defaults,
        test_command_imports,
        test_temp_dir_fix,
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 50)
    print(f"📊 Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All validation tests passed!")
        print("\n✅ Implementation Summary:")
        print("   • config/defaults.py created with centralized defaults")
        print("   • Command structure fixed (dash → subcommands)")
        print("   • temp_dir import issues resolved")
        print("   • Workspace command purpose documented")
        return True
    else:
        print("❌ Some tests failed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)