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
    """Fixture to create a dummy gitignore templates directory."""
    # Create a dummy gitignore directory structure
    # This mimics the /Users/tim/code/gh/provide-io/gitignore/ structure
    # but within a temporary path for testing isolation.
    
    # Create the base directory for templates
    base_templates_dir = tmp_path / "gitignore_templates"
    base_templates_dir.mkdir()

    # Create some dummy template files
    (base_templates_dir / "Python.gitignore").write_text("# Python ignores\n*.pyc\n__pycache__/")
    (base_templates_dir / "Node.gitignore").write_text("# Node ignores\nnode_modules/\nnpm-debug.log")
    (base_templates_dir / "Global.gitignore").write_text("# Global ignores\n.DS_Store\n.env")
    (base_templates_dir / "NonExistent.gitignore").write_text("# This file should not be used") # For negative test cases

    return base_templates_dir

@pytest.fixture
def mock_provide_io_root(monkeypatch, gitignore_templates_dir):
    """
    Mocks the root of the provide-io monorepo to point to our temporary
    gitignore templates directory.
    """
    # This is a bit of a hack, but necessary because the cli.py hardcodes
    # the path to /Users/tim/code/gh/provide-io/gitignore
    # In a real scenario, this path should probably be configurable or
    # relative to the wrkenv project root.
    monkeypatch.setattr(
        "wrkenv.wenv.cli.pathlib.Path",
        lambda path: gitignore_templates_dir if path == "/Users/tim/code/gh/provide-io/gitignore" else Path(path)
    )
    # Also mock the Path.cwd() for config loading
    monkeypatch.setattr(
        "wrkenv.wenv.config.Path.cwd",
        lambda: gitignore_templates_dir # Use the temp dir as CWD for config loading
    )
    monkeypatch.setattr(
        "wrkenv.wenv.cli.Path.cwd",
        lambda: gitignore_templates_dir # Use the temp dir as CWD for cli operations
    )


class TestGitignoreCommands:
    def test_gitignore_build_from_config(self, runner, tmp_path, gitignore_templates_dir, mock_provide_io_root):
        """Test building .gitignore from wrkenv.toml config."""
        # Create a dummy wrkenv.toml in the temporary directory
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "Node"]
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build"])

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

    def test_gitignore_build_with_templates_option(self, runner, tmp_path, gitignore_templates_dir, mock_provide_io_root):
        """Test building .gitignore using --templates option (should override config)."""
        # Create a dummy wrkenv.toml (with different templates)
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "Node"]
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build", "--templates", "Global", "--templates", "Python"])

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

    def test_gitignore_build_no_templates_specified(self, runner, tmp_path, mock_provide_io_root):
        """Test building .gitignore when no templates are specified in config or via option."""
        # Create a dummy wrkenv.toml without gitignore section
        config_content = f"""
project_name = "test-project"
version = "0.1.0"
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build"])

            assert result.exit_code == 0
            assert "No gitignore templates specified in config or via --templates." in result.output
            assert not (tmp_path / ".gitignore").exists()

    def test_gitignore_build_with_non_existent_template(self, runner, tmp_path, gitignore_templates_dir, mock_provide_io_root):
        """Test building .gitignore with a non-existent template."""
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "NonExistent"]
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)

        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build"])

            assert result.exit_code == 0
            assert "Warning: Gitignore template 'NonExistent' not found" in result.output
            assert "✅ .gitignore built successfully" in result.output

            gitignore_file = tmp_path / ".gitignore"
            assert gitignore_file.exists()
            content = gitignore_file.read_text()
            assert "# --- Python ---" in content
            assert "# --- NonExistent ---" not in content # Should not include header for non-existent

    def test_gitignore_build_with_output_option(self, runner, tmp_path, gitignore_templates_dir, mock_provide_io_root):
        """Test building .gitignore to a custom output path."""
        config_content = f"""
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python"]
"""
        (tmp_path / "wrkenv.toml").write_text(config_content)

        custom_output_path = tmp_path / "my_custom.ignore"

        with runner.isolated_filesystem(tmp_path):
            result = runner.invoke(workenv_cli, ["gitignore", "build", "--output", str(custom_output_path)])

            assert result.exit_code == 0
            assert f"✅ .gitignore built successfully at {custom_output_path}" in result.output

            assert custom_output_path.exists()
            content = custom_output_path.read_text()
            assert "# --- Python ---" in content
            assert "*.pyc" in content
            assert not (tmp_path / ".gitignore").exists() # Default file should not be created

