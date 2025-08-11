"""
Tests for Install Operations
=============================
Tests for the install functionality in wrkenv.
"""

import pytest
import pathlib
import tempfile
import zipfile
import tarfile
import shutil
from unittest.mock import patch, Mock, MagicMock, call

from wrkenv.env.operations.install import (
    extract_archive,
    make_executable,
    create_symlink,
    copy_file,
    ensure_directory,
    clean_directory,
    get_file_size,
    is_executable,
)


class TestInstallOperations:
    """Test install operations functionality."""

    def test_extract_archive_zip(self, tmp_path):
        """Test extracting ZIP archive."""
        # Create a test ZIP file
        archive_path = tmp_path / "test.zip"
        extract_dir = tmp_path / "extract"
        
        with zipfile.ZipFile(archive_path, 'w') as zf:
            zf.writestr("test.txt", "Hello World")
            zf.writestr("subdir/file.txt", "Nested file")
        
        # Extract archive
        extract_archive(archive_path, extract_dir)
        
        # Verify files were extracted
        assert (extract_dir / "test.txt").exists()
        assert (extract_dir / "test.txt").read_text() == "Hello World"
        assert (extract_dir / "subdir" / "file.txt").exists()
        assert (extract_dir / "subdir" / "file.txt").read_text() == "Nested file"

    def test_extract_archive_tar_gz(self, tmp_path):
        """Test extracting tar.gz archive."""
        # Create a test tar.gz file
        archive_path = tmp_path / "test.tar.gz"
        extract_dir = tmp_path / "extract"
        
        # Create test files
        test_dir = tmp_path / "test_content"
        test_dir.mkdir()
        (test_dir / "test.txt").write_text("Hello World")
        subdir = test_dir / "subdir"
        subdir.mkdir()
        (subdir / "file.txt").write_text("Nested file")
        
        # Create tar.gz archive
        with tarfile.open(archive_path, "w:gz") as tf:
            tf.add(test_dir / "test.txt", arcname="test.txt")
            tf.add(subdir / "file.txt", arcname="subdir/file.txt")
        
        # Extract archive
        extract_archive(archive_path, extract_dir)
        
        # Verify files were extracted
        assert (extract_dir / "test.txt").exists()
        assert (extract_dir / "test.txt").read_text() == "Hello World"
        assert (extract_dir / "subdir" / "file.txt").exists()
        assert (extract_dir / "subdir" / "file.txt").read_text() == "Nested file"

    def test_extract_archive_unsupported(self, tmp_path):
        """Test extracting unsupported archive type."""
        archive_path = tmp_path / "test.unknown"
        archive_path.write_text("Not an archive")
        extract_dir = tmp_path / "extract"
        
        with pytest.raises(ValueError, match="Unsupported archive type"):
            extract_archive(archive_path, extract_dir)

    def test_find_binary_in_archive_direct(self, tmp_path):
        """Test finding binary directly in archive root."""
        extract_dir = tmp_path / "extract"
        extract_dir.mkdir()
        
        # Create binary in root
        binary_path = extract_dir / "terraform"
        binary_path.write_text("#!/bin/sh\necho terraform")
        binary_path.chmod(0o755)
        
        result = find_binary_in_archive(extract_dir, "terraform")
        assert result == binary_path

    def test_find_binary_in_archive_nested(self, tmp_path):
        """Test finding binary in nested directory."""
        extract_dir = tmp_path / "extract"
        extract_dir.mkdir()
        
        # Create binary in nested directory
        bin_dir = extract_dir / "bin"
        bin_dir.mkdir()
        binary_path = bin_dir / "terraform"
        binary_path.write_text("#!/bin/sh\necho terraform")
        binary_path.chmod(0o755)
        
        result = find_binary_in_archive(extract_dir, "terraform")
        assert result == binary_path

    def test_find_binary_in_archive_not_found(self, tmp_path):
        """Test when binary is not found in archive."""
        extract_dir = tmp_path / "extract"
        extract_dir.mkdir()
        
        # Create some other files
        (extract_dir / "readme.txt").write_text("Readme")
        
        result = find_binary_in_archive(extract_dir, "terraform")
        assert result is None

    def test_find_binary_in_archive_windows(self, tmp_path):
        """Test finding binary on Windows (with .exe extension)."""
        extract_dir = tmp_path / "extract"
        extract_dir.mkdir()
        
        # Create Windows binary
        binary_path = extract_dir / "terraform.exe"
        binary_path.write_text("Windows binary")
        
        # Mock os.name to simulate Windows
        with patch('os.name', 'nt'):
            result = find_binary_in_archive(extract_dir, "terraform")
            assert result == binary_path

    def test_install_binary_success(self, tmp_path):
        """Test successful binary installation."""
        source = tmp_path / "source" / "terraform"
        source.parent.mkdir()
        source.write_text("#!/bin/sh\necho terraform")
        source.chmod(0o755)
        
        dest_dir = tmp_path / "dest"
        
        install_binary(source, dest_dir, "terraform")
        
        # Verify binary was installed
        installed = dest_dir / "terraform"
        assert installed.exists()
        assert installed.is_file()
        assert installed.stat().st_mode & 0o111  # Check executable

    def test_install_binary_creates_dest_dir(self, tmp_path):
        """Test binary installation creates destination directory."""
        source = tmp_path / "terraform"
        source.write_text("#!/bin/sh\necho terraform")
        source.chmod(0o755)
        
        dest_dir = tmp_path / "new" / "dest"
        
        install_binary(source, dest_dir, "terraform")
        
        # Verify directory was created and binary installed
        assert dest_dir.exists()
        assert (dest_dir / "terraform").exists()

    def test_install_binary_overwrites_existing(self, tmp_path):
        """Test binary installation overwrites existing file."""
        source = tmp_path / "terraform"
        source.write_text("#!/bin/sh\necho new")
        source.chmod(0o755)
        
        dest_dir = tmp_path / "dest"
        dest_dir.mkdir()
        
        # Create existing binary
        existing = dest_dir / "terraform"
        existing.write_text("#!/bin/sh\necho old")
        
        install_binary(source, dest_dir, "terraform")
        
        # Verify binary was overwritten
        assert existing.read_text() == "#!/bin/sh\necho new"

    def test_install_from_archive_success(self, tmp_path):
        """Test complete installation from archive."""
        # Create a ZIP archive with binary
        archive_path = tmp_path / "terraform.zip"
        with zipfile.ZipFile(archive_path, 'w') as zf:
            zf.writestr("terraform", "#!/bin/sh\necho terraform", zipfile.ZipInfo("terraform"))
        
        # Make the binary executable in the zip
        with zipfile.ZipFile(archive_path, 'r') as zf:
            info = zf.getinfo("terraform")
            info.external_attr = 0o755 << 16  # Unix permissions
        
        dest_dir = tmp_path / "bin"
        
        with patch('wrkenv.env.operations.install.extract_archive') as mock_extract:
            with patch('wrkenv.env.operations.install.find_binary_in_archive') as mock_find:
                # Mock extraction
                extract_dir = tmp_path / "temp_extract"
                extract_dir.mkdir()
                binary_path = extract_dir / "terraform"
                binary_path.write_text("#!/bin/sh\necho terraform")
                binary_path.chmod(0o755)
                
                mock_find.return_value = binary_path
                
                install_from_archive(archive_path, dest_dir, "terraform")
        
        # Verify binary was installed
        assert (dest_dir / "terraform").exists()

    def test_install_from_archive_binary_not_found(self, tmp_path):
        """Test installation when binary not found in archive."""
        # Create a ZIP archive without the expected binary
        archive_path = tmp_path / "terraform.zip"
        with zipfile.ZipFile(archive_path, 'w') as zf:
            zf.writestr("readme.txt", "This is a readme")
        
        dest_dir = tmp_path / "bin"
        
        with patch('wrkenv.env.operations.install.extract_archive'):
            with patch('wrkenv.env.operations.install.find_binary_in_archive', return_value=None):
                with pytest.raises(FileNotFoundError, match="Binary 'terraform' not found"):
                    install_from_archive(archive_path, dest_dir, "terraform")

    def test_cleanup_temp_files(self, tmp_path):
        """Test cleaning up temporary files."""
        # Create temp files
        temp_file = tmp_path / "temp.zip"
        temp_file.write_text("temp")
        
        temp_dir = tmp_path / "temp_extract"
        temp_dir.mkdir()
        (temp_dir / "file.txt").write_text("content")
        
        # Clean up
        cleanup_temp_files([temp_file, temp_dir])
        
        # Verify files were removed
        assert not temp_file.exists()
        assert not temp_dir.exists()

    def test_cleanup_temp_files_handles_errors(self, tmp_path):
        """Test cleanup handles errors gracefully."""
        # Create a file that doesn't exist
        nonexistent = tmp_path / "nonexistent.txt"
        
        # Should not raise exception
        cleanup_temp_files([nonexistent])
        
        # Test with permission error
        temp_file = tmp_path / "temp.txt"
        temp_file.write_text("temp")
        
        with patch('pathlib.Path.unlink', side_effect=PermissionError("Permission denied")):
            # Should not raise exception
            cleanup_temp_files([temp_file])


# 🍲🥄🧪🪄