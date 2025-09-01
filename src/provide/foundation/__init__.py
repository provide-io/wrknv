"""
Provide Foundation
==================
Foundation utilities for the Provide ecosystem.
"""

import logging
from typing import Any


class Logger:
    """Simple logger wrapper for provide.foundation compatibility."""
    
    def __init__(self, name: str = "provide.foundation"):
        self._logger = logging.getLogger(name)
        # Set default level
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            )
            self._logger.addHandler(handler)
            self._logger.setLevel(logging.INFO)
    
    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug message."""
        self._logger.debug(message, extra=kwargs)
    
    def info(self, message: str, **kwargs: Any) -> None:
        """Log info message."""
        self._logger.info(message, extra=kwargs)
    
    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning message."""
        self._logger.warning(message, extra=kwargs)
    
    def error(self, message: str, **kwargs: Any) -> None:
        """Log error message."""
        self._logger.error(message, extra=kwargs)
    
    def critical(self, message: str, **kwargs: Any) -> None:
        """Log critical message."""
        self._logger.critical(message, extra=kwargs)


# Create a global logger instance
logger = Logger()