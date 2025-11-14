#!/usr/bin/env python3
#
# wrknv/cli/commands/gitignore.py
#
"""
Gitignore Commands
==================
Commands for managing .gitignore files.
"""

import pathlib
import sys
from typing import Optional

import click

from wrknv.gitignore import GitignoreManager, ProjectDetector
from wrknv.wenv.config import WorkenvConfig


@click.group(name="gitignore")
def gitignore_group():
    """🚫 Manage .gitignore files."""
    pass


@gitignore_group.command(name="list")
@click.option("--category", "-c", help="Filter by category (e.g., Global, community)")
def gitignore_list(category: Optional[str]):
    """List available gitignore templates."""
    manager = GitignoreManager()
    templates = manager.list_available_templates(category=category)
    
    if not templates:
        click.echo("No templates found")
        return
    
    if category:
        click.echo(f"Templates in category '{category}':")
    else:
        click.echo("Available templates:")
    
    for template in templates:
        click.echo(f"  • {template}")
    
    click.echo(f"\nTotal: {len(templates)} templates")


@gitignore_group.command(name="search")
@click.argument("pattern")
def gitignore_search(pattern: str):
    """Search for gitignore templates."""
    manager = GitignoreManager()
    results = manager.search_templates(pattern)
    
    if not results:
        click.echo(f"No templates matching '{pattern}'")
        return
    
    click.echo(f"Templates matching '{pattern}':")
    for template in results:
        click.echo(f"  • {template}")


@gitignore_group.command(name="suggest")
@click.option("--scan-depth", "-d", default=5, help="Maximum directory depth to scan")
def gitignore_suggest(scan_depth: int):
    """Suggest templates based on project analysis."""
    manager = GitignoreManager()
    report = manager.get_detection_report()
    
    click.echo(report)
    click.echo()
    
    # Get suggestions
    detector = ProjectDetector()
    detector.scan_directory(pathlib.Path.cwd(), max_depth=scan_depth)
    suggestions = detector.suggest_templates()
    
    if suggestions:
        click.echo("Suggested templates:")
        for template in suggestions:
            click.echo(f"  • {template}")
        click.echo(f"\nRun: wrknv gitignore build -t {' -t '.join(suggestions)}")
    else:
        click.echo("No templates suggested")


@gitignore_group.command(name="update")
@click.option("--force", "-f", is_flag=True, help="Force update even if cache is valid")
def gitignore_update(force: bool):
    """Update gitignore templates from GitHub."""
    manager = GitignoreManager()
    click.echo("Updating gitignore templates from GitHub...")
    
    if manager.update_templates(force=force):
        click.echo("✅ Templates updated successfully")
    else:
        if not force:
            click.echo("Templates are already up to date. Use --force to update anyway.")
        else:
            click.echo("❌ Failed to update templates")


@gitignore_group.command(name="add")
@click.argument("templates", nargs=-1, required=True)
@click.option(
    "--custom-rule",
    "-r",
    multiple=True,
    help="Add custom ignore rules",
)
def gitignore_add(templates: tuple[str, ...], custom_rule: tuple[str, ...]):
    """Add templates to existing .gitignore."""
    manager = GitignoreManager()
    
    if manager.add_templates(
        templates=list(templates),
        custom_rules=list(custom_rule),
    ):
        click.echo(f"✅ Added {len(templates)} template(s) to .gitignore")
    else:
        click.echo("❌ Failed to add templates")
        sys.exit(1)


@gitignore_group.command(name="build")
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=pathlib.Path),
    default=pathlib.Path(".gitignore"),
    help="Output path for the .gitignore file",
)
@click.option(
    "--templates",
    "-t",
    multiple=True,
    help="Specify templates to include (e.g., Python, Node). Overrides config.",
)
def gitignore_build(output: pathlib.Path, templates: tuple[str, ...]):
    """Build a .gitignore file from templates."""
    config = WorkenvConfig()
    gitignore_content = []

    config_data = config.to_dict()
    gitignore_config = config_data.get("gitignore", {})

    # Determine templates to use
    if templates:
        selected_templates = list(templates)
    elif gitignore_config.get("templates"):
        selected_templates = gitignore_config.get("templates")
    else:
        selected_templates = []  # Ensure it's an empty list if no templates found

    if not selected_templates:
        click.echo("No gitignore templates specified in config or via --templates.")
        return

    # Determine the gitignore templates directory
    if gitignore_config.get("templates_path"):
        gitignore_dir = pathlib.Path(gitignore_config.get("templates_path"))
    else:
        # Fallback to the hardcoded path if not configured
        gitignore_dir = pathlib.Path("/REDACTED_ABS_PATH")

    for template_name in selected_templates:
        template_file = gitignore_dir / f"{template_name}.gitignore"
        if template_file.exists():
            gitignore_content.append(f"# --- {template_name} ---")
            gitignore_content.append(template_file.read_text())
            gitignore_content.append("\n")  # Add a newline for separation
        else:
            click.echo(
                f"Warning: Gitignore template '{template_name}' not found at {template_file}",
                err=True,
            )

    if gitignore_content:
        output.write_text("\n".join(gitignore_content))
        click.echo(f"✅ .gitignore built successfully at {output}")
    else:
        click.echo("No content generated for .gitignore.")