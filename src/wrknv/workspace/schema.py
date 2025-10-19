# wrknv/workspace/schema.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Workspace Configuration Schema
=============================
Configuration models for multi-repo workspace management.
"""

from __future__ import annotations
from pathlib import Path
from typing import Any
from attrs import define, field
from provide.foundation.config import BaseConfig
