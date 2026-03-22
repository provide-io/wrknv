# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#
# wrknv/env/package/commands.py
#
"""
Package Commands Implementation
===============================
Command implementations for package management using flavorpack Python API.
"""

from pathlib import Path
import shutil
from typing import Any

from provide.foundation import logger

from wrknv.config import WorkenvConfig

from .manager import PackageManager
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


def x__check_flavor_installed__mutmut_orig() -> None:
    """Check if flavorpack is installed."""
    try:
        import flavor  # noqa: F401
    except ImportError as e:
        raise ImportError("flavorpack not installed. Install it with: uv tool install flavorpack") from e


def x__check_flavor_installed__mutmut_1() -> None:
    """Check if flavorpack is installed."""
    try:
        import flavor  # noqa: F401
    except ImportError as e:
        raise ImportError(None) from e


def x__check_flavor_installed__mutmut_2() -> None:
    """Check if flavorpack is installed."""
    try:
        import flavor  # noqa: F401
    except ImportError as e:
        raise ImportError("XXflavorpack not installed. Install it with: uv tool install flavorpackXX") from e


def x__check_flavor_installed__mutmut_3() -> None:
    """Check if flavorpack is installed."""
    try:
        import flavor  # noqa: F401
    except ImportError as e:
        raise ImportError("flavorpack not installed. install it with: uv tool install flavorpack") from e


def x__check_flavor_installed__mutmut_4() -> None:
    """Check if flavorpack is installed."""
    try:
        import flavor  # noqa: F401
    except ImportError as e:
        raise ImportError("FLAVORPACK NOT INSTALLED. INSTALL IT WITH: UV TOOL INSTALL FLAVORPACK") from e

x__check_flavor_installed__mutmut_mutants : ClassVar[MutantDict] = {
'x__check_flavor_installed__mutmut_1': x__check_flavor_installed__mutmut_1, 
    'x__check_flavor_installed__mutmut_2': x__check_flavor_installed__mutmut_2, 
    'x__check_flavor_installed__mutmut_3': x__check_flavor_installed__mutmut_3, 
    'x__check_flavor_installed__mutmut_4': x__check_flavor_installed__mutmut_4
}

def _check_flavor_installed(*args, **kwargs):
    result = _mutmut_trampoline(x__check_flavor_installed__mutmut_orig, x__check_flavor_installed__mutmut_mutants, args, kwargs)
    return result 

_check_flavor_installed.__signature__ = _mutmut_signature(x__check_flavor_installed__mutmut_orig)
x__check_flavor_installed__mutmut_orig.__name__ = 'x__check_flavor_installed'


