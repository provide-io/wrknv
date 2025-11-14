"""
Gitignore Management Module
===========================
Comprehensive gitignore file management for wrknv projects.
"""

from .builder import GitignoreBuilder
from .detector import ProjectDetector
from .manager import GitignoreManager
from .templates import TemplateHandler

__all__ = [
    "GitignoreManager",
    "TemplateHandler",
    "GitignoreBuilder",
    "ProjectDetector",
]