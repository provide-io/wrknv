# wrknv/gitignore/detector.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Project Detector for Gitignore Templates
=========================================
Auto-detects project types and suggests appropriate gitignore templates.
"""

from __future__ import annotations
import json
from pathlib import Path
from provide.foundation import logger
