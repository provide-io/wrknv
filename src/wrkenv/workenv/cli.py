#!/usr/bin/env python3
#
# wrkenv/workenv/cli.py
#
"""
wrkenv CLI Commands
===================
Command-line interface for wrkenv tool management.
"""

import pathlib
import sys

import click

from wrkenv.workenv.config import WorkenvConfig, WorkenvConfigError
from wrkenv.workenv.managers.factory import get_supported_tools, get_tool_manager


@click.group(name="wrkenv")
def workenv_cli():
    """🧰🌍 Manage development environment tools and versions.

    wrkenv provides cross-platform tool installation and version management
    for development environments, including Terraform, OpenTofu, Go, UV, and more.
    """
    pass


# === MAJOR TOOLS (Direct syntax) ===


@workenv_cli.group(name="tf")
def workenv_tf():
    """🏗️  Manage Terraform/OpenTofu installations."""
    pass


@workenv_tf.command(name="list")
@click.option(
    "--tf-version", help="Filter versions (e.g., opentofu-*, terraform>=1.11)"
)
@click.option(
    "--remote", is_flag=True, help="Show available remote versions instead of local"
)
def tf_list(tf_version: str | None, remote: bool):
    """📋 List installed Terraform and OpenTofu versions (use --remote for available).

    Examples:
        wrkenv tf list                        # List installed versions
        wrkenv tf list --remote               # List available versions
        wrkenv tf list --tf-version=opentofu-*  # Show installed OpenTofu versions
        wrkenv tf list --remote --tf-version=terraform>=1.11  # Show available Terraform >= 1.11
    """
    config = WorkenvConfig()

    if remote:
        # Show available remote versions
        _list_remote_versions(config, tf_version)
    else:
        # Show locally installed versions (default)
        _list_local_versions(config, tf_version)


def _parse_tf_version(tf_version: str) -> tuple[str | None, str | None]:
    """Parse version string like 'opentofu-1.6.2' or 'terraform>=1.11'."""
    if "-" not in tf_version:
        return None, None

    parts = tf_version.split("-", 1)
    tool_name = parts[0]
    version_spec = parts[1]

    if tool_name == "opentofu":
        tool_name = "tofu"
    elif tool_name != "terraform":
        return None, None

    return tool_name, version_spec


def _filter_versions_by_comparison(versions: list[str], version_spec: str) -> list[str]:
    """Filter versions by comparison operator."""
    import re

    from packaging import version as pkg_version

    match = re.match(r"([><=]+)(.+)", version_spec)
    if not match:
        return []

    op = match.group(1)
    target = match.group(2)

    filtered = []
    for version in versions:
        try:
            v = pkg_version.parse(version)
            t = pkg_version.parse(target)

            if op == ">=":
                if v >= t:
                    filtered.append(version)
            elif op == ">":
                if v > t:
                    filtered.append(version)
            elif op == "<=":
                if v <= t:
                    filtered.append(version)
            elif op == "<":
                if v < t:
                    filtered.append(version)
            elif op == "==":
                if v == t:
                    filtered.append(version)
        except Exception:
            # Skip versions that can't be parsed
            continue

    return filtered


def _list_remote_versions(config: WorkenvConfig, tf_version: str | None):
    """List available remote versions."""
    tools_to_check = []

    if tf_version:
        # Parse the version filter
        tool_name, version_spec = _parse_tf_version(tf_version)
        if tool_name:
            tools_to_check = [tool_name]
        else:
            click.echo(f"Invalid version filter: {tf_version}", err=True)
            sys.exit(1)
    else:
        # Show both terraform and tofu
        tools_to_check = ["terraform", "tofu"]

    for tool_name in tools_to_check:
        try:
            manager = get_tool_manager(tool_name, config)
            versions = manager.get_available_versions()

            # Apply version filtering if specified
            if tf_version and version_spec:
                if "*" in version_spec:
                    # Simple wildcard matching
                    import fnmatch

                    versions = [v for v in versions if fnmatch.fnmatch(v, version_spec)]
                elif any(op in version_spec for op in [">=", ">", "<=", "<", "=="]):
                    # Comparison operators
                    versions = _filter_versions_by_comparison(versions, version_spec)
                else:
                    # Exact match
                    versions = [v for v in versions if v == version_spec]

            if versions:
                display_name = "OpenTofu" if tool_name == "tofu" else "Terraform"
                click.echo(f"\n{display_name} versions available:")
                for version in sorted(versions, reverse=True)[:10]:  # Show top 10
                    click.echo(f"  {version}")
                if len(versions) > 10:
                    click.echo(f"  ... and {len(versions) - 10} more")
            else:
                click.echo(f"No matching versions found for {tool_name}")

        except Exception as e:
            click.echo(f"Error fetching versions for {tool_name}: {e}", err=True)


