#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python3
"""Parse bandit security report and exit 1 if HIGH severity issues are found."""
import json
from pathlib import Path
import sys


def main() -> None:
    with Path("bandit-report.json").open() as f:
        data = json.load(f)

    results = data.get("results", [])
    if not results:
        print("No security issues found!")
        return

    print("Security issues found:")
    for issue in results:
        print(f"  - {issue['issue_text']} ({issue['issue_severity']}) at {issue['filename']}:{issue['line_number']}")

    if any(issue["issue_severity"] == "HIGH" for issue in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
