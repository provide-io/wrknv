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

    def test_wrapper_delegates_to_terraform_flavor(self, tmp_path):
        """Test wrapper executes hctf when flavor is terraform."""
        # GIVEN: A workenv with terraform flavor
        workenv_dir = tmp_path / "workenv" / "test_darwin_arm64"
        bin_dir = workenv_dir / "bin"
        bin_dir.mkdir(parents=True)
        
        # Create fake hctf binary
        hctf_bin = bin_dir / "hctf"
        hctf_bin.write_text("#!/bin/sh\necho 'Terraform v1.9.3'\n")
        hctf_bin.chmod(0o755)
        
        # Create soup.toml with terraform flavor
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
terraform_flavor = "terraform"
        """)
        
        # Import the wrapper module
        wrapper_path = pathlib.Path(__file__).parent.parent.parent / "src" / "tofusoup" / "workenv" / "scripts" / "terraform-wrapper.py"
        
        # Mock the environment
        with patch('sys.argv', ['terraform', 'version']):
            with patch('pathlib.Path.cwd', return_value=tmp_path):
                with patch('pathlib.Path.resolve') as mock_resolve:
                    # Make resolve return the bin_dir for the script location
                    mock_resolve.return_value = bin_dir / "terraform"
                    
                    # Import and test get_terraform_flavor
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("wrapper", wrapper_path)
                    wrapper = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(wrapper)
                    
                    with patch.object(wrapper, 'get_workenv_root', return_value=workenv_dir):
                        flavor = wrapper.get_terraform_flavor()
                        assert flavor == "terraform"

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
        
        # Create soup.toml with opentofu flavor
        soup_toml = tmp_path / "soup.toml"
        soup_toml.write_text("""
[workenv]
terraform_flavor = "opentofu"
        """)
        
        # Import the wrapper module
        wrapper_path = pathlib.Path(__file__).parent.parent.parent / "src" / "tofusoup" / "workenv" / "scripts" / "terraform-wrapper.py"
        
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
                        flavor = wrapper.get_terraform_flavor()
                        assert flavor == "opentofu"

    def test_wrapper_default_flavor_without_config(self, tmp_path):
        """Test wrapper defaults to terraform without config."""
        # GIVEN: No soup.toml exists
        workenv_dir = tmp_path / "workenv" / "test_darwin_arm64" 
        bin_dir = workenv_dir / "bin"
        bin_dir.mkdir(parents=True)
        
        # Import the wrapper module
        wrapper_path = pathlib.Path(__file__).parent.parent.parent / "src" / "tofusoup" / "workenv" / "scripts" / "terraform-wrapper.py"
        
        # Import and test
        import importlib.util
        spec = importlib.util.spec_from_file_location("wrapper", wrapper_path)
        wrapper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(wrapper)
        
        with patch('pathlib.Path.cwd', return_value=tmp_path):
            with patch.object(wrapper, 'get_workenv_root', return_value=workenv_dir):
                flavor = wrapper.get_terraform_flavor()
                assert flavor == "terraform"

# 🍲🥄🧪🪄