def _list_local_versions(config: WorkenvConfig, tf_version: str | None):
    """List locally installed versions."""
    tools_to_check = []

    if tf_version:
        # Parse the version filter
        tool_name, version_spec = _parse_tf_version(tf_version)
        if tool_name:
            tools_to_check = [tool_name]
        else:
            click.echo(f"Invalid version filter: {tf_version}", err=True)
            sys.exit(1)
    else:
        # Show both terraform and tofu
        tools_to_check = ["terraform", "tofu"]

    found_any = False
    for tool_name in tools_to_check:
        try:
            manager = get_tool_manager(tool_name, config)
            versions = manager.get_installed_versions()

            # Apply version filtering if specified
            if tf_version and version_spec:
                if "*" in version_spec:
                    # Simple wildcard matching
                    import fnmatch

                    versions = [v for v in versions if fnmatch.fnmatch(v, version_spec)]
                elif any(op in version_spec for op in [">=", ">", "<=", "<", "=="]):
                    # Comparison operators
                    versions = _filter_versions_by_comparison(versions, version_spec)
                else:
                    # Exact match
                    versions = [v for v in versions if v == version_spec]

            if versions:
                found_any = True
                display_name = "OpenTofu" if tool_name == "tofu" else "Terraform"
                click.echo(f"\n{display_name} versions installed:")
                for version in sorted(versions, reverse=True):
                    click.echo(f"  {version}")

        except Exception as e:
            click.echo(f"Error listing versions for {tool_name}: {e}", err=True)

    if not found_any:
        click.echo("No Terraform or OpenTofu versions installed.")


# === Status Command ===


@workenv_cli.command(name="status")
def status_command():
    """📊 Show status of all managed tools."""
    config = WorkenvConfig()
    supported_tools = get_supported_tools()

    click.echo("🧰 wrkenv Tool Status\n")

    for tool_name in supported_tools:
        try:
            manager = get_tool_manager(tool_name, config)
            installed_versions = manager.get_installed_versions()

            if installed_versions:
                click.echo(f"{tool_name}:")
                for version in sorted(installed_versions, reverse=True):
                    click.echo(f"  ✓ {version}")
            else:
                click.echo(f"{tool_name}: (none installed)")

        except Exception as e:
            click.echo(f"{tool_name}: ❌ Error - {e}")

    click.echo()


# === Install Command ===


@workenv_cli.command(name="install")
@click.argument("tool")
@click.argument("version")
def install_command(tool: str, version: str):
    """📦 Install a specific tool version.

    Examples:
        wrkenv install terraform 1.5.7
        wrkenv install tofu 1.6.2
        wrkenv install go 1.21.5
    """
    config = WorkenvConfig()

    try:
        manager = get_tool_manager(tool, config)
        click.echo(f"Installing {tool} version {version}...")
        manager.install_version(version)
        click.echo(f"✅ Successfully installed {tool} {version}")
    except Exception as e:
        click.echo(f"❌ Error installing {tool} {version}: {e}", err=True)
        sys.exit(1)


# === Profile Commands ===


@workenv_cli.group(name="profile")
def workenv_profile():
    """👤 Manage workenv profiles."""
    pass


@workenv_profile.command(name="list")
def profile_list():
    """List available profiles."""
    config = WorkenvConfig()
    # Implementation needed
    click.echo("Profile management not yet implemented")


# === Entry Point ===


def entry_point():
    """Main entry point for the wrkenv CLI."""
    workenv_cli()


if __name__ == "__main__":
    entry_point()


# 🧰🌍🖥️🪄