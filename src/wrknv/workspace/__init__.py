"""
Multi-Repo Workspace Management Package
=======================================
Manage configurations across multiple independent Git repositories.
"""

from .manager import WorkspaceManager
from .discovery import WorkspaceDiscovery
from .sync import WorkspaceSync
from .schema import WorkspaceConfig, RepoConfig

__all__ = [
    "WorkspaceManager",
    "WorkspaceDiscovery",
    "WorkspaceSync",
    "WorkspaceConfig",
    "RepoConfig",
]