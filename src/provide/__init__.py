"""
Provide namespace package
========================
"""

# Import from foundation and expose at package level
from provide.foundation import logger, config

__all__ = ['logger', 'config']