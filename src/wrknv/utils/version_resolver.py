# wrknv/utils/version_resolver.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Version Resolution Utilities
============================
Handles resolution of version patterns like "1.11.x" to specific versions.
"""

from __future__ import annotations
from provide.foundation.logger import get_logger
import semver
