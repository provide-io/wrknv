import unittest
from unittest.mock import patch, MagicMock
from wrknv.container.commands import build_container, start_container, enter_container, stop_container, restart_container, container_status, container_logs, clean_container, rebuild_container
from wrknv.container.manager import ContainerManager
from wrknv.wenv.schema import WorkenvConfig

class TestContainerManager(unittest.TestCase):
    @patch('wrknv.container.manager.ContainerManager.build_image')
    def test_build_container(self, mock_build_image):
        # Arrange
        mock_build_image.return_value = True
        config = WorkenvConfig(project_name="test-project")

        # Act
        result = build_container(config, rebuild=True)

        # Assert
        self.assertTrue(result)
        mock_build_image.assert_called_once_with(rebuild=True)

    @patch('wrknv.container.manager.ContainerManager.start')
    def test_start_container(self, mock_start):
        # Arrange
        mock_start.return_value = True
        config = WorkenvConfig(project_name="test-project")

        # Act
        result = start_container(config, rebuild=True)

        # Assert
        self.assertTrue(result)
        mock_start.assert_called_once_with(force_rebuild=True)

    @patch('wrknv.container.manager.ContainerManager.enter')
    def test_enter_container(self, mock_enter):
        # Arrange
        config = WorkenvConfig(project_name="test-project")

        # Act
        enter_container(config, command=['ls', '-l'])

        # Assert
        mock_enter.assert_called_once_with(
            command=['ls', '-l'],
            shell=None,
            working_dir=None,
            environment=None,
            user=None,
            auto_start=False
        )

    @patch('wrknv.container.manager.ContainerManager.stop')
    def test_stop_container(self, mock_stop):
        # Arrange
        mock_stop.return_value = True
        config = WorkenvConfig(project_name="test-project")

        # Act
        result = stop_container(config)

        # Assert
        self.assertTrue(result)
        mock_stop.assert_called_once_with()

    @patch('wrknv.container.manager.ContainerManager.restart')
    def test_restart_container(self, mock_restart):
        # Arrange
        mock_restart.return_value = True
        config = WorkenvConfig(project_name="test-project")

        # Act
        result = restart_container(config)

        # Assert
        self.assertTrue(result)
        mock_restart.assert_called_once_with()

    @patch('wrknv.container.manager.ContainerManager.status')
    def test_container_status(self, mock_status):
        # Arrange
        mock_status.return_value = {
            'docker_available': True,
            'image_exists': True,
            'container_exists': True,
            'container_running': True,
            'container_info': {
                'id': '12345',
                'state': 'running'
            }
        }
        config = WorkenvConfig(project_name="test-project")

        # Act
        container_status(config)

        # Assert
        mock_status.assert_called_once_with()

    @patch('wrknv.container.manager.ContainerManager.logs')
    def test_container_logs(self, mock_logs):
        # Arrange
        config = WorkenvConfig(project_name="test-project")

        # Act
        container_logs(config, follow=True, tail=100)

        # Assert
        mock_logs.assert_called_once_with(
            follow=True,
            tail=100,
            since=None,
            timestamps=False,
            details=False
        )

    @patch('wrknv.container.manager.ContainerManager.clean')
    def test_clean_container(self, mock_clean):
        # Arrange
        mock_clean.return_value = True
        config = WorkenvConfig(project_name="test-project")

        # Act
        result = clean_container(config)

        # Assert
        self.assertTrue(result)
        mock_clean.assert_called_once_with()

    @patch('wrknv.container.manager.ContainerManager.start')
    @patch('wrknv.container.manager.ContainerManager.build_image')
    @patch('wrknv.container.manager.ContainerManager.clean')
    def test_rebuild_container(self, mock_clean, mock_build_image, mock_start):
        # Arrange
        mock_clean.return_value = True
        mock_build_image.return_value = True
        mock_start.return_value = True
        config = WorkenvConfig(project_name="test-project")

        # Act
        result = rebuild_container(config)

        # Assert
        self.assertTrue(result)
        mock_clean.assert_called_once_with()
        mock_build_image.assert_called_once_with(rebuild=True)
        mock_start.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()