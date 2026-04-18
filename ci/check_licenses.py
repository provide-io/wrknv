#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Check pip-licenses JSON output (from stdin) for problematic copyleft licenses."""

import json
import sys

PROBLEMATIC = ["GPL", "AGPL", "LGPL", "SSPL"]


def main() -> None:
    data = json.loads(sys.stdin.read())
    issues = []

    for pkg in data:
        license_name = pkg.get("License", "").upper()
        if any(p in license_name for p in PROBLEMATIC):
            issues.append(f"{pkg['Name']}: {pkg['License']}")

    if issues:
        print("Potentially problematic licenses found:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nPlease review these licenses for compatibility.")
    else:
        print("No problematic licenses detected.")


if __name__ == "__main__":
    main()
