#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Workspace Configuration Synchronization
=======================================
Synchronize configurations across repositories in workspace."""

from __future__ import annotations

import difflib
from pathlib import Path
from typing import Any

from provide.foundation import logger

from .schema import RepoConfig, WorkspaceConfig
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


class WorkspaceSync:
    """Synchronize configurations across repositories."""

    def xǁWorkspaceSyncǁ__init____mutmut_orig(self, workspace_config: WorkspaceConfig) -> None:
        self.config = workspace_config

    def xǁWorkspaceSyncǁ__init____mutmut_1(self, workspace_config: WorkspaceConfig) -> None:
        self.config = None
    
    xǁWorkspaceSyncǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁ__init____mutmut_1': xǁWorkspaceSyncǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁ__init____mutmut_orig)
    xǁWorkspaceSyncǁ__init____mutmut_orig.__name__ = 'xǁWorkspaceSyncǁ__init__'

    async def xǁWorkspaceSyncǁsync_all__mutmut_orig(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_1(self, dry_run: bool = True) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_2(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info(None, repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_3(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=None, dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_4(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=None)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_5(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info(repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_6(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_7(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), )

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_8(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("XX🔄 Starting workspace syncXX", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_9(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_10(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 STARTING WORKSPACE SYNC", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_11(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = None
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_12(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = None
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_13(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(None, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_14(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, None)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_15(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_16(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, )
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_17(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = None
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_18(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error(None, repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_19(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=None, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_20(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=None)
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_21(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error(repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_22(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_23(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, )
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_24(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("XX❌ Failed to sync repoXX", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_25(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_26(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ FAILED TO SYNC REPO", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_27(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(None))
                results[repo.name] = {"error": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_28(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = None

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_29(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"XXerrorXX": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_30(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"ERROR": str(e)}

        return results

    async def xǁWorkspaceSyncǁsync_all__mutmut_31(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync all repositories in workspace."""
        logger.info("🔄 Starting workspace sync", repos=len(self.config.repos), dry_run=dry_run)

        results = {}
        for repo in self.config.repos:
            try:
                result = await self.sync_repo(repo, dry_run)
                results[repo.name] = result
            except Exception as e:
                logger.error("❌ Failed to sync repo", repo=repo.name, error=str(e))
                results[repo.name] = {"error": str(None)}

        return results
    
    xǁWorkspaceSyncǁsync_all__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁsync_all__mutmut_1': xǁWorkspaceSyncǁsync_all__mutmut_1, 
        'xǁWorkspaceSyncǁsync_all__mutmut_2': xǁWorkspaceSyncǁsync_all__mutmut_2, 
        'xǁWorkspaceSyncǁsync_all__mutmut_3': xǁWorkspaceSyncǁsync_all__mutmut_3, 
        'xǁWorkspaceSyncǁsync_all__mutmut_4': xǁWorkspaceSyncǁsync_all__mutmut_4, 
        'xǁWorkspaceSyncǁsync_all__mutmut_5': xǁWorkspaceSyncǁsync_all__mutmut_5, 
        'xǁWorkspaceSyncǁsync_all__mutmut_6': xǁWorkspaceSyncǁsync_all__mutmut_6, 
        'xǁWorkspaceSyncǁsync_all__mutmut_7': xǁWorkspaceSyncǁsync_all__mutmut_7, 
        'xǁWorkspaceSyncǁsync_all__mutmut_8': xǁWorkspaceSyncǁsync_all__mutmut_8, 
        'xǁWorkspaceSyncǁsync_all__mutmut_9': xǁWorkspaceSyncǁsync_all__mutmut_9, 
        'xǁWorkspaceSyncǁsync_all__mutmut_10': xǁWorkspaceSyncǁsync_all__mutmut_10, 
        'xǁWorkspaceSyncǁsync_all__mutmut_11': xǁWorkspaceSyncǁsync_all__mutmut_11, 
        'xǁWorkspaceSyncǁsync_all__mutmut_12': xǁWorkspaceSyncǁsync_all__mutmut_12, 
        'xǁWorkspaceSyncǁsync_all__mutmut_13': xǁWorkspaceSyncǁsync_all__mutmut_13, 
        'xǁWorkspaceSyncǁsync_all__mutmut_14': xǁWorkspaceSyncǁsync_all__mutmut_14, 
        'xǁWorkspaceSyncǁsync_all__mutmut_15': xǁWorkspaceSyncǁsync_all__mutmut_15, 
        'xǁWorkspaceSyncǁsync_all__mutmut_16': xǁWorkspaceSyncǁsync_all__mutmut_16, 
        'xǁWorkspaceSyncǁsync_all__mutmut_17': xǁWorkspaceSyncǁsync_all__mutmut_17, 
        'xǁWorkspaceSyncǁsync_all__mutmut_18': xǁWorkspaceSyncǁsync_all__mutmut_18, 
        'xǁWorkspaceSyncǁsync_all__mutmut_19': xǁWorkspaceSyncǁsync_all__mutmut_19, 
        'xǁWorkspaceSyncǁsync_all__mutmut_20': xǁWorkspaceSyncǁsync_all__mutmut_20, 
        'xǁWorkspaceSyncǁsync_all__mutmut_21': xǁWorkspaceSyncǁsync_all__mutmut_21, 
        'xǁWorkspaceSyncǁsync_all__mutmut_22': xǁWorkspaceSyncǁsync_all__mutmut_22, 
        'xǁWorkspaceSyncǁsync_all__mutmut_23': xǁWorkspaceSyncǁsync_all__mutmut_23, 
        'xǁWorkspaceSyncǁsync_all__mutmut_24': xǁWorkspaceSyncǁsync_all__mutmut_24, 
        'xǁWorkspaceSyncǁsync_all__mutmut_25': xǁWorkspaceSyncǁsync_all__mutmut_25, 
        'xǁWorkspaceSyncǁsync_all__mutmut_26': xǁWorkspaceSyncǁsync_all__mutmut_26, 
        'xǁWorkspaceSyncǁsync_all__mutmut_27': xǁWorkspaceSyncǁsync_all__mutmut_27, 
        'xǁWorkspaceSyncǁsync_all__mutmut_28': xǁWorkspaceSyncǁsync_all__mutmut_28, 
        'xǁWorkspaceSyncǁsync_all__mutmut_29': xǁWorkspaceSyncǁsync_all__mutmut_29, 
        'xǁWorkspaceSyncǁsync_all__mutmut_30': xǁWorkspaceSyncǁsync_all__mutmut_30, 
        'xǁWorkspaceSyncǁsync_all__mutmut_31': xǁWorkspaceSyncǁsync_all__mutmut_31
    }
    
    def sync_all(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁsync_all__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁsync_all__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sync_all.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁsync_all__mutmut_orig)
    xǁWorkspaceSyncǁsync_all__mutmut_orig.__name__ = 'xǁWorkspaceSyncǁsync_all'

    async def xǁWorkspaceSyncǁsync_repo__mutmut_orig(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_1(self, repo: RepoConfig, dry_run: bool = True) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_2(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = None

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_3(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(None)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_4(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = None

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_5(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(None, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_6(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, None)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_7(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_8(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, )

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_9(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = None
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_10(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = None
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_11(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path * filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_12(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = None
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_13(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(None, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_14(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, None, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_15(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, None)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_16(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_17(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_18(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, )
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_19(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = None

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_20(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = None

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_21(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "XXrepoXX": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_22(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "REPO": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_23(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "XXchangesXX": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_24(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "CHANGES": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_25(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "XXfiles_updatedXX": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_26(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "FILES_UPDATED": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_27(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(None),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_28(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(2 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_29(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get(None, False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_30(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", None)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_31(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get(False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_32(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", )),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_33(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("XXchangedXX", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_34(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("CHANGED", False)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_35(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", True)),
        }

        logger.debug("📋 Repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_36(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug(None, **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_37(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug(**result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_38(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 Repo sync result", )
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_39(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("XX📋 Repo sync resultXX", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_40(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 repo sync result", **result)
        return result

    async def xǁWorkspaceSyncǁsync_repo__mutmut_41(self, repo: RepoConfig, dry_run: bool = False) -> dict[str, Any]:
        """Sync single repository configuration."""

        # Build template context
        context = self._build_template_context(repo)

        # Generate configurations
        configs = self._generate_configs(repo, context)

        # Apply changes
        changes = {}
        for filename, new_content in configs.items():
            file_path = repo.path / filename
            change_info = await self._apply_config_change(file_path, new_content, dry_run)
            changes[filename] = change_info

        result = {
            "repo": repo.name,
            "changes": changes,
            "files_updated": sum(1 for c in changes.values() if c.get("changed", False)),
        }

        logger.debug("📋 REPO SYNC RESULT", **result)
        return result
    
    xǁWorkspaceSyncǁsync_repo__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁsync_repo__mutmut_1': xǁWorkspaceSyncǁsync_repo__mutmut_1, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_2': xǁWorkspaceSyncǁsync_repo__mutmut_2, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_3': xǁWorkspaceSyncǁsync_repo__mutmut_3, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_4': xǁWorkspaceSyncǁsync_repo__mutmut_4, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_5': xǁWorkspaceSyncǁsync_repo__mutmut_5, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_6': xǁWorkspaceSyncǁsync_repo__mutmut_6, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_7': xǁWorkspaceSyncǁsync_repo__mutmut_7, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_8': xǁWorkspaceSyncǁsync_repo__mutmut_8, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_9': xǁWorkspaceSyncǁsync_repo__mutmut_9, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_10': xǁWorkspaceSyncǁsync_repo__mutmut_10, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_11': xǁWorkspaceSyncǁsync_repo__mutmut_11, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_12': xǁWorkspaceSyncǁsync_repo__mutmut_12, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_13': xǁWorkspaceSyncǁsync_repo__mutmut_13, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_14': xǁWorkspaceSyncǁsync_repo__mutmut_14, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_15': xǁWorkspaceSyncǁsync_repo__mutmut_15, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_16': xǁWorkspaceSyncǁsync_repo__mutmut_16, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_17': xǁWorkspaceSyncǁsync_repo__mutmut_17, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_18': xǁWorkspaceSyncǁsync_repo__mutmut_18, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_19': xǁWorkspaceSyncǁsync_repo__mutmut_19, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_20': xǁWorkspaceSyncǁsync_repo__mutmut_20, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_21': xǁWorkspaceSyncǁsync_repo__mutmut_21, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_22': xǁWorkspaceSyncǁsync_repo__mutmut_22, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_23': xǁWorkspaceSyncǁsync_repo__mutmut_23, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_24': xǁWorkspaceSyncǁsync_repo__mutmut_24, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_25': xǁWorkspaceSyncǁsync_repo__mutmut_25, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_26': xǁWorkspaceSyncǁsync_repo__mutmut_26, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_27': xǁWorkspaceSyncǁsync_repo__mutmut_27, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_28': xǁWorkspaceSyncǁsync_repo__mutmut_28, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_29': xǁWorkspaceSyncǁsync_repo__mutmut_29, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_30': xǁWorkspaceSyncǁsync_repo__mutmut_30, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_31': xǁWorkspaceSyncǁsync_repo__mutmut_31, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_32': xǁWorkspaceSyncǁsync_repo__mutmut_32, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_33': xǁWorkspaceSyncǁsync_repo__mutmut_33, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_34': xǁWorkspaceSyncǁsync_repo__mutmut_34, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_35': xǁWorkspaceSyncǁsync_repo__mutmut_35, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_36': xǁWorkspaceSyncǁsync_repo__mutmut_36, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_37': xǁWorkspaceSyncǁsync_repo__mutmut_37, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_38': xǁWorkspaceSyncǁsync_repo__mutmut_38, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_39': xǁWorkspaceSyncǁsync_repo__mutmut_39, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_40': xǁWorkspaceSyncǁsync_repo__mutmut_40, 
        'xǁWorkspaceSyncǁsync_repo__mutmut_41': xǁWorkspaceSyncǁsync_repo__mutmut_41
    }
    
    def sync_repo(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁsync_repo__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁsync_repo__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sync_repo.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁsync_repo__mutmut_orig)
    xǁWorkspaceSyncǁsync_repo__mutmut_orig.__name__ = 'xǁWorkspaceSyncǁsync_repo'

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_orig(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_1(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = None

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_2(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(None)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_3(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            None
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_4(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "XXproject_nameXX": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_5(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "PROJECT_NAME": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_6(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "XXpackage_typeXX": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_7(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "PACKAGE_TYPE": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_8(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "XXfeaturesXX": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_9(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "FEATURES": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_10(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(None)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_11(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault(None, "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_12(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", None)
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_13(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_14(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", )
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_15(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("XXversionXX", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_16(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("VERSION", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_17(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "XX1.0.0XX")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_18(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault(None, "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_19(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", None)
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_20(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_21(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", )
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_22(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("XXpython_versionXX", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_23(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("PYTHON_VERSION", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_24(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "XX3.11XX")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_25(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault(None, f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_26(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", None)
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_27(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault(f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_28(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", )
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_29(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("XXdescriptionXX", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_30(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("DESCRIPTION", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_31(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault(None, True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_32(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", None)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_33(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault(True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_34(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", )
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_35(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("XXuse_mypyXX", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_36(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("USE_MYPY", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_37(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", False)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_38(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault(None, True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_39(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", None)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_40(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault(True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_41(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", )
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_42(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("XXuse_pytestXX", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_43(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("USE_PYTEST", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_44(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", False)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_45(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault(None, True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_46(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", None)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_47(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault(True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_48(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", )

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_49(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("XXuse_coverageXX", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_50(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("USE_COVERAGE", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_51(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", False)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_52(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type != "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_53(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "XXfoundation-basedXX":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_54(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "FOUNDATION-BASED":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_55(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                None,
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_56(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                None,
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_57(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_58(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_59(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "XXworkspace_sourcesXX",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_60(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "WORKSPACE_SOURCES",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_61(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "XXprovide-foundationXX": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_62(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "PROVIDE-FOUNDATION": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_63(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"XXworkspaceXX": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_64(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"WORKSPACE": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_65(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": False},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_66(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "XXprovide-testkitXX": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_67(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "PROVIDE-TESTKIT": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_68(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"XXworkspaceXX": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_69(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"WORKSPACE": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_70(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": False},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_71(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type != "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_72(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "XXpyvider-pluginXX":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_73(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "PYVIDER-PLUGIN":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_74(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                None,
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_75(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                None,
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_76(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_77(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_78(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "XXworkspace_sourcesXX",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_79(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "WORKSPACE_SOURCES",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_80(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "XXpyviderXX": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_81(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "PYVIDER": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_82(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"XXworkspaceXX": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_83(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"WORKSPACE": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_84(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": False},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_85(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "XXpyvider-ctyXX": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_86(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "PYVIDER-CTY": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_87(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"XXworkspaceXX": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_88(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"WORKSPACE": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_89(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": False},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_90(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "XXprovide-foundationXX": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_91(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "PROVIDE-FOUNDATION": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_92(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"XXworkspaceXX": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_93(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"WORKSPACE": True},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_94(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": False},
                    "provide-testkit": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_95(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "XXprovide-testkitXX": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_96(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "PROVIDE-TESTKIT": {"workspace": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_97(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"XXworkspaceXX": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_98(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"WORKSPACE": True},
                },
            )

        return context

    def xǁWorkspaceSyncǁ_build_template_context__mutmut_99(self, repo: RepoConfig) -> dict[str, Any]:
        """Build context for template rendering."""
        # Start with global standards
        context = dict(self.config.global_standards)

        # Add repo-specific values
        context.update(
            {
                "project_name": repo.name,
                "package_type": repo.type,
                "features": repo.features,
            }
        )

        # Add custom values (highest priority)
        context.update(repo.custom_values)

        # Set sensible defaults if not provided
        context.setdefault("version", "1.0.0")
        context.setdefault("python_version", "3.11")
        context.setdefault("description", f"Description for {repo.name}")
        context.setdefault("use_mypy", True)
        context.setdefault("use_pytest", True)
        context.setdefault("use_coverage", True)

        # Configure features based on repo type
        if repo.type == "foundation-based":
            context.setdefault(
                "workspace_sources",
                {
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": True},
                },
            )
        elif repo.type == "pyvider-plugin":
            context.setdefault(
                "workspace_sources",
                {
                    "pyvider": {"workspace": True},
                    "pyvider-cty": {"workspace": True},
                    "provide-foundation": {"workspace": True},
                    "provide-testkit": {"workspace": False},
                },
            )

        return context
    
    xǁWorkspaceSyncǁ_build_template_context__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁ_build_template_context__mutmut_1': xǁWorkspaceSyncǁ_build_template_context__mutmut_1, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_2': xǁWorkspaceSyncǁ_build_template_context__mutmut_2, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_3': xǁWorkspaceSyncǁ_build_template_context__mutmut_3, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_4': xǁWorkspaceSyncǁ_build_template_context__mutmut_4, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_5': xǁWorkspaceSyncǁ_build_template_context__mutmut_5, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_6': xǁWorkspaceSyncǁ_build_template_context__mutmut_6, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_7': xǁWorkspaceSyncǁ_build_template_context__mutmut_7, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_8': xǁWorkspaceSyncǁ_build_template_context__mutmut_8, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_9': xǁWorkspaceSyncǁ_build_template_context__mutmut_9, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_10': xǁWorkspaceSyncǁ_build_template_context__mutmut_10, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_11': xǁWorkspaceSyncǁ_build_template_context__mutmut_11, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_12': xǁWorkspaceSyncǁ_build_template_context__mutmut_12, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_13': xǁWorkspaceSyncǁ_build_template_context__mutmut_13, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_14': xǁWorkspaceSyncǁ_build_template_context__mutmut_14, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_15': xǁWorkspaceSyncǁ_build_template_context__mutmut_15, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_16': xǁWorkspaceSyncǁ_build_template_context__mutmut_16, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_17': xǁWorkspaceSyncǁ_build_template_context__mutmut_17, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_18': xǁWorkspaceSyncǁ_build_template_context__mutmut_18, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_19': xǁWorkspaceSyncǁ_build_template_context__mutmut_19, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_20': xǁWorkspaceSyncǁ_build_template_context__mutmut_20, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_21': xǁWorkspaceSyncǁ_build_template_context__mutmut_21, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_22': xǁWorkspaceSyncǁ_build_template_context__mutmut_22, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_23': xǁWorkspaceSyncǁ_build_template_context__mutmut_23, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_24': xǁWorkspaceSyncǁ_build_template_context__mutmut_24, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_25': xǁWorkspaceSyncǁ_build_template_context__mutmut_25, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_26': xǁWorkspaceSyncǁ_build_template_context__mutmut_26, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_27': xǁWorkspaceSyncǁ_build_template_context__mutmut_27, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_28': xǁWorkspaceSyncǁ_build_template_context__mutmut_28, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_29': xǁWorkspaceSyncǁ_build_template_context__mutmut_29, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_30': xǁWorkspaceSyncǁ_build_template_context__mutmut_30, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_31': xǁWorkspaceSyncǁ_build_template_context__mutmut_31, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_32': xǁWorkspaceSyncǁ_build_template_context__mutmut_32, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_33': xǁWorkspaceSyncǁ_build_template_context__mutmut_33, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_34': xǁWorkspaceSyncǁ_build_template_context__mutmut_34, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_35': xǁWorkspaceSyncǁ_build_template_context__mutmut_35, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_36': xǁWorkspaceSyncǁ_build_template_context__mutmut_36, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_37': xǁWorkspaceSyncǁ_build_template_context__mutmut_37, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_38': xǁWorkspaceSyncǁ_build_template_context__mutmut_38, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_39': xǁWorkspaceSyncǁ_build_template_context__mutmut_39, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_40': xǁWorkspaceSyncǁ_build_template_context__mutmut_40, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_41': xǁWorkspaceSyncǁ_build_template_context__mutmut_41, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_42': xǁWorkspaceSyncǁ_build_template_context__mutmut_42, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_43': xǁWorkspaceSyncǁ_build_template_context__mutmut_43, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_44': xǁWorkspaceSyncǁ_build_template_context__mutmut_44, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_45': xǁWorkspaceSyncǁ_build_template_context__mutmut_45, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_46': xǁWorkspaceSyncǁ_build_template_context__mutmut_46, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_47': xǁWorkspaceSyncǁ_build_template_context__mutmut_47, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_48': xǁWorkspaceSyncǁ_build_template_context__mutmut_48, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_49': xǁWorkspaceSyncǁ_build_template_context__mutmut_49, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_50': xǁWorkspaceSyncǁ_build_template_context__mutmut_50, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_51': xǁWorkspaceSyncǁ_build_template_context__mutmut_51, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_52': xǁWorkspaceSyncǁ_build_template_context__mutmut_52, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_53': xǁWorkspaceSyncǁ_build_template_context__mutmut_53, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_54': xǁWorkspaceSyncǁ_build_template_context__mutmut_54, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_55': xǁWorkspaceSyncǁ_build_template_context__mutmut_55, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_56': xǁWorkspaceSyncǁ_build_template_context__mutmut_56, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_57': xǁWorkspaceSyncǁ_build_template_context__mutmut_57, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_58': xǁWorkspaceSyncǁ_build_template_context__mutmut_58, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_59': xǁWorkspaceSyncǁ_build_template_context__mutmut_59, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_60': xǁWorkspaceSyncǁ_build_template_context__mutmut_60, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_61': xǁWorkspaceSyncǁ_build_template_context__mutmut_61, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_62': xǁWorkspaceSyncǁ_build_template_context__mutmut_62, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_63': xǁWorkspaceSyncǁ_build_template_context__mutmut_63, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_64': xǁWorkspaceSyncǁ_build_template_context__mutmut_64, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_65': xǁWorkspaceSyncǁ_build_template_context__mutmut_65, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_66': xǁWorkspaceSyncǁ_build_template_context__mutmut_66, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_67': xǁWorkspaceSyncǁ_build_template_context__mutmut_67, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_68': xǁWorkspaceSyncǁ_build_template_context__mutmut_68, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_69': xǁWorkspaceSyncǁ_build_template_context__mutmut_69, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_70': xǁWorkspaceSyncǁ_build_template_context__mutmut_70, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_71': xǁWorkspaceSyncǁ_build_template_context__mutmut_71, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_72': xǁWorkspaceSyncǁ_build_template_context__mutmut_72, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_73': xǁWorkspaceSyncǁ_build_template_context__mutmut_73, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_74': xǁWorkspaceSyncǁ_build_template_context__mutmut_74, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_75': xǁWorkspaceSyncǁ_build_template_context__mutmut_75, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_76': xǁWorkspaceSyncǁ_build_template_context__mutmut_76, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_77': xǁWorkspaceSyncǁ_build_template_context__mutmut_77, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_78': xǁWorkspaceSyncǁ_build_template_context__mutmut_78, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_79': xǁWorkspaceSyncǁ_build_template_context__mutmut_79, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_80': xǁWorkspaceSyncǁ_build_template_context__mutmut_80, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_81': xǁWorkspaceSyncǁ_build_template_context__mutmut_81, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_82': xǁWorkspaceSyncǁ_build_template_context__mutmut_82, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_83': xǁWorkspaceSyncǁ_build_template_context__mutmut_83, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_84': xǁWorkspaceSyncǁ_build_template_context__mutmut_84, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_85': xǁWorkspaceSyncǁ_build_template_context__mutmut_85, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_86': xǁWorkspaceSyncǁ_build_template_context__mutmut_86, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_87': xǁWorkspaceSyncǁ_build_template_context__mutmut_87, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_88': xǁWorkspaceSyncǁ_build_template_context__mutmut_88, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_89': xǁWorkspaceSyncǁ_build_template_context__mutmut_89, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_90': xǁWorkspaceSyncǁ_build_template_context__mutmut_90, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_91': xǁWorkspaceSyncǁ_build_template_context__mutmut_91, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_92': xǁWorkspaceSyncǁ_build_template_context__mutmut_92, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_93': xǁWorkspaceSyncǁ_build_template_context__mutmut_93, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_94': xǁWorkspaceSyncǁ_build_template_context__mutmut_94, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_95': xǁWorkspaceSyncǁ_build_template_context__mutmut_95, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_96': xǁWorkspaceSyncǁ_build_template_context__mutmut_96, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_97': xǁWorkspaceSyncǁ_build_template_context__mutmut_97, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_98': xǁWorkspaceSyncǁ_build_template_context__mutmut_98, 
        'xǁWorkspaceSyncǁ_build_template_context__mutmut_99': xǁWorkspaceSyncǁ_build_template_context__mutmut_99
    }
    
    def _build_template_context(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁ_build_template_context__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁ_build_template_context__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _build_template_context.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁ_build_template_context__mutmut_orig)
    xǁWorkspaceSyncǁ_build_template_context__mutmut_orig.__name__ = 'xǁWorkspaceSyncǁ_build_template_context'

    def _generate_configs(self, repo: RepoConfig, context: dict[str, Any]) -> dict[str, str]:
        """Generate configuration files for repository."""
        # Configuration generation has been removed with workenv module
        return {}

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_orig(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_1(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = None

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_2(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "XXpathXX": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_3(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "PATH": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_4(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(None),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_5(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "XXexistsXX": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_6(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "EXISTS": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_7(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "XXchangedXX": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_8(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "CHANGED": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_9(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": True,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_10(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "XXdiffXX": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_11(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "DIFF": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_12(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = None
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_13(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = "XXXX"
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_14(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = None
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_15(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning(None, path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_16(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=None, error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_17(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=None)
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_18(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning(path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_19(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_20(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), )
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_21(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("XX⚠️ Failed to read fileXX", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_22(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_23(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ FAILED TO READ FILE", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_24(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(None), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_25(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(None))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_26(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = None
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_27(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["XXerrorXX"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_28(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["ERROR"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_29(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(None)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_30(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() != new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_31(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = None

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_32(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            None
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_33(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                None,
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_34(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                None,
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_35(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=None,
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_36(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=None,
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_37(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm=None,
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_38(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_39(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_40(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_41(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_42(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_43(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=None),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_44(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=False),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_45(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=None),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_46(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=False),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_47(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(None),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_48(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(None),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_49(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="XXXX",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_50(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = None
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_51(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["XXchangedXX"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_52(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["CHANGED"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_53(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = False
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_54(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = None

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_55(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["XXdiffXX"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_56(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["DIFF"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_57(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(None)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_58(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "XXXX".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_59(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info(None, path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_60(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=None)
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_61(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info(path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_62(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", )
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_63(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("XX🔍 Would update fileXX", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_64(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_65(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 WOULD UPDATE FILE", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_66(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(None))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_67(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=None, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_68(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=None)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_69(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_70(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, )

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_71(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=False, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_72(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=False)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_73(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(None)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_74(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error(None, path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_75(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=None, error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_76(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=None)
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_77(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error(path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_78(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_79(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), )
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_80(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("XX❌ Failed to write fileXX", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_81(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_82(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ FAILED TO WRITE FILE", path=str(file_path), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_83(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(None), error=str(e))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_84(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(None))
                change_info["error"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_85(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = None

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_86(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["XXerrorXX"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_87(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["ERROR"] = str(e)

        return change_info

    async def xǁWorkspaceSyncǁ_apply_config_change__mutmut_88(self, file_path: Path, new_content: str, dry_run: bool) -> dict[str, Any]:
        """Apply configuration change to file."""
        change_info = {
            "path": str(file_path),
            "exists": file_path.exists(),
            "changed": False,
            "diff": None,
        }

        # Read current content
        current_content = ""
        if file_path.exists():
            try:
                current_content = file_path.read_text()
            except Exception as e:
                logger.warning("⚠️ Failed to read file", path=str(file_path), error=str(e))
                change_info["error"] = str(e)
                return change_info

        # Check if content changed
        if current_content.strip() == new_content.strip():
            return change_info

        # Generate diff
        diff_lines = list(
            difflib.unified_diff(
                current_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=str(file_path),
                tofile=str(file_path),
                lineterm="",
            )
        )

        change_info["changed"] = True
        change_info["diff"] = "".join(diff_lines)

        if dry_run:
            logger.info("🔍 Would update file", path=str(file_path))
        else:
            try:
                # Ensure parent directory exists
                file_path.parent.mkdir(parents=True, exist_ok=True)

                # Write new content
                file_path.write_text(new_content)

            except Exception as e:
                logger.error("❌ Failed to write file", path=str(file_path), error=str(e))
                change_info["error"] = str(None)

        return change_info
    
    xǁWorkspaceSyncǁ_apply_config_change__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁ_apply_config_change__mutmut_1': xǁWorkspaceSyncǁ_apply_config_change__mutmut_1, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_2': xǁWorkspaceSyncǁ_apply_config_change__mutmut_2, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_3': xǁWorkspaceSyncǁ_apply_config_change__mutmut_3, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_4': xǁWorkspaceSyncǁ_apply_config_change__mutmut_4, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_5': xǁWorkspaceSyncǁ_apply_config_change__mutmut_5, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_6': xǁWorkspaceSyncǁ_apply_config_change__mutmut_6, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_7': xǁWorkspaceSyncǁ_apply_config_change__mutmut_7, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_8': xǁWorkspaceSyncǁ_apply_config_change__mutmut_8, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_9': xǁWorkspaceSyncǁ_apply_config_change__mutmut_9, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_10': xǁWorkspaceSyncǁ_apply_config_change__mutmut_10, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_11': xǁWorkspaceSyncǁ_apply_config_change__mutmut_11, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_12': xǁWorkspaceSyncǁ_apply_config_change__mutmut_12, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_13': xǁWorkspaceSyncǁ_apply_config_change__mutmut_13, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_14': xǁWorkspaceSyncǁ_apply_config_change__mutmut_14, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_15': xǁWorkspaceSyncǁ_apply_config_change__mutmut_15, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_16': xǁWorkspaceSyncǁ_apply_config_change__mutmut_16, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_17': xǁWorkspaceSyncǁ_apply_config_change__mutmut_17, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_18': xǁWorkspaceSyncǁ_apply_config_change__mutmut_18, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_19': xǁWorkspaceSyncǁ_apply_config_change__mutmut_19, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_20': xǁWorkspaceSyncǁ_apply_config_change__mutmut_20, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_21': xǁWorkspaceSyncǁ_apply_config_change__mutmut_21, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_22': xǁWorkspaceSyncǁ_apply_config_change__mutmut_22, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_23': xǁWorkspaceSyncǁ_apply_config_change__mutmut_23, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_24': xǁWorkspaceSyncǁ_apply_config_change__mutmut_24, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_25': xǁWorkspaceSyncǁ_apply_config_change__mutmut_25, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_26': xǁWorkspaceSyncǁ_apply_config_change__mutmut_26, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_27': xǁWorkspaceSyncǁ_apply_config_change__mutmut_27, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_28': xǁWorkspaceSyncǁ_apply_config_change__mutmut_28, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_29': xǁWorkspaceSyncǁ_apply_config_change__mutmut_29, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_30': xǁWorkspaceSyncǁ_apply_config_change__mutmut_30, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_31': xǁWorkspaceSyncǁ_apply_config_change__mutmut_31, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_32': xǁWorkspaceSyncǁ_apply_config_change__mutmut_32, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_33': xǁWorkspaceSyncǁ_apply_config_change__mutmut_33, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_34': xǁWorkspaceSyncǁ_apply_config_change__mutmut_34, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_35': xǁWorkspaceSyncǁ_apply_config_change__mutmut_35, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_36': xǁWorkspaceSyncǁ_apply_config_change__mutmut_36, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_37': xǁWorkspaceSyncǁ_apply_config_change__mutmut_37, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_38': xǁWorkspaceSyncǁ_apply_config_change__mutmut_38, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_39': xǁWorkspaceSyncǁ_apply_config_change__mutmut_39, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_40': xǁWorkspaceSyncǁ_apply_config_change__mutmut_40, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_41': xǁWorkspaceSyncǁ_apply_config_change__mutmut_41, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_42': xǁWorkspaceSyncǁ_apply_config_change__mutmut_42, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_43': xǁWorkspaceSyncǁ_apply_config_change__mutmut_43, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_44': xǁWorkspaceSyncǁ_apply_config_change__mutmut_44, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_45': xǁWorkspaceSyncǁ_apply_config_change__mutmut_45, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_46': xǁWorkspaceSyncǁ_apply_config_change__mutmut_46, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_47': xǁWorkspaceSyncǁ_apply_config_change__mutmut_47, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_48': xǁWorkspaceSyncǁ_apply_config_change__mutmut_48, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_49': xǁWorkspaceSyncǁ_apply_config_change__mutmut_49, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_50': xǁWorkspaceSyncǁ_apply_config_change__mutmut_50, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_51': xǁWorkspaceSyncǁ_apply_config_change__mutmut_51, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_52': xǁWorkspaceSyncǁ_apply_config_change__mutmut_52, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_53': xǁWorkspaceSyncǁ_apply_config_change__mutmut_53, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_54': xǁWorkspaceSyncǁ_apply_config_change__mutmut_54, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_55': xǁWorkspaceSyncǁ_apply_config_change__mutmut_55, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_56': xǁWorkspaceSyncǁ_apply_config_change__mutmut_56, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_57': xǁWorkspaceSyncǁ_apply_config_change__mutmut_57, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_58': xǁWorkspaceSyncǁ_apply_config_change__mutmut_58, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_59': xǁWorkspaceSyncǁ_apply_config_change__mutmut_59, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_60': xǁWorkspaceSyncǁ_apply_config_change__mutmut_60, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_61': xǁWorkspaceSyncǁ_apply_config_change__mutmut_61, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_62': xǁWorkspaceSyncǁ_apply_config_change__mutmut_62, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_63': xǁWorkspaceSyncǁ_apply_config_change__mutmut_63, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_64': xǁWorkspaceSyncǁ_apply_config_change__mutmut_64, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_65': xǁWorkspaceSyncǁ_apply_config_change__mutmut_65, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_66': xǁWorkspaceSyncǁ_apply_config_change__mutmut_66, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_67': xǁWorkspaceSyncǁ_apply_config_change__mutmut_67, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_68': xǁWorkspaceSyncǁ_apply_config_change__mutmut_68, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_69': xǁWorkspaceSyncǁ_apply_config_change__mutmut_69, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_70': xǁWorkspaceSyncǁ_apply_config_change__mutmut_70, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_71': xǁWorkspaceSyncǁ_apply_config_change__mutmut_71, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_72': xǁWorkspaceSyncǁ_apply_config_change__mutmut_72, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_73': xǁWorkspaceSyncǁ_apply_config_change__mutmut_73, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_74': xǁWorkspaceSyncǁ_apply_config_change__mutmut_74, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_75': xǁWorkspaceSyncǁ_apply_config_change__mutmut_75, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_76': xǁWorkspaceSyncǁ_apply_config_change__mutmut_76, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_77': xǁWorkspaceSyncǁ_apply_config_change__mutmut_77, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_78': xǁWorkspaceSyncǁ_apply_config_change__mutmut_78, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_79': xǁWorkspaceSyncǁ_apply_config_change__mutmut_79, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_80': xǁWorkspaceSyncǁ_apply_config_change__mutmut_80, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_81': xǁWorkspaceSyncǁ_apply_config_change__mutmut_81, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_82': xǁWorkspaceSyncǁ_apply_config_change__mutmut_82, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_83': xǁWorkspaceSyncǁ_apply_config_change__mutmut_83, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_84': xǁWorkspaceSyncǁ_apply_config_change__mutmut_84, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_85': xǁWorkspaceSyncǁ_apply_config_change__mutmut_85, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_86': xǁWorkspaceSyncǁ_apply_config_change__mutmut_86, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_87': xǁWorkspaceSyncǁ_apply_config_change__mutmut_87, 
        'xǁWorkspaceSyncǁ_apply_config_change__mutmut_88': xǁWorkspaceSyncǁ_apply_config_change__mutmut_88
    }
    
    def _apply_config_change(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁ_apply_config_change__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁ_apply_config_change__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _apply_config_change.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁ_apply_config_change__mutmut_orig)
    xǁWorkspaceSyncǁ_apply_config_change__mutmut_orig.__name__ = 'xǁWorkspaceSyncǁ_apply_config_change'

    def xǁWorkspaceSyncǁcheck_drift__mutmut_orig(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_1(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info(None)

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_2(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("XX🔍 Checking configuration driftXX")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_3(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_4(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 CHECKING CONFIGURATION DRIFT")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_5(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = None
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_6(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = None

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_7(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "XXrepos_checkedXX": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_8(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "REPOS_CHECKED": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_9(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "XXdrift_detectedXX": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_10(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "DRIFT_DETECTED": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_11(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": True,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_12(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "XXrepo_driftsXX": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_13(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "REPO_DRIFTS": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_14(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = None
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_15(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(None)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_16(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["XXhas_driftXX"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_17(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["HAS_DRIFT"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_18(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = None
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_19(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["XXdrift_detectedXX"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_20(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["DRIFT_DETECTED"] = True
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_21(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = False
                repo_drifts[repo.name] = repo_drift

        return drift_report

    def xǁWorkspaceSyncǁcheck_drift__mutmut_22(self) -> dict[str, Any]:
        """Check for configuration drift across repositories."""
        logger.info("🔍 Checking configuration drift")

        repo_drifts: dict[str, Any] = {}
        drift_report: dict[str, Any] = {
            "repos_checked": len(self.config.repos),
            "drift_detected": False,
            "repo_drifts": repo_drifts,
        }

        for repo in self.config.repos:
            repo_drift = self._check_repo_drift(repo)
            if repo_drift["has_drift"]:
                drift_report["drift_detected"] = True
                repo_drifts[repo.name] = None

        return drift_report
    
    xǁWorkspaceSyncǁcheck_drift__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁcheck_drift__mutmut_1': xǁWorkspaceSyncǁcheck_drift__mutmut_1, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_2': xǁWorkspaceSyncǁcheck_drift__mutmut_2, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_3': xǁWorkspaceSyncǁcheck_drift__mutmut_3, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_4': xǁWorkspaceSyncǁcheck_drift__mutmut_4, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_5': xǁWorkspaceSyncǁcheck_drift__mutmut_5, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_6': xǁWorkspaceSyncǁcheck_drift__mutmut_6, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_7': xǁWorkspaceSyncǁcheck_drift__mutmut_7, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_8': xǁWorkspaceSyncǁcheck_drift__mutmut_8, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_9': xǁWorkspaceSyncǁcheck_drift__mutmut_9, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_10': xǁWorkspaceSyncǁcheck_drift__mutmut_10, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_11': xǁWorkspaceSyncǁcheck_drift__mutmut_11, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_12': xǁWorkspaceSyncǁcheck_drift__mutmut_12, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_13': xǁWorkspaceSyncǁcheck_drift__mutmut_13, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_14': xǁWorkspaceSyncǁcheck_drift__mutmut_14, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_15': xǁWorkspaceSyncǁcheck_drift__mutmut_15, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_16': xǁWorkspaceSyncǁcheck_drift__mutmut_16, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_17': xǁWorkspaceSyncǁcheck_drift__mutmut_17, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_18': xǁWorkspaceSyncǁcheck_drift__mutmut_18, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_19': xǁWorkspaceSyncǁcheck_drift__mutmut_19, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_20': xǁWorkspaceSyncǁcheck_drift__mutmut_20, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_21': xǁWorkspaceSyncǁcheck_drift__mutmut_21, 
        'xǁWorkspaceSyncǁcheck_drift__mutmut_22': xǁWorkspaceSyncǁcheck_drift__mutmut_22
    }
    
    def check_drift(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁcheck_drift__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁcheck_drift__mutmut_mutants"), args, kwargs, self)
        return result 
    
    check_drift.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁcheck_drift__mutmut_orig)
    xǁWorkspaceSyncǁcheck_drift__mutmut_orig.__name__ = 'xǁWorkspaceSyncǁcheck_drift'

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_orig(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_1(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = None
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_2(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(None)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_3(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = None

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_4(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(None, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_5(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, None)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_6(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_7(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, )

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_8(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = None
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_9(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = None

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_10(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "XXrepoXX": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_11(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "REPO": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_12(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "XXhas_driftXX": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_13(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "HAS_DRIFT": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_14(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": True,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_15(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "XXfile_driftsXX": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_16(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "FILE_DRIFTS": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_17(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = None

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_18(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path * filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_19(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_20(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = None
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_21(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["XXhas_driftXX"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_22(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["HAS_DRIFT"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_23(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = False
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_24(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = None
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_25(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "XXstatusXX": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_26(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "STATUS": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_27(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "XXmissingXX",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_28(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "MISSING",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_29(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "XXexpectedXX": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_30(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "EXPECTED": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_31(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                break

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_32(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = None
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_33(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() == expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_34(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = None
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_35(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["XXhas_driftXX"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_36(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["HAS_DRIFT"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_37(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = False
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_38(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = None
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_39(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "XXstatusXX": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_40(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "STATUS": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_41(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "XXdifferentXX",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_42(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "DIFFERENT",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_43(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "XXcurrent_linesXX": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_44(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "CURRENT_LINES": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_45(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "XXexpected_linesXX": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_46(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "EXPECTED_LINES": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_47(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = None
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_48(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["XXhas_driftXX"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_49(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["HAS_DRIFT"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_50(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = False
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_51(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = None

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_52(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "XXstatusXX": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_53(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "STATUS": "error",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_54(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "XXerrorXX",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_55(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "ERROR",
                    "error": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_56(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "XXerrorXX": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_57(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "ERROR": str(e),
                }

        return drift_info

    def xǁWorkspaceSyncǁ_check_repo_drift__mutmut_58(self, repo: RepoConfig) -> dict[str, Any]:
        """Check drift for a single repository."""
        context = self._build_template_context(repo)
        expected_configs = self._generate_configs(repo, context)

        file_drifts: dict[str, dict[str, Any]] = {}
        drift_info: dict[str, Any] = {
            "repo": repo.name,
            "has_drift": False,
            "file_drifts": file_drifts,
        }

        for filename, expected_content in expected_configs.items():
            file_path = repo.path / filename

            if not file_path.exists():
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "missing",
                    "expected": len(expected_content.splitlines()),
                }
                continue

            try:
                current_content = file_path.read_text()
                if current_content.strip() != expected_content.strip():
                    drift_info["has_drift"] = True
                    file_drifts[filename] = {
                        "status": "different",
                        "current_lines": len(current_content.splitlines()),
                        "expected_lines": len(expected_content.splitlines()),
                    }
            except Exception as e:
                drift_info["has_drift"] = True
                file_drifts[filename] = {
                    "status": "error",
                    "error": str(None),
                }

        return drift_info
    
    xǁWorkspaceSyncǁ_check_repo_drift__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_1': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_1, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_2': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_2, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_3': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_3, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_4': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_4, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_5': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_5, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_6': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_6, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_7': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_7, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_8': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_8, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_9': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_9, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_10': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_10, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_11': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_11, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_12': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_12, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_13': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_13, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_14': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_14, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_15': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_15, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_16': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_16, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_17': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_17, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_18': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_18, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_19': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_19, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_20': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_20, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_21': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_21, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_22': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_22, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_23': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_23, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_24': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_24, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_25': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_25, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_26': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_26, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_27': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_27, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_28': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_28, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_29': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_29, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_30': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_30, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_31': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_31, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_32': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_32, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_33': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_33, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_34': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_34, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_35': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_35, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_36': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_36, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_37': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_37, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_38': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_38, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_39': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_39, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_40': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_40, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_41': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_41, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_42': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_42, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_43': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_43, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_44': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_44, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_45': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_45, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_46': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_46, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_47': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_47, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_48': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_48, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_49': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_49, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_50': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_50, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_51': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_51, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_52': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_52, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_53': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_53, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_54': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_54, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_55': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_55, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_56': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_56, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_57': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_57, 
        'xǁWorkspaceSyncǁ_check_repo_drift__mutmut_58': xǁWorkspaceSyncǁ_check_repo_drift__mutmut_58
    }
    
    def _check_repo_drift(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁ_check_repo_drift__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁ_check_repo_drift__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_repo_drift.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁ_check_repo_drift__mutmut_orig)
    xǁWorkspaceSyncǁ_check_repo_drift__mutmut_orig.__name__ = 'xǁWorkspaceSyncǁ_check_repo_drift'

    def xǁWorkspaceSyncǁvalidate_templates__mutmut_orig(self) -> bool:
        """Validate that all templates are available and functional.

        Note: Template generation has been removed with workenv module.
        This method now returns True as a no-op for backward compatibility.
        """
        # Template generation was removed with workenv module refactoring
        # This method is kept for API compatibility but always returns True
        return True

    def xǁWorkspaceSyncǁvalidate_templates__mutmut_1(self) -> bool:
        """Validate that all templates are available and functional.

        Note: Template generation has been removed with workenv module.
        This method now returns True as a no-op for backward compatibility.
        """
        # Template generation was removed with workenv module refactoring
        # This method is kept for API compatibility but always returns True
        return False
    
    xǁWorkspaceSyncǁvalidate_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkspaceSyncǁvalidate_templates__mutmut_1': xǁWorkspaceSyncǁvalidate_templates__mutmut_1
    }
    
    def validate_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkspaceSyncǁvalidate_templates__mutmut_orig"), object.__getattribute__(self, "xǁWorkspaceSyncǁvalidate_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    validate_templates.__signature__ = _mutmut_signature(xǁWorkspaceSyncǁvalidate_templates__mutmut_orig)
    xǁWorkspaceSyncǁvalidate_templates__mutmut_orig.__name__ = 'xǁWorkspaceSyncǁvalidate_templates'


# 🧰🌍🔚
