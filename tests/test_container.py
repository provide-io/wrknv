import unittest
from unittest.mock import patch, MagicMock
from wrkenv.container.commands import build_container, start_container, enter_container, stop_container, restart_container, container_status, container_logs, clean_container, rebuild_container
from wrkenv.container.manager import ContainerManager
from wrkenv.env.config import WorkenvConfig

class TestContainerManager(unittest.TestCase):
    def test_init(self):
        # Arrange
        config = WorkenvConfig()

        # Act
        manager = ContainerManager(config)

        # Assert
        self.assertEqual(manager.config, config)
        self.assertEqual(manager.client.api.base_url, 'unix://var/run/docker.sock')


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

    @patch('wrkenv.container.commands.ContainerManager')
    def test_enter_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        config = WorkenvConfig()

        # Act
        enter_container(config, command=['ls', '-l'])

        # Assert
        mock_manager.enter.assert_called_once_with(command=['ls', '-l'])

    @patch('wrkenv.container.commands.ContainerManager')
    def test_stop_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.stop.return_value = True
        config = WorkenvConfig()

        # Act
        result = stop_container(config)

        # Assert
        self.assertTrue(result)
        mock_manager.stop.assert_called_once_with()

    @patch('wrkenv.container.commands.ContainerManager')
    def test_restart_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.restart.return_value = True
        config = WorkenvConfig()

        # Act
        result = restart_container(config)

        # Assert
        self.assertTrue(result)
        mock_manager.restart.assert_called_once_with()

    @patch('wrkenv.container.commands.ContainerManager')
    def test_container_status(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.status.return_value = {
            'docker_available': True,
            'image_exists': True,
            'container_exists': True,
            'container_running': True,
            'container_info': {
                'id': '12345',
                'state': 'running'
            }
        }
        config = WorkenvConfig()

        # Act
        container_status(config)

        # Assert
        mock_manager.status.assert_called_once_with()

    @patch('wrkenv.container.commands.ContainerManager')
    def test_container_logs(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        config = WorkenvConfig()

        # Act
        container_logs(config, follow=True, tail=100)

        # Assert
        mock_manager.logs.assert_called_once_with(follow=True, tail=100)

    @patch('wrkenv.container.commands.ContainerManager')
    def test_clean_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.clean.return_value = True
        config = WorkenvConfig()

        # Act
        result = clean_container(config)

        # Assert
        self.assertTrue(result)
        mock_manager.clean.assert_called_once_with()

    @patch('wrkenv.container.commands.ContainerManager')
    def test_rebuild_container(self, MockContainerManager):
        # Arrange
        mock_manager = MockContainerManager.return_value
        mock_manager.clean.return_value = True
        mock_manager.build_image.return_value = True
        mock_manager.start.return_value = True
        config = WorkenvConfig()

        # Act
        result = rebuild_container(config)

        # Assert
        self.assertTrue(result)
        mock_manager.clean.assert_called_once_with()
        mock_manager.build_image.assert_called_once_with(rebuild=True)
        mock_manager.start.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()