# wrknv/gitignore/templates.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Template Handler for Gitignore Files
=====================================
Manages gitignore templates from GitHub's collection.
"""

from __future__ import annotations
from pathlib import Path
import tempfile
from provide.foundation import logger
from provide.foundation.archive.operations import ArchiveOperations
from provide.foundation.file import safe_move, safe_rmtree
from provide.foundation.resilience import retry
from provide.foundation.transport import get
