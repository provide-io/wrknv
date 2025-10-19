# wrknv/workspace/sync.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Workspace Configuration Synchronization
=======================================
Synchronize configurations across repositories in workspace.
"""

from __future__ import annotations
import difflib
from pathlib import Path
from typing import Any
from provide.foundation import logger
from wrknv.workenv.config_templates import ConfigTemplateGenerator
from .schema import RepoConfig, WorkspaceConfig
