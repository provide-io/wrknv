"""
wrknv Emoji Hierarchy Definitions
==================================
Defines the emoji hierarchy for wrknv modules.
"""

from __future__ import annotations

# wrknv emoji hierarchy - organized by functionality
WRKNV_EMOJI_HIERARCHY = {
    # Core wrknv
    "wrknv": "🧰",
    # CLI interface
    "wrknv.cli": "⌨️",
    "wrknv.cli.commands": "🎯",
    "wrknv.cli.commands.tools": "🔧",
    "wrknv.cli.commands.terraform": "🟦",
    "wrknv.cli.commands.config": "⚙️",
    "wrknv.cli.commands.container": "🐳",
    "wrknv.cli.commands.gitignore": "📄",
    "wrknv.cli.commands.profile": "👤",
    "wrknv.cli.commands.setup": "🌱",
    # Work environment management
    "wrknv.wenv": "🌍",
    "wrknv.managers": "📦",
    "wrknv.managers.terraform": "🟦",
    "wrknv.managers.tofu": "🌿",
    "wrknv.managers.ibm_tf": "🔵",
    "wrknv.managers.go": "🐹",
    "wrknv.managers.uv": "⚡",
    "wrknv.wenv.version_resolver": "🔍",
    "wrknv.wenv.env_generator": "📝",
    "wrknv.wenv.doctor": "🩺",
    "wrknv.wenv.operations": "⚙️",
    # Configuration system
    "wrknv.config": "⚙️",
    "wrknv.config.core": "🔩",
    "wrknv.config.sources": "📋",
    # Package management
    "wrknv.package": "📤",
    "wrknv.package.manager": "📦",
    # Container operations
    "wrknv.container": "🐳",
    # Gitignore management
    "wrknv.gitignore": "📄",
    "wrknv.gitignore.manager": "📝",
}
