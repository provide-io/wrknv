#
# wrkenv/workenv/operations/download.py
#
"""
TofuSoup Workenv Download Operations
====================================
Functions for downloading and verifying tool archives.
"""

import hashlib
import pathlib
import urllib.request
from urllib.parse import urlparse

from pyvider.telemetry import logger


def download_file(
    url: str, output_path: pathlib.Path, show_progress: bool = True
) -> None:
    """Download a file from URL to output path with optional progress display."""

    logger.info(f"Downloading {url} to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    def progress_hook(block_num: int, block_size: int, total_size: int) -> None:
        """Progress hook for urllib.request.urlretrieve."""
        if show_progress and total_size > 0:
            downloaded = block_num * block_size
            percent = min(100, (downloaded * 100) // total_size)
            if block_num % 50 == 0:  # Only log every 50 blocks to avoid spam
                logger.debug(
                    f"Download progress: {percent}% ({downloaded}/{total_size} bytes)"
                )

    try:
        urllib.request.urlretrieve(url, output_path, reporthook=progress_hook)
        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        # Clean up partial download
        if output_path.exists():
            output_path.unlink()
        raise Exception(f"Failed to download {url}: {e}")


def verify_checksum(
    file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256"
) -> bool:
    """Verify file checksum using specified algorithm."""

    if not file_path.exists():
        logger.error(f"File not found for checksum verification: {file_path}")
        return False

    logger.debug(f"Verifying {algorithm} checksum for {file_path}")

    try:
        # Create hash object
        if algorithm.lower() == "sha256":
            hasher = hashlib.sha256()
        elif algorithm.lower() == "sha1":
            hasher = hashlib.sha1()
        elif algorithm.lower() == "md5":
            hasher = hashlib.md5()
        else:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")

        # Read file in chunks to handle large files
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)

        actual_checksum = hasher.hexdigest()

        # Compare checksums (case-insensitive)
        if actual_checksum.lower() == expected_checksum.lower():
            logger.debug(f"Checksum verification successful for {file_path}")
            return True
        else:
            logger.error(
                f"Checksum mismatch for {file_path}: expected {expected_checksum}, got {actual_checksum}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to verify checksum for {file_path}: {e}")
        return False


def download_checksum_file(
    checksum_url: str, output_dir: pathlib.Path
) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(parsed_url.path).name
    if not filename:
        filename = "checksums.txt"

    checksum_path = output_dir / filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def parse_checksum_file(
    checksum_path: pathlib.Path, target_filename: str
) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with open(checksum_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) >= 2:
                    checksum = parts[0]
                    filename = parts[1]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(
                        target_filename
                    ):
                        logger.debug(
                            f"Found checksum for {target_filename}: {checksum}"
                        )
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def get_filename_from_url(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 0x7FFFFFFF}"

    return filename


def validate_download_url(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return False


# 🍲🥄📄🪄
