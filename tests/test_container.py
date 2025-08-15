import unittest
from unittest.mock import patch, MagicMock
from wrkenv.container.commands import build_container, start_container
from wrkenv.env.config import WorkenvConfig

class TestContainer(unittest.TestCase):
    @patch('wrkenv.container.commands.ContainerManager')
    def test_build_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.build_image.return_value = True
        config = WorkenvConfig()

        # Act
        result = build_container(config, rebuild=True)

        # Assert
        self.assertTrue(result)
        mock_manager.build_image.assert_called_once_with(rebuild=True)

    @patch('wrkenv.container.commands.ContainerManager')
    def test_start_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.start.return_value = True
        config = WorkenvConfig()

        # Act
        result = start_container(config, rebuild=True)

        # Assert
        self.assertTrue(result)
        mock_manager.start.assert_called_once_with(force_rebuild=True)

if __name__ == '__main__':
    unittest.main()