#!/usr/bin/env python3
#
# wrkenv/env/cli.py
#
"""
wrkenv CLI Commands
===================
Command-line interface for wrkenv tool management.
"""

import json
import pathlib
import shutil
import sys
from pathlib import Path

import click
from click import secho

from wrkenv.wenv.config import WorkenvConfig
from wrkenv.wenv.exceptions import (
    DependencyError,
    ProfileError,
)
from wrkenv.wenv.managers.factory import get_tool_manager
from wrkenv.wenv.visual import (
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
@click.option("--check", is_flag=True, help="Check system dependencies")
@click.option(
    "--completions",
    type=click.Choice(["bash", "zsh", "fish"]),
    help="Generate shell completions",
)
@click.option(
    "--install", is_flag=True, help="Install completions (use with --completions)"
)
def setup_command(
    shell_integration: bool,
    init: bool,
    force: bool,
    check: bool,
    completions: str,
    install: bool,
):
    """Set up wrkenv environment and integrations."""
    import subprocess
    from pathlib import Path

    from wrkenv.wenv.workenv import WorkenvManager

    if check:
        # Check system dependencies
        print_info("Checking system dependencies...", Emoji.INFO)

        required_deps = ["git", "curl", "python3"]
        optional_deps = ["docker", "wget"]
        missing_required = []
        missing_optional = []

        for dep in required_deps:
            if shutil.which(dep):
                print_success(f"  ✓ {dep}")
            else:
                print_error(f"  ✗ {dep} (required)")
                missing_required.append(dep)

        for dep in optional_deps:
            if shutil.which(dep):
                print_info(f"  ✓ {dep} (optional)")
            else:
                print_warning(f"  ✗ {dep} (optional)")
                missing_optional.append(dep)

        if missing_required:
            raise DependencyError(missing_required, "wrkenv core functionality")
        else:
            print_success("All required dependencies are installed!")
        return

    if completions:
        # Generate shell completions
        from wrkenv.wenv.completions import generate_completions

        completion_script = generate_completions(completions)

        if install:
            # Install completions to appropriate location
            install_path = None
            if completions == "bash":
                # Try common bash completion directories
                for path in [
                    Path.home() / ".bash_completion.d",
                    Path("/etc/bash_completion.d"),
                    Path("/usr/local/etc/bash_completion.d"),
                ]:
                    if path.exists() and path.is_dir():
                        install_path = path / "wrkenv"
                        break

                if not install_path:
                    # Create user directory
                    user_dir = Path.home() / ".bash_completion.d"
                    user_dir.mkdir(exist_ok=True)
                    install_path = user_dir / "wrkenv"

            elif completions == "zsh":
                # Zsh completion paths
                for path in [
                    Path.home() / ".zsh/completions",
                    Path("/usr/local/share/zsh/site-functions"),
                ]:
                    if path.exists() and path.is_dir():
                        install_path = path / "_wrkenv"
                        break

                if not install_path:
                    # Create user directory
                    user_dir = Path.home() / ".zsh/completions"
                    user_dir.mkdir(parents=True, exist_ok=True)
                    install_path = user_dir / "_wrkenv"

            elif completions == "fish":
                # Fish completion path
                fish_dir = Path.home() / ".config/fish/completions"
                fish_dir.mkdir(parents=True, exist_ok=True)
                install_path = fish_dir / "wrkenv.fish"

            if install_path:
                install_path.write_text(completion_script)
                print_success(
                    f"✅ Installed {completions} completions to {install_path}"
                )

                if completions == "bash":
                    print_info("Add this to your ~/.bashrc:")
                    print_info(f"  source {install_path}")
                elif completions == "zsh":
                    print_info("Add this to your ~/.zshrc:")
                    print_info(f"  fpath=({install_path.parent} $fpath)")
                    print_info("  autoload -U compinit && compinit")
        else:
            # Just output the completion script
            click.echo(completion_script)
        return

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
        print_info("  --check               Check system dependencies")
        print_info("  --completions SHELL   Generate shell completions (bash/zsh/fish)")


# === Direct Tool Commands ===


@workenv_cli.command(name="tf")
@click.argument("version", required=False)
@click.option("--latest", is_flag=True, help="Install latest version")
@click.option("--list", is_flag=True, help="List available versions")
@click.option("--dry-run", is_flag=True, help="Show what would be installed")
@click.option("--terraform", is_flag=True, help="Install Terraform instead of OpenTofu")
def tf_command(
    version: str | None, latest: bool, list: bool, dry_run: bool, terraform: bool
):
    """Install or manage Terraform/OpenTofu versions."""
    config = WorkenvConfig()

    # Determine which tool to manage
    tool_name = "terraform" if terraform else "tofu"
    tool_display = "Terraform" if terraform else "OpenTofu"
    tool_emoji = Emoji.TERRAFORM if terraform else Emoji.OPENTOFU

    if list:
        # List available versions
        try:
            manager = get_tool_manager(tool_name, config)
            print_info(f"Available {tool_display} versions:", tool_emoji)
            manager.list_versions()
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    elif latest:
        # Install latest version
        try:
            manager = get_tool_manager(tool_name, config)
            manager.install_latest(dry_run=dry_run)
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    elif version:
        # Install specific version
        try:
            manager = get_tool_manager(tool_name, config)
            if dry_run:
                print_info(f"[DRY-RUN] Would install {tool_display} {version}")
            else:
                print_info(
                    f"Installing {tool_display} {version}...",
                    f"{tool_emoji} {Emoji.DOWNLOAD}",
                )
            manager.install_version(version, dry_run=dry_run)
            if not dry_run:
                print_success(f"Successfully installed {tool_display} {version}")
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    else:
        print_warning("Please specify a version, --latest, or --list")
        print_info("Examples:")
        print_info("  wrkenv tf --list              # List OpenTofu versions")
        print_info("  wrkenv tf 1.8.0               # Install OpenTofu 1.8.0")
        print_info("  wrkenv tf --terraform 1.5.7   # Install Terraform 1.5.7")
        print_info("  wrkenv tf --terraform --list  # List Terraform versions")
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


# === Generate Env Command ===


@workenv_cli.command(name="generate-env")
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=pathlib.Path),
    default=pathlib.Path("env.sh"),
    help="Output path for the environment script",
)
@click.option(
    "--shell",
    type=click.Choice(["bash", "zsh", "sh", "powershell", "ps1"]),
    default="sh",
    help="Target shell type",
)
@click.option(
    "--project-dir",
    type=click.Path(exists=True, dir_okay=True, path_type=pathlib.Path),
    default=pathlib.Path.cwd(),
    help="Project directory to generate env script for",
)
def generate_env_command(output: pathlib.Path, shell: str, project_dir: pathlib.Path):
    """🌍 Generate optimized environment setup script."""
    from wrkenv.wenv.env_generator import create_project_env_scripts

    click.echo(f"🔧 Generating environment scripts for {project_dir.name}...")

    try:
        # Use the existing function that works
        sh_path, ps1_path = create_project_env_scripts(project_dir)

        # Move to requested output location if different
        if shell in ["powershell", "ps1"]:
            if output != ps1_path:
                import shutil

                shutil.move(str(ps1_path), str(output))
                ps1_path = output
            click.echo(f"✅ Generated {ps1_path}")
        else:
            if output != sh_path:
                import shutil

                shutil.move(str(sh_path), str(output))
                sh_path = output
            click.echo(f"✅ Generated {sh_path}")

        click.echo("\nTo use the environment:")
        click.echo(f"  source {output}")

    except FileNotFoundError as e:
        click.echo(f"❌ Error: {e}")
        click.echo("Make sure you're in a project directory with pyproject.toml")


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
        click.echo("No profiles found")


