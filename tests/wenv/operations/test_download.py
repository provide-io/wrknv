#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for wrknv.wenv.operations.download module."""

from __future__ import annotations

import asyncio
import pathlib
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.wenv.operations.download import (
    download_checksum_file,
    download_file,
    download_with_mirrors,
    get_filename_from_url,
    parse_checksum_file,
    validate_download_url,
    verify_checksum,
)


class TestValidateDownloadUrl(FoundationTestCase):
    """Tests for validate_download_url."""

    def test_valid_https_url(self) -> None:
        assert validate_download_url("https://example.com/file.tar.gz") is True

    def test_valid_http_url(self) -> None:
        assert validate_download_url("http://example.com/file.tar.gz") is True

    def test_invalid_scheme_ftp(self) -> None:
        assert validate_download_url("ftp://example.com/file.tar.gz") is False

    def test_missing_scheme(self) -> None:
        assert validate_download_url("example.com/file.tar.gz") is False

    def test_missing_netloc(self) -> None:
        assert validate_download_url("https://") is False

    def test_empty_string(self) -> None:
        assert validate_download_url("") is False

    def test_https_mixed_case(self) -> None:
        assert validate_download_url("HTTPS://example.com/file.tar.gz") is True


class TestGetFilenameFromUrl(FoundationTestCase):
    """Tests for get_filename_from_url."""

    def test_extracts_filename(self) -> None:
        result = get_filename_from_url("https://example.com/path/to/file.tar.gz")
        assert result == "file.tar.gz"

    def test_extracts_versioned_filename(self) -> None:
        result = get_filename_from_url("https://github.com/owner/repo/releases/download/v1.0/tool_1.0_linux.tar.gz")
        assert result == "tool_1.0_linux.tar.gz"

    def test_fallback_for_no_filename(self) -> None:
        result = get_filename_from_url("https://example.com/")
        # Falls back to hash-based name
        assert result.startswith("download_")

    def test_handles_query_params(self) -> None:
        result = get_filename_from_url("https://example.com/file.zip?token=abc")
        assert result == "file.zip"


class TestParseChecksumFile(FoundationTestCase):
    """Tests for parse_checksum_file."""

    def test_returns_none_when_file_missing(self) -> None:
        result = parse_checksum_file(pathlib.Path("/nonexistent/checksums.txt"), "file.tar.gz")
        assert result is None

    def test_finds_checksum_by_filename(self) -> None:
        tmp = self.create_temp_dir()
        checksum_file = tmp / "SHA256SUMS"
        checksum_file.write_text(
            "abc123def456  file.tar.gz\n"
            "999888777666  other.tar.gz\n"
        )
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result == "abc123def456"

    def test_skips_comment_lines(self) -> None:
        tmp = self.create_temp_dir()
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text(
            "# This is a comment\n"
            "abc123  file.tar.gz\n"
        )
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result == "abc123"

    def test_skips_empty_lines(self) -> None:
        tmp = self.create_temp_dir()
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text("\n\nabc123  file.tar.gz\n")
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result == "abc123"

    def test_strips_asterisk_prefix_from_filename(self) -> None:
        tmp = self.create_temp_dir()
        checksum_file = tmp / "checksums.txt"
        # BSD-style checksum with * prefix on filename
        checksum_file.write_text("abc123  *file.tar.gz\n")
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result == "abc123"

    def test_returns_none_when_target_not_found(self) -> None:
        tmp = self.create_temp_dir()
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text("abc123  other.tar.gz\n")
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result is None

    def test_handles_suffix_match(self) -> None:
        tmp = self.create_temp_dir()
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text("abc123  ./subdir/file.tar.gz\n")
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result == "abc123"

    def test_returns_none_on_parse_error(self) -> None:
        tmp = self.create_temp_dir()
        checksum_file = tmp / "checksums.txt"
        # Create file that will cause read error by making it a directory
        checksum_file.mkdir()
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result is None


class TestVerifyChecksum(FoundationTestCase):
    """Tests for verify_checksum."""

    def test_delegates_to_foundation(self) -> None:
        with mock.patch("wrknv.wenv.operations.download.verify_file", return_value=True) as mock_vf:
            result = verify_checksum(pathlib.Path("/tmp/file"), "abc123")
        assert result is True
        mock_vf.assert_called_once_with(pathlib.Path("/tmp/file"), "abc123", "sha256")

    def test_passes_algorithm(self) -> None:
        with mock.patch("wrknv.wenv.operations.download.verify_file", return_value=False) as mock_vf:
            result = verify_checksum(pathlib.Path("/tmp/file"), "abc123", "md5")
        assert result is False
        mock_vf.assert_called_once_with(pathlib.Path("/tmp/file"), "abc123", "md5")


