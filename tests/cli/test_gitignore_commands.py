import pytest
from click.testing import CliRunner
from pathlib import Path
import shutil

from wrkenv.wenv.cli import workenv_cli

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def gitignore_templates_dir(tmp_path):
    """Fixture to create dummy gitignore template files directly in tmp_path."""
    (tmp_path / "Python.gitignore").write_text("# Python ignores\n*.pyc\n__pycache__/")
    (tmp_path / "Node.gitignore").write_text("# Node ignores\nnode_modules/\nnpm-debug.log")
    (tmp_path / "Global.gitignore").write_text("# Global ignores\n.DS_Store\n.env")
    (tmp_path / "NonExistent.gitignore").write_text("# This file should not be used") # For negative test cases
    return tmp_path


class TestGitignoreCommands:
    def test_gitignore_build_from_config(self, runner, tmp_path, gitignore_templates_dir, monkeypatch):
        """Test building .gitignore from wrkenv.toml config."""
        # Create a dummy wrkenv.toml in the temporary directory
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "Node"]
templates_path = "{gitignore_templates_dir}"
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)
        monkeypatch.setenv("WRKENV_CONFIG_PATH", str(tmp_path / "wrkenv.toml"))

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build"], catch_exceptions=False)

            assert result.exit_code == 0
            assert "✅ .gitignore built successfully" in result.output

            gitignore_file = tmp_path / ".gitignore"
            assert gitignore_file.exists()

            content = gitignore_file.read_text()
            assert "# --- Python ---" in content
            assert "*.pyc" in content
            assert "__pycache__/" in content
            assert "# --- Node ---" in content
            assert "node_modules/" in content
            assert "npm-debug.log" in content
            assert ".DS_Store" not in content # Should not include Global.gitignore

    def test_gitignore_build_with_templates_option(self, runner, tmp_path, gitignore_templates_dir, monkeypatch):
        """Test building .gitignore using --templates option (should override config)."""
        # Create a dummy wrkenv.toml (with different templates)
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "Node"]
templates_path = "{gitignore_templates_dir}"
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)
        monkeypatch.setenv("WRKENV_CONFIG_PATH", str(tmp_path / "wrkenv.toml"))

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build", "--templates", "Global", "--templates", "Python"], catch_exceptions=False)

            assert result.exit_code == 0
            assert "✅ .gitignore built successfully" in result.output

            gitignore_file = tmp_path / ".gitignore"
            assert gitignore_file.exists()

            content = gitignore_file.read_text()
            assert "# --- Global ---" in content
            assert ".DS_Store" in content
            assert ".env" in content
            assert "# --- Python ---" in content
            assert "*.pyc" in content
            assert "node_modules/" not in content # Should not include Node.gitignore

            assert result.exit_code == 0
            assert "✅ .gitignore built successfully" in result.output

            gitignore_file = tmp_path / ".gitignore"
            assert gitignore_file.exists()

            content = gitignore_file.read_text()
            assert "# --- Global ---" in content
            assert ".DS_Store" in content
            assert ".env" in content
            assert "# --- Python ---" in content
            assert "*.pyc" in content
            assert "node_modules/" not in content # Should not include Node.gitignore

    def test_gitignore_build_no_templates_specified(self, runner, tmp_path, monkeypatch):
        """Test building .gitignore when no templates are specified in config or via option."""
        # Create a dummy wrkenv.toml without gitignore section
        config_content = f"""
project_name = "test-project"
version = "0.1.0"
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)
        monkeypatch.setenv("WRKENV_CONFIG_PATH", str(tmp_path / "wrkenv.toml"))

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build"], catch_exceptions=False)

            assert result.exit_code == 0
            assert "No gitignore templates specified in config or via --templates." in result.output
            assert not (tmp_path / ".gitignore").exists()

            assert result.exit_code == 0
            assert "No gitignore templates specified in config or via --templates." in result.output
            assert not (tmp_path / ".gitignore").exists()

    def test_gitignore_build_with_non_existent_template(self, runner, tmp_path, gitignore_templates_dir, monkeypatch):
        """Test building .gitignore with a non-existent template."""
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "NonExistent"]
templates_path = "{gitignore_templates_dir}"
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)
        monkeypatch.setenv("WRKENV_CONFIG_PATH", str(tmp_path / "wrkenv.toml"))

        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build"], catch_exceptions=False)

            assert result.exit_code == 0
            assert "Warning: Gitignore template 'NonExistent' not found" in result.stderr
            assert "✅ .gitignore built successfully" in result.output

            gitignore_file = tmp_path / ".gitignore"
            assert gitignore_file.exists()
            content = gitignore_file.read_text()
            assert "# --- Python ---" in content
            assert "# --- NonExistent ---" not in content # Should not include header for non-existent

            assert result.exit_code == 0
            assert "Warning: Gitignore template 'NonExistent' not found" in result.stderr
            assert "✅ .gitignore built successfully" in result.output

            gitignore_file = tmp_path / ".gitignore"
            assert gitignore_file.exists()
            content = gitignore_file.read_text()
            assert "# --- Python ---" in content
            assert "# --- NonExistent ---" not in content # Should not include header for non-existent

    def test_gitignore_build_with_output_option(self, runner, tmp_path, gitignore_templates_dir, monkeypatch):
        """Test building .gitignore to a custom output path."""
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python"]
templates_path = "{gitignore_templates_dir}"
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)
        monkeypatch.setenv("WRKENV_CONFIG_PATH", str(tmp_path / "wrkenv.toml"))

        custom_output_path = tmp_path / "my_custom.ignore"

        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build", "--output", str(custom_output_path)], catch_exceptions=False)

            assert result.exit_code == 0
            assert f"✅ .gitignore built successfully at {custom_output_path}" in result.output

            assert custom_output_path.exists()
            content = custom_output_path.read_text()
            assert "# --- Python ---" in content
            assert "*.pyc" in content
            assert not (tmp_path / ".gitignore").exists() # Default file should not be created

