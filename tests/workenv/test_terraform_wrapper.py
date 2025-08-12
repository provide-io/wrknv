"""
Tests for Terraform Wrapper Script
==================================
Tests for the terraform wrapper that delegates to the chosen flavor.
"""

import pytest
import pathlib
import json
import subprocess
import sys
from unittest.mock import patch, Mock


class TestTerraformWrapper:
    """Test terraform wrapper script functionality."""

    def test_wrapper_delegates_to_ibm_terraform_flavor(self, tmp_path):
        """Test wrapper executes ibmtf when flavor is ibm."""
        # GIVEN: A workenv with ibm terraform flavor
        workenv_dir = tmp_path / "workenv" / "test_darwin_arm64"
        bin_dir = workenv_dir / "bin"
        bin_dir.mkdir(parents=True)
        
        # Create fake ibmtf binary
        ibmtf_bin = bin_dir / "ibmtf"
        ibmtf_bin.write_text("#!/bin/sh\necho 'IBM Terraform v1.9.3'\n")
        ibmtf_bin.chmod(0o755)
        
        # Create wrkenv.toml with ibm flavor
        wrkenv_toml = tmp_path / "wrkenv.toml"
        wrkenv_toml.write_text("""
[workenv]
tf_flavor = "ibm"
        """)
        
        # Import the wrapper module
        wrapper_path = pathlib.Path(__file__).parent.parent.parent / "src" / "wrkenv" / "env" / "scripts" / "terraform-wrapper.py"
        
        # Mock the environment
        with patch('sys.argv', ['terraform', 'version']):
            with patch('pathlib.Path.cwd', return_value=tmp_path):
                with patch('pathlib.Path.resolve') as mock_resolve:
                    # Make resolve return the bin_dir for the script location
                    mock_resolve.return_value = bin_dir / "terraform"
                    
                    # Import and test get_tf_flavor
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("wrapper", wrapper_path)
                    wrapper = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(wrapper)
                    
                    with patch.object(wrapper, 'get_workenv_root', return_value=workenv_dir):
                        flavor = wrapper.get_tf_flavor()
                        assert flavor == "ibm"

    def test_wrapper_delegates_to_tofu_flavor(self, tmp_path):
        """Test wrapper executes tofu when flavor is opentofu."""
        # GIVEN: A workenv with opentofu flavor
        workenv_dir = tmp_path / "workenv" / "test_darwin_arm64"
        bin_dir = workenv_dir / "bin"
        bin_dir.mkdir(parents=True)
        
        # Create fake tofu binary
        tofu_bin = bin_dir / "tofu"
        tofu_bin.write_text("#!/bin/sh\necho 'OpenTofu v1.10.5'\n")
        tofu_bin.chmod(0o755)
        
        # Create wrkenv.toml with opentofu flavor
        wrkenv_toml = tmp_path / "wrkenv.toml"
        wrkenv_toml.write_text("""
[workenv]
tf_flavor = "opentofu"
        """)
        
        # Import the wrapper module
        wrapper_path = pathlib.Path(__file__).parent.parent.parent / "src" / "wrkenv" / "env" / "scripts" / "terraform-wrapper.py"
        
        # Mock the environment
        with patch('sys.argv', ['terraform', 'version']):
            with patch('pathlib.Path.cwd', return_value=tmp_path):
                with patch('pathlib.Path.resolve') as mock_resolve:
                    mock_resolve.return_value = bin_dir / "terraform"
                    
                    # Import and test
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("wrapper", wrapper_path)
                    wrapper = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(wrapper)
                    
                    with patch.object(wrapper, 'get_workenv_root', return_value=workenv_dir):
                        flavor = wrapper.get_tf_flavor()
                        assert flavor == "opentofu"

    def test_wrapper_default_flavor_without_config(self, tmp_path):
        """Test wrapper defaults to ibm without config."""
        # GIVEN: No wrkenv.toml exists
        workenv_dir = tmp_path / "workenv" / "test_darwin_arm64" 
        bin_dir = workenv_dir / "bin"
        bin_dir.mkdir(parents=True)
        
        # Import the wrapper module
        wrapper_path = pathlib.Path(__file__).parent.parent.parent / "src" / "wrkenv" / "env" / "scripts" / "terraform-wrapper.py"
        
        # Import and test
        import importlib.util
        spec = importlib.util.spec_from_file_location("wrapper", wrapper_path)
        wrapper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(wrapper)
        
        with patch('pathlib.Path.cwd', return_value=tmp_path):
            with patch.object(wrapper, 'get_workenv_root', return_value=workenv_dir):
                flavor = wrapper.get_tf_flavor()
                assert flavor == "ibm"

# 🍲🥄🧪🪄
