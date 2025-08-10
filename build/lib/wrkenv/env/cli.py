#!/usr/bin/env python3
#
# wrkenv/env/cli.py
#
"""
wrkenv CLI Commands
===================
Command-line interface for wrkenv tool management.
"""

import pathlib
import sys

import click

from wrkenv.env.config import WorkenvConfig
from wrkenv.env.managers.factory import get_tool_manager
from wrkenv.env.visual import (
    Emoji,
    get_console,
    get_tool_emoji,
    print_error,
    print_info,
    print_success,
    print_warning,
)


@click.group(name="workenv", invoke_without_command=True)
@click.pass_context
def workenv_cli(ctx):
    """🧰🌍 Manage development environment tools and versions.

    wrkenv provides cross-platform tool installation and version management
    for development environments, including Terraform, OpenTofu, Go, UV, and more.
    """
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


# === Setup Commands ===


@workenv_cli.command(name="setup")
@click.option("--shell-integration", is_flag=True, help="Set up shell aliases")
@click.option("--init", is_flag=True, help="Initialize wrkenv's own workenv")
@click.option("--force", is_flag=True, help="Force recreate workenv")
def setup_command(shell_integration: bool, init: bool, force: bool):
    """Set up wrkenv environment and integrations."""
    import subprocess
    from pathlib import Path

    from wrkenv.env.workenv import WorkenvManager

    if init:
        # Set up wrkenv's own workenv
        print_info("Setting up wrkenv workenv...", Emoji.CONFIG)
        WorkenvManager.setup_workenv(force=force)
        return

    if shell_integration:
        # Look for script in the repository root
        script_path = (
            Path(__file__).parent.parent.parent.parent
            / "scripts"
            / "shell-integration.sh"
        )
        if script_path.exists():
            print_info("Setting up shell integration...", Emoji.CONFIG)
            try:
                subprocess.run(["bash", str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print_error("Failed to set up shell integration")
                sys.exit(1)
        else:
            print_error(f"Shell integration script not found at {script_path}")
            sys.exit(1)
    else:
        print_info("Available setup options:")
        print_info("  --init                Create wrkenv's own workenv")
        print_info("  --shell-integration   Set up shell aliases and shortcuts")


# === Direct Tool Commands ===


@workenv_cli.command(name="tf")
@click.argument("version", required=False)
@click.option("--latest", is_flag=True, help="Install latest version")
@click.option("--list", is_flag=True, help="List available versions")
@click.option("--dry-run", is_flag=True, help="Show what would be installed")
def tf_command(version: str | None, latest: bool, list: bool, dry_run: bool):
    """Install or manage OpenTofu versions."""
    config = WorkenvConfig()

    if list:
        # List available versions
        try:
            manager = get_tool_manager("tofu", config)
            print_info("Available OpenTofu versions:", Emoji.OPENTOFU)
            manager.list_versions()
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    elif latest:
        # Install latest version
        try:
            manager = get_tool_manager("tofu", config)
            manager.install_latest(dry_run=dry_run)
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    elif version:
        # Install specific version
        try:
            manager = get_tool_manager("tofu", config)
            if dry_run:
                print_info(f"[DRY-RUN] Would install OpenTofu {version}")
            else:
                print_info(
                    f"Installing OpenTofu {version}...",
                    f"{Emoji.OPENTOFU} {Emoji.DOWNLOAD}",
                )
            manager.install_version(version, dry_run=dry_run)
            if not dry_run:
                print_success(f"Successfully installed OpenTofu {version}")
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    else:
        print_warning("Please specify a version, --latest, or --list")
        sys.exit(1)


@workenv_cli.command(name="terraform")
@click.argument("version")
@click.option("--dry-run", is_flag=True, help="Show what would be installed")
def terraform_command(version: str, dry_run: bool):
    """Install specific Terraform version."""
    config = WorkenvConfig()

    try:
        manager = get_tool_manager("terraform", config)
        if dry_run:
            click.echo(f"[DRY-RUN] Would install Terraform {version}")
        else:
            click.echo(f"Installing Terraform {version}...")
        manager.install_version(version, dry_run=dry_run)
        if not dry_run:
            click.echo(f"✅ Successfully installed Terraform {version}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


# === Status Command ===


@workenv_cli.command(name="status")
def status_command():
    """📊 Show status of all managed tools."""
    from rich.table import Table

    config = WorkenvConfig()
    tools = config.get_all_tools()
    console = get_console()

    if not tools:
        print_warning("No tools configured")
        return

    # Create status table
    table = Table(title=f"{Emoji.STATUS} Tool Status", show_header=True)
    table.add_column("Tool", style="cyan")
    table.add_column("Configured Version", style="yellow")
    table.add_column("Status", style="green")

    for tool_name, version in tools.items():
        tool_emoji = get_tool_emoji(tool_name)
        # Check if tool is installed (simplified for now)
        table.add_row(
            f"{tool_emoji} {tool_name}",
            version or "Not specified",
            f"{Emoji.INFO} Configured",
        )

    console.print(table)


# === Sync Command ===


@workenv_cli.command(name="sync")
def sync_command():
    """🔄 Install all tools defined in configuration."""
    config = WorkenvConfig()
    tools = config.get_all_tools()

    if not tools:
        click.echo("No tools configured in workenv configuration")
        return

    click.echo("Syncing tools from configuration...")

    for tool_name, version in tools.items():
        try:
            manager = get_tool_manager(tool_name, config)
            click.echo(f"\nInstalling {tool_name} {version}...")
            manager.install_version(version, dry_run=False)
            click.echo(f"✅ Successfully installed {tool_name} {version}")
        except Exception as e:
            click.echo(f"❌ Error installing {tool_name} {version}: {e}")


# === Matrix Test Command ===


@workenv_cli.command(name="matrix-test")
def matrix_test_command():
    """🧪 Run tests against multiple tool version combinations."""
    try:
        from wrkenv.env.testing.matrix import VersionMatrix
    except ImportError:
        click.echo("Matrix testing not available", err=True)
        sys.exit(1)

    config = WorkenvConfig()

    # Get matrix configuration
    matrix_config = config.get_setting("matrix", {})
    if not matrix_config:
        click.echo("No matrix configuration found")
        sys.exit(1)

    matrix = VersionMatrix(matrix_config)

    # Run the matrix tests
    click.echo("Running matrix tests...")
    results = matrix.run_tests(lambda versions: True)  # Dummy test function

    click.echo("\nResults:")
    click.echo(f"  Success: {results.get('success_count', 0)}")
    click.echo(f"  Failure: {results.get('failure_count', 0)}")


# === Container Commands ===


@workenv_cli.group(name="container")
def container_group():
    """🐳 Manage development containers."""
    pass


@container_group.command(name="build")
@click.option("--rebuild", is_flag=True, help="Force rebuild without cache")
def container_build(rebuild: bool):
    """Build the development container image."""
    from wrkenv.container import build_container

    config = WorkenvConfig()

    if build_container(config, rebuild=rebuild):
        click.echo("✅ Container image built successfully")
    else:
        click.echo("❌ Failed to build container image", err=True)
        sys.exit(1)


@container_group.command(name="start")
@click.option("--rebuild", is_flag=True, help="Rebuild image before starting")
def container_start(rebuild: bool):
    """Start the development container."""
    from wrkenv.container import start_container

    config = WorkenvConfig()

    if start_container(config, rebuild=rebuild):
        click.echo("✅ Container started successfully")
        click.echo("Run 'wrkenv container enter' to access the container")
    else:
        click.echo("❌ Failed to start container", err=True)
        sys.exit(1)


@container_group.command(name="enter")
@click.argument("command", nargs=-1, required=False)
def container_enter(command: tuple):
    """Enter the running container."""
    from wrkenv.container import enter_container

    config = WorkenvConfig()

    # Convert tuple to list
    cmd_list = list(command) if command else None
    enter_container(config, command=cmd_list)


@container_group.command(name="stop")
def container_stop():
    """Stop the development container."""
    from wrkenv.container import stop_container

    config = WorkenvConfig()

    if stop_container(config):
        click.echo("✅ Container stopped successfully")
    else:
        click.echo("❌ Failed to stop container", err=True)
        sys.exit(1)


@container_group.command(name="restart")
def container_restart():
    """Restart the development container."""
    from wrkenv.container import restart_container

    config = WorkenvConfig()

    if restart_container(config):
        click.echo("✅ Container restarted successfully")
    else:
        click.echo("❌ Failed to restart container", err=True)
        sys.exit(1)


@container_group.command(name="status")
def container_status_cmd():
    """Show container status."""
    from wrkenv.container import container_status

    config = WorkenvConfig()
    container_status(config)


@container_group.command(name="logs")
@click.option("-f", "--follow", is_flag=True, help="Follow log output")
@click.option("-n", "--tail", default=100, help="Number of lines to show")
def container_logs_cmd(follow: bool, tail: int):
    """Show container logs."""
    from wrkenv.container import container_logs

    config = WorkenvConfig()
    container_logs(config, follow=follow, tail=tail)


@container_group.command(name="clean")
def container_clean():
    """Remove container and image."""
    from wrkenv.container import clean_container

    config = WorkenvConfig()

    if clean_container(config):
        click.echo("✅ Container resources cleaned successfully")
    else:
        click.echo("❌ Failed to clean container resources", err=True)
        sys.exit(1)


@container_group.command(name="rebuild")
def container_rebuild():
    """Rebuild container from scratch."""
    from wrkenv.container import rebuild_container

    config = WorkenvConfig()

    if rebuild_container(config):
        click.echo("✅ Container rebuilt successfully")
    else:
        click.echo("❌ Failed to rebuild container", err=True)
        sys.exit(1)


# === Profile Commands ===


@workenv_cli.group(name="profile")
def profile_group():
    """👤 Manage workenv profiles."""
    pass


@profile_group.command(name="list")
def profile_list():
    """List available profiles."""
    config = WorkenvConfig()

    profiles = config.list_profiles()

    if profiles:
        click.echo("Available profiles:")
        for name in profiles:
            if name == config.get_current_profile():
                click.echo(f"  * {name} (active)")
            else:
                click.echo(f"    {name}")
    else:
        click.echo("No profiles configured")


@profile_group.command(name="save")
@click.argument("name")
def profile_save(name: str):
    """Save current tool versions as a profile."""
    config = WorkenvConfig()

    config.save_profile(name)
    click.echo(f"Saved profile '{name}'")


@profile_group.command(name="load")
@click.argument("name")
def profile_load(name: str):
    """Load and install tools from a profile."""
    config = WorkenvConfig()

    profile = config.get_profile(name)
    if not profile:
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)

    click.echo(f"Loading profile '{name}'...")
    for tool_name, version in profile.items():
        try:
            manager = get_tool_manager(tool_name, config)
            click.echo(f"Installing {tool_name} {version}...")
            manager.install_version(version, dry_run=False)
            click.echo(f"✅ Successfully installed {tool_name} {version}")
        except Exception as e:
            click.echo(f"❌ Error installing {tool_name} {version}: {e}")


# === Config Commands ===


@workenv_cli.group(name="config")
def config_group():
    """⚙️ Manage workenv configuration."""
    pass


@config_group.command(name="show")
def config_show():
    """Show current configuration."""
    config = WorkenvConfig()
    config.show_config()


@config_group.command(name="edit")
def config_edit():
    """Edit configuration file."""
    config = WorkenvConfig()
    config.edit_config()


# === Package Commands ===


@workenv_cli.group(name="package")
def package_group():
    """📦 Manage provider packages."""
    pass


@package_group.command(name="build")
@click.option(
    "--manifest",
    default="pyproject.toml",
    type=click.Path(
        exists=True, dir_okay=False, resolve_path=True, path_type=pathlib.Path
    ),
    help="Path to the pyproject.toml manifest file.",
)
@click.option(
    "--dry-run", is_flag=True, help="Show what would be built without building"
)
def package_build(manifest: pathlib.Path, dry_run: bool):
    """Build a provider package from manifest."""
    from wrkenv.package import build_package

    config = WorkenvConfig()

    if dry_run:
        click.echo("[DRY-RUN] Would build package from manifest")
        click.echo(f"  Manifest: {manifest}")
        return

    click.echo("🚀 Building provider package...")
    try:
        artifacts = build_package(manifest, config, dry_run)
        for artifact in artifacts:
            click.echo(f"✅ Successfully built: {artifact}")
    except ImportError as e:
        click.echo(f"❌ {e}", err=True)
        click.echo("Install flavor with: pip install flavor", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Build failed: {e}", err=True)
        sys.exit(1)


@package_group.command(name="verify")
@click.argument(
    "package_file",
    type=click.Path(
        exists=True, dir_okay=False, resolve_path=True, path_type=pathlib.Path
    ),
)
def package_verify(package_file: pathlib.Path):
    """Verify a package file's integrity and signature."""
    from wrkenv.package import verify_package

    config = WorkenvConfig()

    click.echo(f"🔍 Verifying '{package_file}'...")
    try:
        verify_package(package_file, config)
        click.echo("✅ Package verification successful.")
    except Exception as e:
        click.echo(f"❌ Verification failed: {e}", err=True)
        sys.exit(1)


@package_group.command(name="keygen")
@click.option(
    "--out-dir",
    default="keys",
    type=click.Path(
        file_okay=False, writable=True, resolve_path=True, path_type=pathlib.Path
    ),
    help="Directory to save the ECDSA key pair.",
)
def package_keygen(out_dir: pathlib.Path):
    """Generate signing keys for packages."""
    from wrkenv.package import generate_keys

    config = WorkenvConfig()

    try:
        private_key, public_key = generate_keys(out_dir, config)
        click.echo(f"✅ Keys generated in '{out_dir}'")
        click.echo(f"  Private: {private_key}")
        click.echo(f"  Public: {public_key}")
    except Exception as e:
        click.echo(f"❌ Key generation failed: {e}", err=True)
        sys.exit(1)


@package_group.command(name="clean")
def package_clean():
    """Clean package build cache."""
    from wrkenv.package import clean_cache

    config = WorkenvConfig()

    click.echo("🧹 Cleaning package cache...")
    try:
        clean_cache(config)
        click.echo("✅ Cache cleaned.")
    except Exception as e:
        click.echo(f"❌ Clean failed: {e}", err=True)
        sys.exit(1)


@package_group.command(name="init")
@click.argument(
    "project_dir",
    type=click.Path(file_okay=False, writable=True, path_type=pathlib.Path),
)
def package_init(project_dir: pathlib.Path):
    """Initialize a new provider project."""
    from wrkenv.package import init_provider

    config = WorkenvConfig()

    try:
        path = init_provider(project_dir, config)
        click.echo(f"✅ New provider project created at {path}")
    except Exception as e:
        click.echo(f"❌ Initialization failed: {e}", err=True)
        sys.exit(1)


@package_group.command(name="list")
def package_list():
    """List built packages."""
    from wrkenv.package import list_packages

    config = WorkenvConfig()

    packages = list_packages(config)
    if not packages:
        click.echo("No packages found")
        return

    click.echo("📦 Built packages:")
    for pkg in packages:
        click.echo(f"  {pkg['name']} - {pkg.get('version', 'unknown')} ({pkg['size']})")


@package_group.command(name="info")
@click.argument(
    "package_file",
    type=click.Path(
        exists=True, dir_okay=False, resolve_path=True, path_type=pathlib.Path
    ),
)
def package_info(package_file: pathlib.Path):
    """Show detailed information about a package."""
    from wrkenv.package import get_package_info

    config = WorkenvConfig()

    try:
        info = get_package_info(package_file, config)
        click.echo(f"📦 Package: {info['name']}")
        click.echo(f"  Version: {info['version']}")
        click.echo(f"  Size: {info['size']}")
        click.echo(f"  Signature: {info['signature']}")
        click.echo(f"  Python: {info['python_version']}")
        if info.get("dependencies"):
            click.echo(f"  Dependencies: {', '.join(info['dependencies'])}")
    except Exception as e:
        click.echo(f"❌ Failed to get package info: {e}", err=True)
        sys.exit(1)


@package_group.command(name="sign")
@click.argument(
    "package_file",
    type=click.Path(
        exists=True, dir_okay=False, resolve_path=True, path_type=pathlib.Path
    ),
)
@click.option(
    "--key",
    type=click.Path(exists=True, dir_okay=False, readable=True, path_type=pathlib.Path),
    required=True,
    help="Path to private signing key",
)
def package_sign(package_file: pathlib.Path, key: pathlib.Path):
    """Sign an existing package."""
    from wrkenv.package import sign_package

    config = WorkenvConfig()

    try:
        sign_package(package_file, key, config)
        click.echo("✅ Package signed successfully")
    except NotImplementedError:
        click.echo("❌ Package signing not yet implemented", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Signing failed: {e}", err=True)
        sys.exit(1)


@package_group.command(name="publish")
@click.argument(
    "package_file",
    type=click.Path(
        exists=True, dir_okay=False, resolve_path=True, path_type=pathlib.Path
    ),
)
@click.option("--registry", default="default", help="Registry to publish to")
def package_publish(package_file: pathlib.Path, registry: str):
    """Publish package to registry."""
    from wrkenv.package import publish_package

    config = WorkenvConfig()

    click.echo(f"📤 Publishing to {registry}...")
    try:
        result = publish_package(package_file, registry, config)
        click.echo("✅ Package published successfully")
        click.echo(f"  URL: {result['url']}")
        click.echo(f"  SHA256: {result['sha256']}")
    except Exception as e:
        click.echo(f"❌ Publish failed: {e}", err=True)
        sys.exit(1)


@package_group.command(name="config")
def package_config():
    """Show package configuration."""
    config = WorkenvConfig()

    package_config = config.get_setting("package", {})
    if not package_config:
        click.echo("No package configuration found")
        return

    click.echo("📦 Package configuration:")
    for key, value in package_config.items():
        click.echo(f"  {key}: {value}")


@package_group.command(name="matrix-test")
@click.option("--matrix", required=True, help="Matrix configuration name")
def package_matrix_test(matrix: str):
    """Run package builds with tool version matrix."""
    config = WorkenvConfig()

    matrix_config = config.get_setting(f"matrix.{matrix}", {})
    if not matrix_config:
        click.echo(f"Matrix configuration '{matrix}' not found", err=True)
        sys.exit(1)

    click.echo(f"🧪 Running matrix test: {matrix}")
    click.echo("Matrix testing not yet fully implemented")
    # TODO: Implement matrix testing with version combinations


# === TF Subcommands (moved to tf command above) ===
# Removed tf group to avoid conflict with tf command


# === Entry Point ===


def entry_point():
    """Main entry point for the wrkenv CLI."""
    workenv_cli()


if __name__ == "__main__":
    entry_point()


# 🧰🌍🖥️🪄
