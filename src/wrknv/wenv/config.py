"""
wenv Configuration (Compatibility Module)
==========================================
Imports from the new configuration module structure.
"""

from __future__ import annotations

# Import everything from the new configuration module
from wrknv.wenv.configuration import (
    ConfigSource,
    EnvironmentConfigSource,
    FileConfigSource,
    ValidatedTomlSource,
    WorkenvConfig,
    WorkenvConfigError,
    WorkenvProfileManager,
)

# Maintain backward compatibility
__all__ = [
    "ConfigSource",
    "EnvironmentConfigSource",
    "FileConfigSource",
    "ValidatedTomlSource",
    "WorkenvConfig",
    "WorkenvConfigError",
    "WorkenvProfileManager",
]
