"""
Multi-Repo Workspace Management Package
=======================================
Manage configurations across multiple independent Git repositories.
"""

from __future__ import annotations

from .discovery import WorkspaceDiscovery
from .manager import WorkspaceManager
from .schema import RepoConfig, WorkspaceConfig
from .sync import WorkspaceSync

__all__ = [
    "RepoConfig",
    "WorkspaceConfig",
    "WorkspaceDiscovery",
    "WorkspaceManager",
    "WorkspaceSync",
]
