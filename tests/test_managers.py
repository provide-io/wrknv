import unittest
from unittest.mock import patch, MagicMock
from wrkenv.env.managers.base import BaseToolManager
from wrkenv.env.config import WorkenvConfig

class ConcreteToolManager(BaseToolManager):
    tool_name = 'test'
    executable_name = 'test'

    def get_download_url(self, version: str) -> str:
        return f'https://example.com/{self.tool_name}/{version}'

    def get_available_versions(self) -> list[str]:
        return ['1.0.0', '1.1.0']

    def _install_from_archive(self, archive_path: str, version: str) -> None:
        pass

    def get_checksum_url(self, version: str) -> str | None:
        return f'https://example.com/{self.tool_name}/{version}/checksums.txt'

class TestManagers(unittest.TestCase):
    def test_base_tool_manager_init(self):
        # Arrange
        config = WorkenvConfig()

        # Act
        manager = ConcreteToolManager(config)

        # Assert
        self.assertEqual(manager.config, config)

    def test_get_binary_path(self):
        # Arrange
        config = WorkenvConfig()
        manager = ConcreteToolManager(config)
        expected_path = manager.install_path / manager.tool_name / '1.0.0' / 'bin' / manager.executable_name

        # Act
        binary_path = manager.get_binary_path('1.0.0')

        # Assert
        self.assertEqual(binary_path, expected_path)

    @patch('pathlib.Path.iterdir')
    @patch('pathlib.Path.exists', return_value=True)
    def test_get_installed_versions(self, mock_exists, mock_iterdir):
        # Arrange
        config = WorkenvConfig()
        manager = ConcreteToolManager(config)
        
        # Mock iterdir to return dummy version directories
        mock_iterdir.return_value = [
            MagicMock(is_dir=MagicMock(return_value=True), name='1.0.0'),
            MagicMock(is_dir=MagicMock(return_value=True), name='1.1.0'),
            MagicMock(is_dir=MagicMock(return_value=True), name='invalid'),
            MagicMock(is_dir=MagicMock(return_value=True), name='2.0.0'),
        ]

        # Act
        versions = manager.get_installed_versions()

        # Assert
        self.assertEqual(versions, ['2.0.0', '1.1.0', '1.0.0'])

if __name__ == '__main__':
    unittest.main()