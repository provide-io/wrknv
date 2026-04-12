#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for VolumeManager coverage gaps.

Targets missing lines:
  48→51, 61-64 (create_volume error/driver branch)
  76-92 (remove_volume with/without force, error path)
  107, 112→117, 114→113, 119-121 (list_volumes: filter label, empty stdout, json error)
  132-142 (inspect_volume)
  193-196 (backup_volume error)
  214-255 (restore_volume success)
  259-271 (restore_volume file-not-found and error paths)
  299, 313, 326 (backup/restore/clean stubs)
"""

from __future__ import annotations

import json
from pathlib import Path
import tempfile

from provide.foundation.process import CompletedProcess, ProcessError
from provide.testkit.mocking import MagicMock, patch
import pytest
from rich.console import Console

from wrknv.container.operations.volumes import VolumeManager
from wrknv.container.runtime.docker import DockerRuntime


def _make_manager(backup_dir: Path | None = None) -> tuple[VolumeManager, MagicMock]:
    """Build a VolumeManager with a mocked console."""
    runtime = DockerRuntime(runtime_name="docker", runtime_command="docker")
    console = MagicMock(spec=Console)
    if backup_dir is None:
        backup_dir = Path(tempfile.gettempdir()) / "wrknv_test_backups"
    mgr = VolumeManager(runtime=runtime, console=console, backup_dir=backup_dir)
    return mgr, console


@pytest.mark.container
class TestCreateVolumeErrorAndDriverBranch:
    """Test create_volume driver/options branch and error path (lines 48→51, 61-64)."""

    @patch("wrknv.container.operations.volumes.run")
    def test_create_volume_without_driver_skips_driver_flag(self, mock_run) -> None:
        """Test create_volume without driver does not add --driver (branch 48→51)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "create"], returncode=0, stdout="myvol", stderr=""
        )
        mgr, _ = _make_manager()

        result = mgr.create_volume(name="myvol", driver=None, options=None)

        assert result is True
        cmd = mock_run.call_args[0][0]
        assert "--driver" not in cmd
        assert "myvol" in cmd

    @patch("wrknv.container.operations.volumes.run")
    def test_create_volume_process_error_returns_false(self, mock_run) -> None:
        """Test create_volume returns False and prints error on ProcessError (lines 61-64)."""
        mock_run.side_effect = ProcessError(
            message="volume already exists",
            command=["docker", "volume", "create"],
            returncode=1,
        )
        mgr, console = _make_manager()

        result = mgr.create_volume(name="myvol", driver=None, options=None)

        assert result is False
        console.print.assert_called_once()
        printed = console.print.call_args[0][0]
        assert "Failed to create volume" in printed


@pytest.mark.container
class TestRemoveVolume:
    """Test remove_volume with/without force and error path (lines 76-92)."""

    @patch("wrknv.container.operations.volumes.run")
    def test_remove_volume_without_force(self, mock_run) -> None:
        """Test remove_volume without force omits -f flag (branch 76-84)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "rm"], returncode=0, stdout="myvol", stderr=""
        )
        mgr, _ = _make_manager()

        result = mgr.remove_volume(name="myvol", force=False)

        assert result is True
        cmd = mock_run.call_args[0][0]
        assert "-f" not in cmd
        assert "myvol" in cmd

    @patch("wrknv.container.operations.volumes.run")
    def test_remove_volume_with_force(self, mock_run) -> None:
        """Test remove_volume with force adds -f flag (line 80)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "rm"], returncode=0, stdout="myvol", stderr=""
        )
        mgr, _ = _make_manager()

        result = mgr.remove_volume(name="myvol", force=True)

        assert result is True
        cmd = mock_run.call_args[0][0]
        assert "-f" in cmd

    @patch("wrknv.container.operations.volumes.run")
    def test_remove_volume_process_error_returns_false(self, mock_run) -> None:
        """Test remove_volume returns False and prints error on ProcessError (lines 89-92)."""
        mock_run.side_effect = ProcessError(
            message="volume in use",
            command=["docker", "volume", "rm"],
            returncode=1,
        )
        mgr, console = _make_manager()

        result = mgr.remove_volume(name="myvol", force=False)

        assert result is False
        console.print.assert_called_once()
        printed = console.print.call_args[0][0]
        assert "Failed to remove volume" in printed


