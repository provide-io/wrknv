
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

    def test_get_install_dir(self):
        # Arrange
        config = WorkenvConfig()
        manager = ConcreteToolManager(config)

        # Act
        install_dir = manager.get_install_dir('1.0.0')

        # Assert
        self.assertEqual(install_dir.name, '1.0.0')
        self.assertEqual(install_dir.parent.name, 'test')
        self.assertEqual(install_dir.parent.parent.name, 'tools')
        self.assertEqual(install_dir.parent.parent.parent.name, '.wrkenv')
        self.assertEqual(install_dir.parent.parent.parent.parent, manager.home_dir)

if __name__ == '__main__':
    unittest.main()
