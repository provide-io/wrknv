#
# wrknv/env/package/commands.py
#
"""
Package Commands Implementation
===============================
Command implementations for package management using flavor CLI.
"""

from pathlib import Path
import shutil
import subprocess

from provide.foundation import logger

from wrknv.wenv.config import WorkenvConfig

from .manager import PackageManager


def _check_flavor_cli() -> bool:
    """Check if flavor CLI is available."""
    if not shutil.which("flavor"):
        raise ImportError(
            "flavor CLI not found. Install it with: uv pip install --system flavorpack"
        )
    return True


def _run_flavor_command(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    """Run a flavor CLI command."""
    _check_flavor_cli()
    cmd = ["flavor"] + args
    logger.debug(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)


def build_package(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    # Check if flavor is available
    _check_flavor_cli()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment
    env = manager.setup_build_environment()

    # Build using flavor CLI
    cmd = ["flavor", "pack", "--manifest", str(manifest_path)]

    logger.info(f"Building package from {manifest_path}")
    result = subprocess.run(
        cmd,
        cwd=manifest_path.parent,
        capture_output=True,
        text=True,
        env=env,
    )

    if result.returncode != 0:
        logger.error(f"Build failed: {result.stderr}")
        raise RuntimeError(f"flavor pack failed: {result.stderr}")

    logger.info(result.stdout)

    # Find generated packages in dist/
    dist_dir = manifest_path.parent / "dist"
    if dist_dir.exists():
        packages = list(dist_dir.glob("*.psp"))
        return packages

    return []


def verify_package(package_path: Path, config: WorkenvConfig | None = None) -> None:
    """Verify a package file."""
    _check_flavor_cli()

    logger.info(f"Verifying package: {package_path}")
    result = _run_flavor_command(["verify", str(package_path)])

    if result.returncode == 0:
        logger.info("Package verification successful")
    else:
        raise RuntimeError(f"Package verification failed: {result.stderr}")


def generate_keys(
    output_dir: Path, config: WorkenvConfig | None = None
) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_cli()

    output_dir.mkdir(parents=True, exist_ok=True)

    # flavor keygen generates keys in the specified directory
    logger.info(f"Generating signing keys in {output_dir}")
    result = _run_flavor_command(["keygen"], cwd=output_dir)

    if result.returncode != 0:
        raise RuntimeError(f"Key generation failed: {result.stderr}")

    logger.info(result.stdout)

    # flavor keygen creates private.pem and public.pem
    private_key = output_dir / "private.pem"
    public_key = output_dir / "public.pem"

    if not private_key.exists() or not public_key.exists():
        raise RuntimeError("Key files not found after generation")

    return (private_key, public_key)


def clean_cache(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_cli()

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    result = _run_flavor_command(["clean"])

    if result.returncode == 0:
        logger.info("Flavor cache cleaned")
    else:
        logger.warning(f"Failed to clean flavor cache: {result.stderr}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def init_provider(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "keys").mkdir(exist_ok=True)

    # Create basic pyproject.toml
    pyproject = project_dir / "pyproject.toml"
    pyproject.write_text(
        """[project]
name = "provider-example"
version = "0.1.0"
description = "Example Terraform provider"
requires-python = ">=3.11"

[tool.flavor]
provider_name = "example"
entry_point = "provider.main:serve"

[tool.flavor.signing]
private_key_path = "keys/private.pem"
public_key_path = "keys/public.pem"
"""
    )

    logger.info(f"Initialized provider project at {project_dir}")
    return project_dir


def list_packages(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)
    output_dir = manager.get_package_output_dir()

    packages = []
    if output_dir.exists():
        for psp_file in output_dir.glob("*.psp"):
            stat = psp_file.stat()
            packages.append(
                {
                    "name": psp_file.stem,
                    "version": "unknown",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def get_package_info(
    package_path: Path, config: WorkenvConfig | None = None
) -> dict[str, any]:
    """Get detailed information about a package."""
    _check_flavor_cli()

    # Use flavor inspect command
    result = _run_flavor_command(["inspect", str(package_path)])

    if result.returncode != 0:
        raise RuntimeError(f"Package inspection failed: {result.stderr}")

    # Parse the output (flavor inspect provides package metadata)
    stat = package_path.stat()
    return {
        "name": package_path.stem,
        "version": "unknown",  # Parse from inspect output
        "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
        "signature": "unknown",  # Parse from inspect output
        "python_version": "unknown",
        "dependencies": [],
        "raw_output": result.stdout,
    }


def sign_package(
    package_path: Path, key_path: Path, config: WorkenvConfig | None = None
) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    # Use --private-key flag with flavor pack to sign during build
    logger.info("Package signing is done during build with --private-key")
    logger.info(f"To sign {package_path}, rebuild with: flavor pack --private-key {key_path}")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def publish_package(
    package_path: Path, registry: str, config: WorkenvConfig | None = None
) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "status": "mock",
    }


# 🧰🌍🖥️🪄