@pytest.mark.container
class TestListVolumes:
    """Test list_volumes branches (lines 107, 112→117, 114→113, 119-121)."""

    @patch("wrknv.container.operations.volumes.run")
    def test_list_volumes_with_filter_label(self, mock_run) -> None:
        """Test list_volumes adds --filter when filter_label provided (line 107)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"],
            returncode=0,
            stdout='{"Name":"vol1","Driver":"local"}',
            stderr="",
        )
        mgr, _ = _make_manager()

        volumes = mgr.list_volumes(filter_label="project=myapp")

        assert len(volumes) == 1
        cmd = mock_run.call_args[0][0]
        assert "--filter" in cmd
        assert "label=project=myapp" in cmd

    @patch("wrknv.container.operations.volumes.run")
    def test_list_volumes_empty_stdout_returns_empty(self, mock_run) -> None:
        """Test list_volumes with empty stdout returns empty list (branch 112→117)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"], returncode=0, stdout="", stderr=""
        )
        mgr, _ = _make_manager()

        volumes = mgr.list_volumes(filter_label=None)

        assert volumes == []

    @patch("wrknv.container.operations.volumes.run")
    def test_list_volumes_blank_lines_skipped(self, mock_run) -> None:
        """Test list_volumes skips blank lines in stdout (branch 114→113)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"],
            returncode=0,
            stdout='{"Name":"vol1","Driver":"local"}\n\n{"Name":"vol2","Driver":"local"}\n',
            stderr="",
        )
        mgr, _ = _make_manager()

        volumes = mgr.list_volumes(filter_label=None)

        assert len(volumes) == 2

    @patch("wrknv.container.operations.volumes.run")
    def test_list_volumes_json_error_returns_empty(self, mock_run) -> None:
        """Test list_volumes returns empty list on JSONDecodeError (lines 119-121)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"],
            returncode=0,
            stdout="not valid json at all",
            stderr="",
        )
        mgr, _ = _make_manager()

        volumes = mgr.list_volumes(filter_label=None)

        assert volumes == []

    @patch("wrknv.container.operations.volumes.run")
    def test_list_volumes_process_error_returns_empty(self, mock_run) -> None:
        """Test list_volumes returns empty list on ProcessError (lines 119-121)."""
        mock_run.side_effect = ProcessError(
            message="daemon not running",
            command=["docker", "volume", "ls"],
            returncode=1,
        )
        mgr, _ = _make_manager()

        volumes = mgr.list_volumes(filter_label=None)

        assert volumes == []


@pytest.mark.container
class TestInspectVolume:
    """Test inspect_volume (lines 132-142)."""

    @patch("wrknv.container.operations.volumes.run")
    def test_inspect_volume_returns_first_element(self, mock_run) -> None:
        """Test inspect_volume parses JSON and returns first element (lines 132-137)."""
        volume_data = [{"Name": "myvol", "Driver": "local", "Mountpoint": "/var/lib/docker/volumes/myvol"}]
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "inspect"],
            returncode=0,
            stdout=json.dumps(volume_data),
            stderr="",
        )
        mgr, _ = _make_manager()

        info = mgr.inspect_volume("myvol")

        assert info["Name"] == "myvol"
        assert info["Driver"] == "local"

    @patch("wrknv.container.operations.volumes.run")
    def test_inspect_volume_empty_array_returns_empty_dict(self, mock_run) -> None:
        """Test inspect_volume returns {} when JSON array is empty (line 137)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "inspect"],
            returncode=0,
            stdout=json.dumps([]),
            stderr="",
        )
        mgr, _ = _make_manager()

        info = mgr.inspect_volume("myvol")

        assert info == {}

    @patch("wrknv.container.operations.volumes.run")
    def test_inspect_volume_empty_stdout_returns_empty_dict(self, mock_run) -> None:
        """Test inspect_volume returns {} when stdout is empty (branch 135)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "inspect"], returncode=0, stdout="", stderr=""
        )
        mgr, _ = _make_manager()

        info = mgr.inspect_volume("myvol")

        assert info == {}

    @patch("wrknv.container.operations.volumes.run")
    def test_inspect_volume_process_error_returns_empty_dict(self, mock_run) -> None:
        """Test inspect_volume returns {} on ProcessError (lines 140-142)."""
        mock_run.side_effect = ProcessError(
            message="no such volume",
            command=["docker", "volume", "inspect"],
            returncode=1,
        )
        mgr, _ = _make_manager()

        info = mgr.inspect_volume("nonexistent")

        assert info == {}

    @patch("wrknv.container.operations.volumes.run")
    def test_inspect_volume_json_error_returns_empty_dict(self, mock_run) -> None:
        """Test inspect_volume returns {} on JSONDecodeError (lines 140-142)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "inspect"],
            returncode=0,
            stdout="invalid json {{{",
            stderr="",
        )
        mgr, _ = _make_manager()

        info = mgr.inspect_volume("myvol")

        assert info == {}


@pytest.mark.container
class TestBackupVolumeError:
    """Test backup_volume error path (lines 193-196)."""

    @patch("wrknv.container.operations.volumes.run")
    def test_backup_volume_process_error_returns_none(self, mock_run) -> None:
        """Test backup_volume returns None and prints error on ProcessError (lines 193-196)."""
        mock_run.side_effect = ProcessError(
            message="alpine not found",
            command=["docker", "run"],
            returncode=1,
        )
        mgr, console = _make_manager()

        result = mgr.backup_volume(
            volume_name="myvol",
            container_name="mycontainer",
            mount_path="/data",
        )

        assert result is None
        console.print.assert_called()
        # find the error print call
        error_calls = [c for c in console.print.call_args_list if "Backup failed" in str(c)]
        assert error_calls


@pytest.mark.container
class TestRestoreVolume:
    """Test restore_volume happy path and error paths (lines 214-271)."""

    def setup_method(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.mgr, self.console = _make_manager(backup_dir=self.tmp)

    @patch("wrknv.container.operations.volumes.run")
    def test_restore_volume_success(self, mock_run) -> None:
        """Test restore_volume runs tar command and returns True (lines 214-245)."""
        mock_run.return_value = CompletedProcess(args=["docker", "run"], returncode=0, stdout="", stderr="")

        backup_file = self.tmp / "myvol_20240101.tar"
        backup_file.write_text("fake tar content")

        result = self.mgr.restore_volume(
            volume_name="myvol",
            backup_file=backup_file,
            mount_path="/data",
        )

        assert result is True
        mock_run.assert_called_once()
        cmd = mock_run.call_args[0][0]
        assert "run" in cmd
        assert "--rm" in cmd
        assert "alpine" in cmd
        assert "tar" in cmd
        assert "-xzf" in cmd

    def test_restore_volume_file_not_found_returns_false(self) -> None:
        """Test restore_volume returns False when backup file doesn't exist (lines 215-217)."""
        missing = self.tmp / "nonexistent.tar"

        result = self.mgr.restore_volume(
            volume_name="myvol",
            backup_file=missing,
            mount_path="/data",
        )

        assert result is False
        self.console.print.assert_called_once()
        printed = self.console.print.call_args[0][0]
        assert "Backup file not found" in printed

    @patch("wrknv.container.operations.volumes.run")
    def test_restore_volume_process_error_returns_false(self, mock_run) -> None:
        """Test restore_volume returns False and prints error on ProcessError (lines 259-271)."""
        mock_run.side_effect = ProcessError(
            message="volume locked",
            command=["docker", "run"],
            returncode=1,
        )
        backup_file = self.tmp / "myvol_20240101.tar"
        backup_file.write_text("fake tar content")

        result = self.mgr.restore_volume(
            volume_name="myvol",
            backup_file=backup_file,
            mount_path="/data",
        )

        assert result is False
        self.console.print.assert_called()
        error_calls = [c for c in self.console.print.call_args_list if "Restore failed" in str(c)]
        assert error_calls