class TestDownloadChecksumFile(FoundationTestCase):
    """Tests for download_checksum_file."""

    def test_returns_none_for_empty_url(self) -> None:
        tmp = self.create_temp_dir()
        result = download_checksum_file("", tmp)
        assert result is None

    def test_returns_path_on_success(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("wrknv.wenv.operations.download.download_file") as mock_dl:
            result = download_checksum_file("https://example.com/SHA256SUMS", tmp)
        assert result is not None
        assert result.name == "SHA256SUMS"
        mock_dl.assert_called_once()

    def test_returns_none_on_download_failure(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch(
            "wrknv.wenv.operations.download.download_file",
            side_effect=Exception("network error"),
        ):
            result = download_checksum_file("https://example.com/SHA256SUMS", tmp)
        assert result is None

    def test_uses_fallback_filename_when_none_in_url(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("wrknv.wenv.operations.download.download_file"):
            result = download_checksum_file("https://example.com/", tmp)
        assert result is not None
        assert result.name == "checksums.txt"


class TestDownloadFile(FoundationTestCase):
    """Tests for download_file (synchronous wrapper)."""

    def test_calls_asyncio_run(self) -> None:
        with mock.patch("wrknv.wenv.operations.download.asyncio.run") as mock_run:
            download_file("https://example.com/file.tar.gz", pathlib.Path("/tmp/file.tar.gz"))
        mock_run.assert_called_once()

    def test_passes_show_progress_false(self) -> None:
        with mock.patch("wrknv.wenv.operations.download.asyncio.run") as mock_run:
            download_file(
                "https://example.com/file.tar.gz",
                pathlib.Path("/tmp/file.tar.gz"),
                show_progress=False,
            )
        mock_run.assert_called_once()


class TestDownloadWithMirrors(FoundationTestCase):
    """Tests for download_with_mirrors (synchronous wrapper)."""

    def test_calls_asyncio_run(self) -> None:
        with mock.patch("wrknv.wenv.operations.download.asyncio.run") as mock_run:
            download_with_mirrors(
                ["https://mirror1.example.com/file.tar.gz"],
                pathlib.Path("/tmp/file.tar.gz"),
            )
        mock_run.assert_called_once()


class TestDownloadFileAsync(FoundationTestCase):
    """Tests for download_file_async."""

    def test_raises_on_failure(self) -> None:
        from wrknv.wenv.operations.download import download_file_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_progress = mock.AsyncMock(
            side_effect=Exception("connection error")
        )
        mock_downloader.add_progress_callback = mock.Mock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch(
                "wrknv.wenv.operations.download.UniversalClient",
                return_value=mock_client,
            ),
            mock.patch(
                "wrknv.wenv.operations.download.ToolDownloader",
                return_value=mock_downloader,
            ),pytest.raises(Exception, match="Failed to download")
        ):
            asyncio.run(download_file_async("https://example.com/file.tar.gz", pathlib.Path("/tmp/f")))

    def test_success_path(self) -> None:
        tmp = self.create_temp_dir()
        from wrknv.wenv.operations.download import download_file_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_progress = mock.AsyncMock()
        mock_downloader.add_progress_callback = mock.Mock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch(
                "wrknv.wenv.operations.download.UniversalClient",
                return_value=mock_client,
            ),
            mock.patch(
                "wrknv.wenv.operations.download.ToolDownloader",
                return_value=mock_downloader,
            ),
        ):
            asyncio.run(
                download_file_async("https://example.com/file.tar.gz", tmp / "file.tar.gz")
            )
        mock_downloader.download_with_progress.assert_called_once()

    def test_with_progress_callback(self) -> None:
        """Test download_file_async with progress_callback provided."""
        tmp = self.create_temp_dir()
        from wrknv.wenv.operations.download import download_file_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_progress = mock.AsyncMock()
        mock_downloader.add_progress_callback = mock.Mock()

        callback_calls = []
        def my_callback(downloaded: int, total: int) -> None:
            callback_calls.append((downloaded, total))

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
        ):
            asyncio.run(download_file_async(
                "https://example.com/file.tar.gz",
                tmp / "file.tar.gz",
                progress_callback=my_callback,
            ))

        # add_progress_callback called at least once (for progress_callback + possibly show_progress)
        assert mock_downloader.add_progress_callback.call_count >= 1

    def test_with_show_progress_false(self) -> None:
        """Test download_file_async with show_progress=False."""
        tmp = self.create_temp_dir()
        from wrknv.wenv.operations.download import download_file_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_progress = mock.AsyncMock()
        mock_downloader.add_progress_callback = mock.Mock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
        ):
            asyncio.run(download_file_async(
                "https://example.com/file.tar.gz",
                tmp / "file.tar.gz",
                show_progress=False,
            ))

        mock_downloader.download_with_progress.assert_called_once()