def x_build_package__mutmut_orig(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_1(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = True
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_2(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(None)
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_3(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" * "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_4(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent * "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_5(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "XXdistXX" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_6(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "DIST" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_7(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "XXpackage.pspXX"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_8(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "PACKAGE.PSP"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_9(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is not None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_10(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = None

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_11(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = None

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_12(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(None)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_13(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = None
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_14(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = None
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_15(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is not None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_16(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(None)

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_17(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(None)}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_18(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = None

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_19(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(None)

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_20(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = None
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_21(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=None,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_22(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=None,
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_23(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=None,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_24(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_25(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_26(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_27(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent * "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_28(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "XXdistXX",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_29(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "DIST",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_30(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=False,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_31(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(None)
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_32(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = None
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_33(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(None)
        raise RuntimeError(f"Package build failed: {e}") from e


def x_build_package__mutmut_34(
    manifest_path: Path, config: WorkenvConfig | None = None, dry_run: bool = False
) -> list[Path]:
    """Build a package from manifest file."""
    if dry_run:
        logger.info(f"[DRY-RUN] Would build package from {manifest_path}")
        return [manifest_path.parent / "dist" / "package.psp"]

    _check_flavor_installed()

    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)

    # Check required tools
    tools = manager.check_required_tools()
    missing = {k: v for k, v in tools.items() if v is None}
    if missing:
        logger.warning(f"Missing required tools: {list(missing.keys())}")

    # Set up build environment (for environment variables)
    _env = manager.setup_build_environment()

    # Build using flavorpack Python API
    from flavor import build_package_from_manifest

    logger.info(f"Building package from {manifest_path}")

    try:
        packages = build_package_from_manifest(
            manifest_path=manifest_path,
            output_path=manifest_path.parent / "dist",
            show_progress=True,
        )
        logger.info(f"Successfully built {len(packages)} package(s)")
        built_packages: list[Path] = packages
        return built_packages
    except Exception as e:
        logger.error(f"Build failed: {e}")
        raise RuntimeError(None) from e

x_build_package__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_package__mutmut_1': x_build_package__mutmut_1, 
    'x_build_package__mutmut_2': x_build_package__mutmut_2, 
    'x_build_package__mutmut_3': x_build_package__mutmut_3, 
    'x_build_package__mutmut_4': x_build_package__mutmut_4, 
    'x_build_package__mutmut_5': x_build_package__mutmut_5, 
    'x_build_package__mutmut_6': x_build_package__mutmut_6, 
    'x_build_package__mutmut_7': x_build_package__mutmut_7, 
    'x_build_package__mutmut_8': x_build_package__mutmut_8, 
    'x_build_package__mutmut_9': x_build_package__mutmut_9, 
    'x_build_package__mutmut_10': x_build_package__mutmut_10, 
    'x_build_package__mutmut_11': x_build_package__mutmut_11, 
    'x_build_package__mutmut_12': x_build_package__mutmut_12, 
    'x_build_package__mutmut_13': x_build_package__mutmut_13, 
    'x_build_package__mutmut_14': x_build_package__mutmut_14, 
    'x_build_package__mutmut_15': x_build_package__mutmut_15, 
    'x_build_package__mutmut_16': x_build_package__mutmut_16, 
    'x_build_package__mutmut_17': x_build_package__mutmut_17, 
    'x_build_package__mutmut_18': x_build_package__mutmut_18, 
    'x_build_package__mutmut_19': x_build_package__mutmut_19, 
    'x_build_package__mutmut_20': x_build_package__mutmut_20, 
    'x_build_package__mutmut_21': x_build_package__mutmut_21, 
    'x_build_package__mutmut_22': x_build_package__mutmut_22, 
    'x_build_package__mutmut_23': x_build_package__mutmut_23, 
    'x_build_package__mutmut_24': x_build_package__mutmut_24, 
    'x_build_package__mutmut_25': x_build_package__mutmut_25, 
    'x_build_package__mutmut_26': x_build_package__mutmut_26, 
    'x_build_package__mutmut_27': x_build_package__mutmut_27, 
    'x_build_package__mutmut_28': x_build_package__mutmut_28, 
    'x_build_package__mutmut_29': x_build_package__mutmut_29, 
    'x_build_package__mutmut_30': x_build_package__mutmut_30, 
    'x_build_package__mutmut_31': x_build_package__mutmut_31, 
    'x_build_package__mutmut_32': x_build_package__mutmut_32, 
    'x_build_package__mutmut_33': x_build_package__mutmut_33, 
    'x_build_package__mutmut_34': x_build_package__mutmut_34
}

def build_package(*args, **kwargs):
    result = _mutmut_trampoline(x_build_package__mutmut_orig, x_build_package__mutmut_mutants, args, kwargs)
    return result 

build_package.__signature__ = _mutmut_signature(x_build_package__mutmut_orig)
x_build_package__mutmut_orig.__name__ = 'x_build_package'


def x_verify_package__mutmut_orig(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info("Package verification successful")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_1(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(None)

    try:
        result = flavor_verify(package_path)
        logger.info("Package verification successful")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_2(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = None
        logger.info("Package verification successful")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_3(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(None)
        logger.info("Package verification successful")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_4(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info(None)
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_5(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info("XXPackage verification successfulXX")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_6(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info("package verification successful")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_7(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info("PACKAGE VERIFICATION SUCCESSFUL")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_8(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info("Package verification successful")
        verified: dict[str, Any] = None
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_9(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info("Package verification successful")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(None)
        raise RuntimeError(f"Package verification failed: {e}") from e


def x_verify_package__mutmut_10(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Verify a package file."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Verifying package: {package_path}")

    try:
        result = flavor_verify(package_path)
        logger.info("Package verification successful")
        verified: dict[str, Any] = result
        return verified
    except Exception as e:
        logger.error(f"Package verification failed: {e}")
        raise RuntimeError(None) from e

x_verify_package__mutmut_mutants : ClassVar[MutantDict] = {
'x_verify_package__mutmut_1': x_verify_package__mutmut_1, 
    'x_verify_package__mutmut_2': x_verify_package__mutmut_2, 
    'x_verify_package__mutmut_3': x_verify_package__mutmut_3, 
    'x_verify_package__mutmut_4': x_verify_package__mutmut_4, 
    'x_verify_package__mutmut_5': x_verify_package__mutmut_5, 
    'x_verify_package__mutmut_6': x_verify_package__mutmut_6, 
    'x_verify_package__mutmut_7': x_verify_package__mutmut_7, 
    'x_verify_package__mutmut_8': x_verify_package__mutmut_8, 
    'x_verify_package__mutmut_9': x_verify_package__mutmut_9, 
    'x_verify_package__mutmut_10': x_verify_package__mutmut_10
}

def verify_package(*args, **kwargs):
    result = _mutmut_trampoline(x_verify_package__mutmut_orig, x_verify_package__mutmut_mutants, args, kwargs)
    return result 

verify_package.__signature__ = _mutmut_signature(x_verify_package__mutmut_orig)
x_verify_package__mutmut_orig.__name__ = 'x_verify_package'


def x_generate_keys__mutmut_orig(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_1(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=None, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_2(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=None)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_3(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_4(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, )

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_5(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=False, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_6(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=False)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_7(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(None)

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_8(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = None
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_9(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(None)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_10(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(None)
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_11(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(None)
        raise RuntimeError(f"Key generation failed: {e}") from e


def x_generate_keys__mutmut_12(output_dir: Path, config: WorkenvConfig | None = None) -> tuple[Path, Path]:
    """Generate signing key pair."""
    _check_flavor_installed()

    from flavor.packaging import generate_key_pair

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Generating signing keys in {output_dir}")

    try:
        private_key, public_key = generate_key_pair(output_dir)
        logger.info(f"Generated key pair: {private_key.name}, {public_key.name}")
        return (private_key, public_key)
    except Exception as e:
        logger.error(f"Key generation failed: {e}")
        raise RuntimeError(None) from e

x_generate_keys__mutmut_mutants : ClassVar[MutantDict] = {
'x_generate_keys__mutmut_1': x_generate_keys__mutmut_1, 
    'x_generate_keys__mutmut_2': x_generate_keys__mutmut_2, 
    'x_generate_keys__mutmut_3': x_generate_keys__mutmut_3, 
    'x_generate_keys__mutmut_4': x_generate_keys__mutmut_4, 
    'x_generate_keys__mutmut_5': x_generate_keys__mutmut_5, 
    'x_generate_keys__mutmut_6': x_generate_keys__mutmut_6, 
    'x_generate_keys__mutmut_7': x_generate_keys__mutmut_7, 
    'x_generate_keys__mutmut_8': x_generate_keys__mutmut_8, 
    'x_generate_keys__mutmut_9': x_generate_keys__mutmut_9, 
    'x_generate_keys__mutmut_10': x_generate_keys__mutmut_10, 
    'x_generate_keys__mutmut_11': x_generate_keys__mutmut_11, 
    'x_generate_keys__mutmut_12': x_generate_keys__mutmut_12
}

def generate_keys(*args, **kwargs):
    result = _mutmut_trampoline(x_generate_keys__mutmut_orig, x_generate_keys__mutmut_mutants, args, kwargs)
    return result 

generate_keys.__signature__ = _mutmut_signature(x_generate_keys__mutmut_orig)
x_generate_keys__mutmut_orig.__name__ = 'x_generate_keys'


def x_clean_cache__mutmut_orig(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_1(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info(None)
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_2(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("XXCleaning flavor cache...XX")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_3(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_4(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("CLEANING FLAVOR CACHE...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_5(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info(None)
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_6(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("XXFlavor cache cleanedXX")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_7(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_8(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("FLAVOR CACHE CLEANED")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_9(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(None)

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_10(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is not None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_11(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = None
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_12(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = None
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_13(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(None)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_14(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = None
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_15(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(None, ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_16(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=None)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_17(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(ignore_errors=True)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_18(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, )
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_19(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=False)
        logger.info(f"Cleaned package cache at {cache_dir}")


def x_clean_cache__mutmut_20(config: WorkenvConfig | None = None) -> None:
    """Clean package build cache."""
    _check_flavor_installed()

    from flavor import clean_cache as flavor_clean

    # Clean flavor cache
    logger.info("Cleaning flavor cache...")
    try:
        flavor_clean()
        logger.info("Flavor cache cleaned")
    except Exception as e:
        logger.warning(f"Failed to clean flavor cache: {e}")

    # Clean wrknv package cache
    if config is None:
        config = WorkenvConfig()
    manager = PackageManager(config)
    cache_dir = manager.get_package_cache_dir()
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
        logger.info(None)

x_clean_cache__mutmut_mutants : ClassVar[MutantDict] = {
'x_clean_cache__mutmut_1': x_clean_cache__mutmut_1, 
    'x_clean_cache__mutmut_2': x_clean_cache__mutmut_2, 
    'x_clean_cache__mutmut_3': x_clean_cache__mutmut_3, 
    'x_clean_cache__mutmut_4': x_clean_cache__mutmut_4, 
    'x_clean_cache__mutmut_5': x_clean_cache__mutmut_5, 
    'x_clean_cache__mutmut_6': x_clean_cache__mutmut_6, 
    'x_clean_cache__mutmut_7': x_clean_cache__mutmut_7, 
    'x_clean_cache__mutmut_8': x_clean_cache__mutmut_8, 
    'x_clean_cache__mutmut_9': x_clean_cache__mutmut_9, 
    'x_clean_cache__mutmut_10': x_clean_cache__mutmut_10, 
    'x_clean_cache__mutmut_11': x_clean_cache__mutmut_11, 
    'x_clean_cache__mutmut_12': x_clean_cache__mutmut_12, 
    'x_clean_cache__mutmut_13': x_clean_cache__mutmut_13, 
    'x_clean_cache__mutmut_14': x_clean_cache__mutmut_14, 
    'x_clean_cache__mutmut_15': x_clean_cache__mutmut_15, 
    'x_clean_cache__mutmut_16': x_clean_cache__mutmut_16, 
    'x_clean_cache__mutmut_17': x_clean_cache__mutmut_17, 
    'x_clean_cache__mutmut_18': x_clean_cache__mutmut_18, 
    'x_clean_cache__mutmut_19': x_clean_cache__mutmut_19, 
    'x_clean_cache__mutmut_20': x_clean_cache__mutmut_20
}

def clean_cache(*args, **kwargs):
    result = _mutmut_trampoline(x_clean_cache__mutmut_orig, x_clean_cache__mutmut_mutants, args, kwargs)
    return result 

clean_cache.__signature__ = _mutmut_signature(x_clean_cache__mutmut_orig)
x_clean_cache__mutmut_orig.__name__ = 'x_clean_cache'


def x_init_provider__mutmut_orig(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
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


def x_init_provider__mutmut_1(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=None, exist_ok=True)

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


def x_init_provider__mutmut_2(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=None)

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


def x_init_provider__mutmut_3(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(exist_ok=True)

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


def x_init_provider__mutmut_4(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, )

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


def x_init_provider__mutmut_5(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=False, exist_ok=True)

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


def x_init_provider__mutmut_6(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=False)

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


def x_init_provider__mutmut_7(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=None)
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


def x_init_provider__mutmut_8(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir * "src").mkdir(exist_ok=True)
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


def x_init_provider__mutmut_9(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "XXsrcXX").mkdir(exist_ok=True)
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


def x_init_provider__mutmut_10(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "SRC").mkdir(exist_ok=True)
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


def x_init_provider__mutmut_11(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=False)
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


def x_init_provider__mutmut_12(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=None)
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


def x_init_provider__mutmut_13(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir * "tests").mkdir(exist_ok=True)
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


def x_init_provider__mutmut_14(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "XXtestsXX").mkdir(exist_ok=True)
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


def x_init_provider__mutmut_15(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "TESTS").mkdir(exist_ok=True)
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


def x_init_provider__mutmut_16(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=False)
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


def x_init_provider__mutmut_17(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "keys").mkdir(exist_ok=None)

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


def x_init_provider__mutmut_18(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir * "keys").mkdir(exist_ok=True)

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


def x_init_provider__mutmut_19(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "XXkeysXX").mkdir(exist_ok=True)

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


def x_init_provider__mutmut_20(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "KEYS").mkdir(exist_ok=True)

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


def x_init_provider__mutmut_21(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "keys").mkdir(exist_ok=False)

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


def x_init_provider__mutmut_22(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "keys").mkdir(exist_ok=True)

    # Create basic pyproject.toml
    pyproject = None
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


def x_init_provider__mutmut_23(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "keys").mkdir(exist_ok=True)

    # Create basic pyproject.toml
    pyproject = project_dir * "pyproject.toml"
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


def x_init_provider__mutmut_24(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "keys").mkdir(exist_ok=True)

    # Create basic pyproject.toml
    pyproject = project_dir / "XXpyproject.tomlXX"
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


def x_init_provider__mutmut_25(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
    """Initialize a new provider project."""
    # Basic project scaffolding
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create basic structure
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "keys").mkdir(exist_ok=True)

    # Create basic pyproject.toml
    pyproject = project_dir / "PYPROJECT.TOML"
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


def x_init_provider__mutmut_26(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
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
        None
    )

    logger.info(f"Initialized provider project at {project_dir}")
    return project_dir


def x_init_provider__mutmut_27(project_dir: Path, config: WorkenvConfig | None = None) -> Path:
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

    logger.info(None)
    return project_dir

x_init_provider__mutmut_mutants : ClassVar[MutantDict] = {
'x_init_provider__mutmut_1': x_init_provider__mutmut_1, 
    'x_init_provider__mutmut_2': x_init_provider__mutmut_2, 
    'x_init_provider__mutmut_3': x_init_provider__mutmut_3, 
    'x_init_provider__mutmut_4': x_init_provider__mutmut_4, 
    'x_init_provider__mutmut_5': x_init_provider__mutmut_5, 
    'x_init_provider__mutmut_6': x_init_provider__mutmut_6, 
    'x_init_provider__mutmut_7': x_init_provider__mutmut_7, 
    'x_init_provider__mutmut_8': x_init_provider__mutmut_8, 
    'x_init_provider__mutmut_9': x_init_provider__mutmut_9, 
    'x_init_provider__mutmut_10': x_init_provider__mutmut_10, 
    'x_init_provider__mutmut_11': x_init_provider__mutmut_11, 
    'x_init_provider__mutmut_12': x_init_provider__mutmut_12, 
    'x_init_provider__mutmut_13': x_init_provider__mutmut_13, 
    'x_init_provider__mutmut_14': x_init_provider__mutmut_14, 
    'x_init_provider__mutmut_15': x_init_provider__mutmut_15, 
    'x_init_provider__mutmut_16': x_init_provider__mutmut_16, 
    'x_init_provider__mutmut_17': x_init_provider__mutmut_17, 
    'x_init_provider__mutmut_18': x_init_provider__mutmut_18, 
    'x_init_provider__mutmut_19': x_init_provider__mutmut_19, 
    'x_init_provider__mutmut_20': x_init_provider__mutmut_20, 
    'x_init_provider__mutmut_21': x_init_provider__mutmut_21, 
    'x_init_provider__mutmut_22': x_init_provider__mutmut_22, 
    'x_init_provider__mutmut_23': x_init_provider__mutmut_23, 
    'x_init_provider__mutmut_24': x_init_provider__mutmut_24, 
    'x_init_provider__mutmut_25': x_init_provider__mutmut_25, 
    'x_init_provider__mutmut_26': x_init_provider__mutmut_26, 
    'x_init_provider__mutmut_27': x_init_provider__mutmut_27
}

def init_provider(*args, **kwargs):
    result = _mutmut_trampoline(x_init_provider__mutmut_orig, x_init_provider__mutmut_mutants, args, kwargs)
    return result 

init_provider.__signature__ = _mutmut_signature(x_init_provider__mutmut_orig)
x_init_provider__mutmut_orig.__name__ = 'x_init_provider'


def x_list_packages__mutmut_orig(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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


def x_list_packages__mutmut_1(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is not None:
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


def x_list_packages__mutmut_2(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = None

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


def x_list_packages__mutmut_3(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = None
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


def x_list_packages__mutmut_4(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(None)
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


def x_list_packages__mutmut_5(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)
    output_dir = None

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


def x_list_packages__mutmut_6(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)
    output_dir = manager.get_package_output_dir()

    packages = None
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


def x_list_packages__mutmut_7(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)
    output_dir = manager.get_package_output_dir()

    packages = []
    if output_dir.exists():
        for psp_file in output_dir.glob(None):
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


def x_list_packages__mutmut_8(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)
    output_dir = manager.get_package_output_dir()

    packages = []
    if output_dir.exists():
        for psp_file in output_dir.glob("XX*.pspXX"):
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


def x_list_packages__mutmut_9(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)
    output_dir = manager.get_package_output_dir()

    packages = []
    if output_dir.exists():
        for psp_file in output_dir.glob("*.PSP"):
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


def x_list_packages__mutmut_10(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
    """List built packages."""
    if config is None:
        config = WorkenvConfig()

    manager = PackageManager(config)
    output_dir = manager.get_package_output_dir()

    packages = []
    if output_dir.exists():
        for psp_file in output_dir.glob("*.psp"):
            stat = None
            packages.append(
                {
                    "name": psp_file.stem,
                    "version": "unknown",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_11(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                None
            )

    return packages


def x_list_packages__mutmut_12(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "XXnameXX": psp_file.stem,
                    "version": "unknown",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_13(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "NAME": psp_file.stem,
                    "version": "unknown",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_14(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "XXversionXX": "unknown",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_15(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "VERSION": "unknown",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_16(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "version": "XXunknownXX",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_17(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "version": "UNKNOWN",  # Would need to inspect package
                    "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_18(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "XXsizeXX": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_19(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "SIZE": f"{stat.st_size / 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_20(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "size": f"{stat.st_size / 1024 * 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_21(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "size": f"{stat.st_size * 1024 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_22(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "size": f"{stat.st_size / 1025 / 1024:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_23(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "size": f"{stat.st_size / 1024 / 1025:.1f}MB",
                    "path": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_24(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "XXpathXX": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_25(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "PATH": str(psp_file),
                }
            )

    return packages


def x_list_packages__mutmut_26(config: WorkenvConfig | None = None) -> list[dict[str, str]]:
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
                    "path": str(None),
                }
            )

    return packages

x_list_packages__mutmut_mutants : ClassVar[MutantDict] = {
'x_list_packages__mutmut_1': x_list_packages__mutmut_1, 
    'x_list_packages__mutmut_2': x_list_packages__mutmut_2, 
    'x_list_packages__mutmut_3': x_list_packages__mutmut_3, 
    'x_list_packages__mutmut_4': x_list_packages__mutmut_4, 
    'x_list_packages__mutmut_5': x_list_packages__mutmut_5, 
    'x_list_packages__mutmut_6': x_list_packages__mutmut_6, 
    'x_list_packages__mutmut_7': x_list_packages__mutmut_7, 
    'x_list_packages__mutmut_8': x_list_packages__mutmut_8, 
    'x_list_packages__mutmut_9': x_list_packages__mutmut_9, 
    'x_list_packages__mutmut_10': x_list_packages__mutmut_10, 
    'x_list_packages__mutmut_11': x_list_packages__mutmut_11, 
    'x_list_packages__mutmut_12': x_list_packages__mutmut_12, 
    'x_list_packages__mutmut_13': x_list_packages__mutmut_13, 
    'x_list_packages__mutmut_14': x_list_packages__mutmut_14, 
    'x_list_packages__mutmut_15': x_list_packages__mutmut_15, 
    'x_list_packages__mutmut_16': x_list_packages__mutmut_16, 
    'x_list_packages__mutmut_17': x_list_packages__mutmut_17, 
    'x_list_packages__mutmut_18': x_list_packages__mutmut_18, 
    'x_list_packages__mutmut_19': x_list_packages__mutmut_19, 
    'x_list_packages__mutmut_20': x_list_packages__mutmut_20, 
    'x_list_packages__mutmut_21': x_list_packages__mutmut_21, 
    'x_list_packages__mutmut_22': x_list_packages__mutmut_22, 
    'x_list_packages__mutmut_23': x_list_packages__mutmut_23, 
    'x_list_packages__mutmut_24': x_list_packages__mutmut_24, 
    'x_list_packages__mutmut_25': x_list_packages__mutmut_25, 
    'x_list_packages__mutmut_26': x_list_packages__mutmut_26
}

def list_packages(*args, **kwargs):
    result = _mutmut_trampoline(x_list_packages__mutmut_orig, x_list_packages__mutmut_mutants, args, kwargs)
    return result 

list_packages.__signature__ = _mutmut_signature(x_list_packages__mutmut_orig)
x_list_packages__mutmut_orig.__name__ = 'x_list_packages'


def x_get_package_info__mutmut_orig(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_1(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(None)

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_2(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = None

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_3(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(None)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_4(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = None
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_5(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "XXnameXX": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_6(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "NAME": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_7(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "XXsizeXX": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_8(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "SIZE": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_9(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 * 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_10(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size * 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_11(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1025 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_12(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1025:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_13(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "XXpathXX": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_14(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "PATH": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_15(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(None),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_16(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "XXverificationXX": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_17(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "VERIFICATION": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_18(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(None)
        raise RuntimeError(f"Package inspection failed: {e}") from e


def x_get_package_info__mutmut_19(package_path: Path, config: WorkenvConfig | None = None) -> dict[str, Any]:
    """Get detailed information about a package."""
    _check_flavor_installed()

    from flavor import verify_package as flavor_verify

    logger.info(f"Inspecting package: {package_path}")

    try:
        # verify_package returns package metadata including verification info
        verification_result = flavor_verify(package_path)

        stat = package_path.stat()
        return {
            "name": package_path.stem,
            "size": f"{stat.st_size / 1024 / 1024:.1f}MB",
            "path": str(package_path),
            "verification": verification_result,
        }
    except Exception as e:
        logger.error(f"Package inspection failed: {e}")
        raise RuntimeError(None) from e

x_get_package_info__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_package_info__mutmut_1': x_get_package_info__mutmut_1, 
    'x_get_package_info__mutmut_2': x_get_package_info__mutmut_2, 
    'x_get_package_info__mutmut_3': x_get_package_info__mutmut_3, 
    'x_get_package_info__mutmut_4': x_get_package_info__mutmut_4, 
    'x_get_package_info__mutmut_5': x_get_package_info__mutmut_5, 
    'x_get_package_info__mutmut_6': x_get_package_info__mutmut_6, 
    'x_get_package_info__mutmut_7': x_get_package_info__mutmut_7, 
    'x_get_package_info__mutmut_8': x_get_package_info__mutmut_8, 
    'x_get_package_info__mutmut_9': x_get_package_info__mutmut_9, 
    'x_get_package_info__mutmut_10': x_get_package_info__mutmut_10, 
    'x_get_package_info__mutmut_11': x_get_package_info__mutmut_11, 
    'x_get_package_info__mutmut_12': x_get_package_info__mutmut_12, 
    'x_get_package_info__mutmut_13': x_get_package_info__mutmut_13, 
    'x_get_package_info__mutmut_14': x_get_package_info__mutmut_14, 
    'x_get_package_info__mutmut_15': x_get_package_info__mutmut_15, 
    'x_get_package_info__mutmut_16': x_get_package_info__mutmut_16, 
    'x_get_package_info__mutmut_17': x_get_package_info__mutmut_17, 
    'x_get_package_info__mutmut_18': x_get_package_info__mutmut_18, 
    'x_get_package_info__mutmut_19': x_get_package_info__mutmut_19
}

def get_package_info(*args, **kwargs):
    result = _mutmut_trampoline(x_get_package_info__mutmut_orig, x_get_package_info__mutmut_mutants, args, kwargs)
    return result 

get_package_info.__signature__ = _mutmut_signature(x_get_package_info__mutmut_orig)
x_get_package_info__mutmut_orig.__name__ = 'x_get_package_info'


def x_sign_package__mutmut_orig(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_1(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info(None)
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_2(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("XXPackage signing is done during build with signing keysXX")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_3(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_4(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("PACKAGE SIGNING IS DONE DURING BUILD WITH SIGNING KEYS")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_5(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(None)
    raise NotImplementedError(
        "Package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_6(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        None
    )


def x_sign_package__mutmut_7(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "XXPackage signing is performed during build. XX"
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_8(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "package signing is performed during build. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_9(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "PACKAGE SIGNING IS PERFORMED DURING BUILD. "
        "Use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_10(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "XXUse 'wrknv package build' with signing keys configured in pyproject.tomlXX"
    )


def x_sign_package__mutmut_11(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "use 'wrknv package build' with signing keys configured in pyproject.toml"
    )


def x_sign_package__mutmut_12(package_path: Path, key_path: Path, config: WorkenvConfig | None = None) -> None:
    """Sign an existing package."""
    # Flavor packages are signed during the pack process
    logger.info("Package signing is done during build with signing keys")
    logger.info(f"To sign {package_path}, rebuild with signing keys configured")
    raise NotImplementedError(
        "Package signing is performed during build. "
        "USE 'WRKNV PACKAGE BUILD' WITH SIGNING KEYS CONFIGURED IN PYPROJECT.TOML"
    )

x_sign_package__mutmut_mutants : ClassVar[MutantDict] = {
'x_sign_package__mutmut_1': x_sign_package__mutmut_1, 
    'x_sign_package__mutmut_2': x_sign_package__mutmut_2, 
    'x_sign_package__mutmut_3': x_sign_package__mutmut_3, 
    'x_sign_package__mutmut_4': x_sign_package__mutmut_4, 
    'x_sign_package__mutmut_5': x_sign_package__mutmut_5, 
    'x_sign_package__mutmut_6': x_sign_package__mutmut_6, 
    'x_sign_package__mutmut_7': x_sign_package__mutmut_7, 
    'x_sign_package__mutmut_8': x_sign_package__mutmut_8, 
    'x_sign_package__mutmut_9': x_sign_package__mutmut_9, 
    'x_sign_package__mutmut_10': x_sign_package__mutmut_10, 
    'x_sign_package__mutmut_11': x_sign_package__mutmut_11, 
    'x_sign_package__mutmut_12': x_sign_package__mutmut_12
}

def sign_package(*args, **kwargs):
    result = _mutmut_trampoline(x_sign_package__mutmut_orig, x_sign_package__mutmut_mutants, args, kwargs)
    return result 

sign_package.__signature__ = _mutmut_signature(x_sign_package__mutmut_orig)
x_sign_package__mutmut_orig.__name__ = 'x_sign_package'


def x_publish_package__mutmut_orig(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
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


def x_publish_package__mutmut_1(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(None)

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "status": "mock",
    }


def x_publish_package__mutmut_2(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "XXurlXX": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "status": "mock",
    }


def x_publish_package__mutmut_3(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "URL": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "status": "mock",
    }


def x_publish_package__mutmut_4(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "XXsha256XX": "abc123def456",  # Would calculate real hash
        "status": "mock",
    }


def x_publish_package__mutmut_5(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "SHA256": "abc123def456",  # Would calculate real hash
        "status": "mock",
    }


def x_publish_package__mutmut_6(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "XXabc123def456XX",  # Would calculate real hash
        "status": "mock",
    }


def x_publish_package__mutmut_7(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "ABC123DEF456",  # Would calculate real hash
        "status": "mock",
    }


def x_publish_package__mutmut_8(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "XXstatusXX": "mock",
    }


def x_publish_package__mutmut_9(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "STATUS": "mock",
    }


def x_publish_package__mutmut_10(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "status": "XXmockXX",
    }


def x_publish_package__mutmut_11(package_path: Path, registry: str, config: WorkenvConfig | None = None) -> dict[str, str]:
    """Publish package to a registry."""
    # This would need a registry client implementation
    logger.info(f"Publishing {package_path} to {registry}")

    # For now, return mock data
    # TODO: Implement actual registry publishing
    return {
        "url": f"https://{registry}.example.com/{package_path.stem}",
        "sha256": "abc123def456",  # Would calculate real hash
        "status": "MOCK",
    }

x_publish_package__mutmut_mutants : ClassVar[MutantDict] = {
'x_publish_package__mutmut_1': x_publish_package__mutmut_1, 
    'x_publish_package__mutmut_2': x_publish_package__mutmut_2, 
    'x_publish_package__mutmut_3': x_publish_package__mutmut_3, 
    'x_publish_package__mutmut_4': x_publish_package__mutmut_4, 
    'x_publish_package__mutmut_5': x_publish_package__mutmut_5, 
    'x_publish_package__mutmut_6': x_publish_package__mutmut_6, 
    'x_publish_package__mutmut_7': x_publish_package__mutmut_7, 
    'x_publish_package__mutmut_8': x_publish_package__mutmut_8, 
    'x_publish_package__mutmut_9': x_publish_package__mutmut_9, 
    'x_publish_package__mutmut_10': x_publish_package__mutmut_10, 
    'x_publish_package__mutmut_11': x_publish_package__mutmut_11
}

def publish_package(*args, **kwargs):
    result = _mutmut_trampoline(x_publish_package__mutmut_orig, x_publish_package__mutmut_mutants, args, kwargs)
    return result 

publish_package.__signature__ = _mutmut_signature(x_publish_package__mutmut_orig)
x_publish_package__mutmut_orig.__name__ = 'x_publish_package'


# 🧰🌍🖥️🪄
