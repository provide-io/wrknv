"""
Workenv CLI Commands
===================
Commands for managing development workenvs.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from provide.foundation.hub import register_command
from provide.foundation import logger
from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning

from wrknv.workenv import WorkenvExporter, WorkenvImporter, WorkenvPackager
from wrknv.workenv.registry import WorkenvRegistry
from wrknv.config import WorkenvConfig
from wrknv.wenv.workenv import WorkenvManager


# Register the workenv group first
@register_command("workenv", group=True, description="Manage development workenvs")
def workenv_group():
    """Commands for managing workenvs."""
    pass


@register_command("workenv.create", description="Create a new workenv")
def create(
    name: str | None = None,
    python: str | None = None,
    from_config: Path | None = None,
    force: bool = False
):
        """Create a new workenv."""
        logger.info("🚀 Creating workenv", name=name, python=python)

        try:
            manager = WorkenvManager()

            if from_config and from_config.exists():
                # Load configuration from specific file
                config = WorkenvConfig.load(config_file=from_config)
                workenv_name = name or config.project_name
            else:
                # Use current directory config or defaults
                config = WorkenvConfig.load()
                workenv_name = name or config.project_name

            # Create workenv
            workenv_path = manager.create_workenv(
                base_path=Path.cwd(),
                force=force
            )

            echo_success(f"✅ Workenv created: {workenv_path}")
            echo_info(f"💡 Activate with: source {workenv_path.parent.parent}/env.sh")

        except Exception as e:
            echo_error(f"❌ Failed to create workenv: {e}")
            raise

@register_command("workenv.export", description="Export workenv for distribution")
def export(
    output: Path,
    name: str | None = None,
    version: str = "1.0.0",
    format_type: str = "psp"
):
        """Export workenv for distribution."""
        echo_info(f"📦 Exporting workenv to {output} (format: {format_type})")

        try:
            # Load current configuration
            config = WorkenvConfig.load()
            exporter = WorkenvExporter(config)

            # Export workenv
            export_result = exporter.export(
                output_dir=output,
                name=name,
                version=version
            )

            # Package if requested
            if format_type == "psp":
                packager = WorkenvPackager()
                package_path = output.parent / f"{export_result.name}-{version}.psp"

                packager.package(
                    export=export_result,
                    output_path=package_path,
                    format_type="psp"
                )

                echo_success(f"✅ Workenv packaged: {package_path}")
            else:
                echo_success(f"✅ Workenv exported: {output}")

        except Exception as e:
            echo_error(f"❌ Failed to export workenv: {e}")
            raise

@register_command("workenv.import", description="Import a packaged workenv")
def import_workenv(
    package: str,
    directory: Path = Path("."),
    activate: bool = True,
    verify: bool = True
):
        """Import a packaged workenv."""
        import asyncio

        async def _import_workenv():
            logger.info("📦⬇️ Importing workenv", package=package)

            try:
                importer = WorkenvImporter()

                if package.startswith(("http://", "https://")):
                    # Import from URL
                    workenv_path = await importer.import_from_url(
                        url=package,
                        target_dir=directory,
                        verify_signature=verify
                    )
                else:
                    # Import from local file
                    package_path = Path(package)
                    workenv_path = await importer.import_from_package(
                        package_path=package_path,
                        target_dir=directory,
                        activate=activate
                    )

                logger.success(f"✅ Workenv imported: {workenv_path}")

                if activate:
                    env_script = directory / "env.sh"
                    if env_script.exists():
                        logger.info(f"💡 Activate with: source {env_script}")

            except Exception as e:
                logger.error("❌ Failed to import workenv", error=str(e))
                raise

        asyncio.run(_import_workenv())

@register_command("workenv.list", description="List available workenvs")
def list_workenvs(registry_url: str | None = None):
        """List available workenvs."""
        try:
            # List local workenvs
            workenv_dir = Path.home() / ".wrknv" / "cache" / "packages"
            if workenv_dir.exists():
                local_packages = list(workenv_dir.glob("*.psp"))
                if local_packages:
                    echo_info("🏠 Local workenvs:")
                    for package in local_packages:
                        echo_info(f"  - {package.stem}")
                else:
                    echo_info("🏠 No local workenvs found")
            else:
                echo_info("🏠 No local workenv cache directory found")
                echo_info(f"   Expected at: {workenv_dir}")

            # List registry workenvs (placeholder)
            if registry_url:
                echo_info(f"🌐 Registry workenvs from {registry_url}:")
                echo_info("  (Registry integration coming soon)")

        except Exception as e:
            echo_error(f"❌ Failed to list workenvs: {e}")
            raise

@register_command("workenv.activate", description="Show activation command for workenv")
def activate(name: str | None = None):
        """Show activation command for workenv."""
        try:
            # Find workenv
            if name:
                workenv_dir = Path.cwd() / "workenv"
                possible_paths = list(workenv_dir.glob(f"{name}_*"))
                if possible_paths:
                    workenv_path = possible_paths[0]
                else:
                    echo_error(f"❌ Workenv not found: {name}")
                    return
            else:
                # Use current project workenv
                env_script = Path.cwd() / "env.sh"
                if env_script.exists():
                    echo_info(f"💡 Activate with: source {env_script}")
                    return
                else:
                    echo_error("❌ No workenv found in current directory")
                    return

            # Show activation command
            if workenv_path.exists():
                echo_info(f"💡 Activate workenv: source workenv/env.sh")
                echo_info(f"📁 Workenv path: {workenv_path}")
            else:
                echo_error(f"❌ Workenv path does not exist: {workenv_path}")

        except Exception as e:
            echo_error(f"❌ Failed to get activation command: {e}")
            raise

@register_command("workenv.publish", description="Publish workenv to registry")
def publish(
    package: Path,
    registry_url: str | None = None,
    api_key: str | None = None
):
        """Publish workenv to registry."""
        import asyncio

        async def _publish():
            logger.info("📤 Publishing workenv", package=str(package))

            try:
                if not package.exists():
                    logger.error(f"❌ Package not found: {package}")
                    return

                # Extract metadata from package
                packager = WorkenvPackager()
                metadata = packager.inspect_package(package)

                if not metadata:
                    logger.error("❌ Failed to extract package metadata")
                    return

                # Publish to registry
                async with WorkenvRegistry(registry_url) as registry:
                    success = await registry.publish(
                        package_path=package,
                        metadata=metadata,
                        api_key=api_key
                    )

                    if success:
                        logger.success("✅ Workenv published successfully")
                    else:
                        logger.error("❌ Failed to publish workenv")

            except Exception as e:
                logger.error("❌ Failed to publish workenv", error=str(e))
                raise

        asyncio.run(_publish())

@register_command("workenv.search", description="Search for workenvs in registry")
def search(
    query: str,
    registry_url: str | None = None,
    limit: int = 10
):
        """Search for workenvs in registry."""
        import asyncio

        async def _search():
            logger.info("🔍 Searching workenvs", query=query)

            try:
                async with WorkenvRegistry(registry_url) as registry:
                    results = await registry.search(query)

                    if results:
                        logger.info(f"🔍 Found {len(results)} workenvs:")
                        for i, result in enumerate(results[:limit]):
                            name = result.get("name", "unknown")
                            version = result.get("version", "unknown")
                            description = result.get("description", "No description")
                            logger.info(f"  {i+1}. {name} ({version}) - {description}")
                    else:
                        logger.info("🔍 No workenvs found matching query")

            except Exception as e:
                logger.error("❌ Failed to search workenvs", error=str(e))
                raise

        asyncio.run(_search())

@register_command("workenv.verify", description="Verify workenv package integrity")
def verify(package: Path):
        """Verify workenv package integrity."""
        logger.info("🔍 Verifying workenv package", package=str(package))

        try:
            if not package.exists():
                logger.error(f"❌ Package not found: {package}")
                return

            packager = WorkenvPackager()
            is_valid = packager.verify_package(package)

            if is_valid:
                logger.success("✅ Package verification passed")
            else:
                logger.error("❌ Package verification failed")

        except Exception as e:
            logger.error("❌ Failed to verify package", error=str(e))
            raise

@register_command("workenv.info", description="Get information about a workenv package")
def info(
    name: str,
    registry_url: str | None = None
):
        """Get information about a workenv package."""
        import asyncio

        async def _info():
            logger.info("ℹ️ Getting workenv info", name=name)

            try:
                async with WorkenvRegistry(registry_url) as registry:
                    info = await registry.get_package_info(name)

                    if info:
                        logger.info(f"📦 Package: {info.get('name', name)}")
                        logger.info(f"📝 Description: {info.get('description', 'No description')}")
                        logger.info(f"🏷️ Latest version: {info.get('latest_version', 'unknown')}")

                        versions = info.get("versions", [])
                        if versions:
                            logger.info(f"📚 Available versions: {len(versions)}")
                            for version in versions[-5:]:  # Show last 5 versions
                                logger.info(f"  - {version.get('version', 'unknown')}")
                    else:
                        logger.error(f"❌ Package not found: {name}")

            except Exception as e:
                logger.error("❌ Failed to get package info", error=str(e))
                raise

        asyncio.run(_info())

@register_command("workenv.clean", description="Clean local workenv cache")
def clean(registry_url: str | None = None):
        """Clean local workenv cache."""
        import asyncio

        async def _clean():
            logger.info("🧹 Cleaning workenv cache")

            try:
                async with WorkenvRegistry(registry_url) as registry:
                    count = await registry.clear_cache()
                    logger.success(f"✅ Cleaned {count} cached packages")

            except Exception as e:
                logger.error("❌ Failed to clean cache", error=str(e))
                raise

        asyncio.run(_clean())