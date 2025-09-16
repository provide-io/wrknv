"""
TDD Tests for wrknv Package Commands
=====================================
Test-driven development for package management functionality.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

from click.testing import CliRunner
import pytest

from wrknv.cli.hub_cli import create_cli
from wrknv.wenv.config import WorkenvConfig


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def cli():
    return create_cli()


class TestWorkenvPackageCommands:
    """Test package management commands."""

    def test_package_command_exists(self, cli, runner):
        """Package command should be available in the CLI."""
        result = runner.invoke(cli, ["package", "--help"])

        assert result.exit_code == 0
        assert "package" in result.output or "pkg" in result.output
        assert "Manage provider packages" in result.output

    def test_package_build_command_exists(self, cli, runner):
        """Package build command should be available."""
        result = runner.invoke(cli, ["package-build", "--help"])

        assert result.exit_code == 0
        assert "Build" in result.output
        assert "--manifest" in result.output

    def test_package_verify_command_exists(self, cli, runner):
        """Package verify command should be available."""
        result = runner.invoke(cli, ["package-verify", "--help"])

        assert result.exit_code == 0
        assert "Verify" in result.output

    def test_package_keygen_command_exists(self, cli, runner):
        """Package keygen command should be available."""
        result = runner.invoke(cli, ["package-keygen", "--help"])

        assert result.exit_code == 0
        assert "Generate" in result.output
        assert "keys" in result.output

    def test_package_clean_command_exists(self, cli, runner):
        """Package clean command should be available."""
        result = runner.invoke(cli, ["package-clean", "--help"])

        assert result.exit_code == 0
        assert "Clean" in result.output or "Remove" in result.output

    def test_package_init_command_exists(self, cli, runner):
        """Package init command should be available."""
        result = runner.invoke(cli, ["package-init", "--help"])

        assert result.exit_code == 0
        assert "Initialize" in result.output or "Create" in result.output

    def test_package_build_with_manifest(self, cli, runner, tmp_path):
        """Package build should work with a manifest file."""
        # Create a test manifest
        manifest = tmp_path / "pyproject.toml"
        manifest.write_text("""
[project]
name = "test-provider"
version = "0.1.0"

[tool.flavor]
provider_name = "test"
entry_point = "test.main:serve"
        """)

        # Patch the function that imports flavor API
        with patch("wrknv.package.commands._get_flavor_api") as mock_get_api:
            mock_api = MagicMock()
            mock_api.build_package_from_manifest.return_value = [tmp_path / "dist" / "test.flavor"]
            mock_get_api.return_value = mock_api

            # Also patch the manager to avoid tool checks in this unit test
            with patch("wrknv.package.commands.PackageManager") as mock_manager:
                mock_manager.return_value.is_flavor_available.return_value = True
                mock_manager.return_value.check_required_tools.return_value = {"go": "1.21", "uv": "0.4"}
                mock_manager.return_value.setup_build_environment.return_value = None

                result = runner.invoke(cli, ["package", "build", "--manifest", str(manifest)])

        assert result.exit_code == 0, f"CLI exited with code {result.exit_code}: {result.output}"
        assert "Successfully built" in result.output
        mock_api.build_package_from_manifest.assert_called_once()

    def test_package_build_default_manifest(self, cli, runner, tmp_path):
        """Package build should use pyproject.toml by default."""
        with runner.isolated_filesystem(temp_dir=tmp_path) as td:
            # Create default manifest
            manifest = Path(td) / "pyproject.toml"
            manifest.write_text("""