@profile_group.command(name="save")
@click.argument("name")
@click.option("--force", is_flag=True, help="Overwrite existing profile")
def profile_save(name: str, force: bool):
    """Save current tool versions as a profile."""
    config = WorkenvConfig()

    # Check if profile exists
    if not force and config.profile_exists(name):
        if not click.confirm(f"Profile '{name}' already exists. Overwrite?"):
            return

    # Get current tools
    tools = config.get_all_tools()
    config.save_profile(name, tools)
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


@profile_group.command(name="show")
@click.argument("name")
def profile_show(name: str):
    """Show details of a profile."""
    config = WorkenvConfig()

    profile = config.get_profile(name)
    if not profile:
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)

    click.echo(f"Profile: {name}")
    for tool_name, version in profile.items():
        click.echo(f"  {tool_name}: {version}")


@profile_group.command(name="delete")
@click.argument("name")
def profile_delete(name: str):
    """Delete a profile."""
    config = WorkenvConfig()

    if not config.profile_exists(name):
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)

    if click.confirm(f"Delete profile '{name}'?"):
        if config.delete_profile(name):
            click.echo(f"Profile '{name}' deleted")
        else:
            click.echo(f"Failed to delete profile '{name}'")
            sys.exit(1)


@profile_group.command(name="export")
@click.argument("name")
@click.option("--output", "-o", help="Output file path")
def profile_export(name: str, output: str):
    """Export a profile to a file."""
    import tomli_w

    config = WorkenvConfig()
    profile = config.get_profile(name)

    if not profile:
        click.echo(f"Profile '{name}' not found")
        sys.exit(1)

    profile_data = {"name": name, "tools": profile}

    if output:
        output_path = pathlib.Path(output)
    else:
        output_path = pathlib.Path(f"{name}-profile.toml")

    with open(output_path, "w") as f:
        f.write(tomli_w.dumps(profile_data))

    click.echo(f"Exported profile '{name}' to {output_path}")


