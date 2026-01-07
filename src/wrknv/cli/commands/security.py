#
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Security Scanning Commands
==========================
Commands for managing security scanner configurations."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys

from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation.hub import register_command

from wrknv.security import SecurityAllowlistManager, load_security_config


# Register the security group
@register_command("security", group=True, description="Manage security scanning configurations")
def security_group() -> None:
    """Commands for managing security scanner allowlists."""


@register_command(
    "security.generate",
    description="Generate security scanner configuration files",
)
def security_generate(
    dry_run: bool = False,
    tool: str | None = None,
) -> None:
    """Generate configuration files for security scanners.

    Reads allowlist from pyproject.toml [tool.security] or wrknv.toml [security]
    and generates configuration files for TruffleHog, Gitleaks, and GitGuardian.

    Args:
        dry_run: Show what would be generated without writing files
        tool: Generate only for specific tool (trufflehog, gitleaks, gitguardian)
    """
    config = load_security_config()
    if not config:
        echo_error("No security configuration found.")
        echo_info("Add [tool.security] to pyproject.toml or [security] to wrknv.toml:")
        echo_info("")
        echo_info("  [tool.security]  # or [security] in wrknv.toml")
        echo_info('  description = "Test fixtures and example credentials"')
        echo_info("  allowed_paths = [")
        echo_info('      "tests/certs/*.key",')
        echo_info('      "docs/**/*.md",')
        echo_info("  ]")
        sys.exit(1)

    manager = SecurityAllowlistManager(config=config)

    # Validate configuration
    is_valid, errors = manager.validate()
    if not is_valid:
        echo_error("Invalid security configuration:")
        for error in errors:
            echo_error(f"  • {error}")
        sys.exit(1)

    if dry_run:
        echo_info("[DRY-RUN] Would generate:")

    # Generate specific tool or all
    if tool:
        tool_map = {
            "trufflehog": (".trufflehog-exclude-paths.txt", manager.generate_trufflehog),
            "gitleaks": (".gitleaks.toml", manager.generate_gitleaks),
            "gitguardian": (".gitguardian.yaml", manager.generate_gitguardian),
        }
        if tool.lower() not in tool_map:
            echo_error(f"Unknown tool: {tool}")
            echo_info("Available tools: trufflehog, gitleaks, gitguardian")
            sys.exit(1)

        filename, generator = tool_map[tool.lower()]
        if dry_run:
            echo_info(f"  • {filename}")
            echo_info("")
            echo_info(generator())
        else:
            filepath = Path.cwd() / filename
            filepath.write_text(generator())
            echo_success(f"Generated {filepath}")
    else:
        results = manager.write_all(dry_run=dry_run)
        if not dry_run:
            success_count = sum(results.values())
            total_count = len(results)
            if success_count == total_count:
                echo_success(f"Generated {success_count} configuration files")
            else:
                echo_warning(f"Generated {success_count}/{total_count} files")
                for filename, success in results.items():
                    if not success:
                        echo_error(f"  Failed: {filename}")


@register_command(
    "security.validate",
    description="Validate security configuration",
)
def security_validate() -> None:
    """Validate security scanner configuration syntax and paths."""
    config = load_security_config()
    if not config:
        echo_error("No security configuration found.")
        sys.exit(1)

    manager = SecurityAllowlistManager(config=config)
    is_valid, errors = manager.validate()

    if is_valid:
        echo_success("✓ Security configuration is valid")
        echo_info(f"  Description: {config.description}")
        echo_info(f"  Allowed paths: {len(config.allowed_paths)}")
        for path in config.allowed_paths[:10]:  # Show first 10
            echo_info(f"    • {path}")
        if len(config.allowed_paths) > 10:
            echo_info(f"    ... and {len(config.allowed_paths) - 10} more")
    else:
        echo_error("✗ Security configuration has errors:")
        for error in errors:
            echo_error(f"  • {error}")
        sys.exit(1)


@register_command(
    "security.preview",
    description="Preview generated security configurations",
)
def security_preview(tool: str | None = None) -> None:
    """Preview what security configurations would be generated.

    Args:
        tool: Specific tool to preview (trufflehog, gitleaks, gitguardian)
    """
    config = load_security_config()
    if not config:
        echo_error("No security configuration found.")
        sys.exit(1)

    manager = SecurityAllowlistManager(config=config)
    echo_info(manager.preview(tool=tool))


