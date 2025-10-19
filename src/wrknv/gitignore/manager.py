# wrknv/gitignore/manager.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gitignore Manager
=================
Central manager for gitignore operations.
"""

from __future__ import annotations
from pathlib import Path
from provide.foundation import logger
from .builder import GitignoreBuilder
from .detector import ProjectDetector
from .templates import TemplateHandler
