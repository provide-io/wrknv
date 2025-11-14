"""
Provide Foundation
==================
Foundation utilities for the Provide ecosystem.
"""

import logging
from typing import Any, Dict, Optional


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


class Config:
    """Simple configuration container for provide.foundation compatibility."""
    
    def __init__(self, data: Optional[Dict[str, Any]] = None):
        self._data = data or {}
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self._data.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        self._data[key] = value
    
    def update(self, data: Dict[str, Any]) -> None:
        """Update configuration with dictionary."""
        self._data.update(data)
    
    def to_dict(self) -> Dict[str, Any]:
        """Get configuration as dictionary."""
        return self._data.copy()


# Create global instances
logger = Logger()
config = Config()