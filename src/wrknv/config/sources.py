# wrknv/config/sources.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Configuration Sources for wrknv
================================
Different sources for loading configuration.
from __future__ import annotations
import os
from pathlib import Path
from typing import Any
from provide.foundation.file import read_toml
