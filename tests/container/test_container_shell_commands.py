#
# tests/container/test_container_shell_commands.py
#
"""
Test Container Shell Commands
=============================
Tests for container shell, exec, and logs commands.
"""

import subprocess
from pathlib import Path
from unittest.mock import MagicMock, Mock, call, patch

import pytest
from click.testing import CliRunner

from wrknv.container.manager import ContainerManager
from wrknv.container.shell_commands import (
    exec_in_container,
    get_container_logs,
    shell_into_container,
)
from wrknv.wenv.schema import ContainerConfig, WorkenvConfig


class TestShellCommand:
    """Test shell command for interactive container access."""

    @pytest.fixture
    def mock_manager(self):
        """Create a mock container manager."""
        manager = Mock(spec=ContainerManager)
        manager.CONTAINER_NAME = "test-project-dev"
        manager.container_running = Mock(return_value=True)
        manager.container_exists = Mock(return_value=True)
        return manager

    @pytest.fixture
    def test_config(self):
        """Create test configuration."""
        return WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(enabled=True),
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_shell_basic(self, mock_manager_class, mock_run, test_config):
        """Test basic shell command execution."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        # Mock run_command to return successful result
        mock_run.return_value = Mock(returncode=0)
        
        result = shell_into_container(test_config)
        
        assert result is True
        mock_run.assert_called_once_with(
            ["docker", "exec", "-it", "test-project-dev", "/bin/bash"],
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_shell_with_custom_shell(self, mock_manager_class, mock_run, test_config):
        """Test shell command with custom shell."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        # Mock run_command to return successful result
        mock_run.return_value = Mock(returncode=0)
        
        result = shell_into_container(test_config, shell="/bin/zsh")
        
        assert result is True
        mock_run.assert_called_once_with(
            ["docker", "exec", "-it", "test-project-dev", "/bin/zsh"],
            check=False
        )

    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_shell_container_not_running(self, mock_manager_class, test_config):
        """Test shell when container is not running."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = False
        mock_manager.container_exists.return_value = True
        mock_manager.start.return_value = False
        mock_manager_class.return_value = mock_manager
        
        result = shell_into_container(test_config)
        
        assert result is False

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_shell_auto_start(self, mock_manager_class, mock_run, test_config):
        """Test shell with auto-start when container is stopped."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = False
        mock_manager.container_exists.return_value = True
        mock_manager.start.return_value = True
        mock_manager_class.return_value = mock_manager
        
        # After start, container is running
        mock_manager.container_running.side_effect = [False, True]
        
        # Mock run_command to return successful result
        mock_run.return_value = Mock(returncode=0)
        
        result = shell_into_container(test_config, auto_start=True)
        
        assert result is True
        mock_manager.start.assert_called_once()
        mock_run.assert_called_once()

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_shell_with_working_dir(self, mock_manager_class, mock_run, test_config):
        """Test shell with custom working directory."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        # Mock run_command to return successful result
        mock_run.return_value = Mock(returncode=0)
        
        result = shell_into_container(test_config, working_dir="/app")
        
        assert result is True
        mock_run.assert_called_once_with(
            ["docker", "exec", "-it", "-w", "/app", "test-project-dev", "/bin/bash"],
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_shell_with_environment(self, mock_manager_class, mock_run, test_config):
        """Test shell with environment variables."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        # Mock run_command to return successful result
        mock_run.return_value = Mock(returncode=0)
        
        env_vars = {"DEBUG": "true", "APP_ENV": "development"}
        result = shell_into_container(test_config, environment=env_vars)
        
        assert result is True
        expected_cmd = [
            "docker", "exec", "-it",
            "-e", "DEBUG=true",
            "-e", "APP_ENV=development",
            "test-project-dev", "/bin/bash"
        ]
        mock_run.assert_called_once_with(expected_cmd, check=False)


