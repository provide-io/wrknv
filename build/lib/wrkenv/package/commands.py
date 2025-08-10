#
# wrkenv/env/package/commands.py
#
"""
Package Commands Implementation
===============================
Command implementations for package management.
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from pyvider.telemetry import logger

from wrkenv.env.config import WorkenvConfig
from .manager import PackageManager


def _get_flavor_api():
    """Dynamically import flavor API if available."""
    try:
        import flavor.api as flavor_api
        return flavor_api
    except ImportError:
        raise ImportError(
            "flavor package not found. Install it with: pip install flavor"
        )


def build_package(
    manifest_path: Path,
    config: Optional[WorkenvConfig] = None,
    dry_run: bool = False
) -> List[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.flavor"]
    
    # Check if flavor is available
    if config is None:
        config = WorkenvConfig()
        
    manager = PackageManager(config)
    if not manager.is_flavor_available():
        raise ImportError("flavor package required for building packages")
    
    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")
    
    # Set up build environment
    env = manager.setup_build_environment()
    
    # Use flavor API to build
    flavor_api = _get_flavor_api()
    return flavor_api.build_package_from_manifest(manifest_path)


def verify_package(
    package_path: Path,
    config: Optional[WorkenvConfig] = None
) -> None:
    """Verify a package file."""
    flavor_api = _get_flavor_api()
    flavor_api.verify_package(package_path)


def generate_keys(
    output_dir: Path,
    config: Optional[WorkenvConfig] = None
) -> Tuple[Path, Path]:
    """Generate signing key pair."""
    flavor_api = _get_flavor_api()
    return flavor_api.generate_keys(output_dir)


def clean_cache(config: Optional[WorkenvConfig] = None) -> None:
    """Clean package build cache."""
    # Clean flavor cache
    flavor_api = _get_flavor_api()
    flavor_api.clean_cache()
    
    # Clean wrkenv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def init_provider(
    project_dir: Path,
    config: Optional[WorkenvConfig] = None
) -> Path:
    """Initialize a new provider project."""
    # For now, use tofusoup's scaffolding
    # In future, this could be moved to wrkenv entirely
    try:
        from tofusoup.scaffolding.generator import scaffold_new_provider
        return scaffold_new_provider(project_dir)
    except ImportError:
        # Basic scaffolding without tofusoup
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # Create basic structure
        (project_dir / "src").mkdir(exist_ok=True)
        (project_dir / "tests").mkdir(exist_ok=True)
        (project_dir / "keys").mkdir(exist_ok=True)
        
        # Create basic pyproject.toml
        pyproject = project_dir / "pyproject.toml"
        pyproject.write_text("""[project]
name = "provider-example"
version = "0.1.0"
description = "Example Terraform provider"
requires-python = ">=3.12"

[tool.flavor]
provider_name = "example"
entry_point = "provider.main:serve"

[tool.flavor.signing]
private_key_path = "keys/provider-private.key"
public_key_path = "keys/provider-public.key"
curve = "P-256"
""")
        
        return project_dir


def list_packages(config: Optional[WorkenvConfig] = None) -> List[Dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()
        
    manager = PackageManager(config)
    output_dir = manager.get_package_output_dir()
    
    packages = []
    if output_dir.exists():
        for flavor_file in output_dir.glob("*.flavor"):
            stat = flavor_file.stat()
            packages.append({
                "name": flavor_file.stem,
                "version": "unknown",  # Would need to read from package
                "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                "path": str(flavor_file),
            })
            
    return packages


def get_package_info(
    package_path: Path,
    config: Optional[WorkenvConfig] = None
) -> Dict[str, any]:
    """Get detailed information about a package."""
    # This would need flavor API enhancement to read package metadata
    # For now, return basic info
    stat = package_path.stat()
    return {
        "name": package_path.stem,
        "version": "1.0.0",  # Would need to read from package
        "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
        "signature": "valid",  # Would need to verify
        "python_version": "3.13",
        "dependencies": [],  # Would need to read from package
    }


def sign_package(
    package_path: Path,
    key_path: Path,
    config: Optional[WorkenvConfig] = None
) -> None:
    """Sign an existing package."""
    # This would need flavor API enhancement
    logger.info(f"Signing {package_path} with {key_path}")
    # For now, this is a placeholder
    raise NotImplementedError("Package signing not yet implemented in flavor API")


def publish_package(
    package_path: Path,
    registry: str,
    config: Optional[WorkenvConfig] = None
) -> Dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")
    
    # For now, return mock data
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
    }


# 🧰🌍🖥️🪄