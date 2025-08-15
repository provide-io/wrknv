import unittest
from unittest.mock import patch, MagicMock
from wrkenv.container.commands import build_container
from wrkenv.env.config import WorkenvConfig

class TestContainer(unittest.TestCase):
    @patch('wrkenv.container.manager.ContainerManager')
    def test_build_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.build.return_value = True
        config = WorkenvConfig()

        # Act
        result = build_container(config, rebuild=True)

        # Assert
        self.assertTrue(result)
        mock_manager.build.assert_called_once_with(rebuild=True)

if __name__ == '__main__':
    unittest.main()