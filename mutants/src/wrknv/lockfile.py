#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Lockfile Management
==================
Manage wrknv.lock files for reproducible environments."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from attrs import define, field

from wrknv.config import WorkenvConfig
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


@define
class ResolvedTool:
    """A resolved tool with exact version and metadata."""

    name: str
    version: str
    resolved_from: str  # Original pattern like "1.11.x"
    checksum: str | None = None
    installed_at: str | None = None  # ISO timestamp
    install_path: str | None = None


@define
class Lockfile:
    """Represents a wrknv.lock file."""

    config_checksum: str  # Hash of the config that generated this lock
    resolved_tools: dict[str, ResolvedTool] = field(factory=dict)
    created_at: str | None = None  # ISO timestamp
    wrknv_version: str = "0.3.0"

    @classmethod
    def from_config(cls, config: WorkenvConfig) -> Lockfile:
        """Create a lockfile from a config."""
        from provide.foundation.time import provide_now

        # Calculate config checksum
        config_dict = config.to_dict()
        config_str = str(sorted(config_dict.items()))
        config_checksum = hashlib.sha256(config_str.encode()).hexdigest()[:12]

        return cls(
            config_checksum=config_checksum,
            created_at=provide_now().isoformat(),
        )

    def add_resolved_tool(
        self,
        name: str,
        version: str,
        resolved_from: str,
        checksum: str | None = None,
        install_path: str | None = None,
    ) -> None:
        """Add a resolved tool to the lockfile."""
        from provide.foundation.time import provide_now

        self.resolved_tools[name] = ResolvedTool(
            name=name,
            version=version,
            resolved_from=resolved_from,
            checksum=checksum,
            installed_at=provide_now().isoformat(),
            install_path=install_path,
        )

    def get_resolved_version(self, tool_name: str) -> str | None:
        """Get the resolved version for a tool."""
        tool = self.resolved_tools.get(tool_name)
        return tool.version if tool else None

    def is_tool_installed(self, tool_name: str) -> bool:
        """Check if a tool is marked as installed."""
        tool = self.resolved_tools.get(tool_name)
        return tool is not None and tool.installed_at is not None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "config_checksum": self.config_checksum,
            "created_at": self.created_at,
            "wrknv_version": self.wrknv_version,
            "resolved_tools": {
                name: {
                    "name": tool.name,
                    "version": tool.version,
                    "resolved_from": tool.resolved_from,
                    "checksum": tool.checksum,
                    "installed_at": tool.installed_at,
                    "install_path": tool.install_path,
                }
                for name, tool in self.resolved_tools.items()
            },
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Lockfile:
        """Create from dictionary."""
        resolved_tools = {}
        for name, tool_data in data.get("resolved_tools", {}).items():
            resolved_tools[name] = ResolvedTool(
                name=tool_data["name"],
                version=tool_data["version"],
                resolved_from=tool_data["resolved_from"],
                checksum=tool_data.get("checksum"),
                installed_at=tool_data.get("installed_at"),
                install_path=tool_data.get("install_path"),
            )

        return cls(
            config_checksum=data["config_checksum"],
            resolved_tools=resolved_tools,
            created_at=data.get("created_at"),
            wrknv_version=data.get("wrknv_version", "0.3.0"),
        )


