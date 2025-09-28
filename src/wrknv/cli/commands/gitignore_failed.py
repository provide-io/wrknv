"""
gitignore Commands for wrknv
=============================
Commands for managing .gitignore templates.
"""
from __future__ import annotations


from pathlib import Path

from provide.foundation.cli import echo_error, echo_info, echo_success
from provide.foundation.hub import register_command

from wrknv.config import WorkenvConfig
from wrknv.gitignore.manager import GitignoreManager


@register_command(
    "gitignore",
    description="Manage .gitignore templates",
    group=True,
)
def gitignore():
    """Manage .gitignore templates."""
    pass


@register_command(
    "list",
    parent="gitignore",
    description="List available gitignore templates",
)
def gitignore_list(category: str | None = None):
    """List available gitignore templates."""
    config = WorkenvConfig.load()
    gitignore_config = config.get_setting("gitignore", {})
    templates_path = gitignore_config.get("templates_path")
    manager = GitignoreManager(cache_dir=Path(templates_path) if templates_path else None)

    templates = manager.list_available_templates(category=category)

    if not templates:
        echo_info("No templates found")
        return

    if category:
        echo_info(f"Templates in category '{category}':")
    else:
        echo_info("Available templates:")

    for template in templates:
        echo_info(f"  • {template}")

    echo_info(f"\nTotal: {len(templates)} templates")


@register_command(
    "search",
    parent="gitignore",
    description="Search for gitignore templates",
)
def gitignore_search(pattern: str):
    """Search for gitignore templates matching a pattern."""
    config = WorkenvConfig.load()
    gitignore_config = config.get_setting("gitignore", {})
    templates_path = gitignore_config.get("templates_path")
    manager = GitignoreManager(cache_dir=Path(templates_path) if templates_path else None)

    results = manager.search_templates(pattern)

    if not results:
        echo_info(f"No templates found matching '{pattern}'")
        return

    echo_info(f"Templates matching '{pattern}':")
    for template in results:
        echo_info(f"  • {template}")

    echo_info(f"\nTotal: {len(results)} templates")


@register_command(
    "show",
    parent="gitignore",
    description="Show content of a gitignore template",
)
def gitignore_show(template: str, raw: bool = False):
    """
    Show the content of a gitignore template.

    Args:
        template: Name of the template to show
        raw: Show raw content without formatting
    """
    config = WorkenvConfig.load()
    gitignore_config = config.get_setting("gitignore", {})
    templates_path = gitignore_config.get("templates_path")
    manager = GitignoreManager(cache_dir=Path(templates_path) if templates_path else None)

    content = manager.get_template_content(template)

    if content is None:
        echo_error(f"Template '{template}' not found")
        return

    if raw:
        print(content)
    else:
        echo_info(f"Content of '{template}.gitignore':")
        echo_info("-" * 40)
        print(content)
        echo_info("-" * 40)


@register_command(
    "build",
    parent="gitignore",
    description="Build a .gitignore file from templates",
)
def gitignore_build(
    templates: list[str],
    output: Path | None = None,
    merge: bool = False,
):
    """
    Build a .gitignore file from one or more templates.

    Args:
        templates: List of template names to combine
        output: Output file path (default: .gitignore)
        merge: Merge with existing .gitignore file
    """
    config = WorkenvConfig.load()
    gitignore_config = config.get_setting("gitignore", {})
    templates_path = gitignore_config.get("templates_path")
    manager = GitignoreManager(cache_dir=Path(templates_path) if templates_path else None)

    output_path = output or Path(".gitignore")

    # Build content from templates
    contents = []
    for template in templates:
        content = manager.get_template_content(template)
        if content is None:
            echo_error(f"Template '{template}' not found")
            return
        contents.append(f"# {template}.gitignore\n{content}")

    combined_content = "\n\n".join(contents)

    # Handle merge
    if merge and output_path.exists():
        existing_content = output_path.read_text()
        combined_content = f"{existing_content}\n\n# Added by wrknv\n\n{combined_content}"

    # Write output
    output_path.write_text(combined_content)
    echo_success(f"Generated {output_path} from {len(templates)} template(s)")


@register_command(
    "detect",
    parent="gitignore",
    description="Detect project types and suggest templates",
)
def gitignore_detect(apply: bool = False):
    """
    Detect project types and suggest appropriate gitignore templates.

    Args:
        apply: Automatically apply detected templates
    """
    config = WorkenvConfig.load()
    gitignore_config = config.get_setting("gitignore", {})
    templates_path = gitignore_config.get("templates_path")
    manager = GitignoreManager(cache_dir=Path(templates_path) if templates_path else None)

    detected = manager.detect_project_types()

    if not detected:
        echo_info("No known project types detected")
        return

    echo_info("Detected project types:")
    for project_type in detected:
        echo_info(f"  • {project_type}")

    if apply:
        gitignore_build(detected, merge=True)
    else:
        echo_info("\nTo apply these templates, run:")
        templates_str = " ".join(detected)
        echo_info(f"  wrknv gitignore build {templates_str} --merge")


@register_command(
    "update",
    parent="gitignore",
    description="Update gitignore template cache",
)
def gitignore_update(force: bool = False):
    """
    Update the gitignore template cache from GitHub.

    Args:
        force: Force update even if cache is recent
    """
    config = WorkenvConfig.load()
    gitignore_config = config.get_setting("gitignore", {})
    templates_path = gitignore_config.get("templates_path")
    manager = GitignoreManager(cache_dir=Path(templates_path) if templates_path else None)

    echo_info("Updating gitignore templates from GitHub...")

    try:
        manager.update_cache(force=force)
        echo_success("Successfully updated gitignore templates")
    except Exception as e:
        echo_error(f"Failed to update templates: {e}")