@pytest.mark.container
class TestShowVolumes:
    """Test show_volumes table display."""

    @patch("wrknv.container.operations.volumes.run")
    def test_show_volumes_empty_prints_no_volumes_message(self, mock_run) -> None:
        """Test show_volumes with no volumes prints 'No volumes found' (lines 261-263)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"], returncode=0, stdout="", stderr=""
        )
        mgr, console = _make_manager()

        mgr.show_volumes()

        console.print.assert_called_once()
        printed = console.print.call_args[0][0]
        assert "No volumes found" in printed

    @patch("wrknv.container.operations.volumes.run")
    def test_show_volumes_with_data_prints_table(self, mock_run) -> None:
        """Test show_volumes renders a Rich table when volumes exist (lines 265-279)."""
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"],
            returncode=0,
            stdout='{"Name":"vol1","Driver":"local","Mountpoint":"/var/lib/docker/volumes/vol1/_data"}',
            stderr="",
        )
        mgr, console = _make_manager()

        mgr.show_volumes()

        console.print.assert_called_once()

    @patch("wrknv.container.operations.volumes.run")
    def test_show_volumes_long_mountpoint_truncated(self, mock_run) -> None:
        """Test show_volumes truncates Mountpoint longer than 50 chars (line 274-277)."""
        long_path = "/var/lib/docker/volumes/" + "a" * 50 + "/_data"
        mock_run.return_value = CompletedProcess(
            args=["docker", "volume", "ls"],
            returncode=0,
            stdout=json.dumps({"Name": "vol1", "Driver": "local", "Mountpoint": long_path}),
            stderr="",
        )
        mgr, console = _make_manager()

        # Should not raise
        mgr.show_volumes()

        console.print.assert_called_once()


@pytest.mark.container
class TestStubMethods:
    """Test backup/restore/clean stubs return True (lines 299, 313, 326)."""

    def setup_method(self) -> None:
        self.mgr, _ = _make_manager()

    def test_backup_stub_returns_true(self) -> None:
        """Test backup() stub returns True (line 299)."""
        result = self.mgr.backup()
        assert result is True

    def test_backup_with_args_returns_true(self) -> None:
        """Test backup() stub with all args still returns True."""
        result = self.mgr.backup(backup_path=Path("/tmp/backup"), volumes=["vol1"], compress=False)
        assert result is True

    def test_restore_stub_returns_true(self) -> None:
        """Test restore() stub returns True (line 313)."""
        result = self.mgr.restore(backup_path=Path("/tmp/backup.tar.gz"))
        assert result is True

    def test_restore_with_force_returns_true(self) -> None:
        """Test restore() stub with force=True still returns True."""
        result = self.mgr.restore(backup_path=Path("/tmp/backup.tar.gz"), force=True)
        assert result is True

    def test_clean_stub_returns_true(self) -> None:
        """Test clean() stub returns True (line 326)."""
        result = self.mgr.clean()
        assert result is True

    def test_clean_with_preserve_returns_true(self) -> None:
        """Test clean() stub with preserve list still returns True."""
        result = self.mgr.clean(preserve=["vol1", "vol2"])
        assert result is True


# 🧰🌍🔚