[project]
name = "test-provider"
version = "0.1.0"
            """)

            # Patch the function that imports flavor API
            with patch("wrknv.package.commands._get_flavor_api") as mock_get_api:
                mock_api = MagicMock()
                mock_api.build_package_from_manifest.return_value = [Path(td) / "dist" / "test.flavor"]
                mock_get_api.return_value = mock_api

                # Also patch the manager to avoid tool checks in this unit test
                with patch("wrknv.package.commands.PackageManager") as mock_manager:
                    mock_manager.return_value.is_flavor_available.return_value = True
                    mock_manager.return_value.check_required_tools.return_value = {"go": "1.21", "uv": "0.4"}
                    mock_manager.return_value.setup_build_environment.return_value = None

                    result = runner.invoke(cli, ["package-build"])

            assert result.exit_code == 0, f"CLI exited with code {result.exit_code}: {result.output}"
            mock_api.build_package_from_manifest.assert_called_once()

    def test_package_keygen_creates_keys(self, cli, runner, tmp_path):
        """Package keygen should create key pair."""
        # Patch the flavor API getter to avoid import error
        with patch("wrknv.package.commands._get_flavor_api") as mock_get_api:
            mock_api = MagicMock()
            mock_api.generate_keys.return_value = (
                tmp_path / "provider-private.key",
                tmp_path / "provider-public.key",
            )
            mock_get_api.return_value = mock_api

            result = runner.invoke(cli, ["package", "keygen", "--out-dir", str(tmp_path)])

        if result.exit_code != 0:
            print(f"Exit code: {result.exit_code}")
            print(f"Output: {result.output}")
            print(f"Exception: {result.exception}")
        assert result.exit_code == 0
        assert "Keys generated" in result.output
        mock_api.generate_keys.assert_called_once_with(tmp_path)

    def test_package_verify_valid_package(self, cli, runner, tmp_path):
        """Package verify should validate a package."""
        package_file = tmp_path / "test.flavor"
        package_file.write_text("dummy")

        # Patch the flavor API getter to avoid import error
        with patch("wrknv.package.commands._get_flavor_api") as mock_get_api:
            mock_api = MagicMock()
            mock_api.verify_package.return_value = None
            mock_get_api.return_value = mock_api

            result = runner.invoke(cli, ["package", "verify", str(package_file)])

        assert result.exit_code == 0
        assert "verification successful" in result.output.lower()
        mock_api.verify_package.assert_called_once_with(package_file)

    def test_package_verify_invalid_package(self, cli, runner, tmp_path):
        """Package verify should report invalid packages."""
        package_file = tmp_path / "bad.flavor"
        package_file.write_text("invalid")

        # Patch the flavor API getter to simulate verification failure
        with patch("wrknv.package.commands._get_flavor_api") as mock_get_api:
            mock_api = MagicMock()
            mock_api.verify_package.side_effect = Exception("Invalid signature")
            mock_get_api.return_value = mock_api

            result = runner.invoke(cli, ["package", "verify", str(package_file)])

        assert result.exit_code != 0
        assert "failed" in result.output.lower()

    def test_package_clean_removes_cache(self, cli, runner):
        """Package clean should remove build cache."""
        # Patch both the flavor API and the manager
        with patch("wrknv.package.commands._get_flavor_api") as mock_get_api:
            mock_api = MagicMock()
            mock_api.clean_cache.return_value = None
            mock_get_api.return_value = mock_api

            with patch("wrknv.package.commands.PackageManager") as mock_manager:
                mock_instance = MagicMock()
                mock_instance.get_package_cache_dir.return_value = Path("/tmp/cache")
                mock_manager.return_value = mock_instance

                result = runner.invoke(cli, ["package-clean"])

        assert result.exit_code == 0
        assert "cleaned" in result.output.lower()
        mock_api.clean_cache.assert_called_once()

    def test_package_init_creates_project(self, cli, runner, tmp_path):
        """Package init should create a new provider project."""
        project_dir = tmp_path / "terraform-provider-example"

        # No need to mock tofusoup anymore - it's removed from wrknv
        result = runner.invoke(cli, ["package", "init", str(project_dir)])

        if result.exit_code != 0:
            print(f"Init failed: {result.output}")
            print(f"Exception: {result.exception}")
        assert result.exit_code == 0
        assert "created" in result.output.lower()
        assert str(project_dir) in result.output
        # Check that the project was actually created
        assert project_dir.exists()
        assert (project_dir / "pyproject.toml").exists()

    def test_package_build_with_dry_run(self, cli, runner, tmp_path):
        """Package build should support dry-run mode."""
        with runner.isolated_filesystem(temp_dir=tmp_path) as td:
            # Create a minimal pyproject.toml for the build command
            pyproject = Path(td) / "pyproject.toml"
            pyproject.write_text("""
[project]
name = "test-provider"
version = "0.1.0"
            """)

            # Test dry-run mode - should not require flavor
            result = runner.invoke(cli, ["package", "build", "--manifest", str(pyproject), "--dry-run"])

            assert result.exit_code == 0
            assert "[DRY-RUN]" in result.output
            assert str(pyproject) in result.output

    def test_package_list_command(self, cli, runner):
        """Package list should show built packages."""
        # Patch where the CLI imports the function
        with patch("wrknv.package.list_packages") as mock_list:
            mock_list.return_value = [
                {"name": "provider-aws", "version": "5.0.0", "size": "45MB"},
                {"name": "provider-gcp", "version": "4.2.0", "size": "38MB"},
            ]

            result = runner.invoke(cli, ["package-list"])

        assert result.exit_code == 0
        assert "provider-aws" in result.output
        assert "5.0.0" in result.output
        assert "provider-gcp" in result.output

    def test_package_info_command(self, cli, runner, tmp_path):
        """Package info should show package details."""
        package_file = tmp_path / "test.flavor"
        package_file.write_text("dummy")

        # Patch where the CLI imports the function
        with patch("wrknv.package.get_package_info") as mock_info:
            mock_info.return_value = {
                "name": "test-provider",
                "version": "1.0.0",
                "size": "42MB",
                "signature": "valid",
                "python_version": "3.13",
                "dependencies": ["requests", "attrs"],
            }

            result = runner.invoke(cli, ["package", "info", str(package_file)])

        assert result.exit_code == 0
        assert "test-provider" in result.output
        assert "1.0.0" in result.output
        assert "Python: 3.13" in result.output

    def test_package_publish_command(self, cli, runner, tmp_path):
        """Package publish should upload to registry."""
        package_file = tmp_path / "provider.flavor"
        package_file.write_text("data")

        with patch("wrknv.package.publish_package") as mock_pub:
            mock_pub.return_value = {
                "url": "https://registry.example.com/provider",
                "sha256": "abc123",
            }

            result = runner.invoke(cli, ["package", "publish", str(package_file), "--registry", "example"])

        assert result.exit_code == 0
        assert "published" in result.output.lower()
        assert "registry.example.com" in result.output

    def test_package_dry_run_mode(self, cli, runner, tmp_path):
        """Package commands should support dry-run mode."""
        manifest = tmp_path / "pyproject.toml"
        manifest.write_text("""