@register_command(
    "security.scan",
    description="Run security scanners with generated configs",
)
def security_scan(
    tool: str | None = None,
    generate: bool = True,
) -> None:
    """Run security scanners with the configured allowlists.

    Args:
        tool: Specific scanner to run (trufflehog, gitleaks)
        generate: Generate/update config files before scanning (default: True)
    """
    # Generate configs first if requested
    if generate:
        config = load_security_config()
        if config:
            manager = SecurityAllowlistManager(config=config)
            manager.write_all()
            echo_info("Updated security scanner configurations")
        else:
            echo_warning("No security configuration found, running scanners without allowlist")

    # Define available scanners
    scanners = {
        "trufflehog": _run_trufflehog,
        "gitleaks": _run_gitleaks,
    }

    if tool:
        tool_lower = tool.lower()
        if tool_lower not in scanners:
            echo_error(f"Unknown scanner: {tool}")
            echo_info("Available scanners: trufflehog, gitleaks")
            sys.exit(1)
        scanners[tool_lower]()
    else:
        # Run all available scanners
        any_failed = False
        for name, runner in scanners.items():
            echo_info(f"\n{'=' * 40}")
            echo_info(f"Running {name}...")
            echo_info(f"{'=' * 40}")
            if not runner():
                any_failed = True

        if any_failed:
            sys.exit(1)


def _run_trufflehog() -> bool:
    """Run TruffleHog scanner.

    Returns:
        True if scan passed (no secrets found), False otherwise
    """
    if not shutil.which("trufflehog"):
        echo_warning("TruffleHog not installed. Install with: brew install trufflehog")
        return True  # Don't fail if not installed

    exclude_file = Path.cwd() / ".trufflehog-exclude-paths.txt"
    cmd = ["trufflehog", "git", "file://.", "--fail"]

    if exclude_file.exists():
        cmd.extend(["--exclude-paths", str(exclude_file)])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if result.returncode == 0:
            echo_success("✓ TruffleHog: No secrets found")
            return True
        else:
            echo_error("✗ TruffleHog found potential secrets:")
            if result.stdout:
                echo_info(result.stdout)
            if result.stderr:
                echo_info(result.stderr)
            return False
    except FileNotFoundError:
        echo_warning("TruffleHog not found in PATH")
        return True


def _run_gitleaks() -> bool:
    """Run Gitleaks scanner.

    Returns:
        True if scan passed (no secrets found), False otherwise
    """
    if not shutil.which("gitleaks"):
        echo_warning("Gitleaks not installed. Install with: brew install gitleaks")
        return True  # Don't fail if not installed

    config_file = Path.cwd() / ".gitleaks.toml"
    cmd = ["gitleaks", "git", "."]

    if config_file.exists():
        cmd.extend(["--config", str(config_file)])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if result.returncode == 0:
            echo_success("✓ Gitleaks: No secrets found")
            return True
        else:
            echo_error("✗ Gitleaks found potential secrets:")
            if result.stdout:
                echo_info(result.stdout)
            if result.stderr:
                echo_info(result.stderr)
            return False
    except FileNotFoundError:
        echo_warning("Gitleaks not found in PATH")
        return True


@register_command(
    "security.show",
    description="Show current security configuration",
)
def security_show() -> None:
    """Show the current security configuration and its source."""
    config = load_security_config()
    if not config:
        echo_info("No security configuration found.")
        echo_info("")
        echo_info("To configure, add to pyproject.toml or wrknv.toml:")
        echo_info("")
        echo_info("  [tool.security]  # pyproject.toml")
        echo_info("  # or")
        echo_info("  [security]  # wrknv.toml")
        echo_info("")
        echo_info('  description = "Test fixtures and example credentials"')
        echo_info("  allowed_paths = [")
        echo_info('      "tests/certs/*.key",')
        echo_info('      "docs/**/*.md",')
        echo_info("  ]")
        return

    echo_info("Security Configuration")
    echo_info("=" * 40)
    echo_info(f"Description: {config.description}")
    echo_info(f"Allowed paths ({len(config.allowed_paths)}):")
    for path in config.allowed_paths:
        echo_info(f"  • {path}")


# 🧰🌍🔚
