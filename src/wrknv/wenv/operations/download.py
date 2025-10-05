#
# wrknv/workenv/operations/download.py
#
"""
wrknv Download Operations
====================================
Functions for downloading and verifying tool archives using foundation transport.
"""
from __future__ import annotations


import asyncio
import pathlib
from collections.abc import Callable
from urllib.parse import urlparse

from provide.foundation import logger
from provide.foundation.crypto import verify_file
from provide.foundation.transport import UniversalClient


async def download_file_async(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    progress_callback: Callable[[int, int], None] | None = None,
) -> None:
    """Download a file using foundation transport with streaming.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        progress_callback: Optional callback(downloaded_bytes, total_bytes)
    """
    logger.info(f"Downloading {url} to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    downloaded = 0
    total_size = 0

    try:
        async with UniversalClient(default_headers=headers or {}) as client:
            # Try to get total size from HEAD request
            try:
                head_response = await client.head(url)
                if "content-length" in head_response.headers:
                    total_size = int(head_response.headers["content-length"])
            except Exception:
                pass  # Size unknown, continue without it

            # Stream download
            with open(output_path, "wb") as f:
                async for chunk in client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Progress reporting
                    if show_progress and total_size > 0:
                        percent = min(100, (downloaded * 100) // total_size)
                        if downloaded % (1024 * 1024) < len(chunk):  # Log every ~1MB
                            logger.debug(
                                f"Download progress: {percent}% ({downloaded}/{total_size} bytes)"
                            )

                    # Custom callback
                    if progress_callback and total_size > 0:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {output_path.name} ({downloaded} bytes)")

    except Exception as e:
        # Clean up partial download
        if output_path.exists():
            output_path.unlink()
        raise Exception(f"Failed to download {url}: {e}")


def download_file(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
    """
    asyncio.run(download_file_async(url, output_path, show_progress, headers))


def verify_checksum(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, expected_checksum, algorithm)


def download_checksum_file(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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


def parse_checksum_file(checksum_path: pathlib.Path, target_filename: str) -> str | None:
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
                    if filename == target_filename or filename.endswith(target_filename):
                        logger.debug(f"Found checksum for {target_filename}: {checksum}")
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