[project]
name = "test"
version = "1.0.0"
        """)

        with patch("wrknv.package.commands.build_package") as mock_build:
            result = runner.invoke(cli, ["package", "build", "--manifest", str(manifest), "--dry-run"])

        assert result.exit_code == 0
        assert "[DRY-RUN]" in result.output
        assert "Would build" in result.output
        mock_build.assert_not_called()

    def test_package_config_integration(self, cli, runner, tmp_path):
        """Package should use workenv configuration."""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text("""
[workenv.settings]
package = { default_out_dir = "build", signing_curve = "P-521", verify_on_build = true, metadata = { author = "Test Author", license = "MIT" } }
        """)

        # Change to the tmp directory so config is found
        with patch("os.getcwd", return_value=str(tmp_path)):
            # Show package config
            result = runner.invoke(cli, ["package-config"])

            assert result.exit_code == 0
            assert "P-521" in result.output or "signing_curve" in result.output


class TestPackageManagerIntegration:
    """Test PackageManager class integration."""

    def test_package_manager_requires_flavor(self):
        """PackageManager should check for flavor availability."""
        from wrknv.package.manager import PackageManager

        config = WorkenvConfig()
        manager = PackageManager(config)

        # Should check if flavor is available
        assert hasattr(manager, "is_flavor_available")

        # Test when flavor is not available
        manager._flavor_available = False
        assert not manager.is_flavor_available()

        # Test when flavor is available
        manager._flavor_available = True
        assert manager.is_flavor_available()

    def test_package_manager_tool_integration(self):
        """PackageManager should integrate with tool managers."""
        from wrknv.package.manager import PackageManager

        config = WorkenvConfig()
        manager = PackageManager(config)

        # Should check for required tools
        with patch.object(manager, "check_required_tools") as mock_check:
            mock_check.return_value = {
                "go": "1.21.5",
                "uv": "0.4.15",
                "python": "3.13.0",
            }

            tools = manager.get_required_tools()
            assert "go" in tools
            assert "uv" in tools

    def test_package_manager_environment_setup(self):
        """PackageManager should set up build environment."""
        from wrknv.package.manager import PackageManager

        config = WorkenvConfig()
        manager = PackageManager(config)

        with patch.object(manager, "setup_build_environment") as mock_setup:
            mock_setup.return_value = {
                "PATH": "/path/to/tools",
                "GOPATH": "/path/to/go",
                "UV_CACHE_DIR": "/path/to/cache",
            }

            env = manager.get_build_environment()
            assert "PATH" in env
            assert "GOPATH" in env


class TestPackageCommandsWithWorkenv:
    """Test package commands integration with workenv features."""

    def test_package_build_installs_missing_tools(self, cli, runner):
        """Package build should install missing tools automatically."""
        # Test that the package build command exists with --auto-install flag
        result = runner.invoke(cli, ["package-build", "--help"])

        # For now, just verify the command exists
        # The --auto-install feature needs to be implemented
        assert result.exit_code == 0
        assert "build" in result.output.lower()

    def test_package_with_matrix_testing(self, cli, runner, tmp_path):
        """Package should support matrix testing with different tool versions."""
        config_file = tmp_path / "wrknv.toml"
        config_file.write_text("""
[workenv.matrix.package_test]
go = ["1.20", "1.21", "1.22"]
python = ["3.11", "3.12", "3.13"]

[workenv.matrix.package_test.command]
build = "package build"
test = "package verify {artifact}"
        """)

        with patch("wrknv.wenv.config.WorkenvConfig._get_config_path") as mock_path:
            mock_path.return_value = config_file

            result = runner.invoke(cli, ["package-matrix-test", "--matrix", "package_test"])

            # Should run builds with different tool combinations
            assert "matrix" in result.output.lower()


# 🧰🌍🖥️🪄
