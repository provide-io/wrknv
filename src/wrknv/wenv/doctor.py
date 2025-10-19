# wrknv/wenv/doctor.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Doctor command for diagnosing wrknv environment issues.

This module provides diagnostic tools to help users identify and fix
common problems with their wrknv setup.
"""

from __future__ import annotations
import os
from pathlib import Path
import platform
import shutil
import sys
from provide.foundation.process import run
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
