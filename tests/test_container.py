import unittest
from unittest.mock import patch, MagicMock
from wrkenv.container.commands import build_container
from wrkenv.env.config import WorkenvConfig

class TestContainer(unittest.TestCase):
    @patch('wrkenv.container.commands.build_container')
    def test_build_container(self, mock_build_container):
        # Arrange
        mock_build_container.return_value = True
        config = WorkenvConfig()

        # Act
        result = build_container(config, rebuild=True)

        # Assert
        self.assertTrue(result)
        mock_build_container.assert_called_once_with(config, rebuild=True)

if __name__ == '__main__':
    unittest.main()