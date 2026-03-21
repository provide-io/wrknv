#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Workspace Manager
================
Manage multi-repo workspaces with configuration synchronization."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from provide.foundation import logger
from provide.foundation.file import read_toml, write_toml

from .discovery import WorkspaceDiscovery
from .schema import RepoConfig, TemplateSource, WorkspaceConfig
from .sync import WorkspaceSync
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


class WorkspaceManager:
    """Manage multi-repo workspaces."""

    def xǁWorkspaceManagerǁ__init____mutmut_orig(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_1(self, root: Path | None = None) -> None:
        self.root = None
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_2(self, root: Path | None = None) -> None:
        self.root = root and Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_3(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = None
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_4(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root * ".wrknv"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_5(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / "XX.wrknvXX"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_6(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".WRKNV"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_7(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = None
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_8(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir * "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_9(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "XXworkspace.tomlXX"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_10(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "WORKSPACE.TOML"
        self.discovery = WorkspaceDiscovery(self.root)

    def xǁWorkspaceManagerǁ__init____mutmut_11(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = None

    def xǁWorkspaceManagerǁ__init____mutmut_12(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(None)
    
    xǁWorkspaceManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁ__init____mutmut_1': xǁWorkspaceManagerǁ__init____mutmut_1, 
        'xǁWorkspaceManagerǁ__init____mutmut_2': xǁWorkspaceManagerǁ__init____mutmut_2, 
        'xǁWorkspaceManagerǁ__init____mutmut_3': xǁWorkspaceManagerǁ__init____mutmut_3, 
        'xǁWorkspaceManagerǁ__init____mutmut_4': xǁWorkspaceManagerǁ__init____mutmut_4, 
        'xǁWorkspaceManagerǁ__init____mutmut_5': xǁWorkspaceManagerǁ__init____mutmut_5, 
        'xǁWorkspaceManagerǁ__init____mutmut_6': xǁWorkspaceManagerǁ__init____mutmut_6, 
        'xǁWorkspaceManagerǁ__init____mutmut_7': xǁWorkspaceManagerǁ__init____mutmut_7, 
        'xǁWorkspaceManagerǁ__init____mutmut_8': xǁWorkspaceManagerǁ__init____mutmut_8, 
        'xǁWorkspaceManagerǁ__init____mutmut_9': xǁWorkspaceManagerǁ__init____mutmut_9, 
        'xǁWorkspaceManagerǁ__init____mutmut_10': xǁWorkspaceManagerǁ__init____mutmut_10, 
        'xǁWorkspaceManagerǁ__init____mutmut_11': xǁWorkspaceManagerǁ__init____mutmut_11, 
        'xǁWorkspaceManagerǁ__init____mutmut_12': xǁWorkspaceManagerǁ__init____mutmut_12
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁ__init____mutmut_orig)
    xǁWorkspaceManagerǁ__init____mutmut_orig.__name__ = 'xǁWorkspaceManagerǁ__init__'

    def xǁWorkspaceManagerǁinit_workspace__mutmut_orig(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_1(
        self, template_source: str | None = None, auto_discover: bool = False
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_2(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info(None, root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_3(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=None)

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_4(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info(root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_5(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", )

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_6(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("XX🚀 Initializing workspaceXX", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_7(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_8(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 INITIALIZING WORKSPACE", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_9(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(None))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_10(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=None)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_11(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=False)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_12(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = None
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_13(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = None
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_14(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = None
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_15(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=None,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_16(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=None,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_17(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=None,
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_18(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=None,
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_19(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=None,
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_20(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_21(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_22(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_23(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_24(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_25(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name and repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_26(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type and "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_27(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "XXunknownXX",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_28(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "UNKNOWN",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_29(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(None),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_30(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(None),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_31(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info(None, count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_32(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=None)

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_33(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info(count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_34(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", )

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_35(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("XX📋 Auto-discovered repositoriesXX", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_36(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_37(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 AUTO-DISCOVERED REPOSITORIES", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_38(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = ""
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_39(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = None

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_40(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type=None,
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_41(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=None,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_42(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_43(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_44(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="XXlocalXX" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_45(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="LOCAL" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_46(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(None).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_47(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "XXgitXX",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_48(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "GIT",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_49(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = None

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_50(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=None,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_51(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=None,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_52(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=None,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_53(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=None,
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_54(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_55(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_56(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_57(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            )

        # Save configuration
        self.save_config(config)

        return config

    def xǁWorkspaceManagerǁinit_workspace__mutmut_58(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(None)

        return config
    
    xǁWorkspaceManagerǁinit_workspace__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁinit_workspace__mutmut_1': xǁWorkspaceManagerǁinit_workspace__mutmut_1, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_2': xǁWorkspaceManagerǁinit_workspace__mutmut_2, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_3': xǁWorkspaceManagerǁinit_workspace__mutmut_3, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_4': xǁWorkspaceManagerǁinit_workspace__mutmut_4, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_5': xǁWorkspaceManagerǁinit_workspace__mutmut_5, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_6': xǁWorkspaceManagerǁinit_workspace__mutmut_6, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_7': xǁWorkspaceManagerǁinit_workspace__mutmut_7, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_8': xǁWorkspaceManagerǁinit_workspace__mutmut_8, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_9': xǁWorkspaceManagerǁinit_workspace__mutmut_9, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_10': xǁWorkspaceManagerǁinit_workspace__mutmut_10, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_11': xǁWorkspaceManagerǁinit_workspace__mutmut_11, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_12': xǁWorkspaceManagerǁinit_workspace__mutmut_12, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_13': xǁWorkspaceManagerǁinit_workspace__mutmut_13, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_14': xǁWorkspaceManagerǁinit_workspace__mutmut_14, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_15': xǁWorkspaceManagerǁinit_workspace__mutmut_15, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_16': xǁWorkspaceManagerǁinit_workspace__mutmut_16, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_17': xǁWorkspaceManagerǁinit_workspace__mutmut_17, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_18': xǁWorkspaceManagerǁinit_workspace__mutmut_18, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_19': xǁWorkspaceManagerǁinit_workspace__mutmut_19, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_20': xǁWorkspaceManagerǁinit_workspace__mutmut_20, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_21': xǁWorkspaceManagerǁinit_workspace__mutmut_21, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_22': xǁWorkspaceManagerǁinit_workspace__mutmut_22, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_23': xǁWorkspaceManagerǁinit_workspace__mutmut_23, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_24': xǁWorkspaceManagerǁinit_workspace__mutmut_24, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_25': xǁWorkspaceManagerǁinit_workspace__mutmut_25, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_26': xǁWorkspaceManagerǁinit_workspace__mutmut_26, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_27': xǁWorkspaceManagerǁinit_workspace__mutmut_27, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_28': xǁWorkspaceManagerǁinit_workspace__mutmut_28, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_29': xǁWorkspaceManagerǁinit_workspace__mutmut_29, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_30': xǁWorkspaceManagerǁinit_workspace__mutmut_30, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_31': xǁWorkspaceManagerǁinit_workspace__mutmut_31, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_32': xǁWorkspaceManagerǁinit_workspace__mutmut_32, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_33': xǁWorkspaceManagerǁinit_workspace__mutmut_33, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_34': xǁWorkspaceManagerǁinit_workspace__mutmut_34, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_35': xǁWorkspaceManagerǁinit_workspace__mutmut_35, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_36': xǁWorkspaceManagerǁinit_workspace__mutmut_36, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_37': xǁWorkspaceManagerǁinit_workspace__mutmut_37, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_38': xǁWorkspaceManagerǁinit_workspace__mutmut_38, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_39': xǁWorkspaceManagerǁinit_workspace__mutmut_39, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_40': xǁWorkspaceManagerǁinit_workspace__mutmut_40, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_41': xǁWorkspaceManagerǁinit_workspace__mutmut_41, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_42': xǁWorkspaceManagerǁinit_workspace__mutmut_42, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_43': xǁWorkspaceManagerǁinit_workspace__mutmut_43, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_44': xǁWorkspaceManagerǁinit_workspace__mutmut_44, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_45': xǁWorkspaceManagerǁinit_workspace__mutmut_45, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_46': xǁWorkspaceManagerǁinit_workspace__mutmut_46, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_47': xǁWorkspaceManagerǁinit_workspace__mutmut_47, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_48': xǁWorkspaceManagerǁinit_workspace__mutmut_48, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_49': xǁWorkspaceManagerǁinit_workspace__mutmut_49, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_50': xǁWorkspaceManagerǁinit_workspace__mutmut_50, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_51': xǁWorkspaceManagerǁinit_workspace__mutmut_51, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_52': xǁWorkspaceManagerǁinit_workspace__mutmut_52, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_53': xǁWorkspaceManagerǁinit_workspace__mutmut_53, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_54': xǁWorkspaceManagerǁinit_workspace__mutmut_54, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_55': xǁWorkspaceManagerǁinit_workspace__mutmut_55, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_56': xǁWorkspaceManagerǁinit_workspace__mutmut_56, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_57': xǁWorkspaceManagerǁinit_workspace__mutmut_57, 
        'xǁWorkspaceManagerǁinit_workspace__mutmut_58': xǁWorkspaceManagerǁinit_workspace__mutmut_58
    }
    
    def init_workspace(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁinit_workspace__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁinit_workspace__mutmut_mutants"), args, kwargs, self)
        return result 
    
    init_workspace.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁinit_workspace__mutmut_orig)
    xǁWorkspaceManagerǁinit_workspace__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁinit_workspace'

    def xǁWorkspaceManagerǁload_config__mutmut_orig(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_1(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_2(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = None
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_3(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(None, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_4(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default=None)
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_5(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_6(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, )
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_7(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_8(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(None)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_9(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error(None, error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_10(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=None)
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_11(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error(error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_12(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", )
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_13(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("XX❌ Failed to load workspace configXX", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_14(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ failed to load workspace config", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_15(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ FAILED TO LOAD WORKSPACE CONFIG", error=str(e))
            return None

    def xǁWorkspaceManagerǁload_config__mutmut_16(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            data = read_toml(self.config_path, default={})
            if not data:
                return None
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(None))
            return None
    
    xǁWorkspaceManagerǁload_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁload_config__mutmut_1': xǁWorkspaceManagerǁload_config__mutmut_1, 
        'xǁWorkspaceManagerǁload_config__mutmut_2': xǁWorkspaceManagerǁload_config__mutmut_2, 
        'xǁWorkspaceManagerǁload_config__mutmut_3': xǁWorkspaceManagerǁload_config__mutmut_3, 
        'xǁWorkspaceManagerǁload_config__mutmut_4': xǁWorkspaceManagerǁload_config__mutmut_4, 
        'xǁWorkspaceManagerǁload_config__mutmut_5': xǁWorkspaceManagerǁload_config__mutmut_5, 
        'xǁWorkspaceManagerǁload_config__mutmut_6': xǁWorkspaceManagerǁload_config__mutmut_6, 
        'xǁWorkspaceManagerǁload_config__mutmut_7': xǁWorkspaceManagerǁload_config__mutmut_7, 
        'xǁWorkspaceManagerǁload_config__mutmut_8': xǁWorkspaceManagerǁload_config__mutmut_8, 
        'xǁWorkspaceManagerǁload_config__mutmut_9': xǁWorkspaceManagerǁload_config__mutmut_9, 
        'xǁWorkspaceManagerǁload_config__mutmut_10': xǁWorkspaceManagerǁload_config__mutmut_10, 
        'xǁWorkspaceManagerǁload_config__mutmut_11': xǁWorkspaceManagerǁload_config__mutmut_11, 
        'xǁWorkspaceManagerǁload_config__mutmut_12': xǁWorkspaceManagerǁload_config__mutmut_12, 
        'xǁWorkspaceManagerǁload_config__mutmut_13': xǁWorkspaceManagerǁload_config__mutmut_13, 
        'xǁWorkspaceManagerǁload_config__mutmut_14': xǁWorkspaceManagerǁload_config__mutmut_14, 
        'xǁWorkspaceManagerǁload_config__mutmut_15': xǁWorkspaceManagerǁload_config__mutmut_15, 
        'xǁWorkspaceManagerǁload_config__mutmut_16': xǁWorkspaceManagerǁload_config__mutmut_16
    }
    
    def load_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁload_config__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁload_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    load_config.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁload_config__mutmut_orig)
    xǁWorkspaceManagerǁload_config__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁload_config'

    def xǁWorkspaceManagerǁsave_config__mutmut_orig(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_1(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(None, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_2(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, None, atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_3(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=None)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_4(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_5(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_6(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), )
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_7(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=False)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_8(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug(None, path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_9(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=None)

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_10(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug(path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_11(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", )

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_12(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("XX💾 Workspace config savedXX", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_13(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_14(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 WORKSPACE CONFIG SAVED", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_15(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(None))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_16(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error(None, error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_17(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=None)
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_18(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error(error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_19(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", )
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_20(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("XX❌ Failed to save workspace configXX", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_21(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ failed to save workspace config", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_22(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ FAILED TO SAVE WORKSPACE CONFIG", error=str(e))
            raise

    def xǁWorkspaceManagerǁsave_config__mutmut_23(self, config: WorkspaceConfig) -> None:
        """Save workspace configuration."""
        try:
            # Convert to dictionary and write with foundation's atomic TOML writer
            write_toml(self.config_path, config.to_dict(), atomic=True)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(None))
            raise
    
    xǁWorkspaceManagerǁsave_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁsave_config__mutmut_1': xǁWorkspaceManagerǁsave_config__mutmut_1, 
        'xǁWorkspaceManagerǁsave_config__mutmut_2': xǁWorkspaceManagerǁsave_config__mutmut_2, 
        'xǁWorkspaceManagerǁsave_config__mutmut_3': xǁWorkspaceManagerǁsave_config__mutmut_3, 
        'xǁWorkspaceManagerǁsave_config__mutmut_4': xǁWorkspaceManagerǁsave_config__mutmut_4, 
        'xǁWorkspaceManagerǁsave_config__mutmut_5': xǁWorkspaceManagerǁsave_config__mutmut_5, 
        'xǁWorkspaceManagerǁsave_config__mutmut_6': xǁWorkspaceManagerǁsave_config__mutmut_6, 
        'xǁWorkspaceManagerǁsave_config__mutmut_7': xǁWorkspaceManagerǁsave_config__mutmut_7, 
        'xǁWorkspaceManagerǁsave_config__mutmut_8': xǁWorkspaceManagerǁsave_config__mutmut_8, 
        'xǁWorkspaceManagerǁsave_config__mutmut_9': xǁWorkspaceManagerǁsave_config__mutmut_9, 
        'xǁWorkspaceManagerǁsave_config__mutmut_10': xǁWorkspaceManagerǁsave_config__mutmut_10, 
        'xǁWorkspaceManagerǁsave_config__mutmut_11': xǁWorkspaceManagerǁsave_config__mutmut_11, 
        'xǁWorkspaceManagerǁsave_config__mutmut_12': xǁWorkspaceManagerǁsave_config__mutmut_12, 
        'xǁWorkspaceManagerǁsave_config__mutmut_13': xǁWorkspaceManagerǁsave_config__mutmut_13, 
        'xǁWorkspaceManagerǁsave_config__mutmut_14': xǁWorkspaceManagerǁsave_config__mutmut_14, 
        'xǁWorkspaceManagerǁsave_config__mutmut_15': xǁWorkspaceManagerǁsave_config__mutmut_15, 
        'xǁWorkspaceManagerǁsave_config__mutmut_16': xǁWorkspaceManagerǁsave_config__mutmut_16, 
        'xǁWorkspaceManagerǁsave_config__mutmut_17': xǁWorkspaceManagerǁsave_config__mutmut_17, 
        'xǁWorkspaceManagerǁsave_config__mutmut_18': xǁWorkspaceManagerǁsave_config__mutmut_18, 
        'xǁWorkspaceManagerǁsave_config__mutmut_19': xǁWorkspaceManagerǁsave_config__mutmut_19, 
        'xǁWorkspaceManagerǁsave_config__mutmut_20': xǁWorkspaceManagerǁsave_config__mutmut_20, 
        'xǁWorkspaceManagerǁsave_config__mutmut_21': xǁWorkspaceManagerǁsave_config__mutmut_21, 
        'xǁWorkspaceManagerǁsave_config__mutmut_22': xǁWorkspaceManagerǁsave_config__mutmut_22, 
        'xǁWorkspaceManagerǁsave_config__mutmut_23': xǁWorkspaceManagerǁsave_config__mutmut_23
    }
    
    def save_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁsave_config__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁsave_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    save_config.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁsave_config__mutmut_orig)
    xǁWorkspaceManagerǁsave_config__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁsave_config'

    def xǁWorkspaceManagerǁadd_repo__mutmut_orig(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_1(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = None
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_2(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(None)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_3(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_4(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(None)

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_5(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = None

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_6(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(None)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_7(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = None

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_8(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=None,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_9(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=None,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_10(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=None,
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_11(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=None,
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_12(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=None,
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_13(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_14(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_15(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_16(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_17(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_18(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name and repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_19(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name and repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_20(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type and "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_21(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type and repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_22(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "XXunknownXX",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_23(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "UNKNOWN",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_24(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile and self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_25(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(None),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_26(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(None),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_27(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = None
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_28(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is not None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_29(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = None

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_30(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=None)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_31(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=True)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_32(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = None
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_33(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(None)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁadd_repo__mutmut_34(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(None)

        return updated_config
    
    xǁWorkspaceManagerǁadd_repo__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁadd_repo__mutmut_1': xǁWorkspaceManagerǁadd_repo__mutmut_1, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_2': xǁWorkspaceManagerǁadd_repo__mutmut_2, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_3': xǁWorkspaceManagerǁadd_repo__mutmut_3, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_4': xǁWorkspaceManagerǁadd_repo__mutmut_4, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_5': xǁWorkspaceManagerǁadd_repo__mutmut_5, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_6': xǁWorkspaceManagerǁadd_repo__mutmut_6, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_7': xǁWorkspaceManagerǁadd_repo__mutmut_7, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_8': xǁWorkspaceManagerǁadd_repo__mutmut_8, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_9': xǁWorkspaceManagerǁadd_repo__mutmut_9, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_10': xǁWorkspaceManagerǁadd_repo__mutmut_10, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_11': xǁWorkspaceManagerǁadd_repo__mutmut_11, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_12': xǁWorkspaceManagerǁadd_repo__mutmut_12, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_13': xǁWorkspaceManagerǁadd_repo__mutmut_13, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_14': xǁWorkspaceManagerǁadd_repo__mutmut_14, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_15': xǁWorkspaceManagerǁadd_repo__mutmut_15, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_16': xǁWorkspaceManagerǁadd_repo__mutmut_16, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_17': xǁWorkspaceManagerǁadd_repo__mutmut_17, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_18': xǁWorkspaceManagerǁadd_repo__mutmut_18, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_19': xǁWorkspaceManagerǁadd_repo__mutmut_19, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_20': xǁWorkspaceManagerǁadd_repo__mutmut_20, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_21': xǁWorkspaceManagerǁadd_repo__mutmut_21, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_22': xǁWorkspaceManagerǁadd_repo__mutmut_22, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_23': xǁWorkspaceManagerǁadd_repo__mutmut_23, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_24': xǁWorkspaceManagerǁadd_repo__mutmut_24, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_25': xǁWorkspaceManagerǁadd_repo__mutmut_25, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_26': xǁWorkspaceManagerǁadd_repo__mutmut_26, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_27': xǁWorkspaceManagerǁadd_repo__mutmut_27, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_28': xǁWorkspaceManagerǁadd_repo__mutmut_28, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_29': xǁWorkspaceManagerǁadd_repo__mutmut_29, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_30': xǁWorkspaceManagerǁadd_repo__mutmut_30, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_31': xǁWorkspaceManagerǁadd_repo__mutmut_31, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_32': xǁWorkspaceManagerǁadd_repo__mutmut_32, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_33': xǁWorkspaceManagerǁadd_repo__mutmut_33, 
        'xǁWorkspaceManagerǁadd_repo__mutmut_34': xǁWorkspaceManagerǁadd_repo__mutmut_34
    }
    
    def add_repo(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁadd_repo__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁadd_repo__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_repo.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁadd_repo__mutmut_orig)
    xǁWorkspaceManagerǁadd_repo__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁadd_repo'

    def xǁWorkspaceManagerǁremove_repo__mutmut_orig(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_1(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = None
        if config is None:
            raise RuntimeError("No workspace configuration found")

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_2(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is not None:
            raise RuntimeError("No workspace configuration found")

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_3(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError(None)

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_4(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("XXNo workspace configuration foundXX")

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_5(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("no workspace configuration found")

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_6(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("NO WORKSPACE CONFIGURATION FOUND")

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_7(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        updated_config = None
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_8(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        updated_config = config.remove_repo(None)
        self.save_config(updated_config)

        return updated_config

    def xǁWorkspaceManagerǁremove_repo__mutmut_9(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        updated_config = config.remove_repo(name)
        self.save_config(None)

        return updated_config
    
    xǁWorkspaceManagerǁremove_repo__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁremove_repo__mutmut_1': xǁWorkspaceManagerǁremove_repo__mutmut_1, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_2': xǁWorkspaceManagerǁremove_repo__mutmut_2, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_3': xǁWorkspaceManagerǁremove_repo__mutmut_3, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_4': xǁWorkspaceManagerǁremove_repo__mutmut_4, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_5': xǁWorkspaceManagerǁremove_repo__mutmut_5, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_6': xǁWorkspaceManagerǁremove_repo__mutmut_6, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_7': xǁWorkspaceManagerǁremove_repo__mutmut_7, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_8': xǁWorkspaceManagerǁremove_repo__mutmut_8, 
        'xǁWorkspaceManagerǁremove_repo__mutmut_9': xǁWorkspaceManagerǁremove_repo__mutmut_9
    }
    
    def remove_repo(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁremove_repo__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁremove_repo__mutmut_mutants"), args, kwargs, self)
        return result 
    
    remove_repo.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁremove_repo__mutmut_orig)
    xǁWorkspaceManagerǁremove_repo__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁremove_repo'

    async def xǁWorkspaceManagerǁsync_all__mutmut_orig(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_1(self, dry_run: bool = True) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_2(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = None
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_3(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is not None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_4(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError(None)

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_5(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("XXNo workspace configuration foundXX")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_6(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("no workspace configuration found")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_7(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("NO WORKSPACE CONFIGURATION FOUND")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_8(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = None
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_9(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(None)
        return await sync.sync_all(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_all__mutmut_10(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=None)
    
    xǁWorkspaceManagerǁsync_all__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁsync_all__mutmut_1': xǁWorkspaceManagerǁsync_all__mutmut_1, 
        'xǁWorkspaceManagerǁsync_all__mutmut_2': xǁWorkspaceManagerǁsync_all__mutmut_2, 
        'xǁWorkspaceManagerǁsync_all__mutmut_3': xǁWorkspaceManagerǁsync_all__mutmut_3, 
        'xǁWorkspaceManagerǁsync_all__mutmut_4': xǁWorkspaceManagerǁsync_all__mutmut_4, 
        'xǁWorkspaceManagerǁsync_all__mutmut_5': xǁWorkspaceManagerǁsync_all__mutmut_5, 
        'xǁWorkspaceManagerǁsync_all__mutmut_6': xǁWorkspaceManagerǁsync_all__mutmut_6, 
        'xǁWorkspaceManagerǁsync_all__mutmut_7': xǁWorkspaceManagerǁsync_all__mutmut_7, 
        'xǁWorkspaceManagerǁsync_all__mutmut_8': xǁWorkspaceManagerǁsync_all__mutmut_8, 
        'xǁWorkspaceManagerǁsync_all__mutmut_9': xǁWorkspaceManagerǁsync_all__mutmut_9, 
        'xǁWorkspaceManagerǁsync_all__mutmut_10': xǁWorkspaceManagerǁsync_all__mutmut_10
    }
    
    def sync_all(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁsync_all__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁsync_all__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sync_all.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁsync_all__mutmut_orig)
    xǁWorkspaceManagerǁsync_all__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁsync_all'

    async def xǁWorkspaceManagerǁsync_repo__mutmut_orig(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_1(self, name: str, dry_run: bool = True) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_2(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = None
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_3(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is not None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_4(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError(None)

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_5(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("XXNo workspace configuration foundXX")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_6(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("no workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_7(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("NO WORKSPACE CONFIGURATION FOUND")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_8(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = None
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_9(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(None)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_10(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is not None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_11(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(None)

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_12(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = None
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_13(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(None)
        return await sync.sync_repo(repo, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_14(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(None, dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_15(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=None)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_16(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(dry_run=dry_run)

    async def xǁWorkspaceManagerǁsync_repo__mutmut_17(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, )
    
    xǁWorkspaceManagerǁsync_repo__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁsync_repo__mutmut_1': xǁWorkspaceManagerǁsync_repo__mutmut_1, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_2': xǁWorkspaceManagerǁsync_repo__mutmut_2, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_3': xǁWorkspaceManagerǁsync_repo__mutmut_3, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_4': xǁWorkspaceManagerǁsync_repo__mutmut_4, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_5': xǁWorkspaceManagerǁsync_repo__mutmut_5, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_6': xǁWorkspaceManagerǁsync_repo__mutmut_6, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_7': xǁWorkspaceManagerǁsync_repo__mutmut_7, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_8': xǁWorkspaceManagerǁsync_repo__mutmut_8, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_9': xǁWorkspaceManagerǁsync_repo__mutmut_9, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_10': xǁWorkspaceManagerǁsync_repo__mutmut_10, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_11': xǁWorkspaceManagerǁsync_repo__mutmut_11, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_12': xǁWorkspaceManagerǁsync_repo__mutmut_12, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_13': xǁWorkspaceManagerǁsync_repo__mutmut_13, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_14': xǁWorkspaceManagerǁsync_repo__mutmut_14, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_15': xǁWorkspaceManagerǁsync_repo__mutmut_15, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_16': xǁWorkspaceManagerǁsync_repo__mutmut_16, 
        'xǁWorkspaceManagerǁsync_repo__mutmut_17': xǁWorkspaceManagerǁsync_repo__mutmut_17
    }
    
    def sync_repo(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁsync_repo__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁsync_repo__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sync_repo.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁsync_repo__mutmut_orig)
    xǁWorkspaceManagerǁsync_repo__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁsync_repo'

    def xǁWorkspaceManagerǁcheck_drift__mutmut_orig(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_1(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = None
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_2(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is not None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_3(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError(None)

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_4(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("XXNo workspace configuration foundXX")

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_5(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("no workspace configuration found")

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_6(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("NO WORKSPACE CONFIGURATION FOUND")

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_7(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = None
        return sync.check_drift()

    def xǁWorkspaceManagerǁcheck_drift__mutmut_8(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(None)
        return sync.check_drift()
    
    xǁWorkspaceManagerǁcheck_drift__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁcheck_drift__mutmut_1': xǁWorkspaceManagerǁcheck_drift__mutmut_1, 
        'xǁWorkspaceManagerǁcheck_drift__mutmut_2': xǁWorkspaceManagerǁcheck_drift__mutmut_2, 
        'xǁWorkspaceManagerǁcheck_drift__mutmut_3': xǁWorkspaceManagerǁcheck_drift__mutmut_3, 
        'xǁWorkspaceManagerǁcheck_drift__mutmut_4': xǁWorkspaceManagerǁcheck_drift__mutmut_4, 
        'xǁWorkspaceManagerǁcheck_drift__mutmut_5': xǁWorkspaceManagerǁcheck_drift__mutmut_5, 
        'xǁWorkspaceManagerǁcheck_drift__mutmut_6': xǁWorkspaceManagerǁcheck_drift__mutmut_6, 
        'xǁWorkspaceManagerǁcheck_drift__mutmut_7': xǁWorkspaceManagerǁcheck_drift__mutmut_7, 
        'xǁWorkspaceManagerǁcheck_drift__mutmut_8': xǁWorkspaceManagerǁcheck_drift__mutmut_8
    }
    
    def check_drift(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁcheck_drift__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁcheck_drift__mutmut_mutants"), args, kwargs, self)
        return result 
    
    check_drift.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁcheck_drift__mutmut_orig)
    xǁWorkspaceManagerǁcheck_drift__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁcheck_drift'

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_orig(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_1(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = None
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_2(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is not None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_3(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"XXerrorXX": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_4(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"ERROR": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_5(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "XXNo workspace configuration foundXX"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_6(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "no workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_7(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "NO WORKSPACE CONFIGURATION FOUND"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_8(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = None
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_9(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = None

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_10(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(None)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_11(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "XXrootXX": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_12(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "ROOT": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_13(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(None),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_14(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "XXconfig_pathXX": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_15(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "CONFIG_PATH": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_16(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(None),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_17(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "XXrepos_configuredXX": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_18(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "REPOS_CONFIGURED": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_19(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "XXrepos_discoveredXX": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_20(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "REPOS_DISCOVERED": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_21(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["XXtotal_reposXX"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_22(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["TOTAL_REPOS"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_23(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "XXtype_distributionXX": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_24(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "TYPE_DISTRIBUTION": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_25(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["XXtype_distributionXX"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_26(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["TYPE_DISTRIBUTION"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_27(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "XXissuesXX": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_28(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "ISSUES": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_29(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "XXsync_strategyXX": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_30(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "SYNC_STRATEGY": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_31(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "XXtemplate_sourceXX": config.template_source.to_dict() if config.template_source else None,
        }

    def xǁWorkspaceManagerǁget_workspace_status__mutmut_32(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "TEMPLATE_SOURCE": config.template_source.to_dict() if config.template_source else None,
        }
    
    xǁWorkspaceManagerǁget_workspace_status__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁget_workspace_status__mutmut_1': xǁWorkspaceManagerǁget_workspace_status__mutmut_1, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_2': xǁWorkspaceManagerǁget_workspace_status__mutmut_2, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_3': xǁWorkspaceManagerǁget_workspace_status__mutmut_3, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_4': xǁWorkspaceManagerǁget_workspace_status__mutmut_4, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_5': xǁWorkspaceManagerǁget_workspace_status__mutmut_5, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_6': xǁWorkspaceManagerǁget_workspace_status__mutmut_6, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_7': xǁWorkspaceManagerǁget_workspace_status__mutmut_7, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_8': xǁWorkspaceManagerǁget_workspace_status__mutmut_8, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_9': xǁWorkspaceManagerǁget_workspace_status__mutmut_9, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_10': xǁWorkspaceManagerǁget_workspace_status__mutmut_10, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_11': xǁWorkspaceManagerǁget_workspace_status__mutmut_11, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_12': xǁWorkspaceManagerǁget_workspace_status__mutmut_12, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_13': xǁWorkspaceManagerǁget_workspace_status__mutmut_13, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_14': xǁWorkspaceManagerǁget_workspace_status__mutmut_14, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_15': xǁWorkspaceManagerǁget_workspace_status__mutmut_15, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_16': xǁWorkspaceManagerǁget_workspace_status__mutmut_16, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_17': xǁWorkspaceManagerǁget_workspace_status__mutmut_17, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_18': xǁWorkspaceManagerǁget_workspace_status__mutmut_18, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_19': xǁWorkspaceManagerǁget_workspace_status__mutmut_19, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_20': xǁWorkspaceManagerǁget_workspace_status__mutmut_20, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_21': xǁWorkspaceManagerǁget_workspace_status__mutmut_21, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_22': xǁWorkspaceManagerǁget_workspace_status__mutmut_22, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_23': xǁWorkspaceManagerǁget_workspace_status__mutmut_23, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_24': xǁWorkspaceManagerǁget_workspace_status__mutmut_24, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_25': xǁWorkspaceManagerǁget_workspace_status__mutmut_25, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_26': xǁWorkspaceManagerǁget_workspace_status__mutmut_26, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_27': xǁWorkspaceManagerǁget_workspace_status__mutmut_27, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_28': xǁWorkspaceManagerǁget_workspace_status__mutmut_28, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_29': xǁWorkspaceManagerǁget_workspace_status__mutmut_29, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_30': xǁWorkspaceManagerǁget_workspace_status__mutmut_30, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_31': xǁWorkspaceManagerǁget_workspace_status__mutmut_31, 
        'xǁWorkspaceManagerǁget_workspace_status__mutmut_32': xǁWorkspaceManagerǁget_workspace_status__mutmut_32
    }
    
    def get_workspace_status(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁget_workspace_status__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁget_workspace_status__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_workspace_status.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁget_workspace_status__mutmut_orig)
    xǁWorkspaceManagerǁget_workspace_status__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁget_workspace_status'

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_orig(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_1(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = None
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_2(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "XXfoundationXX": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_3(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "FOUNDATION": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_4(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "XXfoundation-basedXX",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_5(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "FOUNDATION-BASED",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_6(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "XXfoundation-basedXX": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_7(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "FOUNDATION-BASED": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_8(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "XXfoundation-basedXX",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_9(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "FOUNDATION-BASED",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_10(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "XXproviderXX": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_11(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "PROVIDER": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_12(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "XXpyvider-pluginXX",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_13(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "PYVIDER-PLUGIN",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_14(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "XXpyvider-pluginXX": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_15(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "PYVIDER-PLUGIN": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_16(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "XXpyvider-pluginXX",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_17(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "PYVIDER-PLUGIN",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_18(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "XXtestkitXX": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_19(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "TESTKIT": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_20(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "XXtestkit-extensionXX",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_21(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "TESTKIT-EXTENSION",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_22(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "XXpackagingXX": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_23(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "PACKAGING": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_24(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "XXstandaloneXX",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_25(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "STANDALONE",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_26(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(None, "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_27(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", None)

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_28(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get("standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_29(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", )

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_30(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type and "unknown", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_31(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "XXunknownXX", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_32(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "UNKNOWN", "standalone")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_33(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "XXstandaloneXX")

    def xǁWorkspaceManagerǁ_get_default_profile__mutmut_34(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "STANDALONE")
    
    xǁWorkspaceManagerǁ_get_default_profile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁ_get_default_profile__mutmut_1': xǁWorkspaceManagerǁ_get_default_profile__mutmut_1, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_2': xǁWorkspaceManagerǁ_get_default_profile__mutmut_2, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_3': xǁWorkspaceManagerǁ_get_default_profile__mutmut_3, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_4': xǁWorkspaceManagerǁ_get_default_profile__mutmut_4, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_5': xǁWorkspaceManagerǁ_get_default_profile__mutmut_5, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_6': xǁWorkspaceManagerǁ_get_default_profile__mutmut_6, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_7': xǁWorkspaceManagerǁ_get_default_profile__mutmut_7, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_8': xǁWorkspaceManagerǁ_get_default_profile__mutmut_8, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_9': xǁWorkspaceManagerǁ_get_default_profile__mutmut_9, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_10': xǁWorkspaceManagerǁ_get_default_profile__mutmut_10, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_11': xǁWorkspaceManagerǁ_get_default_profile__mutmut_11, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_12': xǁWorkspaceManagerǁ_get_default_profile__mutmut_12, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_13': xǁWorkspaceManagerǁ_get_default_profile__mutmut_13, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_14': xǁWorkspaceManagerǁ_get_default_profile__mutmut_14, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_15': xǁWorkspaceManagerǁ_get_default_profile__mutmut_15, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_16': xǁWorkspaceManagerǁ_get_default_profile__mutmut_16, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_17': xǁWorkspaceManagerǁ_get_default_profile__mutmut_17, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_18': xǁWorkspaceManagerǁ_get_default_profile__mutmut_18, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_19': xǁWorkspaceManagerǁ_get_default_profile__mutmut_19, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_20': xǁWorkspaceManagerǁ_get_default_profile__mutmut_20, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_21': xǁWorkspaceManagerǁ_get_default_profile__mutmut_21, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_22': xǁWorkspaceManagerǁ_get_default_profile__mutmut_22, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_23': xǁWorkspaceManagerǁ_get_default_profile__mutmut_23, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_24': xǁWorkspaceManagerǁ_get_default_profile__mutmut_24, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_25': xǁWorkspaceManagerǁ_get_default_profile__mutmut_25, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_26': xǁWorkspaceManagerǁ_get_default_profile__mutmut_26, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_27': xǁWorkspaceManagerǁ_get_default_profile__mutmut_27, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_28': xǁWorkspaceManagerǁ_get_default_profile__mutmut_28, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_29': xǁWorkspaceManagerǁ_get_default_profile__mutmut_29, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_30': xǁWorkspaceManagerǁ_get_default_profile__mutmut_30, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_31': xǁWorkspaceManagerǁ_get_default_profile__mutmut_31, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_32': xǁWorkspaceManagerǁ_get_default_profile__mutmut_32, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_33': xǁWorkspaceManagerǁ_get_default_profile__mutmut_33, 
        'xǁWorkspaceManagerǁ_get_default_profile__mutmut_34': xǁWorkspaceManagerǁ_get_default_profile__mutmut_34
    }
    
    def _get_default_profile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁ_get_default_profile__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁ_get_default_profile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_default_profile.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁ_get_default_profile__mutmut_orig)
    xǁWorkspaceManagerǁ_get_default_profile__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁ_get_default_profile'

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_orig(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_1(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = None

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_2(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["XXpyprojectXX", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_3(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["PYPROJECT", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_4(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "XXclaudeXX", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_5(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "CLAUDE", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_6(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "XXgitignoreXX"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_7(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "GITIGNORE"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_8(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = None

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_9(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "XXfoundation-basedXX": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_10(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "FOUNDATION-BASED": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_11(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "XXcoverageXX"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_12(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "COVERAGE"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_13(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "XXpyvider-pluginXX": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_14(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "PYVIDER-PLUGIN": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_15(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "XXcoverageXX"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_16(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "COVERAGE"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_17(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "XXtestkitXX": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_18(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "TESTKIT": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_19(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "XXcoverageXX"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_20(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "COVERAGE"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_21(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(None, base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_22(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", None)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_23(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_24(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "unknown", )

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_25(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type and "unknown", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_26(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "XXunknownXX", base_features)

    def xǁWorkspaceManagerǁ_get_default_features__mutmut_27(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": [*base_features, "coverage"],
            "pyvider-plugin": [*base_features, "coverage"],
            "testkit": [*base_features, "coverage"],
        }

        return type_features.get(repo_type or "UNKNOWN", base_features)
    
    xǁWorkspaceManagerǁ_get_default_features__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁ_get_default_features__mutmut_1': xǁWorkspaceManagerǁ_get_default_features__mutmut_1, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_2': xǁWorkspaceManagerǁ_get_default_features__mutmut_2, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_3': xǁWorkspaceManagerǁ_get_default_features__mutmut_3, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_4': xǁWorkspaceManagerǁ_get_default_features__mutmut_4, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_5': xǁWorkspaceManagerǁ_get_default_features__mutmut_5, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_6': xǁWorkspaceManagerǁ_get_default_features__mutmut_6, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_7': xǁWorkspaceManagerǁ_get_default_features__mutmut_7, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_8': xǁWorkspaceManagerǁ_get_default_features__mutmut_8, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_9': xǁWorkspaceManagerǁ_get_default_features__mutmut_9, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_10': xǁWorkspaceManagerǁ_get_default_features__mutmut_10, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_11': xǁWorkspaceManagerǁ_get_default_features__mutmut_11, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_12': xǁWorkspaceManagerǁ_get_default_features__mutmut_12, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_13': xǁWorkspaceManagerǁ_get_default_features__mutmut_13, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_14': xǁWorkspaceManagerǁ_get_default_features__mutmut_14, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_15': xǁWorkspaceManagerǁ_get_default_features__mutmut_15, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_16': xǁWorkspaceManagerǁ_get_default_features__mutmut_16, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_17': xǁWorkspaceManagerǁ_get_default_features__mutmut_17, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_18': xǁWorkspaceManagerǁ_get_default_features__mutmut_18, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_19': xǁWorkspaceManagerǁ_get_default_features__mutmut_19, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_20': xǁWorkspaceManagerǁ_get_default_features__mutmut_20, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_21': xǁWorkspaceManagerǁ_get_default_features__mutmut_21, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_22': xǁWorkspaceManagerǁ_get_default_features__mutmut_22, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_23': xǁWorkspaceManagerǁ_get_default_features__mutmut_23, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_24': xǁWorkspaceManagerǁ_get_default_features__mutmut_24, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_25': xǁWorkspaceManagerǁ_get_default_features__mutmut_25, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_26': xǁWorkspaceManagerǁ_get_default_features__mutmut_26, 
        'xǁWorkspaceManagerǁ_get_default_features__mutmut_27': xǁWorkspaceManagerǁ_get_default_features__mutmut_27
    }
    
    def _get_default_features(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁ_get_default_features__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁ_get_default_features__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_default_features.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁ_get_default_features__mutmut_orig)
    xǁWorkspaceManagerǁ_get_default_features__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁ_get_default_features'

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_orig(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_1(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "XXpython_versionXX": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_2(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "PYTHON_VERSION": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_3(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "XX3.11XX",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_4(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "XXruff_line_lengthXX": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_5(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "RUFF_LINE_LENGTH": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_6(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 112,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_7(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "XXauthorsXX": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_8(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "AUTHORS": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_9(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"XXnameXX": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_10(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"NAME": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_11(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "XXTim PerkinsXX", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_12(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "tim perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_13(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "TIM PERKINS", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_14(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "XXemailXX": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_15(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "EMAIL": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_16(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "XXcode@tim.lifeXX"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_17(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "CODE@TIM.LIFE"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_18(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "XXmaintainersXX": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_19(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "MAINTAINERS": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_20(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"XXnameXX": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_21(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"NAME": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_22(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "XXprovide.ioXX", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_23(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "PROVIDE.IO", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_24(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "XXemailXX": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_25(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "EMAIL": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_26(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "XXcode@provide.ioXX"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_27(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "CODE@PROVIDE.IO"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_28(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "XXlicenseXX": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_29(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "LICENSE": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_30(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "XXApache-2.0XX",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_31(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "apache-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_32(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "APACHE-2.0",
            "development_status": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_33(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "XXdevelopment_statusXX": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_34(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "DEVELOPMENT_STATUS": "3 - Alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_35(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "XX3 - AlphaXX",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_36(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - alpha",
        }

    def xǁWorkspaceManagerǁ_get_default_standards__mutmut_37(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - ALPHA",
        }
    
    xǁWorkspaceManagerǁ_get_default_standards__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁ_get_default_standards__mutmut_1': xǁWorkspaceManagerǁ_get_default_standards__mutmut_1, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_2': xǁWorkspaceManagerǁ_get_default_standards__mutmut_2, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_3': xǁWorkspaceManagerǁ_get_default_standards__mutmut_3, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_4': xǁWorkspaceManagerǁ_get_default_standards__mutmut_4, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_5': xǁWorkspaceManagerǁ_get_default_standards__mutmut_5, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_6': xǁWorkspaceManagerǁ_get_default_standards__mutmut_6, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_7': xǁWorkspaceManagerǁ_get_default_standards__mutmut_7, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_8': xǁWorkspaceManagerǁ_get_default_standards__mutmut_8, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_9': xǁWorkspaceManagerǁ_get_default_standards__mutmut_9, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_10': xǁWorkspaceManagerǁ_get_default_standards__mutmut_10, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_11': xǁWorkspaceManagerǁ_get_default_standards__mutmut_11, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_12': xǁWorkspaceManagerǁ_get_default_standards__mutmut_12, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_13': xǁWorkspaceManagerǁ_get_default_standards__mutmut_13, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_14': xǁWorkspaceManagerǁ_get_default_standards__mutmut_14, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_15': xǁWorkspaceManagerǁ_get_default_standards__mutmut_15, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_16': xǁWorkspaceManagerǁ_get_default_standards__mutmut_16, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_17': xǁWorkspaceManagerǁ_get_default_standards__mutmut_17, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_18': xǁWorkspaceManagerǁ_get_default_standards__mutmut_18, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_19': xǁWorkspaceManagerǁ_get_default_standards__mutmut_19, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_20': xǁWorkspaceManagerǁ_get_default_standards__mutmut_20, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_21': xǁWorkspaceManagerǁ_get_default_standards__mutmut_21, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_22': xǁWorkspaceManagerǁ_get_default_standards__mutmut_22, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_23': xǁWorkspaceManagerǁ_get_default_standards__mutmut_23, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_24': xǁWorkspaceManagerǁ_get_default_standards__mutmut_24, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_25': xǁWorkspaceManagerǁ_get_default_standards__mutmut_25, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_26': xǁWorkspaceManagerǁ_get_default_standards__mutmut_26, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_27': xǁWorkspaceManagerǁ_get_default_standards__mutmut_27, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_28': xǁWorkspaceManagerǁ_get_default_standards__mutmut_28, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_29': xǁWorkspaceManagerǁ_get_default_standards__mutmut_29, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_30': xǁWorkspaceManagerǁ_get_default_standards__mutmut_30, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_31': xǁWorkspaceManagerǁ_get_default_standards__mutmut_31, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_32': xǁWorkspaceManagerǁ_get_default_standards__mutmut_32, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_33': xǁWorkspaceManagerǁ_get_default_standards__mutmut_33, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_34': xǁWorkspaceManagerǁ_get_default_standards__mutmut_34, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_35': xǁWorkspaceManagerǁ_get_default_standards__mutmut_35, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_36': xǁWorkspaceManagerǁ_get_default_standards__mutmut_36, 
        'xǁWorkspaceManagerǁ_get_default_standards__mutmut_37': xǁWorkspaceManagerǁ_get_default_standards__mutmut_37
    }
    
    def _get_default_standards(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁ_get_default_standards__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁ_get_default_standards__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_default_standards.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁ_get_default_standards__mutmut_orig)
    xǁWorkspaceManagerǁ_get_default_standards__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁ_get_default_standards'

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_orig(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_1(self, generate_only: bool = True) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_2(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = None
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_3(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is not None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_4(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError(None)

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_5(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("XXNo workspace configuration found. Run 'wrknv workspace init' first.XX")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_6(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("no workspace configuration found. run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_7(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("NO WORKSPACE CONFIGURATION FOUND. RUN 'WRKNV WORKSPACE INIT' FIRST.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_8(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = None

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_9(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "XXsuccess_countXX": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_10(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "SUCCESS_COUNT": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_11(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 1,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_12(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "XXtotal_countXX": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_13(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "TOTAL_COUNT": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_14(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "XXfailuresXX": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_15(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "FAILURES": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_16(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "XXgeneratedXX": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_17(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "GENERATED": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_18(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = None

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_19(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root * repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_20(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_21(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = None
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_22(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["XXfailuresXX"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_23(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["FAILURES"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_24(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                break

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_25(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_26(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path * "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_27(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "XXpyproject.tomlXX").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_28(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "PYPROJECT.TOML").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_29(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = None
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_30(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["XXfailuresXX"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_31(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["FAILURES"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_32(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "XXNo pyproject.toml foundXX"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_33(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "no pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_34(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "NO PYPROJECT.TOML FOUND"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_35(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                break

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_36(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(None)
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_37(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = None

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_38(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(None)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_39(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    None
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_40(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["XXgeneratedXX"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_41(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["GENERATED"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_42(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"XXrepoXX": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_43(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"REPO": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_44(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "XXsh_pathXX": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_45(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "SH_PATH": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_46(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(None), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_47(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "XXps1_pathXX": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_48(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "PS1_PATH": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_49(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(None)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_50(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] = 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_51(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] -= 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_52(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["XXsuccess_countXX"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_53(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["SUCCESS_COUNT"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_54(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 2

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_55(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(None, error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_56(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=None)
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_57(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(error=str(e))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_58(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", )
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_59(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(None))
                results["failures"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_60(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = None

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_61(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["XXfailuresXX"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_62(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["FAILURES"][repo.name] = str(e)

        return results

    def xǁWorkspaceManagerǁsetup_workspace__mutmut_63(self, generate_only: bool = False) -> dict[str, Any]:
        """Setup all repositories in workspace.

        Args:
            generate_only: If True, only generate env scripts without running them

        Returns:
            Dictionary with setup results
        """
        from wrknv.wenv.env_generator import create_project_env_scripts

        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found. Run 'wrknv workspace init' first.")

        results: dict[str, Any] = {
            "success_count": 0,
            "total_count": len(config.repos),
            "failures": {},
            "generated": [],
        }

        for repo in config.repos:
            repo_path = repo.path if repo.path.is_absolute() else self.root / repo.path

            if not repo_path.exists():
                results["failures"][repo.name] = f"Repository path does not exist: {repo_path}"
                continue

            if not (repo_path / "pyproject.toml").exists():
                results["failures"][repo.name] = "No pyproject.toml found"
                continue

            try:
                # Generate env scripts
                logger.info(f"📝 Generating env scripts for {repo.name}")
                sh_path, ps1_path = create_project_env_scripts(repo_path)

                results["generated"].append(
                    {"repo": repo.name, "sh_path": str(sh_path), "ps1_path": str(ps1_path)}
                )

                results["success_count"] += 1

            except Exception as e:
                logger.error(f"❌ Failed to setup {repo.name}", error=str(e))
                results["failures"][repo.name] = str(None)

        return results
    
    xǁWorkspaceManagerǁsetup_workspace__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceManagerǁsetup_workspace__mutmut_1': xǁWorkspaceManagerǁsetup_workspace__mutmut_1, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_2': xǁWorkspaceManagerǁsetup_workspace__mutmut_2, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_3': xǁWorkspaceManagerǁsetup_workspace__mutmut_3, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_4': xǁWorkspaceManagerǁsetup_workspace__mutmut_4, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_5': xǁWorkspaceManagerǁsetup_workspace__mutmut_5, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_6': xǁWorkspaceManagerǁsetup_workspace__mutmut_6, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_7': xǁWorkspaceManagerǁsetup_workspace__mutmut_7, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_8': xǁWorkspaceManagerǁsetup_workspace__mutmut_8, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_9': xǁWorkspaceManagerǁsetup_workspace__mutmut_9, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_10': xǁWorkspaceManagerǁsetup_workspace__mutmut_10, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_11': xǁWorkspaceManagerǁsetup_workspace__mutmut_11, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_12': xǁWorkspaceManagerǁsetup_workspace__mutmut_12, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_13': xǁWorkspaceManagerǁsetup_workspace__mutmut_13, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_14': xǁWorkspaceManagerǁsetup_workspace__mutmut_14, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_15': xǁWorkspaceManagerǁsetup_workspace__mutmut_15, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_16': xǁWorkspaceManagerǁsetup_workspace__mutmut_16, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_17': xǁWorkspaceManagerǁsetup_workspace__mutmut_17, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_18': xǁWorkspaceManagerǁsetup_workspace__mutmut_18, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_19': xǁWorkspaceManagerǁsetup_workspace__mutmut_19, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_20': xǁWorkspaceManagerǁsetup_workspace__mutmut_20, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_21': xǁWorkspaceManagerǁsetup_workspace__mutmut_21, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_22': xǁWorkspaceManagerǁsetup_workspace__mutmut_22, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_23': xǁWorkspaceManagerǁsetup_workspace__mutmut_23, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_24': xǁWorkspaceManagerǁsetup_workspace__mutmut_24, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_25': xǁWorkspaceManagerǁsetup_workspace__mutmut_25, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_26': xǁWorkspaceManagerǁsetup_workspace__mutmut_26, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_27': xǁWorkspaceManagerǁsetup_workspace__mutmut_27, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_28': xǁWorkspaceManagerǁsetup_workspace__mutmut_28, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_29': xǁWorkspaceManagerǁsetup_workspace__mutmut_29, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_30': xǁWorkspaceManagerǁsetup_workspace__mutmut_30, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_31': xǁWorkspaceManagerǁsetup_workspace__mutmut_31, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_32': xǁWorkspaceManagerǁsetup_workspace__mutmut_32, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_33': xǁWorkspaceManagerǁsetup_workspace__mutmut_33, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_34': xǁWorkspaceManagerǁsetup_workspace__mutmut_34, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_35': xǁWorkspaceManagerǁsetup_workspace__mutmut_35, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_36': xǁWorkspaceManagerǁsetup_workspace__mutmut_36, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_37': xǁWorkspaceManagerǁsetup_workspace__mutmut_37, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_38': xǁWorkspaceManagerǁsetup_workspace__mutmut_38, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_39': xǁWorkspaceManagerǁsetup_workspace__mutmut_39, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_40': xǁWorkspaceManagerǁsetup_workspace__mutmut_40, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_41': xǁWorkspaceManagerǁsetup_workspace__mutmut_41, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_42': xǁWorkspaceManagerǁsetup_workspace__mutmut_42, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_43': xǁWorkspaceManagerǁsetup_workspace__mutmut_43, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_44': xǁWorkspaceManagerǁsetup_workspace__mutmut_44, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_45': xǁWorkspaceManagerǁsetup_workspace__mutmut_45, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_46': xǁWorkspaceManagerǁsetup_workspace__mutmut_46, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_47': xǁWorkspaceManagerǁsetup_workspace__mutmut_47, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_48': xǁWorkspaceManagerǁsetup_workspace__mutmut_48, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_49': xǁWorkspaceManagerǁsetup_workspace__mutmut_49, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_50': xǁWorkspaceManagerǁsetup_workspace__mutmut_50, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_51': xǁWorkspaceManagerǁsetup_workspace__mutmut_51, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_52': xǁWorkspaceManagerǁsetup_workspace__mutmut_52, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_53': xǁWorkspaceManagerǁsetup_workspace__mutmut_53, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_54': xǁWorkspaceManagerǁsetup_workspace__mutmut_54, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_55': xǁWorkspaceManagerǁsetup_workspace__mutmut_55, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_56': xǁWorkspaceManagerǁsetup_workspace__mutmut_56, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_57': xǁWorkspaceManagerǁsetup_workspace__mutmut_57, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_58': xǁWorkspaceManagerǁsetup_workspace__mutmut_58, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_59': xǁWorkspaceManagerǁsetup_workspace__mutmut_59, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_60': xǁWorkspaceManagerǁsetup_workspace__mutmut_60, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_61': xǁWorkspaceManagerǁsetup_workspace__mutmut_61, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_62': xǁWorkspaceManagerǁsetup_workspace__mutmut_62, 
        'xǁWorkspaceManagerǁsetup_workspace__mutmut_63': xǁWorkspaceManagerǁsetup_workspace__mutmut_63
    }
    
    def setup_workspace(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceManagerǁsetup_workspace__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceManagerǁsetup_workspace__mutmut_mutants"), args, kwargs, self)
        return result 
    
    setup_workspace.__signature__ = _mutmut_signature(xǁWorkspaceManagerǁsetup_workspace__mutmut_orig)
    xǁWorkspaceManagerǁsetup_workspace__mutmut_orig.__name__ = 'xǁWorkspaceManagerǁsetup_workspace'


# 🧰🌍🔚
