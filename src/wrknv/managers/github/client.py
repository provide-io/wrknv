# wrknv/managers/github/client.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GitHub Releases API Client
===========================
Client for interacting with GitHub Releases API using provide-foundation transport.
"""

from __future__ import annotations
from collections.abc import Callable
import pathlib
import re
from typing import Literal
from provide.foundation.hub import get_hub
from provide.foundation.logger import get_logger
from provide.foundation.transport import UniversalClient
from wrknv.managers.github.types import Asset, Release, Tag
from wrknv.wenv.resilience import get_circuit_breaker, get_retry_policy
