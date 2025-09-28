"""
Tests for Download Operations
=============================
Tests for the download functionality in wrknv.
"""

from __future__ import annotations

import hashlib
from unittest.mock import patch
import urllib.error
import urllib.request

import pytest

from wrknv.wenv.operations.download import (
    download_checksum_file,
    download_file,
    get_filename_from_url,
    parse_checksum_file,
    validate_download_url,
    verify_checksum,
)


class TestDownloadOperations:
    """Test download operations functionality."""

    def test_verify_checksum_success(self, tmp_path):
        """Test successful checksum verification."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_content = b"Test content"
        test_file.write_bytes(test_content)

        # Calculate expected hash
        expected_hash = hashlib.sha256(test_content).hexdigest()

        # Verify checksum
        result = verify_checksum(test_file, expected_hash)
        assert result is True

    def test_verify_checksum_mismatch(self, tmp_path):
        """Test checksum verification with mismatch."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_bytes(b"Test content")

        # Verify checksum should fail with wrong hash
        result = verify_checksum(test_file, "wronghash")
        assert result is False

    def test_verify_checksum_nonexistent_file(self, tmp_path):
        """Test checksum verification with non-existent file."""
        test_file = tmp_path / "nonexistent.txt"

        # Should return False
        result = verify_checksum(test_file, "somehash")
        assert result is False

    def test_verify_checksum_different_algorithms(self, tmp_path):
        """Test checksum verification with different algorithms."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_content = b"Test content"
        test_file.write_bytes(test_content)

        # Test SHA256
        sha256_hash = hashlib.sha256(test_content).hexdigest()
        assert verify_checksum(test_file, sha256_hash, "sha256") is True

        # Test SHA1
        sha1_hash = hashlib.sha1(test_content).hexdigest()
        assert verify_checksum(test_file, sha1_hash, "sha1") is True

        # Test MD5
        md5_hash = hashlib.md5(test_content).hexdigest()
        assert verify_checksum(test_file, md5_hash, "md5") is True

    def test_verify_checksum_unsupported_algorithm(self, tmp_path):
        """Test checksum verification with unsupported algorithm."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_bytes(b"Test content")

        # Should return False for unsupported algorithm
        result = verify_checksum(test_file, "somehash", "sha512")
        assert result is False

    def test_download_file_success(self, tmp_path):
        """Test successful file download."""
        url = "https://example.com/test.zip"
        dest_path = tmp_path / "test.zip"

        # Mock urlretrieve
        def mock_urlretrieve(url, path, reporthook=None):
            # Simulate file content
            path.write_bytes(b"ZIP file content")
            # Call progress hook if provided
            if reporthook:
                reporthook(1, 16, 16)  # block_num, block_size, total_size

        with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
            download_file(url, dest_path)

        # Verify file was written
        assert dest_path.exists()
        assert dest_path.read_bytes() == b"ZIP file content"

    def test_download_file_with_progress(self, tmp_path):
        """Test file download with progress display."""
        url = "https://example.com/test.zip"
        dest_path = tmp_path / "test.zip"

        progress_calls = []

        def mock_urlretrieve(url, path, reporthook=None):
            path.write_bytes(b"ZIP file content")
            if reporthook:
                # Simulate multiple progress calls
                for i in range(0, 101, 10):
                    reporthook(i, 1, 100)
                    progress_calls.append(i)

        with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
            download_file(url, dest_path, show_progress=True)

        # Verify progress was reported
        assert len(progress_calls) > 0

    def test_download_file_error(self, tmp_path):
        """Test download with error."""
        url = "https://example.com/notfound.zip"
        dest_path = tmp_path / "test.zip"

        # Mock urlretrieve to raise exception
        with patch("urllib.request.urlretrieve") as mock_urlretrieve:
            mock_urlretrieve.side_effect = urllib.error.HTTPError(url, 404, "Not Found", {}, None)

            with pytest.raises(Exception) as exc_info:
                download_file(url, dest_path)

            assert "Failed to download" in str(exc_info.value)

        # File should not exist
        assert not dest_path.exists()

    def test_download_file_creates_parent_directory(self, tmp_path):
        """Test download creates parent directory if needed."""
        url = "https://example.com/test.zip"
        dest_path = tmp_path / "subdir" / "test.zip"

        def mock_urlretrieve(url, path, reporthook=None):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"Test content")

        with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
            download_file(url, dest_path)

        # Verify parent directory was created
        assert dest_path.parent.exists()
        assert dest_path.exists()

    def test_download_checksum_file_success(self, tmp_path):
        """Test successful checksum file download."""
        checksum_url = "https://example.com/checksums.sha256"
        output_dir = tmp_path

        def mock_urlretrieve(url, path, reporthook=None):
            path.write_text("abc123  test.zip\ndef456  other.zip\n")

        with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
            result = download_checksum_file(checksum_url, output_dir)

        assert result is not None
        assert result.name == "checksums.sha256"
        assert result.exists()

    def test_download_checksum_file_no_url(self, tmp_path):
        """Test checksum file download with no URL."""
        result = download_checksum_file("", tmp_path)
        assert result is None

    def test_download_checksum_file_error(self, tmp_path):
        """Test checksum file download with error."""
        checksum_url = "https://example.com/checksums.sha256"

        with patch("urllib.request.urlretrieve") as mock_urlretrieve:
            mock_urlretrieve.side_effect = Exception("Download failed")
            result = download_checksum_file(checksum_url, tmp_path)

        assert result is None

    def test_parse_checksum_file_success(self, tmp_path):
        """Test parsing checksum file."""
        checksum_file = tmp_path / "checksums.sha256"
        checksum_file.write_text("""
# Comment line
abc123  test.zip
def456  other.zip
789xyz  *marked.zip
        """)

        # Find checksum for test.zip
        result = parse_checksum_file(checksum_file, "test.zip")
        assert result == "abc123"

        # Find checksum for marked.zip (with asterisk)
        result = parse_checksum_file(checksum_file, "marked.zip")
        assert result == "789xyz"

    def test_parse_checksum_file_not_found(self, tmp_path):
        """Test parsing checksum file when target not found."""
        checksum_file = tmp_path / "checksums.sha256"
        checksum_file.write_text("abc123  other.zip\n")

        result = parse_checksum_file(checksum_file, "test.zip")
        assert result is None

    def test_parse_checksum_file_nonexistent(self, tmp_path):
        """Test parsing non-existent checksum file."""
        checksum_file = tmp_path / "missing.sha256"
        result = parse_checksum_file(checksum_file, "test.zip")
        assert result is None

    def test_get_filename_from_url(self) -> None:
        """Test extracting filename from URL."""
        # Normal URL
        assert get_filename_from_url("https://example.com/test.zip") == "test.zip"

        # URL with query params
        assert get_filename_from_url("https://example.com/file.tar.gz?v=1") == "file.tar.gz"

        # URL without filename
        result = get_filename_from_url("https://example.com/")
        assert result.startswith("download_")

    def test_validate_download_url(self) -> None:
        """Test URL validation."""
        # Valid URLs
        assert validate_download_url("https://example.com/file.zip") is True
        assert validate_download_url("http://example.com/file.zip") is True

        # Invalid URLs
        assert validate_download_url("ftp://example.com/file.zip") is False
        assert validate_download_url("not-a-url") is False
        assert validate_download_url("") is False
        assert validate_download_url("file:///path/to/file") is False


# 🍲🥄🧪🪄
