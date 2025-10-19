# wrknv/config/persistence.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Configuration Persistence for wrknv
====================================
Save, load, and file operations for configuration data.
"""

from __future__ import annotations
import os
from pathlib import Path
from typing import Any
from provide.foundation.file import read_toml, write_toml
from provide.foundation.logger import get_logger
from provide.foundation.process import run
