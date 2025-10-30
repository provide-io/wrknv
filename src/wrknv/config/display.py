# 
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Display convenience helpers for `WorkenvConfig`."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wrknv.config.core import WorkenvConfig


class WorkenvConfigDisplay:
    """Handles displaying configuration information."""

    def __init__(self, config: WorkenvConfig) -> None:
        """Initialize display handler with config instance."""
        self.config = config

    def show_config(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")
        echo_info(f"  Project: {self.config.project_name} v{self.config.version}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")

# 🧰🌍🔚