@profile_group.command(name="import")
@click.argument("file")
def profile_import(file: str):
    """Import a profile from a file."""
    import tomllib

    file_path = pathlib.Path(file)
    if not file_path.exists():
        click.echo(f"File '{file}' not found")
        sys.exit(1)

    with open(file_path, "rb") as f:
        profile_data = tomllib.load(f)

    name = profile_data.get("name", file_path.stem)
    tools = profile_data.get("tools", {})

    config = WorkenvConfig()
    config.save_profile(name, tools)

    click.echo(f"Imported profile '{name}'")


# === Config Commands ===


@workenv_cli.group(name="config")
def config_group():
    """⚙️ Manage workenv configuration."""
    pass


@config_group.command(name="show")
@click.option("--json", "output_json", is_flag=True, help="Output in JSON format")
@click.option("--profile", help="Show specific profile configuration")
def config_show(output_json: bool, profile: str):
    """Show current configuration."""
    config = WorkenvConfig()

    if profile:
        # Show specific profile
        profile_data = config.get_profile(profile)
        if not profile_data:
            raise ProfileError(profile, available_profiles=config.list_profiles())

        if output_json:
            click.echo(
                json.dumps({"profile": profile, "tools": profile_data}, indent=2)
            )
        else:
            click.echo(f"Profile: {profile}")
            for tool_name, version in profile_data.items():
                click.echo(f"  {tool_name}: {version}")
    elif output_json:
        # Output entire config as JSON
        config_data = config.to_dict()
        click.echo(json.dumps(config_data, indent=2))
    else:
        # Default formatted output
        config.show_config()


@config_group.command(name="edit")
def config_edit():
    """Edit configuration file."""
    config = WorkenvConfig()
    try:
        config.edit_config()
    except RuntimeError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@config_group.command(name="validate")
@click.option("--strict", is_flag=True, help="Strict validation mode")
def config_validate(strict: bool):
    """Validate configuration file syntax and values."""
    config = WorkenvConfig()

    if not config.config_exists():
        print_error("No configuration file found")
        print_info("Create one with: wrkenv config init")
        sys.exit(1)

    try:
        is_valid, errors = config.validate()

        if is_valid:
            print_success("✅ Configuration is valid")
        else:
            print_error("❌ Configuration validation failed:")
            for error in errors:
                click.echo(f"  • {error}", err=True)
            sys.exit(1)

    except Exception as e:
        print_error(f"Validation error: {e}")
        sys.exit(1)


