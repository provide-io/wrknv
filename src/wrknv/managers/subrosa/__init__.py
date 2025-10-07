#
# wrknv/managers/subrosa/__init__.py
#
"""
Sub Rosa Manager Module
=======================
Secret management tools - 'sub rosa' (under the rose) - in confidence.

Provides base class and variants for managing secret management tools:
- OpenBao (open source Vault fork)
- IBM Vault (HashiCorp Vault)
"""

from __future__ import annotations


from .base import SubRosaManager
from .bao import BaoVariant

__all__ = [
    "SubRosaManager",
    "BaoVariant",
]
