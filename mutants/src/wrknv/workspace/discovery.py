#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Workspace Repository Discovery
=============================
Discover and analyze repositories in workspace."""

from __future__ import annotations

from pathlib import Path
import tomllib
from typing import Any

from attrs import define
from provide.foundation import logger
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
class RepoInfo:
    """Information about a discovered repository."""

    path: Path
    name: str | None
    has_git: bool
    has_pyproject: bool
    detected_type: str | None
    current_config: dict[str, Any] | None


class WorkspaceDiscovery:
    """Discovers and analyzes repositories in workspace."""

    def xǁWorkspaceDiscoveryǁ__init____mutmut_orig(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()

    def xǁWorkspaceDiscoveryǁ__init____mutmut_1(self, root: Path | None = None) -> None:
        self.root = None

    def xǁWorkspaceDiscoveryǁ__init____mutmut_2(self, root: Path | None = None) -> None:
        self.root = root and Path.cwd()
    
    xǁWorkspaceDiscoveryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁ__init____mutmut_1': xǁWorkspaceDiscoveryǁ__init____mutmut_1, 
        'xǁWorkspaceDiscoveryǁ__init____mutmut_2': xǁWorkspaceDiscoveryǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁ__init____mutmut_orig)
    xǁWorkspaceDiscoveryǁ__init____mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁ__init__'

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_orig(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_1(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is not None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_2(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = None

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_3(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["XX*XX"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_4(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = None
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_5(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info(None, root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_6(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=None, patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_7(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=None)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_8(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info(root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_9(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_10(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), )

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_11(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("XX🔍 Discovering repositoriesXX", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_12(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_13(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 DISCOVERING REPOSITORIES", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_14(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(None), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_15(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(None):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_16(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() or path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_17(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path == self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_18(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = None
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_19(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(None)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_20(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git or repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_21(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(None)

        logger.info("📋 Discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_22(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info(None, count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_23(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", count=None)
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_24(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info(count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_25(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 Discovered repositories", )
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_26(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("XX📋 Discovered repositoriesXX", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_27(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 discovered repositories", count=len(repos))
        return repos

    def xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_28(self, patterns: list[str] | None = None) -> list[RepoInfo]:
        """Find all Git repos with pyproject.toml."""
        if patterns is None:
            patterns = ["*"]

        repos = []
        logger.info("🔍 Discovering repositories", root=str(self.root), patterns=patterns)

        for pattern in patterns:
            for path in self.root.glob(pattern):
                if path.is_dir() and path != self.root:
                    repo_info = self.analyze_repo(path)
                    if repo_info.has_git and repo_info.has_pyproject:
                        repos.append(repo_info)

        logger.info("📋 DISCOVERED REPOSITORIES", count=len(repos))
        return repos
    
    xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_1': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_1, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_2': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_2, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_3': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_3, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_4': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_4, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_5': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_5, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_6': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_6, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_7': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_7, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_8': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_8, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_9': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_9, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_10': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_10, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_11': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_11, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_12': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_12, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_13': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_13, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_14': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_14, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_15': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_15, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_16': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_16, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_17': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_17, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_18': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_18, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_19': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_19, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_20': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_20, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_21': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_21, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_22': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_22, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_23': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_23, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_24': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_24, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_25': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_25, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_26': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_26, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_27': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_27, 
        'xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_28': xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_28
    }
    
    def discover_repos(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_mutants"), args, kwargs, self)
        return result 
    
    discover_repos.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_orig)
    xǁWorkspaceDiscoveryǁdiscover_repos__mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁdiscover_repos'

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_orig(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_1(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = None
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_2(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path * ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_3(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / "XX.gitXX").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_4(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".GIT").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_5(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = None

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_6(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path * "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_7(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "XXpyproject.tomlXX").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_8(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "PYPROJECT.TOML").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_9(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = ""
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_10(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = ""
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_11(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = ""

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_12(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open(None) as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_13(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path * "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_14(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "XXpyproject.tomlXX").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_15(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "PYPROJECT.TOML").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_16(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("XXrbXX") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_17(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("RB") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_18(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = None

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_19(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(None)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_20(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = None
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_21(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = None
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_22(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get(None)
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_23(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get(None, {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_24(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", None).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_25(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get({}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_26(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", ).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_27(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("XXprojectXX", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_28(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("PROJECT", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_29(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("XXnameXX")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_30(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("NAME")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_31(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = None

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_32(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(None, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_33(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, None)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_34(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_35(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, )

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_36(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning(None, path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_37(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=None, error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_38(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=None)

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_39(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning(path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_40(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_41(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), )

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_42(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("XX⚠️ Failed to parse pyproject.tomlXX", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_43(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_44(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ FAILED TO PARSE PYPROJECT.TOML", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_45(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(None), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_46(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(None))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_47(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_48(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = None

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_49(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=None,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_50(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=None,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_51(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=None,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_52(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=None,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_53(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=None,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_54(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=None,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_55(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_56(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_57(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_58(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            detected_type=detected_type,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_59(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            current_config=current_config,
        )

    def xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_60(self, path: Path) -> RepoInfo:
        """Analyze a single repository."""
        has_git = (path / ".git").exists()
        has_pyproject = (path / "pyproject.toml").exists()

        name = None
        detected_type = None
        current_config = None

        if has_pyproject:
            try:
                with (path / "pyproject.toml").open("rb") as f:
                    pyproject = tomllib.load(f)

                current_config = pyproject
                name = pyproject.get("project", {}).get("name")
                detected_type = self.detect_repo_type(pyproject, path)

            except Exception as e:
                logger.warning("⚠️ Failed to parse pyproject.toml", path=str(path), error=str(e))

        if not name:
            name = path.name

        return RepoInfo(
            path=path,
            name=name,
            has_git=has_git,
            has_pyproject=has_pyproject,
            detected_type=detected_type,
            )
    
    xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_1': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_1, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_2': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_2, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_3': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_3, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_4': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_4, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_5': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_5, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_6': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_6, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_7': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_7, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_8': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_8, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_9': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_9, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_10': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_10, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_11': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_11, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_12': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_12, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_13': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_13, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_14': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_14, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_15': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_15, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_16': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_16, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_17': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_17, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_18': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_18, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_19': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_19, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_20': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_20, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_21': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_21, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_22': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_22, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_23': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_23, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_24': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_24, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_25': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_25, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_26': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_26, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_27': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_27, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_28': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_28, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_29': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_29, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_30': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_30, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_31': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_31, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_32': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_32, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_33': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_33, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_34': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_34, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_35': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_35, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_36': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_36, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_37': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_37, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_38': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_38, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_39': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_39, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_40': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_40, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_41': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_41, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_42': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_42, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_43': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_43, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_44': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_44, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_45': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_45, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_46': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_46, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_47': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_47, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_48': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_48, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_49': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_49, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_50': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_50, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_51': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_51, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_52': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_52, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_53': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_53, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_54': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_54, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_55': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_55, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_56': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_56, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_57': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_57, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_58': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_58, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_59': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_59, 
        'xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_60': xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_60
    }
    
    def analyze_repo(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_mutants"), args, kwargs, self)
        return result 
    
    analyze_repo.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_orig)
    xǁWorkspaceDiscoveryǁanalyze_repo__mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁanalyze_repo'

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_orig(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_1(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = None
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_2(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get(None, {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_3(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", None)
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_4(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get({})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_5(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", )
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_6(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("XXprojectXX", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_7(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("PROJECT", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_8(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = None
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_9(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get(None, "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_10(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", None)
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_11(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_12(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", )
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_13(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("XXnameXX", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_14(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("NAME", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_15(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "XXXX")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_16(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = None

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_17(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get(None, [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_18(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", None)

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_19(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get([])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_20(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", )

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_21(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("XXdependenciesXX", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_22(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("DEPENDENCIES", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_23(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "XXprovide-foundationXX" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_24(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "PROVIDE-FOUNDATION" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_25(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" not in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_26(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "XXfoundationXX"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_27(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "FOUNDATION"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_28(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "XXprovide-testkitXX" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_29(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "PROVIDE-TESTKIT" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_30(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" not in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_31(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "XXtestkitXX"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_32(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "TESTKIT"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_33(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith(None):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_34(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("XXpyvider-XX"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_35(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("PYVIDER-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_36(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "XXpyvider-pluginXX"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_37(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "PYVIDER-PLUGIN"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_38(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name != "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_39(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "XXpyviderXX":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_40(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "PYVIDER":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_41(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "XXproviderXX"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_42(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "PROVIDER"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_43(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "XXflavorXX" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_44(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "FLAVOR" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_45(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" not in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_46(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "XXpackagingXX"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_47(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "PACKAGING"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_48(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = None
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_49(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(None)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_50(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = "XX XX".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_51(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "XXprovide-foundationXX" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_52(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "PROVIDE-FOUNDATION" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_53(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" not in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_54(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "XXfoundation-basedXX"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_55(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "FOUNDATION-BASED"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_56(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "XXpyviderXX" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_57(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "PYVIDER" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_58(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" not in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_59(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "XXpyvider-pluginXX"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_60(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "PYVIDER-PLUGIN"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_61(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" * "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_62(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path * "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_63(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "XXsrcXX" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_64(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "SRC" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_65(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "XXpyviderXX").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_66(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "PYVIDER").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_67(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "XXproviderXX"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_68(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "PROVIDER"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_69(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" * "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_70(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path * "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_71(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "XXsrcXX" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_72(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "SRC" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_73(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "XXprovideXX").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_74(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "PROVIDE").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_75(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "XXfoundation-basedXX"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_76(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "FOUNDATION-BASED"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_77(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = None
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_78(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get(None, [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_79(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", None)
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_80(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get([])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_81(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", )
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_82(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("XXclassifiersXX", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_83(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("CLASSIFIERS", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_84(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "XXTopic :: System :: LoggingXX" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_85(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "topic :: system :: logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_86(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "TOPIC :: SYSTEM :: LOGGING" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_87(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" not in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_88(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "XXfoundation-basedXX"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_89(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "FOUNDATION-BASED"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_90(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "XXTopic :: Software Development :: Build ToolsXX" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_91(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "topic :: software development :: build tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_92(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "TOPIC :: SOFTWARE DEVELOPMENT :: BUILD TOOLS" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_93(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" not in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_94(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "XXpackagingXX"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_95(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "PACKAGING"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_96(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug(None, name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_97(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=None)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_98(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug(name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_99(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", )
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_100(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("XX🤷 Could not detect repo typeXX", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_101(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 could not detect repo type", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_102(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 COULD NOT DETECT REPO TYPE", name=name)
        return "unknown"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_103(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "XXunknownXX"

    def xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_104(self, pyproject: dict[str, Any], path: Path) -> str | None:
        """Determine repository type from pyproject.toml and path."""
        project = pyproject.get("project", {})
        name = project.get("name", "")
        dependencies = project.get("dependencies", [])

        # Check name patterns
        if "provide-foundation" in name:
            return "foundation"
        elif "provide-testkit" in name:
            return "testkit"
        elif name.startswith("pyvider-"):
            return "pyvider-plugin"
        elif name == "pyvider":
            return "provider"
        elif "flavor" in name:
            return "packaging"

        # Check dependencies
        dep_str = " ".join(dependencies)
        if "provide-foundation" in dep_str:
            return "foundation-based"
        elif "pyvider" in dep_str:
            return "pyvider-plugin"

        # Check for specific files
        if (path / "src" / "pyvider").exists():
            return "provider"
        elif (path / "src" / "provide").exists():
            return "foundation-based"

        # Check classifiers
        classifiers = project.get("classifiers", [])
        for classifier in classifiers:
            if "Topic :: System :: Logging" in classifier:
                return "foundation-based"
            elif "Topic :: Software Development :: Build Tools" in classifier:
                return "packaging"

        logger.debug("🤷 Could not detect repo type", name=name)
        return "UNKNOWN"
    
    xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_1': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_1, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_2': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_2, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_3': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_3, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_4': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_4, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_5': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_5, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_6': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_6, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_7': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_7, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_8': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_8, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_9': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_9, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_10': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_10, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_11': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_11, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_12': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_12, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_13': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_13, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_14': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_14, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_15': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_15, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_16': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_16, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_17': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_17, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_18': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_18, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_19': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_19, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_20': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_20, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_21': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_21, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_22': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_22, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_23': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_23, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_24': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_24, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_25': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_25, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_26': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_26, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_27': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_27, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_28': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_28, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_29': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_29, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_30': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_30, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_31': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_31, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_32': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_32, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_33': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_33, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_34': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_34, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_35': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_35, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_36': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_36, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_37': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_37, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_38': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_38, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_39': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_39, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_40': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_40, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_41': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_41, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_42': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_42, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_43': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_43, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_44': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_44, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_45': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_45, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_46': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_46, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_47': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_47, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_48': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_48, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_49': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_49, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_50': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_50, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_51': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_51, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_52': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_52, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_53': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_53, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_54': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_54, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_55': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_55, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_56': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_56, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_57': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_57, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_58': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_58, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_59': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_59, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_60': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_60, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_61': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_61, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_62': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_62, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_63': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_63, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_64': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_64, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_65': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_65, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_66': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_66, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_67': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_67, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_68': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_68, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_69': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_69, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_70': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_70, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_71': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_71, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_72': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_72, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_73': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_73, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_74': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_74, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_75': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_75, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_76': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_76, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_77': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_77, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_78': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_78, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_79': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_79, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_80': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_80, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_81': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_81, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_82': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_82, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_83': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_83, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_84': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_84, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_85': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_85, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_86': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_86, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_87': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_87, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_88': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_88, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_89': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_89, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_90': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_90, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_91': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_91, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_92': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_92, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_93': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_93, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_94': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_94, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_95': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_95, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_96': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_96, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_97': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_97, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_98': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_98, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_99': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_99, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_100': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_100, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_101': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_101, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_102': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_102, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_103': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_103, 
        'xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_104': xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_104
    }
    
    def detect_repo_type(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_mutants"), args, kwargs, self)
        return result 
    
    detect_repo_type.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_orig)
    xǁWorkspaceDiscoveryǁdetect_repo_type__mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁdetect_repo_type'

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_orig(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_1(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = None

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_2(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "XXpathXX": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_3(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "PATH": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_4(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(None),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_5(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "XXexistsXX": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_6(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "EXISTS": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_7(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "XXhas_gitXX": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_8(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "HAS_GIT": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_9(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": True,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_10(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "XXhas_pyprojectXX": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_11(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "HAS_PYPROJECT": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_12(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": True,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_13(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "XXhas_workenvXX": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_14(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "HAS_WORKENV": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_15(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": True,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_16(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "XXhas_claude_mdXX": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_17(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "HAS_CLAUDE_MD": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_18(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": True,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_19(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "XXgit_statusXX": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_20(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "GIT_STATUS": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_21(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_22(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = None
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_23(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["XXhas_gitXX"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_24(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["HAS_GIT"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_25(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path * ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_26(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / "XX.gitXX").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_27(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".GIT").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_28(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = None
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_29(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["XXhas_pyprojectXX"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_30(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["HAS_PYPROJECT"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_31(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path * "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_32(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "XXpyproject.tomlXX").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_33(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "PYPROJECT.TOML").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_34(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = None
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_35(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["XXhas_workenvXX"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_36(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["HAS_WORKENV"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_37(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path * "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_38(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "XXworkenvXX").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_39(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "WORKENV").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_40(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = None

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_41(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["XXhas_claude_mdXX"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_42(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["HAS_CLAUDE_MD"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_43(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path * "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_44(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "XXCLAUDE.mdXX").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_45(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "claude.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_46(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.MD").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_47(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["XXhas_gitXX"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_48(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["HAS_GIT"]:
            status["git_status"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_49(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = None

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_50(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["XXgit_statusXX"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_51(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["GIT_STATUS"] = self._get_git_status(repo_path)

        return status

    def xǁWorkspaceDiscoveryǁget_repo_status__mutmut_52(self, repo_path: Path) -> dict[str, Any]:
        """Get current status of repository."""
        status = {
            "path": str(repo_path),
            "exists": repo_path.exists(),
            "has_git": False,
            "has_pyproject": False,
            "has_workenv": False,
            "has_claude_md": False,
            "git_status": None,
        }

        if not repo_path.exists():
            return status

        status["has_git"] = (repo_path / ".git").exists()
        status["has_pyproject"] = (repo_path / "pyproject.toml").exists()
        status["has_workenv"] = (repo_path / "workenv").exists()
        status["has_claude_md"] = (repo_path / "CLAUDE.md").exists()

        # Get git status if available
        if status["has_git"]:
            status["git_status"] = self._get_git_status(None)

        return status
    
    xǁWorkspaceDiscoveryǁget_repo_status__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_1': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_1, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_2': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_2, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_3': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_3, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_4': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_4, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_5': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_5, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_6': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_6, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_7': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_7, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_8': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_8, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_9': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_9, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_10': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_10, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_11': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_11, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_12': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_12, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_13': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_13, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_14': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_14, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_15': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_15, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_16': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_16, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_17': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_17, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_18': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_18, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_19': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_19, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_20': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_20, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_21': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_21, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_22': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_22, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_23': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_23, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_24': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_24, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_25': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_25, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_26': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_26, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_27': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_27, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_28': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_28, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_29': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_29, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_30': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_30, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_31': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_31, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_32': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_32, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_33': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_33, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_34': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_34, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_35': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_35, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_36': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_36, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_37': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_37, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_38': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_38, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_39': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_39, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_40': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_40, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_41': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_41, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_42': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_42, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_43': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_43, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_44': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_44, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_45': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_45, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_46': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_46, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_47': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_47, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_48': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_48, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_49': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_49, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_50': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_50, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_51': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_51, 
        'xǁWorkspaceDiscoveryǁget_repo_status__mutmut_52': xǁWorkspaceDiscoveryǁget_repo_status__mutmut_52
    }
    
    def get_repo_status(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁget_repo_status__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁget_repo_status__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_repo_status.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁget_repo_status__mutmut_orig)
    xǁWorkspaceDiscoveryǁget_repo_status__mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁget_repo_status'

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_orig(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_1(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = None

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_2(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                None,
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_3(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=None,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_4(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=None,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_5(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=None,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_6(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=None,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_7(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_8(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_9(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_10(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_11(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_12(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["XXgitXX", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_13(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["GIT", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_14(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "XXbranchXX", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_15(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "BRANCH", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_16(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "XX--show-currentXX"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_17(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--SHOW-CURRENT"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_18(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=False,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_19(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=False,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_20(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=False,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_21(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = None

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_22(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                None,
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_23(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=None,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_24(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=None,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_25(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=None,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_26(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=None,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_27(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_28(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_29(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_30(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_31(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_32(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["XXgitXX", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_33(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["GIT", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_34(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "XXstatusXX", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_35(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "STATUS", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_36(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "XX--porcelainXX"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_37(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--PORCELAIN"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_38(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=False,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_39(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=False,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_40(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=False,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_41(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "XXbranchXX": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_42(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "BRANCH": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_43(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "XXdirtyXX": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_44(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "DIRTY": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_45(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(None),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_46(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "XXfiles_changedXX": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_47(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "FILES_CHANGED": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_48(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug(None, path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_49(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=None, error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_50(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=None)
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_51(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug(path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_52(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_53(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), )
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_54(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("XX⚠️ Failed to get git statusXX", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_55(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ failed to get git status", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_56(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ FAILED TO GET GIT STATUS", path=str(repo_path), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_57(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(None), error=str(e))
            return None

    def xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_58(self, repo_path: Path) -> dict[str, Any] | None:
        """Get git status for repository."""
        try:
            from provide.foundation.process import run

            # Get current branch
            branch_result = run(
                ["git", "branch", "--show-current"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            # Get status
            status_result = run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )

            return {
                "branch": branch_result.stdout.strip(),
                "dirty": bool(status_result.stdout.strip()),
                "files_changed": len(status_result.stdout.strip().splitlines()),
            }

        except Exception as e:
            logger.debug("⚠️ Failed to get git status", path=str(repo_path), error=str(None))
            return None
    
    xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_1': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_1, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_2': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_2, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_3': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_3, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_4': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_4, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_5': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_5, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_6': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_6, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_7': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_7, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_8': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_8, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_9': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_9, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_10': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_10, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_11': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_11, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_12': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_12, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_13': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_13, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_14': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_14, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_15': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_15, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_16': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_16, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_17': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_17, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_18': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_18, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_19': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_19, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_20': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_20, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_21': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_21, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_22': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_22, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_23': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_23, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_24': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_24, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_25': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_25, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_26': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_26, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_27': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_27, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_28': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_28, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_29': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_29, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_30': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_30, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_31': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_31, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_32': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_32, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_33': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_33, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_34': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_34, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_35': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_35, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_36': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_36, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_37': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_37, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_38': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_38, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_39': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_39, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_40': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_40, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_41': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_41, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_42': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_42, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_43': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_43, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_44': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_44, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_45': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_45, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_46': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_46, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_47': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_47, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_48': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_48, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_49': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_49, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_50': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_50, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_51': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_51, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_52': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_52, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_53': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_53, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_54': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_54, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_55': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_55, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_56': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_56, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_57': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_57, 
        'xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_58': xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_58
    }
    
    def _get_git_status(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_git_status.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_orig)
    xǁWorkspaceDiscoveryǁ_get_git_status__mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁ_get_git_status'

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_orig(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_1(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = None

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_2(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_3(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(None)
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_4(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = None
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_5(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" * "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_6(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root * ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_7(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / "XX.wrknvXX" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_8(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".WRKNV" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_9(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "XXworkspace.tomlXX"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_10(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "WORKSPACE.TOML"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_11(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_12(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append(None)

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_13(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("XXNo workspace.toml found in .wrknv/XX")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_14(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("no workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_15(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("NO WORKSPACE.TOML FOUND IN .WRKNV/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_16(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = None

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_17(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_18(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(None)

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_19(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_20(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(None)

            if repo.detected_type == "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_21(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type != "unknown":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_22(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "XXunknownXX":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_23(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "UNKNOWN":
                issues.append(f"Could not detect type for repository {repo.name}")

        return issues

    def xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_24(self, root: Path) -> list[str]:
        """Validate workspace structure and return issues."""
        issues = []

        if not root.exists():
            issues.append(f"Workspace root does not exist: {root}")
            return issues

        # Check for workspace config
        workspace_config = root / ".wrknv" / "workspace.toml"
        if not workspace_config.exists():
            issues.append("No workspace.toml found in .wrknv/")

        # Check for common problems
        repos = self.discover_repos()

        for repo in repos:
            if not repo.has_git:
                issues.append(f"Repository {repo.name} is not a git repository")

            if not repo.has_pyproject:
                issues.append(f"Repository {repo.name} has no pyproject.toml")

            if repo.detected_type == "unknown":
                issues.append(None)

        return issues
    
    xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_1': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_1, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_2': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_2, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_3': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_3, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_4': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_4, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_5': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_5, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_6': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_6, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_7': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_7, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_8': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_8, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_9': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_9, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_10': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_10, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_11': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_11, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_12': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_12, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_13': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_13, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_14': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_14, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_15': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_15, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_16': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_16, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_17': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_17, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_18': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_18, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_19': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_19, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_20': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_20, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_21': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_21, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_22': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_22, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_23': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_23, 
        'xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_24': xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_24
    }
    
    def validate_workspace_structure(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_mutants"), args, kwargs, self)
        return result 
    
    validate_workspace_structure.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_orig)
    xǁWorkspaceDiscoveryǁvalidate_workspace_structure__mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁvalidate_workspace_structure'

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_orig(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_1(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = None

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_2(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = None
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_3(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = None
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_4(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type and "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_5(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "XXunknownXX"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_6(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "UNKNOWN"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_7(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = None

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_8(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) - 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_9(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(None, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_10(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, None) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_11(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_12(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, ) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_13(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 1) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_14(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 2

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_15(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "XXrootXX": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_16(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "ROOT": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_17(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(None),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_18(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "XXtotal_reposXX": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_19(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "TOTAL_REPOS": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_20(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "XXtype_distributionXX": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_21(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "TYPE_DISTRIBUTION": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_22(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "XXreposXX": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_23(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "REPOS": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_24(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "XXnameXX": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_25(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "NAME": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_26(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "XXtypeXX": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_27(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "TYPE": repo.detected_type,
                    "path": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_28(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "XXpathXX": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_29(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "PATH": str(repo.path.relative_to(self.root)),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_30(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(None),
                }
                for repo in repos
            ],
        }

    def xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_31(self) -> dict[str, Any]:
        """Get summary of workspace state."""
        repos = self.discover_repos()

        type_counts: dict[str, int] = {}
        for repo in repos:
            repo_type = repo.detected_type or "unknown"
            type_counts[repo_type] = type_counts.get(repo_type, 0) + 1

        return {
            "root": str(self.root),
            "total_repos": len(repos),
            "type_distribution": type_counts,
            "repos": [
                {
                    "name": repo.name,
                    "type": repo.detected_type,
                    "path": str(repo.path.relative_to(None)),
                }
                for repo in repos
            ],
        }
    
    xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_1': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_1, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_2': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_2, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_3': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_3, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_4': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_4, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_5': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_5, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_6': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_6, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_7': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_7, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_8': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_8, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_9': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_9, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_10': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_10, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_11': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_11, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_12': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_12, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_13': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_13, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_14': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_14, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_15': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_15, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_16': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_16, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_17': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_17, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_18': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_18, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_19': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_19, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_20': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_20, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_21': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_21, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_22': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_22, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_23': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_23, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_24': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_24, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_25': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_25, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_26': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_26, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_27': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_27, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_28': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_28, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_29': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_29, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_30': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_30, 
        'xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_31': xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_31
    }
    
    def get_workspace_summary(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_workspace_summary.__signature__ = _mutmut_signature(xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_orig)
    xǁWorkspaceDiscoveryǁget_workspace_summary__mutmut_orig.__name__ = 'xǁWorkspaceDiscoveryǁget_workspace_summary'


# 🧰🌍🔚
