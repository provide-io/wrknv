# wrknv/workspace/manager.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Workspace Manager
================
Manage multi-repo workspaces with configuration synchronization.
"""

from __future__ import annotations
from pathlib import Path
from typing import Any
from provide.foundation import logger
from provide.foundation.file import read_toml, write_toml
from .discovery import WorkspaceDiscovery
from .schema import RepoConfig, TemplateSource, WorkspaceConfig
from .sync import WorkspaceSync
