#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.wenv.operations.download — uncovered branches."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any
from unittest import mock

from provide.testkit import FoundationTestCase

from wrknv.wenv.operations.download import download_file_async, download_with_mirrors_async


def _mock_downloader_setup() -> tuple[mock.Mock, mock.AsyncMock, mock.AsyncMock, list[Any]]:
    """Build mocked hub/client/downloader with callback capture."""
    captured: list[Any] = []
    mock_hub = mock.Mock()
    mock_client = mock.AsyncMock()
    mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = mock.AsyncMock(return_value=False)
    mock_downloader = mock.AsyncMock()
    mock_downloader.add_progress_callback = mock.Mock(
        side_effect=lambda cb: captured.append(cb)
    )
    return mock_hub, mock_client, mock_downloader, captured


class TestDownloadFileAsyncLogProgressCallback(FoundationTestCase):
    """Lines 74->exit and 74->75->76: log_progress callback branches in download_file_async."""

    def _run_with_show_progress(self, tmp_path: Any) -> list[Callable[[int, int], None]]:
        """Run download_file_async with show_progress=True and return captured callbacks."""
        mock_hub, mock_client, mock_downloader, captured = _mock_downloader_setup()
        mock_downloader.download_with_progress = mock.AsyncMock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
        ):
            asyncio.run(
                download_file_async(
                    "https://example.com/file.tar.gz",
                    tmp_path / "file.tar.gz",
                    show_progress=True,
                )
            )
        return captured

    def test_log_progress_total_zero_skips_body(self) -> None:
        """Line 74->exit: total==0 → percent block is skipped entirely."""
        tmp = self.create_temp_dir()
        captured = self._run_with_show_progress(tmp)

        assert len(captured) >= 1
        log_progress = captured[-1]
        # Should not raise and should skip the if body
        log_progress(0, 0)

    def test_log_progress_total_nonzero_executes_body(self) -> None:
        """Lines 74->75->76->77: total>0 + at 1MB boundary → debug log called."""
        tmp = self.create_temp_dir()
        captured = self._run_with_show_progress(tmp)

        assert len(captured) >= 1
        log_progress = captured[-1]
        # downloaded=0, total=1MB → 0 % (1024*1024) == 0 < 1024 → inner if fires
        with mock.patch("wrknv.wenv.operations.download.logger") as mock_logger:
            log_progress(0, 1024 * 1024)
        mock_logger.debug.assert_called_once()


class TestDownloadWithMirrorsAsyncLogProgressCallback(FoundationTestCase):
    """Lines 143->exit and 143->144->145: log_progress callback branches in download_with_mirrors_async."""

    def _run_with_show_progress(self, tmp_path: Any) -> list[Callable[[int, int], None]]:
        """Run download_with_mirrors_async with show_progress=True and return captured callbacks."""
        mock_hub, mock_client, mock_downloader, captured = _mock_downloader_setup()
        mock_downloader.download_with_mirrors = mock.AsyncMock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
        ):
            asyncio.run(
                download_with_mirrors_async(
                    ["https://mirror.example.com/file.tar.gz"],
                    tmp_path / "file.tar.gz",
                    show_progress=True,
                )
            )
        return captured

    def test_log_progress_total_zero_skips_body(self) -> None:
        """Line 143->exit: total==0 → percent block is skipped entirely."""
        tmp = self.create_temp_dir()
        captured = self._run_with_show_progress(tmp)

        assert len(captured) >= 1
        log_progress = captured[-1]
        log_progress(0, 0)  # Should not raise

    def test_log_progress_total_nonzero_executes_body(self) -> None:
        """Lines 143->144->145->146: total>0 + at 1MB boundary → debug log called."""
        tmp = self.create_temp_dir()
        captured = self._run_with_show_progress(tmp)

        assert len(captured) >= 1
        log_progress = captured[-1]
        with mock.patch("wrknv.wenv.operations.download.logger") as mock_logger:
            log_progress(0, 1024 * 1024)
        mock_logger.debug.assert_called_once()


# 🧰🌍🔚
