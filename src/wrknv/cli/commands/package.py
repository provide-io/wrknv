#!/usr/bin/env python3
#
# wrknv/cli/commands/package.py
#
"""
Package Commands
================
Commands for managing provider packages.
"""

import pathlib
import sys

import click

from wrknv.package import (
    build_package,
    clean_cache,
    generate_keys,
    get_package_info,
    init_provider,
    list_packages,
    publish_package,
    sign_package,
    verify_package,
)
from wrknv.wenv.config import WorkenvConfig


@click.group(name="package")
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