class TestDownloadWithMirrorsAsync(FoundationTestCase):
    """Tests for download_with_mirrors_async."""

    def test_success_path(self) -> None:
        tmp = self.create_temp_dir()
        from wrknv.wenv.operations.download import download_with_mirrors_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_mirrors = mock.AsyncMock()
        mock_downloader.add_progress_callback = mock.Mock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
        ):
            asyncio.run(download_with_mirrors_async(
                ["https://mirror1.com/file.tar.gz"],
                tmp / "file.tar.gz",
            ))

        mock_downloader.download_with_mirrors.assert_called_once()

    def test_raises_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        from wrknv.wenv.operations.download import download_with_mirrors_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_mirrors = mock.AsyncMock(side_effect=Exception("all failed"))
        mock_downloader.add_progress_callback = mock.Mock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
            pytest.raises(Exception, match="Failed to download from all mirrors"),
        ):
            asyncio.run(download_with_mirrors_async(
                ["https://mirror1.com/file.tar.gz"],
                tmp / "file.tar.gz",
            ))

    def test_with_show_progress_false(self) -> None:
        tmp = self.create_temp_dir()
        from wrknv.wenv.operations.download import download_with_mirrors_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_mirrors = mock.AsyncMock()
        mock_downloader.add_progress_callback = mock.Mock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
        ):
            asyncio.run(download_with_mirrors_async(
                ["https://mirror1.com/file.tar.gz"],
                tmp / "file.tar.gz",
                show_progress=False,
            ))

        mock_downloader.download_with_mirrors.assert_called_once()

    def test_checksum_verification_failure(self) -> None:
        """Test that checksum mismatch raises exception."""
        tmp = self.create_temp_dir()
        output_file = tmp / "file.tar.gz"
        from wrknv.wenv.operations.download import download_with_mirrors_async

        mock_hub = mock.Mock()
        mock_client = mock.AsyncMock()
        mock_client.__aenter__ = mock.AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = mock.AsyncMock(return_value=False)
        mock_downloader = mock.AsyncMock()
        mock_downloader.download_with_mirrors = mock.AsyncMock()
        mock_downloader.add_progress_callback = mock.Mock()

        with (
            mock.patch("wrknv.wenv.operations.download.get_hub", return_value=mock_hub),
            mock.patch("wrknv.wenv.operations.download.UniversalClient", return_value=mock_client),
            mock.patch("wrknv.wenv.operations.download.ToolDownloader", return_value=mock_downloader),
            mock.patch("wrknv.wenv.operations.download.verify_checksum", return_value=False),
            mock.patch("pathlib.Path.unlink"),
            pytest.raises(Exception, match="Failed to download from all mirrors"),
        ):
            asyncio.run(download_with_mirrors_async(
                ["https://mirror1.com/file.tar.gz"],
                output_file,
                checksum="expected_hash",
            ))


class TestParseChecksumFileEdgeCases(FoundationTestCase):
    """Additional edge case tests for parse_checksum_file."""

    def test_line_with_single_token_is_skipped(self) -> None:
        """Lines with fewer than 2 parts are skipped."""
        tmp = self.create_temp_dir()
        checksum_file = tmp / "checksums.txt"
        checksum_file.write_text("onetoken\nabc123  file.tar.gz\n")
        result = parse_checksum_file(checksum_file, "file.tar.gz")
        assert result == "abc123"


class TestValidateDownloadUrlEdgeCases(FoundationTestCase):
    """Additional edge cases for validate_download_url."""

    def test_non_string_raises_handled(self) -> None:
        """urlparse with non-string raises TypeError, caught and returns False."""
        with mock.patch("wrknv.wenv.operations.download.urlparse", side_effect=Exception("bad")):
            result = validate_download_url("https://example.com/file.tar.gz")
        assert result is False


# 🧰🌍🔚
