
import unittest
from unittest.mock import patch, MagicMock
from wrkenv.env.managers.base import BaseToolManager
from wrkenv.env.config import WorkenvConfig

class TestManagers(unittest.TestCase):
    def test_base_tool_manager_init(self):
        # Arrange
        config = WorkenvConfig()

        # Act
        manager = BaseToolManager(config)

        # Assert
        self.assertEqual(manager.config, config)

if __name__ == '__main__':
    unittest.main()
