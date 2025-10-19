# wrknv/gitignore/builder.py
#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gitignore File Builder
======================
Constructs gitignore files with proper formatting and sections.
from __future__ import annotations
from pathlib import Path
from provide.foundation import logger
from provide.foundation.time import provide_now
