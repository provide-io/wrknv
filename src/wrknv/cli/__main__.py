#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Entry point for `python -m wrknv.cli` (used by PSP launcher on Windows)."""

from wrknv.cli import entry_point

if __name__ == "__main__":
    entry_point()
