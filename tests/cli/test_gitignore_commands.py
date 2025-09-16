from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner
import pytest

from wrknv.cli.hub_cli import create_cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def gitignore_templates_dir(tmp_path):
    """Fixture to provide a path for dummy gitignore template files."""
    return tmp_path


class TestGitignoreCommands:
    def test_gitignore_build_from_config(self, runner, tmp_path, gitignore_templates_dir):
        """Test building .gitignore from wrknv.toml config."""
        # Create a dummy wrknv.toml in the temporary directory
        config_path = tmp_path / "wrknv.toml"
        config_content_template = """
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "Node"]
templates_path = "{templates_path_actual}"
"""

        # Create a pre-configured WorkenvConfig instance
        from wrknv.wenv.config import WorkenvConfig

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path) as isolated_path_str:
            isolated_path = Path(isolated_path_str)
            # Create dummy template files inside the isolated path
            (isolated_path / "Python.gitignore").write_text("# Python ignores\n*.pyc\n__pycache__/")
            (isolated_path / "Node.gitignore").write_text("# Node ignores\nnode_modules/\nnpm-debug.log")
            (isolated_path / "Global.gitignore").write_text("# Global ignores\n.DS_Store\n.env")
            (isolated_path / "NonExistent.gitignore").write_text(
                "# This file should not be used"
            )  # For negative test cases

            # Write config content with the actual isolated path
            config_content = config_content_template.format(templates_path_actual=isolated_path)
            config_path.write_text(config_content)

            mock_config_instance = WorkenvConfig(config_file=config_path)

            # Patch WorkenvConfig in cli.py to return our pre-configured instance
            with patch("wrknv.cli.commands.gitignore.WorkenvConfig", return_value=mock_config_instance):
                cli = create_cli()
                result = runner.invoke(cli, ["gitignore-build"], catch_exceptions=False)

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
                assert ".DS_Store" not in content  # Should not include Global.gitignore

    def test_gitignore_build_with_templates_option(self, runner, tmp_path, gitignore_templates_dir):
        """Test building .gitignore using --templates option (should override config)."""
        # Create a dummy wrknv.toml (with different templates)
        config_path = tmp_path / "wrknv.toml"
        config_content_template = """
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "Node"]
templates_path = "{templates_path_actual}"
"""
        # Create a pre-configured WorkenvConfig instance
        from wrknv.wenv.config import WorkenvConfig

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path) as isolated_path_str:
            isolated_path = Path(isolated_path_str)
            # Create dummy template files inside the isolated path
            (isolated_path / "Python.gitignore").write_text("# Python ignores\n*.pyc\n__pycache__/")
            (isolated_path / "Node.gitignore").write_text("# Node ignores\nnode_modules/\nnpm-debug.log")
            (isolated_path / "Global.gitignore").write_text("# Global ignores\n.DS_Store\n.env")
            (isolated_path / "NonExistent.gitignore").write_text(
                "# This file should not be used"
            )  # For negative test cases

            # Write config content with the actual isolated path
            config_content = config_content_template.format(templates_path_actual=isolated_path)
            config_path.write_text(config_content)

            mock_config_instance = WorkenvConfig(config_file=config_path)

            # Patch WorkenvConfig in cli.py to return our pre-configured instance
            with patch("wrknv.cli.commands.gitignore.WorkenvConfig", return_value=mock_config_instance):
                cli = create_cli()
                result = runner.invoke(
                    cli,
                    ["gitignore-build", "--templates", "Global", "--templates", "Python"],
                    catch_exceptions=False,
                )

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
                assert "node_modules/" not in content  # Should not include Node.gitignore

    def test_gitignore_build_no_templates_specified(self, runner, tmp_path):
        """Test building .gitignore when no templates are specified in config or via option."""
        # Create a dummy wrknv.toml without gitignore section
        config_path = tmp_path / "wrknv.toml"
        config_content = """
project_name = "test-project"
version = "0.1.0"
"""
        config_path.write_text(config_content)

        # Create a pre-configured WorkenvConfig instance
        from wrknv.wenv.config import WorkenvConfig

        mock_config_instance = WorkenvConfig(config_file=config_path)

        # Patch WorkenvConfig in cli.py to return our pre-configured instance
        with patch("wrknv.cli.commands.gitignore.WorkenvConfig", return_value=mock_config_instance):
            # Change current working directory to tmp_path for the test
            with runner.isolated_filesystem(tmp_path):
                cli = create_cli()
                result = runner.invoke(cli, ["gitignore-build"], catch_exceptions=False)

                assert result.exit_code == 0
                assert "No gitignore templates specified in config or via --templates." in result.output
                assert not (tmp_path / ".gitignore").exists()

    def test_gitignore_build_with_non_existent_template(
        self, runner, tmp_path, gitignore_templates_dir, capsys
    ):
        """Test building .gitignore with a non-existent template."""
        config_path = tmp_path / "wrknv.toml"
        config_content_template = """
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python", "NonExistent"]
templates_path = "{templates_path_actual}"
"""
        # Create a pre-configured WorkenvConfig instance
        from wrknv.wenv.config import WorkenvConfig

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path) as isolated_path_str:
            isolated_path = Path(isolated_path_str)
            # Create dummy template files inside the isolated path
            (isolated_path / "Python.gitignore").write_text("# Python ignores\n*.pyc\n__pycache__/")
            (isolated_path / "Node.gitignore").write_text("# Node ignores\nnode_modules/\nnpm-debug.log")
            (isolated_path / "Global.gitignore").write_text("# Global ignores\n.DS_Store\n.env")
            (isolated_path / "NonExistent.gitignore").write_text(
                "# This file should not be used"
            )  # For negative test cases

            # Write config content with the actual isolated path
            config_content = config_content_template.format(templates_path_actual=isolated_path)
            config_path.write_text(config_content)

            mock_config_instance = WorkenvConfig(config_file=config_path)

            # Patch WorkenvConfig in cli.py to return our pre-configured instance
            with patch("wrknv.cli.commands.gitignore.WorkenvConfig", return_value=mock_config_instance):
                cli = create_cli()
                result = runner.invoke(cli, ["gitignore-build"], catch_exceptions=False)

                assert result.exit_code == 0
                out, err = capsys.readouterr()
                assert "Warning: Gitignore template 'NonExistent' not found" in err
                assert "✅ .gitignore built successfully" in out

                gitignore_file = tmp_path / ".gitignore"
                assert gitignore_file.exists()
                content = gitignore_file.read_text()
                assert "# --- Python ---" in content
                assert "# --- NonExistent ---" not in content  # Should not include header for non-existent

    def test_gitignore_build_with_output_option(self, runner, tmp_path, gitignore_templates_dir, capsys):
        """Test building .gitignore to a custom output path."""
        config_path = tmp_path / "wrknv.toml"
        config_content_template = """
project_name = "test-project"
version = "0.1.0"

[gitignore]
templates = ["Python"]
templates_path = "{templates_path_actual}"
"""
        # Create a pre-configured WorkenvConfig instance
        from wrknv.wenv.config import WorkenvConfig

        # Change current working directory to tmp_path for the test
        with runner.isolated_filesystem(tmp_path) as isolated_path_str:
            isolated_path = Path(isolated_path_str)
            # Create dummy template files inside the isolated path
            (isolated_path / "Python.gitignore").write_text("# Python ignores\n*.pyc\n__pycache__/")
            (isolated_path / "Node.gitignore").write_text("# Node ignores\nnode_modules/\nnpm-debug.log")
            (isolated_path / "Global.gitignore").write_text("# Global ignores\n.DS_Store\n.env")
            (isolated_path / "NonExistent.gitignore").write_text(
                "# This file should not be used"
            )  # For negative test cases

            # Write config content with the actual isolated path
            config_content = config_content_template.format(templates_path_actual=isolated_path)
            config_path.write_text(config_content)

            mock_config_instance = WorkenvConfig(config_file=config_path)

            # Patch WorkenvConfig in cli.py to return our pre-configured instance
            with patch("wrknv.cli.commands.gitignore.WorkenvConfig", return_value=mock_config_instance):
                custom_output_path = tmp_path / "my_custom.ignore"

                cli = create_cli()
                result = runner.invoke(
                    cli, ["gitignore", "build", "--output", str(custom_output_path)], catch_exceptions=False
                )

                assert result.exit_code == 0
                assert f"✅ .gitignore built successfully at {custom_output_path}" in result.output

                assert custom_output_path.exists()
                content = custom_output_path.read_text()
                assert "# --- Python ---" in content
                assert "*.pyc" in content
                assert not (tmp_path / ".gitignore").exists()  # Default file should not be created
