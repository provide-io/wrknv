#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for Download Operations
=============================
Tests for the download functionality in wrknv."""

from __future__ import annotations

import hashlib
from unittest.mock import patch

from provide.testkit import FoundationTestCase

from wrknv.wenv.operations.download import (
    download_file,
    get_filename_from_url,
    parse_checksum_file,
    validate_download_url,
    verify_checksum,
)


class TestDownloadOperations(FoundationTestCase):
    """Test download operations functionality."""

    def setup_method(self) -> None:
        """Set up test - patch checksums logger which is frozen at INFO level at import time."""
        super().setup_method()
        self._log_patcher = patch("provide.foundation.crypto.checksums.log")
        self._log_patcher.start()

    def teardown_method(self, method: object = None) -> None:
        """Tear down test."""
        self._log_patcher.stop()

    def test_verify_checksum_success(self) -> None:
        """Test successful checksum verification."""
        tmp_path = self.create_temp_dir()
        test_file = tmp_path / "test.txt"
        test_content = b"Test content"
        test_file.write_bytes(test_content)

        expected_hash = hashlib.sha256(test_content).hexdigest()
        result = verify_checksum(test_file, expected_hash)
        assert result is True

    def test_verify_checksum_mismatch(self) -> None:
        """Test checksum verification with mismatch."""
        tmp_path = self.create_temp_dir()
        test_file = tmp_path / "test.txt"
        test_file.write_bytes(b"Test content")

        result = verify_checksum(test_file, "wronghash")
        assert result is False

    def test_verify_checksum_nonexistent_file(self) -> None:
        """Test checksum verification with non-existent file."""
        tmp_path = self.create_temp_dir()
        test_file = tmp_path / "nonexistent.txt"

        result = verify_checksum(test_file, "somehash")
        assert result is False

    def test_verify_checksum_different_algorithms(self) -> None:
        """Test checksum verification with different algorithms."""
        tmp_path = self.create_temp_dir()
        test_file = tmp_path / "test.txt"
        test_content = b"Test content"
        test_file.write_bytes(test_content)

        sha256_hash = hashlib.sha256(test_content).hexdigest()
        assert verify_checksum(test_file, sha256_hash, "sha256") is True

        sha1_hash = hashlib.sha1(test_content).hexdigest()
        assert verify_checksum(test_file, sha1_hash, "sha1") is True

        md5_hash = hashlib.md5(test_content).hexdigest()
        assert verify_checksum(test_file, md5_hash, "md5") is True

    def test_verify_checksum_unsupported_algorithm(self) -> None:
        """Test checksum verification with unsupported algorithm."""
        tmp_path = self.create_temp_dir()
        test_file = tmp_path / "test.txt"
        test_file.write_bytes(b"Test content")

        result = verify_checksum(test_file, "somehash", "sha512")
        assert result is False

    @patch("wrknv.wenv.operations.download.UniversalClient")
    def test_download_file_success(self, mock_client_class: object) -> None:
        """Test successful file download."""
        from unittest.mock import AsyncMock, MagicMock

        tmp_path = self.create_temp_dir()
        url = "https://example.com/test.zip"
        dest_path = tmp_path / "test.zip"

        mock_response = MagicMock()
        mock_response.is_success.return_value = True
        mock_response.status = 200
        mock_response.headers = {"content-length": "16"}

        mock_client = MagicMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock()
        mock_client.request = AsyncMock(return_value=mock_response)
        mock_client.head = AsyncMock(return_value=mock_response)

        async def mock_stream(url: str, method: str = "GET"):  # type: ignore[return]
            yield b"ZIP file content"

        mock_client.stream = mock_stream
        mock_client_class.return_value = mock_client

        download_file(url, dest_path)

        assert dest_path.exists()
        assert dest_path.read_bytes() == b"ZIP file content"

    @patch("wrknv.wenv.operations.download.UniversalClient")
    def test_download_file_with_progress(self, mock_client_class: object) -> None:
        """Test file download with progress display."""
        from unittest.mock import AsyncMock, MagicMock

        tmp_path = self.create_temp_dir()
        url = "https://example.com/test.zip"
        dest_path = tmp_path / "test.zip"

        mock_response = MagicMock()
        mock_response.is_success.return_value = True
        mock_response.status = 200
        mock_response.headers = {"content-length": "16"}

        mock_client = MagicMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock()
        mock_client.request = AsyncMock(return_value=mock_response)
        mock_client.head = AsyncMock(return_value=mock_response)

        async def mock_stream(url: str, method: str = "GET"):  # type: ignore[return]
            yield b"ZIP file content"

        mock_client.stream = mock_stream
        mock_client_class.return_value = mock_client

        download_file(url, dest_path, show_progress=True)

        assert dest_path.exists()
        assert dest_path.read_bytes() == b"ZIP file content"

    def test_parse_checksum_file_success(self) -> None:
        """Test parsing checksum file."""
        tmp_path = self.create_temp_dir()
        checksum_file = tmp_path / "checksums.sha256"
        checksum_file.write_text("""
# Comment line
abc123  test.zip
def456  other.zip
789xyz  *marked.zip
        """)

        result = parse_checksum_file(checksum_file, "test.zip")
        assert result == "abc123"

        result = parse_checksum_file(checksum_file, "marked.zip")
        assert result == "789xyz"

    def test_parse_checksum_file_not_found(self) -> None:
        """Test parsing checksum file when target not found."""
        tmp_path = self.create_temp_dir()
        checksum_file = tmp_path / "checksums.sha256"
        checksum_file.write_text("abc123  other.zip\n")

        result = parse_checksum_file(checksum_file, "test.zip")
        assert result is None

    def test_parse_checksum_file_nonexistent(self) -> None:
        """Test parsing non-existent checksum file."""
        tmp_path = self.create_temp_dir()
        checksum_file = tmp_path / "missing.sha256"
        result = parse_checksum_file(checksum_file, "test.zip")
        assert result is None

    def test_get_filename_from_url(self) -> None:
        """Test extracting filename from URL."""
        assert get_filename_from_url("https://example.com/test.zip") == "test.zip"
        assert get_filename_from_url("https://example.com/file.tar.gz?v=1") == "file.tar.gz"

        result = get_filename_from_url("https://example.com/")
        assert result.startswith("download_")

    def test_validate_download_url(self) -> None:
        """Test URL validation."""
        assert validate_download_url("https://example.com/file.zip") is True
        assert validate_download_url("http://example.com/file.zip") is True

        assert validate_download_url("ftp://example.com/file.zip") is False
        assert validate_download_url("not-a-url") is False
        assert validate_download_url("") is False
        assert validate_download_url("file:///path/to/file") is False


# 🧰🌍🔚
