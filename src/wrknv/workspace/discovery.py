# wrknv/workspace/discovery.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Workspace Repository Discovery
=============================
Discover and analyze repositories in workspace.
from __future__ import annotations
from pathlib import Path
import tomllib
from typing import Any
from attrs import define
from provide.foundation import logger