@config_group.command(name="init")
@click.option("--force", is_flag=True, help="Overwrite existing configuration")
def config_init(force: bool):
    """Initialize a new configuration file interactively."""
    config_path = Path.cwd() / "wrkenv.toml"

    if config_path.exists() and not force:
        print_error("Configuration file already exists")
        print_info("Use --force to overwrite")
        sys.exit(1)

    # Interactive prompts
    project_name = click.prompt("Project name", default=Path.cwd().name)
    version = click.prompt("Version", default="1.0.0")
    log_level = click.prompt(
        "Log level",
        default="INFO",
        type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]),
    )

    # Ask about common tools
    tools = {}
    if click.confirm("Do you want to configure Terraform/OpenTofu?"):
        tool_choice = click.prompt(
            "Which tool?", type=click.Choice(["terraform", "tofu"]), default="tofu"
        )
        version = click.prompt(
            f"{tool_choice} version",
            default="1.8.0" if tool_choice == "tofu" else "1.5.7",
        )
        tools[tool_choice] = {"version": version}

    if click.confirm("Do you want to configure Go?"):
        version = click.prompt("Go version", default="1.22.1")
        tools["go"] = {"version": version}

    if click.confirm("Do you want to configure UV?"):
        version = click.prompt("UV version", default="0.4.0")
        tools["uv"] = {"version": version}

    # Create configuration
    import tomli_w

    config_data = {
        "project_name": project_name,
        "version": version,
        "log_level": log_level,
    }

    if tools:
        config_data["tools"] = tools

    # Add container section if requested
    if click.confirm("Enable container support?"):
        config_data["container"] = {
            "enabled": True,
            "base_image": "ubuntu:22.04",
            "python_version": "3.11",
        }

    # Write configuration
    with open(config_path, "w") as f:
        f.write(tomli_w.dumps(config_data))

    print_success(f"✅ Created configuration file: {config_path}")
    print_info("You can edit it with: wrkenv config edit")


@config_group.command(name="get")
@click.argument("key")
def config_get(key: str):
    """Get a configuration value."""
    config = WorkenvConfig()

    try:
        value = config.get_setting(key)
        if value is None:
            print_warning(f"Key '{key}' not found")
            sys.exit(1)

        if isinstance(value, (dict, list)):
            secho(json.dumps(value, indent=2), fg="cyan")
        else:
            # Output format expected by tests
            click.echo(f"{key}: {value}")

    except Exception as e:
        print_error(f"Error getting config value: {e}")
        sys.exit(1)


@config_group.command(name="set")
@click.argument("key")
@click.argument("value")
def config_set(key: str, value: str):
    """Set a configuration value."""
    config = WorkenvConfig()

    try:
        # Try to parse value as JSON first (for complex types)
        try:
            parsed_value = json.loads(value)
        except json.JSONDecodeError:
            # Not JSON, treat as string
            parsed_value = value

        if config.set_setting(key, parsed_value):
            print_success(f"✅ Set {key} to {value}")
        else:
            print_error(f"Failed to set {key}")
            sys.exit(1)

    except Exception as e:
        print_error(f"Error setting config value: {e}")
        sys.exit(1)


@config_group.command(name="path")
def config_path():
    """Show path to configuration file."""
    config = WorkenvConfig()
    config_file = config.get_config_path()

    if config_file.exists():
        click.echo(str(config_file.absolute()))
    else:
        print_warning(f"Configuration file not found: {config_file}")
        print_info("Create one with: wrkenv config init")
        sys.exit(1)


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


# === TF Subcommands (moved to tf command above) ===
# Removed tf group to avoid conflict with tf command


# === Entry Point ===


def entry_point():
    """Main entry point for the wrkenv CLI."""
    workenv_cli()


if __name__ == "__main__":
    entry_point()


# 🧰🌍🖥️🪄
