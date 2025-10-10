"""
wenv Configuration (Compatibility Module)
==========================================
DEPRECATED: This module provides backward compatibility.
Use wrknv.config.WorkenvConfig directly instead.
"""

from __future__ import annotations

import warnings

# Import from the unified configuration system
from wrknv.config import (
    WorkenvConfig,
    WorkenvConfigError,
)

# Keep old source classes for compatibility but mark as deprecated
from wrknv.wenv.configuration import (
    ConfigSource,
    EnvironmentConfigSource,
    FileConfigSource,
    ValidatedTomlSource,
    WorkenvProfileManager,
)

# Issue deprecation warning
warnings.warn(
    "wrknv.wenv.config is deprecated. Use wrknv.config.WorkenvConfig instead.",
    DeprecationWarning,
    stacklevel=2,
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