class LockfileManager:
    """Manages wrknv.lock files."""

    def xǁLockfileManagerǁ__init____mutmut_orig(self, project_dir: Path = Path.cwd()) -> None:
        self.project_dir = project_dir
        self.lockfile_path = project_dir / "wrknv.lock"

    def xǁLockfileManagerǁ__init____mutmut_1(self, project_dir: Path = Path.cwd()) -> None:
        self.project_dir = None
        self.lockfile_path = project_dir / "wrknv.lock"

    def xǁLockfileManagerǁ__init____mutmut_2(self, project_dir: Path = Path.cwd()) -> None:
        self.project_dir = project_dir
        self.lockfile_path = None

    def xǁLockfileManagerǁ__init____mutmut_3(self, project_dir: Path = Path.cwd()) -> None:
        self.project_dir = project_dir
        self.lockfile_path = project_dir * "wrknv.lock"

    def xǁLockfileManagerǁ__init____mutmut_4(self, project_dir: Path = Path.cwd()) -> None:
        self.project_dir = project_dir
        self.lockfile_path = project_dir / "XXwrknv.lockXX"

    def xǁLockfileManagerǁ__init____mutmut_5(self, project_dir: Path = Path.cwd()) -> None:
        self.project_dir = project_dir
        self.lockfile_path = project_dir / "WRKNV.LOCK"
    
    xǁLockfileManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLockfileManagerǁ__init____mutmut_1': xǁLockfileManagerǁ__init____mutmut_1, 
        'xǁLockfileManagerǁ__init____mutmut_2': xǁLockfileManagerǁ__init____mutmut_2, 
        'xǁLockfileManagerǁ__init____mutmut_3': xǁLockfileManagerǁ__init____mutmut_3, 
        'xǁLockfileManagerǁ__init____mutmut_4': xǁLockfileManagerǁ__init____mutmut_4, 
        'xǁLockfileManagerǁ__init____mutmut_5': xǁLockfileManagerǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLockfileManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁLockfileManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁLockfileManagerǁ__init____mutmut_orig)
    xǁLockfileManagerǁ__init____mutmut_orig.__name__ = 'xǁLockfileManagerǁ__init__'

    def xǁLockfileManagerǁload_lockfile__mutmut_orig(self) -> Lockfile | None:
        """Load existing lockfile."""
        if not self.lockfile_path.exists():
            return None

        try:
            import json

            with self.lockfile_path.open() as f:
                data = json.load(f)
            return Lockfile.from_dict(data)
        except (json.JSONDecodeError, KeyError, TypeError):
            # Corrupted lockfile - return None to regenerate
            return None

    def xǁLockfileManagerǁload_lockfile__mutmut_1(self) -> Lockfile | None:
        """Load existing lockfile."""
        if self.lockfile_path.exists():
            return None

        try:
            import json

            with self.lockfile_path.open() as f:
                data = json.load(f)
            return Lockfile.from_dict(data)
        except (json.JSONDecodeError, KeyError, TypeError):
            # Corrupted lockfile - return None to regenerate
            return None

    def xǁLockfileManagerǁload_lockfile__mutmut_2(self) -> Lockfile | None:
        """Load existing lockfile."""
        if not self.lockfile_path.exists():
            return None

        try:
            import json

            with self.lockfile_path.open() as f:
                data = None
            return Lockfile.from_dict(data)
        except (json.JSONDecodeError, KeyError, TypeError):
            # Corrupted lockfile - return None to regenerate
            return None

    def xǁLockfileManagerǁload_lockfile__mutmut_3(self) -> Lockfile | None:
        """Load existing lockfile."""
        if not self.lockfile_path.exists():
            return None

        try:
            import json

            with self.lockfile_path.open() as f:
                data = json.load(None)
            return Lockfile.from_dict(data)
        except (json.JSONDecodeError, KeyError, TypeError):
            # Corrupted lockfile - return None to regenerate
            return None

    def xǁLockfileManagerǁload_lockfile__mutmut_4(self) -> Lockfile | None:
        """Load existing lockfile."""
        if not self.lockfile_path.exists():
            return None

        try:
            import json

            with self.lockfile_path.open() as f:
                data = json.load(f)
            return Lockfile.from_dict(None)
        except (json.JSONDecodeError, KeyError, TypeError):
            # Corrupted lockfile - return None to regenerate
            return None
    
    xǁLockfileManagerǁload_lockfile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLockfileManagerǁload_lockfile__mutmut_1': xǁLockfileManagerǁload_lockfile__mutmut_1, 
        'xǁLockfileManagerǁload_lockfile__mutmut_2': xǁLockfileManagerǁload_lockfile__mutmut_2, 
        'xǁLockfileManagerǁload_lockfile__mutmut_3': xǁLockfileManagerǁload_lockfile__mutmut_3, 
        'xǁLockfileManagerǁload_lockfile__mutmut_4': xǁLockfileManagerǁload_lockfile__mutmut_4
    }
    
    def load_lockfile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLockfileManagerǁload_lockfile__mutmut_orig"), object.__getattribute__(self, "xǁLockfileManagerǁload_lockfile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    load_lockfile.__signature__ = _mutmut_signature(xǁLockfileManagerǁload_lockfile__mutmut_orig)
    xǁLockfileManagerǁload_lockfile__mutmut_orig.__name__ = 'xǁLockfileManagerǁload_lockfile'

    def xǁLockfileManagerǁsave_lockfile__mutmut_orig(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(lockfile.to_dict(), f, indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_1(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open(None) as f:
            json.dump(lockfile.to_dict(), f, indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_2(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("XXwXX") as f:
            json.dump(lockfile.to_dict(), f, indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_3(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("W") as f:
            json.dump(lockfile.to_dict(), f, indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_4(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(None, f, indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_5(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(lockfile.to_dict(), None, indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_6(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(lockfile.to_dict(), f, indent=None)

    def xǁLockfileManagerǁsave_lockfile__mutmut_7(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(f, indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_8(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(lockfile.to_dict(), indent=2)

    def xǁLockfileManagerǁsave_lockfile__mutmut_9(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(lockfile.to_dict(), f, )

    def xǁLockfileManagerǁsave_lockfile__mutmut_10(self, lockfile: Lockfile) -> None:
        """Save lockfile to disk."""
        import json

        with self.lockfile_path.open("w") as f:
            json.dump(lockfile.to_dict(), f, indent=3)
    
    xǁLockfileManagerǁsave_lockfile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLockfileManagerǁsave_lockfile__mutmut_1': xǁLockfileManagerǁsave_lockfile__mutmut_1, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_2': xǁLockfileManagerǁsave_lockfile__mutmut_2, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_3': xǁLockfileManagerǁsave_lockfile__mutmut_3, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_4': xǁLockfileManagerǁsave_lockfile__mutmut_4, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_5': xǁLockfileManagerǁsave_lockfile__mutmut_5, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_6': xǁLockfileManagerǁsave_lockfile__mutmut_6, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_7': xǁLockfileManagerǁsave_lockfile__mutmut_7, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_8': xǁLockfileManagerǁsave_lockfile__mutmut_8, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_9': xǁLockfileManagerǁsave_lockfile__mutmut_9, 
        'xǁLockfileManagerǁsave_lockfile__mutmut_10': xǁLockfileManagerǁsave_lockfile__mutmut_10
    }
    
    def save_lockfile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLockfileManagerǁsave_lockfile__mutmut_orig"), object.__getattribute__(self, "xǁLockfileManagerǁsave_lockfile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    save_lockfile.__signature__ = _mutmut_signature(xǁLockfileManagerǁsave_lockfile__mutmut_orig)
    xǁLockfileManagerǁsave_lockfile__mutmut_orig.__name__ = 'xǁLockfileManagerǁsave_lockfile'

    def xǁLockfileManagerǁcreate_lockfile__mutmut_orig(self, config: WorkenvConfig) -> Lockfile:
        """Create a new lockfile from config."""
        return Lockfile.from_config(config)

    def xǁLockfileManagerǁcreate_lockfile__mutmut_1(self, config: WorkenvConfig) -> Lockfile:
        """Create a new lockfile from config."""
        return Lockfile.from_config(None)
    
    xǁLockfileManagerǁcreate_lockfile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLockfileManagerǁcreate_lockfile__mutmut_1': xǁLockfileManagerǁcreate_lockfile__mutmut_1
    }
    
    def create_lockfile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLockfileManagerǁcreate_lockfile__mutmut_orig"), object.__getattribute__(self, "xǁLockfileManagerǁcreate_lockfile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_lockfile.__signature__ = _mutmut_signature(xǁLockfileManagerǁcreate_lockfile__mutmut_orig)
    xǁLockfileManagerǁcreate_lockfile__mutmut_orig.__name__ = 'xǁLockfileManagerǁcreate_lockfile'

    def xǁLockfileManagerǁis_lockfile_valid__mutmut_orig(self, config: WorkenvConfig) -> bool:
        """Check if lockfile is valid for current config."""
        lockfile = self.load_lockfile()
        if not lockfile:
            return False

        # Check config checksum
        current_lockfile = self.create_lockfile(config)
        return lockfile.config_checksum == current_lockfile.config_checksum

    def xǁLockfileManagerǁis_lockfile_valid__mutmut_1(self, config: WorkenvConfig) -> bool:
        """Check if lockfile is valid for current config."""
        lockfile = None
        if not lockfile:
            return False

        # Check config checksum
        current_lockfile = self.create_lockfile(config)
        return lockfile.config_checksum == current_lockfile.config_checksum

    def xǁLockfileManagerǁis_lockfile_valid__mutmut_2(self, config: WorkenvConfig) -> bool:
        """Check if lockfile is valid for current config."""
        lockfile = self.load_lockfile()
        if lockfile:
            return False

        # Check config checksum
        current_lockfile = self.create_lockfile(config)
        return lockfile.config_checksum == current_lockfile.config_checksum

    def xǁLockfileManagerǁis_lockfile_valid__mutmut_3(self, config: WorkenvConfig) -> bool:
        """Check if lockfile is valid for current config."""
        lockfile = self.load_lockfile()
        if not lockfile:
            return True

        # Check config checksum
        current_lockfile = self.create_lockfile(config)
        return lockfile.config_checksum == current_lockfile.config_checksum

    def xǁLockfileManagerǁis_lockfile_valid__mutmut_4(self, config: WorkenvConfig) -> bool:
        """Check if lockfile is valid for current config."""
        lockfile = self.load_lockfile()
        if not lockfile:
            return False

        # Check config checksum
        current_lockfile = None
        return lockfile.config_checksum == current_lockfile.config_checksum

    def xǁLockfileManagerǁis_lockfile_valid__mutmut_5(self, config: WorkenvConfig) -> bool:
        """Check if lockfile is valid for current config."""
        lockfile = self.load_lockfile()
        if not lockfile:
            return False

        # Check config checksum
        current_lockfile = self.create_lockfile(None)
        return lockfile.config_checksum == current_lockfile.config_checksum

    def xǁLockfileManagerǁis_lockfile_valid__mutmut_6(self, config: WorkenvConfig) -> bool:
        """Check if lockfile is valid for current config."""
        lockfile = self.load_lockfile()
        if not lockfile:
            return False

        # Check config checksum
        current_lockfile = self.create_lockfile(config)
        return lockfile.config_checksum != current_lockfile.config_checksum
    
    xǁLockfileManagerǁis_lockfile_valid__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLockfileManagerǁis_lockfile_valid__mutmut_1': xǁLockfileManagerǁis_lockfile_valid__mutmut_1, 
        'xǁLockfileManagerǁis_lockfile_valid__mutmut_2': xǁLockfileManagerǁis_lockfile_valid__mutmut_2, 
        'xǁLockfileManagerǁis_lockfile_valid__mutmut_3': xǁLockfileManagerǁis_lockfile_valid__mutmut_3, 
        'xǁLockfileManagerǁis_lockfile_valid__mutmut_4': xǁLockfileManagerǁis_lockfile_valid__mutmut_4, 
        'xǁLockfileManagerǁis_lockfile_valid__mutmut_5': xǁLockfileManagerǁis_lockfile_valid__mutmut_5, 
        'xǁLockfileManagerǁis_lockfile_valid__mutmut_6': xǁLockfileManagerǁis_lockfile_valid__mutmut_6
    }
    
    def is_lockfile_valid(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLockfileManagerǁis_lockfile_valid__mutmut_orig"), object.__getattribute__(self, "xǁLockfileManagerǁis_lockfile_valid__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_lockfile_valid.__signature__ = _mutmut_signature(xǁLockfileManagerǁis_lockfile_valid__mutmut_orig)
    xǁLockfileManagerǁis_lockfile_valid__mutmut_orig.__name__ = 'xǁLockfileManagerǁis_lockfile_valid'

    def xǁLockfileManagerǁresolve_and_lock__mutmut_orig(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_1(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = None
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_2(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile and not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_3(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_4(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_5(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(None):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_6(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = None

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_7(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(None)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_8(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = None
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_9(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = None

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_10(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(None, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_11(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, None)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_12(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_13(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, )

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_14(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = None
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_15(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(None, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_16(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, None)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_17(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_18(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, )
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_19(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=None,
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_20(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=None,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_21(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=None,
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_22(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_23(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_24(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_25(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(None),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_26(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = None
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_27(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(None, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_28(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, None)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_29(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_30(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, )
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_31(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = None
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_32(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[1]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_33(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=None, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_34(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=None, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_35(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=None
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_36(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_37(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_38(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_39(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                break

        # Save lockfile
        self.save_lockfile(lockfile)
        return lockfile

    def xǁLockfileManagerǁresolve_and_lock__mutmut_40(self, config: WorkenvConfig) -> Lockfile:
        """Resolve tool versions and create/update lockfile."""
        from wrknv.managers.factory import get_tool_manager
        from wrknv.utils.version_resolver import resolve_tool_versions

        # Load existing lockfile or create new one
        lockfile = self.load_lockfile()
        if not lockfile or not self.is_lockfile_valid(config):
            lockfile = self.create_lockfile(config)

        # Resolve each tool
        tools = config.get_all_tools()
        for tool_name, version_pattern in tools.items():
            try:
                manager = get_tool_manager(tool_name, config)

                # Handle matrix format (list of versions)
                if isinstance(version_pattern, list):
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    for resolved_version in resolved_versions:
                        lockfile.add_resolved_tool(
                            name=f"{tool_name}@{resolved_version}",
                            version=resolved_version,
                            resolved_from=str(version_pattern),
                        )
                else:
                    # Single version pattern
                    resolved_versions = resolve_tool_versions(manager, version_pattern)
                    if resolved_versions:
                        resolved_version = resolved_versions[0]
                        lockfile.add_resolved_tool(
                            name=tool_name, version=resolved_version, resolved_from=version_pattern
                        )
            except Exception:
                # nosec B112 - Skip tools that can't be resolved
                continue

        # Save lockfile
        self.save_lockfile(None)
        return lockfile
    
    xǁLockfileManagerǁresolve_and_lock__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLockfileManagerǁresolve_and_lock__mutmut_1': xǁLockfileManagerǁresolve_and_lock__mutmut_1, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_2': xǁLockfileManagerǁresolve_and_lock__mutmut_2, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_3': xǁLockfileManagerǁresolve_and_lock__mutmut_3, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_4': xǁLockfileManagerǁresolve_and_lock__mutmut_4, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_5': xǁLockfileManagerǁresolve_and_lock__mutmut_5, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_6': xǁLockfileManagerǁresolve_and_lock__mutmut_6, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_7': xǁLockfileManagerǁresolve_and_lock__mutmut_7, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_8': xǁLockfileManagerǁresolve_and_lock__mutmut_8, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_9': xǁLockfileManagerǁresolve_and_lock__mutmut_9, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_10': xǁLockfileManagerǁresolve_and_lock__mutmut_10, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_11': xǁLockfileManagerǁresolve_and_lock__mutmut_11, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_12': xǁLockfileManagerǁresolve_and_lock__mutmut_12, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_13': xǁLockfileManagerǁresolve_and_lock__mutmut_13, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_14': xǁLockfileManagerǁresolve_and_lock__mutmut_14, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_15': xǁLockfileManagerǁresolve_and_lock__mutmut_15, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_16': xǁLockfileManagerǁresolve_and_lock__mutmut_16, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_17': xǁLockfileManagerǁresolve_and_lock__mutmut_17, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_18': xǁLockfileManagerǁresolve_and_lock__mutmut_18, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_19': xǁLockfileManagerǁresolve_and_lock__mutmut_19, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_20': xǁLockfileManagerǁresolve_and_lock__mutmut_20, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_21': xǁLockfileManagerǁresolve_and_lock__mutmut_21, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_22': xǁLockfileManagerǁresolve_and_lock__mutmut_22, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_23': xǁLockfileManagerǁresolve_and_lock__mutmut_23, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_24': xǁLockfileManagerǁresolve_and_lock__mutmut_24, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_25': xǁLockfileManagerǁresolve_and_lock__mutmut_25, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_26': xǁLockfileManagerǁresolve_and_lock__mutmut_26, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_27': xǁLockfileManagerǁresolve_and_lock__mutmut_27, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_28': xǁLockfileManagerǁresolve_and_lock__mutmut_28, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_29': xǁLockfileManagerǁresolve_and_lock__mutmut_29, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_30': xǁLockfileManagerǁresolve_and_lock__mutmut_30, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_31': xǁLockfileManagerǁresolve_and_lock__mutmut_31, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_32': xǁLockfileManagerǁresolve_and_lock__mutmut_32, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_33': xǁLockfileManagerǁresolve_and_lock__mutmut_33, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_34': xǁLockfileManagerǁresolve_and_lock__mutmut_34, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_35': xǁLockfileManagerǁresolve_and_lock__mutmut_35, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_36': xǁLockfileManagerǁresolve_and_lock__mutmut_36, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_37': xǁLockfileManagerǁresolve_and_lock__mutmut_37, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_38': xǁLockfileManagerǁresolve_and_lock__mutmut_38, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_39': xǁLockfileManagerǁresolve_and_lock__mutmut_39, 
        'xǁLockfileManagerǁresolve_and_lock__mutmut_40': xǁLockfileManagerǁresolve_and_lock__mutmut_40
    }
    
    def resolve_and_lock(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLockfileManagerǁresolve_and_lock__mutmut_orig"), object.__getattribute__(self, "xǁLockfileManagerǁresolve_and_lock__mutmut_mutants"), args, kwargs, self)
        return result 
    
    resolve_and_lock.__signature__ = _mutmut_signature(xǁLockfileManagerǁresolve_and_lock__mutmut_orig)
    xǁLockfileManagerǁresolve_and_lock__mutmut_orig.__name__ = 'xǁLockfileManagerǁresolve_and_lock'

    def xǁLockfileManagerǁget_locked_versions__mutmut_orig(self) -> dict[str, str]:
        """Get locked versions for all tools."""
        lockfile = self.load_lockfile()
        if not lockfile:
            return {}

        return {tool.name: tool.version for tool in lockfile.resolved_tools.values()}

    def xǁLockfileManagerǁget_locked_versions__mutmut_1(self) -> dict[str, str]:
        """Get locked versions for all tools."""
        lockfile = None
        if not lockfile:
            return {}

        return {tool.name: tool.version for tool in lockfile.resolved_tools.values()}

    def xǁLockfileManagerǁget_locked_versions__mutmut_2(self) -> dict[str, str]:
        """Get locked versions for all tools."""
        lockfile = self.load_lockfile()
        if lockfile:
            return {}

        return {tool.name: tool.version for tool in lockfile.resolved_tools.values()}
    
    xǁLockfileManagerǁget_locked_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLockfileManagerǁget_locked_versions__mutmut_1': xǁLockfileManagerǁget_locked_versions__mutmut_1, 
        'xǁLockfileManagerǁget_locked_versions__mutmut_2': xǁLockfileManagerǁget_locked_versions__mutmut_2
    }
    
    def get_locked_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLockfileManagerǁget_locked_versions__mutmut_orig"), object.__getattribute__(self, "xǁLockfileManagerǁget_locked_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_locked_versions.__signature__ = _mutmut_signature(xǁLockfileManagerǁget_locked_versions__mutmut_orig)
    xǁLockfileManagerǁget_locked_versions__mutmut_orig.__name__ = 'xǁLockfileManagerǁget_locked_versions'


# 🧰🌍🔚
