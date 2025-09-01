"""
Global test configuration and fixtures.
"""

import sys
from unittest.mock import MagicMock

# Mock provide.foundation module before any imports
sys.modules['provide'] = MagicMock()
sys.modules['provide.foundation'] = MagicMock()

# Create a mock logger
mock_logger = MagicMock()
mock_logger.info = MagicMock()
mock_logger.debug = MagicMock()
mock_logger.warning = MagicMock()
mock_logger.error = MagicMock()

sys.modules['provide.foundation'].logger = mock_logger