"""Tests for Python version mismatch detection and venv recreation."""

import sys
from pathlib import Path
from unittest.mock import Mock, patch, call
import pytest
import tempfile
import subprocess
import json


class TestPythonVersionCheck:
    """Test Python version checking in virtual environments."""

    def test_detect_python_version_from_venv(self, tmp_path):
        """Test detecting Python version from existing venv."""
        from wrkenv.env.python_version import get_venv_python_version
        
        # Create a mock venv structure
        venv_dir = tmp_path / "workenv" / "test_darwin_arm64"
        venv_dir.mkdir(parents=True)
        python_bin = venv_dir / "bin" / "python"
        python_bin.parent.mkdir(exist_ok=True)
        
        # Mock subprocess.run to return version info
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(
                stdout='{"version": "3.12.1", "major": 3, "minor": 12, "micro": 1}',
                returncode=0
            )
            
            version_info = get_venv_python_version(venv_dir)
            
            assert version_info == {
                "version": "3.12.1",
                "major": 3,
                "minor": 12,
                "micro": 1
            }
            
            # Verify the command was called correctly
            mock_run.assert_called_once_with(
                [str(python_bin), "-c", 
                 "import sys, json; print(json.dumps({'version': '.'.join(map(str, sys.version_info[:3])), 'major': sys.version_info.major, 'minor': sys.version_info.minor, 'micro': sys.version_info.micro}))"],
                capture_output=True,
                text=True,
                check=False
            )

    def test_detect_python_version_no_venv(self, tmp_path):
        """Test detecting Python version when venv doesn't exist."""
        from wrkenv.env.python_version import get_venv_python_version
        
        venv_dir = tmp_path / "nonexistent"
        version_info = get_venv_python_version(venv_dir)
        
        assert version_info is None

    def test_get_project_python_requirement(self, tmp_path):
        """Test extracting Python version requirement from pyproject.toml."""
        from wrkenv.env.python_version import get_project_python_requirement
        
        pyproject = tmp_path / "pyproject.toml"
        pyproject.write_text("""
[project]
name = "test-project"
requires-python = ">=3.11"
""")
        
        with patch('os.getcwd', return_value=str(tmp_path)):
            requirement = get_project_python_requirement()
            
        assert requirement == ">=3.11"

    def test_get_project_python_requirement_no_file(self):
        """Test when pyproject.toml doesn't exist."""
        from wrkenv.env.python_version import get_project_python_requirement
        
        with patch('os.getcwd', return_value='/nonexistent'):
            requirement = get_project_python_requirement()
            
        assert requirement is None

    def test_check_python_version_compatibility(self):
        """Test checking if Python version meets requirement."""
        from wrkenv.env.python_version import check_python_version_compatibility
        
        # Test various compatibility scenarios
        assert check_python_version_compatibility("3.11.5", ">=3.11") == True
        assert check_python_version_compatibility("3.12.0", ">=3.11") == True
        assert check_python_version_compatibility("3.10.0", ">=3.11") == False
        assert check_python_version_compatibility("3.11.0", ">=3.11,<3.12") == True
        assert check_python_version_compatibility("3.12.0", ">=3.11,<3.12") == False
        assert check_python_version_compatibility("3.11.5", "~=3.11.0") == True
        assert check_python_version_compatibility("3.12.0", "~=3.11.0") == False

    def test_should_recreate_venv(self, tmp_path):
        """Test logic for determining if venv should be recreated."""
        from wrkenv.env.python_version import should_recreate_venv
        
        # Case 1: No existing venv
        result = should_recreate_venv(
            venv_dir=tmp_path / "nonexistent",
            project_requirement=">=3.11"
        )
        assert result == (False, None)  # No venv to recreate
        
        # Case 2: Existing venv with compatible version
        with patch('wrkenv.env.python_version.get_venv_python_version') as mock_get_version:
            mock_get_version.return_value = {
                "version": "3.11.5",
                "major": 3,
                "minor": 11,
                "micro": 5
            }
            
            result = should_recreate_venv(
                venv_dir=tmp_path / "venv",
                project_requirement=">=3.11"
            )
            assert result == (False, None)
        
        # Case 3: Existing venv with incompatible version
        with patch('wrkenv.env.python_version.get_venv_python_version') as mock_get_version:
            mock_get_version.return_value = {
                "version": "3.10.5",
                "major": 3,
                "minor": 10,
                "micro": 5
            }
            
            result = should_recreate_venv(
                venv_dir=tmp_path / "venv",
                project_requirement=">=3.11"
            )
            assert result == (True, "Virtual environment has Python 3.10.5 but project requires >=3.11")

    def test_env_generator_with_python_version_check(self, tmp_path):
        """Test that env_generator includes Python version checking."""
        from wrkenv.env.env_generator import generate_env_scripts
        
        # Create a mock pyproject.toml
        pyproject = tmp_path / "pyproject.toml"
        pyproject.write_text("""
[project]
name = "test-project"
requires-python = ">=3.11"
""")
        
        # Create wrkenv.toml
        wrkenv_toml = tmp_path / "wrkenv.toml"
        wrkenv_toml.write_text("""
[workenv]
tf_flavor = "opentofu"
""")
        
        with patch('os.getcwd', return_value=str(tmp_path)):
            generate_env_scripts()
        
        # Check that env.sh was created
        env_sh = tmp_path / "env.sh"
        assert env_sh.exists()
        
        # Read the generated script
        content = env_sh.read_text()
        
        # Should contain Python version checking logic
        assert "# Check Python version compatibility" in content
        assert "requires-python" in content or ">=3.11" in content
        assert "recreate" in content.lower() or "version mismatch" in content.lower()

    def test_template_includes_version_check(self):
        """Test that the shell template includes version checking."""
        from wrkenv.env.env_generator import EnvGenerator
        
        generator = EnvGenerator()
        
        # Mock the config
        config = {
            "project_name": "test-project",
            "python_requirement": ">=3.11",
            "venv_dir": "workenv/test_darwin_arm64",
            "use_spinner": True,
        }
        
        # Generate just the version check part
        with patch.object(generator, '_get_template') as mock_get_template:
            mock_template = Mock()
            mock_get_template.return_value = mock_template
            
            generator._generate_shell_script("sh", config, Path("/tmp/test.sh"))
            
            # Verify template was called with python_requirement
            assert mock_template.render.called
            call_args = mock_template.render.call_args[1]
            assert "python_requirement" in call_args
            assert call_args["python_requirement"] == ">=3.11"

    def test_venv_recreation_in_generated_script(self, tmp_path):
        """Test that generated script can recreate venv on version mismatch."""
        from wrkenv.env.env_generator import generate_env_scripts
        
        # Create project with Python requirement
        pyproject = tmp_path / "pyproject.toml"
        pyproject.write_text("""
[project]
name = "test-project"
requires-python = ">=3.12"
""")
        
        # Create existing venv marker file
        venv_dir = tmp_path / "workenv" / "test-project_darwin_arm64"
        venv_dir.mkdir(parents=True)
        (venv_dir / ".python-version").write_text("3.11.0")
        
        with patch('os.getcwd', return_value=str(tmp_path)):
            with patch('platform.system', return_value='Darwin'):
                with patch('platform.machine', return_value='arm64'):
                    generate_env_scripts()
        
        env_sh = tmp_path / "env.sh"
        content = env_sh.read_text()
        
        # Should have logic to:
        # 1. Check existing Python version
        # 2. Compare with requirement
        # 3. Recreate if needed
        assert ".python-version" in content
        assert "rm -rf" in content  # For removing old venv
        assert "Python version mismatch" in content or "recreating virtual environment" in content.lower()