class TestExecCommand:
    """Test exec command for running commands in containers."""

    @pytest.fixture
    def test_config(self):
        """Create test configuration."""
        return WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(enabled=True),
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exec_basic(self, mock_manager_class, mock_run, test_config):
        """Test basic command execution."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(
            returncode=0,
            stdout="command output",
            stderr=""
        )
        
        result = exec_in_container(test_config, ["ls", "-la"])
        
        assert result.returncode == 0
        assert result.stdout == "command output"
        mock_run.assert_called_once_with(
            ["docker", "exec", "test-project-dev", "ls", "-la"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exec_with_working_dir(self, mock_manager_class, mock_run, test_config):
        """Test exec with working directory."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0)
        
        exec_in_container(test_config, ["pwd"], working_dir="/app")
        
        mock_run.assert_called_once_with(
            ["docker", "exec", "-w", "/app", "test-project-dev", "pwd"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exec_with_environment(self, mock_manager_class, mock_run, test_config):
        """Test exec with environment variables."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0)
        
        exec_in_container(
            test_config,
            ["echo", "$DEBUG"],
            environment={"DEBUG": "1"}
        )
        
        mock_run.assert_called_once_with(
            ["docker", "exec", "-e", "DEBUG=1", "test-project-dev", "echo", "$DEBUG"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exec_interactive(self, mock_manager_class, mock_run, test_config):
        """Test interactive command execution."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0)
        
        exec_in_container(test_config, ["python"], interactive=True)
        
        mock_run.assert_called_once_with(
            ["docker", "exec", "-it", "test-project-dev", "python"],
            capture_output=False,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exec_with_user(self, mock_manager_class, mock_run, test_config):
        """Test exec with specific user."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_running.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0)
        
        exec_in_container(test_config, ["whoami"], user="nobody")
        
        mock_run.assert_called_once_with(
            ["docker", "exec", "-u", "nobody", "test-project-dev", "whoami"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_exec_container_not_running(self, mock_manager_class, test_config):
        """Test exec when container is not running."""
        mock_manager = Mock()
        mock_manager.container_running.return_value = False
        mock_manager_class.return_value = mock_manager
        
        result = exec_in_container(test_config, ["ls"])
        
        assert result is None


class TestLogsCommand:
    """Test logs command for viewing container logs."""

    @pytest.fixture
    def test_config(self):
        """Create test configuration."""
        return WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(enabled=True),
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_logs_basic(self, mock_manager_class, mock_run, test_config):
        """Test basic logs retrieval."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_exists.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(
            returncode=0,
            stdout="container logs here",
            stderr=""
        )
        
        result = get_container_logs(test_config)
        
        assert result == "container logs here"
        mock_run.assert_called_once_with(
            ["docker", "logs", "test-project-dev"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_logs_with_follow(self, mock_manager_class, mock_run, test_config):
        """Test logs with follow option."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_exists.return_value = True
        mock_manager_class.return_value = mock_manager
        
        # For follow mode, we don't capture output
        get_container_logs(test_config, follow=True)
        
        mock_run.assert_called_once_with(
            ["docker", "logs", "-f", "test-project-dev"],
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_logs_with_tail(self, mock_manager_class, mock_run, test_config):
        """Test logs with tail option."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_exists.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0, stdout="last lines")
        
        result = get_container_logs(test_config, tail=50)
        
        assert result == "last lines"
        mock_run.assert_called_once_with(
            ["docker", "logs", "--tail", "50", "test-project-dev"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_logs_with_timestamps(self, mock_manager_class, mock_run, test_config):
        """Test logs with timestamps."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_exists.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0, stdout="timestamped logs")
        
        result = get_container_logs(test_config, timestamps=True)
        
        assert result == "timestamped logs"
        mock_run.assert_called_once_with(
            ["docker", "logs", "-t", "test-project-dev"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_logs_with_since(self, mock_manager_class, mock_run, test_config):
        """Test logs with since option."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_exists.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0, stdout="recent logs")
        
        result = get_container_logs(test_config, since="1h")
        
        assert result == "recent logs"
        mock_run.assert_called_once_with(
            ["docker", "logs", "--since", "1h", "test-project-dev"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("provide.foundation.process.run_command")
    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_logs_combined_options(self, mock_manager_class, mock_run, test_config):
        """Test logs with multiple options combined."""
        mock_manager = Mock()
        mock_manager.CONTAINER_NAME = "test-project-dev"
        mock_manager.container_exists.return_value = True
        mock_manager_class.return_value = mock_manager
        
        mock_run.return_value = Mock(returncode=0, stdout="filtered logs")
        
        result = get_container_logs(
            test_config,
            tail=100,
            timestamps=True,
            since="30m"
        )
        
        assert result == "filtered logs"
        mock_run.assert_called_once_with(
            ["docker", "logs", "-t", "--tail", "100", "--since", "30m", "test-project-dev"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch("wrknv.container.shell_commands.ContainerManager")
    def test_logs_container_not_exists(self, mock_manager_class, test_config):
        """Test logs when container doesn't exist."""
        mock_manager = Mock()
        mock_manager.container_exists.return_value = False
        mock_manager_class.return_value = mock_manager
        
        result = get_container_logs(test_config)
        
        assert result is None


class TestCLIIntegration:
    """Test CLI integration for shell commands."""

    @pytest.fixture
    def runner(self):
        """Create CLI runner."""
        return CliRunner()

    @pytest.fixture
    def mock_config(self):
        """Mock WorkenvConfig."""
        config = WorkenvConfig(
            project_name="test-project",
            container=ContainerConfig(enabled=True),
        )
        with patch("wrknv.wenv.cli.WorkenvConfig", return_value=config):
            yield config

    @pytest.fixture
    def mock_container_manager(self):
        """Mock ContainerManager."""
        with patch("wrknv.container.manager.ContainerManager") as mock_class:
            manager = Mock()
            manager.CONTAINER_NAME = "test-project-dev"
            manager.container_running.return_value = True
            manager.container_exists.return_value = True
            manager.enter.return_value = True
            manager.logs.return_value = None
            manager.status.return_value = {
                "docker_available": True,
                "image_exists": True,
                "container_exists": True,
                "container_running": True,
                "container_info": {"id": "abc123", "state": "running"}
            }
            mock_class.return_value = manager
            # Also patch in commands module where it's imported
            with patch("wrknv.container.commands.ContainerManager", return_value=manager):
                yield manager

    def test_cli_enter_command(self, runner, mock_config, mock_container_manager):
        """Test CLI enter command."""
        from wrknv.wenv.cli import workenv_cli as cli
        
        result = runner.invoke(cli, ["container", "enter"])
        
        assert result.exit_code == 0
        mock_container_manager.enter.assert_called_once()

    def test_cli_exec_command(self, runner, mock_config, mock_container_manager):
        """Test CLI exec command."""
        from wrknv.wenv.cli import workenv_cli as cli
        
        # Mock exec_in_container at the source
        with patch("wrknv.container.shell_commands.exec_in_container") as mock_exec:
            mock_exec.return_value = Mock(
                returncode=0,
                stdout="exec output",
                stderr=""
            )
            
            result = runner.invoke(cli, ["container", "exec", "--", "ls", "-la"])
            
            if result.exit_code != 0:
                print(f"Error: {result.output}")
            assert result.exit_code == 0
            assert "exec output" in result.output
            mock_exec.assert_called_once()

    def test_cli_logs_command(self, runner, mock_config, mock_container_manager):
        """Test CLI logs command."""
        from wrknv.wenv.cli import workenv_cli as cli
        
        result = runner.invoke(cli, ["container", "logs"])
        
        assert result.exit_code == 0
        mock_container_manager.logs.assert_called_once()

    def test_cli_logs_with_options(self, runner, mock_config, mock_container_manager):
        """Test CLI logs command with options."""
        from wrknv.wenv.cli import workenv_cli as cli
        
        result = runner.invoke(cli, ["container", "logs", "--tail", "50", "--timestamps"])
        
        assert result.exit_code == 0
        # Check that options were passed through
        mock_container_manager.logs.assert_called_once_with(
            follow=False,
            tail=50,
            since=None,
            timestamps=True,
            details=False
        )

    def test_cli_stats_command(self, runner, mock_config, mock_container_manager):
        """Test CLI stats command."""
        from wrknv.wenv.cli import workenv_cli as cli
        
        # Mock get_container_stats at the source
        with patch("wrknv.container.shell_commands.get_container_stats") as mock_stats:
            mock_stats.return_value = {
                "name": "test-project-dev",
                "cpu": "5.2%",
                "memory": {"usage": "256MB / 1GB", "percent": "25%"},
                "network": "1KB / 2KB",
                "disk": "10MB / 20MB",
                "pids": "10"
            }
            
            result = runner.invoke(cli, ["container", "stats"])
            
            assert result.exit_code == 0
            assert "Container Resource Usage" in result.output
            mock_stats.assert_called_once()