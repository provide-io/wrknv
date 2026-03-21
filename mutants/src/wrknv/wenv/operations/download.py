#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""wrknv Download Operations
====================================
Functions for downloading and verifying tool archives using Foundation's ToolDownloader."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
import pathlib
from urllib.parse import urlparse

from provide.foundation import logger
from provide.foundation.crypto import verify_file
from provide.foundation.hub import get_hub
from provide.foundation.resilience import circuit_breaker
from provide.foundation.tools.downloader import ToolDownloader
from provide.foundation.transport import UniversalClient
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


@circuit_breaker(
    failure_threshold=5,
    recovery_timeout=60.0,
    expected_exception=Exception,
)
async def download_file_async(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    progress_callback: Callable[[int, int], None] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file using Foundation's ToolDownloader with streaming.

    Uses circuit breaker to prevent repeated attempts when downloads are failing.
    After 5 failures, will fast-fail for 60 seconds before retrying.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        progress_callback: Optional callback(downloaded_bytes, total_bytes)
        checksum: Optional checksum for verification

    Raises:
        RuntimeError: If circuit breaker is open (too many recent failures)
        Exception: On download failure
    """
    logger.info(f"Downloading {url} to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            # Create ToolDownloader instance
            downloader = ToolDownloader(client)

            # Add progress callback if provided
            if progress_callback:
                downloader.add_progress_callback(progress_callback)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with progress and optional checksum verification
            await downloader.download_with_progress(url, output_path, checksum)

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        # ToolDownloader already cleans up partial downloads on failure
        raise Exception(f"Failed to download {url}: {e}") from e


def x_download_file__mutmut_orig(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, show_progress, headers, checksum=checksum))


def x_download_file__mutmut_1(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = False,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, show_progress, headers, checksum=checksum))


def x_download_file__mutmut_2(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(None)


def x_download_file__mutmut_3(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(None, output_path, show_progress, headers, checksum=checksum))


def x_download_file__mutmut_4(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, None, show_progress, headers, checksum=checksum))


def x_download_file__mutmut_5(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, None, headers, checksum=checksum))


def x_download_file__mutmut_6(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, show_progress, None, checksum=checksum))


def x_download_file__mutmut_7(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, show_progress, headers, checksum=None))


def x_download_file__mutmut_8(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(output_path, show_progress, headers, checksum=checksum))


def x_download_file__mutmut_9(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, show_progress, headers, checksum=checksum))


def x_download_file__mutmut_10(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, headers, checksum=checksum))


def x_download_file__mutmut_11(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, show_progress, checksum=checksum))


def x_download_file__mutmut_12(
    url: str,
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_file_async.

    Args:
        url: URL to download from
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_file_async(url, output_path, show_progress, headers, ))

x_download_file__mutmut_mutants : ClassVar[MutantDict] = {
'x_download_file__mutmut_1': x_download_file__mutmut_1, 
    'x_download_file__mutmut_2': x_download_file__mutmut_2, 
    'x_download_file__mutmut_3': x_download_file__mutmut_3, 
    'x_download_file__mutmut_4': x_download_file__mutmut_4, 
    'x_download_file__mutmut_5': x_download_file__mutmut_5, 
    'x_download_file__mutmut_6': x_download_file__mutmut_6, 
    'x_download_file__mutmut_7': x_download_file__mutmut_7, 
    'x_download_file__mutmut_8': x_download_file__mutmut_8, 
    'x_download_file__mutmut_9': x_download_file__mutmut_9, 
    'x_download_file__mutmut_10': x_download_file__mutmut_10, 
    'x_download_file__mutmut_11': x_download_file__mutmut_11, 
    'x_download_file__mutmut_12': x_download_file__mutmut_12
}

def download_file(*args, **kwargs):
    result = _mutmut_trampoline(x_download_file__mutmut_orig, x_download_file__mutmut_mutants, args, kwargs)
    return result 

download_file.__signature__ = _mutmut_signature(x_download_file__mutmut_orig)
x_download_file__mutmut_orig.__name__ = 'x_download_file'


async def x_download_with_mirrors_async__mutmut_orig(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_1(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = False,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_2(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(None)

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_3(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=None, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_4(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=None)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_5(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_6(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, )

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_7(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=False, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_8(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=False)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_9(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = None
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_10(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=None, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_11(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=None) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_12(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_13(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, ) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_14(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers and {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_15(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = None

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_16(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(None)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_17(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total >= 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_18(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 1:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_19(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = None
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_20(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(None, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_21(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, None)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_22(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min((downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_23(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, )
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_24(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(101, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_25(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) / total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_26(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded / 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_27(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 101) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_28(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 or logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_29(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded / (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_30(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 / 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_31(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1025 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_32(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1025) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_33(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) <= 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_34(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1025 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_35(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(None)

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_36(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(None)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_37(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(None, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_38(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, None)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_39(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_40(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, )

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_41(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum or not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_42(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_43(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(None, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_44(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, None):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_45(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_46(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, ):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_47(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(None)

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_48(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(None)

    except Exception as e:
        raise Exception(f"Failed to download from all mirrors: {e}") from e


async def x_download_with_mirrors_async__mutmut_49(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Download a file trying multiple mirror URLs until one succeeds.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification

    Raises:
        Exception: If all mirrors fail
    """
    logger.info(f"Downloading from mirrors to {output_path}")

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        hub = get_hub()
        async with UniversalClient(hub=hub, default_headers=headers or {}) as client:
            downloader = ToolDownloader(client)

            # Add logging progress callback if enabled
            if show_progress:

                def log_progress(downloaded: int, total: int) -> None:
                    if total > 0:
                        percent = min(100, (downloaded * 100) // total)
                        if downloaded % (1024 * 1024) < 1024 and logger.is_debug_enabled():  # Log every ~1MB
                            logger.debug(f"Download progress: {percent}% ({downloaded}/{total} bytes)")

                downloader.add_progress_callback(log_progress)

            # Download with mirror fallback
            await downloader.download_with_mirrors(mirrors, output_path)

            # Verify checksum if provided (mirror method doesn't support checksum param)
            if checksum and not verify_checksum(output_path, checksum):
                output_path.unlink()
                raise Exception(f"Checksum verification failed for {output_path.name}")

        logger.info(f"Successfully downloaded {output_path.name}")

    except Exception as e:
        raise Exception(None) from e

x_download_with_mirrors_async__mutmut_mutants : ClassVar[MutantDict] = {
'x_download_with_mirrors_async__mutmut_1': x_download_with_mirrors_async__mutmut_1, 
    'x_download_with_mirrors_async__mutmut_2': x_download_with_mirrors_async__mutmut_2, 
    'x_download_with_mirrors_async__mutmut_3': x_download_with_mirrors_async__mutmut_3, 
    'x_download_with_mirrors_async__mutmut_4': x_download_with_mirrors_async__mutmut_4, 
    'x_download_with_mirrors_async__mutmut_5': x_download_with_mirrors_async__mutmut_5, 
    'x_download_with_mirrors_async__mutmut_6': x_download_with_mirrors_async__mutmut_6, 
    'x_download_with_mirrors_async__mutmut_7': x_download_with_mirrors_async__mutmut_7, 
    'x_download_with_mirrors_async__mutmut_8': x_download_with_mirrors_async__mutmut_8, 
    'x_download_with_mirrors_async__mutmut_9': x_download_with_mirrors_async__mutmut_9, 
    'x_download_with_mirrors_async__mutmut_10': x_download_with_mirrors_async__mutmut_10, 
    'x_download_with_mirrors_async__mutmut_11': x_download_with_mirrors_async__mutmut_11, 
    'x_download_with_mirrors_async__mutmut_12': x_download_with_mirrors_async__mutmut_12, 
    'x_download_with_mirrors_async__mutmut_13': x_download_with_mirrors_async__mutmut_13, 
    'x_download_with_mirrors_async__mutmut_14': x_download_with_mirrors_async__mutmut_14, 
    'x_download_with_mirrors_async__mutmut_15': x_download_with_mirrors_async__mutmut_15, 
    'x_download_with_mirrors_async__mutmut_16': x_download_with_mirrors_async__mutmut_16, 
    'x_download_with_mirrors_async__mutmut_17': x_download_with_mirrors_async__mutmut_17, 
    'x_download_with_mirrors_async__mutmut_18': x_download_with_mirrors_async__mutmut_18, 
    'x_download_with_mirrors_async__mutmut_19': x_download_with_mirrors_async__mutmut_19, 
    'x_download_with_mirrors_async__mutmut_20': x_download_with_mirrors_async__mutmut_20, 
    'x_download_with_mirrors_async__mutmut_21': x_download_with_mirrors_async__mutmut_21, 
    'x_download_with_mirrors_async__mutmut_22': x_download_with_mirrors_async__mutmut_22, 
    'x_download_with_mirrors_async__mutmut_23': x_download_with_mirrors_async__mutmut_23, 
    'x_download_with_mirrors_async__mutmut_24': x_download_with_mirrors_async__mutmut_24, 
    'x_download_with_mirrors_async__mutmut_25': x_download_with_mirrors_async__mutmut_25, 
    'x_download_with_mirrors_async__mutmut_26': x_download_with_mirrors_async__mutmut_26, 
    'x_download_with_mirrors_async__mutmut_27': x_download_with_mirrors_async__mutmut_27, 
    'x_download_with_mirrors_async__mutmut_28': x_download_with_mirrors_async__mutmut_28, 
    'x_download_with_mirrors_async__mutmut_29': x_download_with_mirrors_async__mutmut_29, 
    'x_download_with_mirrors_async__mutmut_30': x_download_with_mirrors_async__mutmut_30, 
    'x_download_with_mirrors_async__mutmut_31': x_download_with_mirrors_async__mutmut_31, 
    'x_download_with_mirrors_async__mutmut_32': x_download_with_mirrors_async__mutmut_32, 
    'x_download_with_mirrors_async__mutmut_33': x_download_with_mirrors_async__mutmut_33, 
    'x_download_with_mirrors_async__mutmut_34': x_download_with_mirrors_async__mutmut_34, 
    'x_download_with_mirrors_async__mutmut_35': x_download_with_mirrors_async__mutmut_35, 
    'x_download_with_mirrors_async__mutmut_36': x_download_with_mirrors_async__mutmut_36, 
    'x_download_with_mirrors_async__mutmut_37': x_download_with_mirrors_async__mutmut_37, 
    'x_download_with_mirrors_async__mutmut_38': x_download_with_mirrors_async__mutmut_38, 
    'x_download_with_mirrors_async__mutmut_39': x_download_with_mirrors_async__mutmut_39, 
    'x_download_with_mirrors_async__mutmut_40': x_download_with_mirrors_async__mutmut_40, 
    'x_download_with_mirrors_async__mutmut_41': x_download_with_mirrors_async__mutmut_41, 
    'x_download_with_mirrors_async__mutmut_42': x_download_with_mirrors_async__mutmut_42, 
    'x_download_with_mirrors_async__mutmut_43': x_download_with_mirrors_async__mutmut_43, 
    'x_download_with_mirrors_async__mutmut_44': x_download_with_mirrors_async__mutmut_44, 
    'x_download_with_mirrors_async__mutmut_45': x_download_with_mirrors_async__mutmut_45, 
    'x_download_with_mirrors_async__mutmut_46': x_download_with_mirrors_async__mutmut_46, 
    'x_download_with_mirrors_async__mutmut_47': x_download_with_mirrors_async__mutmut_47, 
    'x_download_with_mirrors_async__mutmut_48': x_download_with_mirrors_async__mutmut_48, 
    'x_download_with_mirrors_async__mutmut_49': x_download_with_mirrors_async__mutmut_49
}

def download_with_mirrors_async(*args, **kwargs):
    result = _mutmut_trampoline(x_download_with_mirrors_async__mutmut_orig, x_download_with_mirrors_async__mutmut_mutants, args, kwargs)
    return result 

download_with_mirrors_async.__signature__ = _mutmut_signature(x_download_with_mirrors_async__mutmut_orig)
x_download_with_mirrors_async__mutmut_orig.__name__ = 'x_download_with_mirrors_async'


def x_download_with_mirrors__mutmut_orig(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, show_progress, headers, checksum))


def x_download_with_mirrors__mutmut_1(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = False,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, show_progress, headers, checksum))


def x_download_with_mirrors__mutmut_2(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(None)


def x_download_with_mirrors__mutmut_3(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(None, output_path, show_progress, headers, checksum))


def x_download_with_mirrors__mutmut_4(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, None, show_progress, headers, checksum))


def x_download_with_mirrors__mutmut_5(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, None, headers, checksum))


def x_download_with_mirrors__mutmut_6(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, show_progress, None, checksum))


def x_download_with_mirrors__mutmut_7(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, show_progress, headers, None))


def x_download_with_mirrors__mutmut_8(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(output_path, show_progress, headers, checksum))


def x_download_with_mirrors__mutmut_9(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, show_progress, headers, checksum))


def x_download_with_mirrors__mutmut_10(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, headers, checksum))


def x_download_with_mirrors__mutmut_11(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, show_progress, checksum))


def x_download_with_mirrors__mutmut_12(
    mirrors: list[str],
    output_path: pathlib.Path,
    show_progress: bool = True,
    headers: dict[str, str] | None = None,
    checksum: str | None = None,
) -> None:
    """Synchronous wrapper for download_with_mirrors_async.

    Args:
        mirrors: List of mirror URLs to try in order
        output_path: Where to save the file
        show_progress: Whether to log progress
        headers: Optional custom headers
        checksum: Optional checksum for verification
    """
    asyncio.run(download_with_mirrors_async(mirrors, output_path, show_progress, headers, ))

x_download_with_mirrors__mutmut_mutants : ClassVar[MutantDict] = {
'x_download_with_mirrors__mutmut_1': x_download_with_mirrors__mutmut_1, 
    'x_download_with_mirrors__mutmut_2': x_download_with_mirrors__mutmut_2, 
    'x_download_with_mirrors__mutmut_3': x_download_with_mirrors__mutmut_3, 
    'x_download_with_mirrors__mutmut_4': x_download_with_mirrors__mutmut_4, 
    'x_download_with_mirrors__mutmut_5': x_download_with_mirrors__mutmut_5, 
    'x_download_with_mirrors__mutmut_6': x_download_with_mirrors__mutmut_6, 
    'x_download_with_mirrors__mutmut_7': x_download_with_mirrors__mutmut_7, 
    'x_download_with_mirrors__mutmut_8': x_download_with_mirrors__mutmut_8, 
    'x_download_with_mirrors__mutmut_9': x_download_with_mirrors__mutmut_9, 
    'x_download_with_mirrors__mutmut_10': x_download_with_mirrors__mutmut_10, 
    'x_download_with_mirrors__mutmut_11': x_download_with_mirrors__mutmut_11, 
    'x_download_with_mirrors__mutmut_12': x_download_with_mirrors__mutmut_12
}

def download_with_mirrors(*args, **kwargs):
    result = _mutmut_trampoline(x_download_with_mirrors__mutmut_orig, x_download_with_mirrors__mutmut_mutants, args, kwargs)
    return result 

download_with_mirrors.__signature__ = _mutmut_signature(x_download_with_mirrors__mutmut_orig)
x_download_with_mirrors__mutmut_orig.__name__ = 'x_download_with_mirrors'


def x_verify_checksum__mutmut_orig(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, expected_checksum, algorithm)


def x_verify_checksum__mutmut_1(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "XXsha256XX") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, expected_checksum, algorithm)


def x_verify_checksum__mutmut_2(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "SHA256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, expected_checksum, algorithm)


def x_verify_checksum__mutmut_3(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(None, expected_checksum, algorithm)


def x_verify_checksum__mutmut_4(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, None, algorithm)


def x_verify_checksum__mutmut_5(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, expected_checksum, None)


def x_verify_checksum__mutmut_6(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(expected_checksum, algorithm)


def x_verify_checksum__mutmut_7(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, algorithm)


def x_verify_checksum__mutmut_8(file_path: pathlib.Path, expected_checksum: str, algorithm: str = "sha256") -> bool:
    """Verify file checksum using specified algorithm."""

    # Use foundation's verify_file which handles all the details
    return verify_file(file_path, expected_checksum, )

x_verify_checksum__mutmut_mutants : ClassVar[MutantDict] = {
'x_verify_checksum__mutmut_1': x_verify_checksum__mutmut_1, 
    'x_verify_checksum__mutmut_2': x_verify_checksum__mutmut_2, 
    'x_verify_checksum__mutmut_3': x_verify_checksum__mutmut_3, 
    'x_verify_checksum__mutmut_4': x_verify_checksum__mutmut_4, 
    'x_verify_checksum__mutmut_5': x_verify_checksum__mutmut_5, 
    'x_verify_checksum__mutmut_6': x_verify_checksum__mutmut_6, 
    'x_verify_checksum__mutmut_7': x_verify_checksum__mutmut_7, 
    'x_verify_checksum__mutmut_8': x_verify_checksum__mutmut_8
}

def verify_checksum(*args, **kwargs):
    result = _mutmut_trampoline(x_verify_checksum__mutmut_orig, x_verify_checksum__mutmut_mutants, args, kwargs)
    return result 

verify_checksum.__signature__ = _mutmut_signature(x_verify_checksum__mutmut_orig)
x_verify_checksum__mutmut_orig.__name__ = 'x_verify_checksum'


def x_download_checksum_file__mutmut_orig(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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


def x_download_checksum_file__mutmut_1(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if checksum_url:
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


def x_download_checksum_file__mutmut_2(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = None
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


def x_download_checksum_file__mutmut_3(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(None)
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


def x_download_checksum_file__mutmut_4(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = None
    if not filename:
        filename = "checksums.txt"

    checksum_path = output_dir / filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_5(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(None).name
    if not filename:
        filename = "checksums.txt"

    checksum_path = output_dir / filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_6(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(parsed_url.path).name
    if filename:
        filename = "checksums.txt"

    checksum_path = output_dir / filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_7(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(parsed_url.path).name
    if not filename:
        filename = None

    checksum_path = output_dir / filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_8(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(parsed_url.path).name
    if not filename:
        filename = "XXchecksums.txtXX"

    checksum_path = output_dir / filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_9(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(parsed_url.path).name
    if not filename:
        filename = "CHECKSUMS.TXT"

    checksum_path = output_dir / filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_10(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(parsed_url.path).name
    if not filename:
        filename = "checksums.txt"

    checksum_path = None

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_11(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
    """Download checksum file and return path."""

    if not checksum_url:
        return None

    # Parse filename from URL
    parsed_url = urlparse(checksum_url)
    filename = pathlib.Path(parsed_url.path).name
    if not filename:
        filename = "checksums.txt"

    checksum_path = output_dir * filename

    try:
        download_file(checksum_url, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_12(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        download_file(None, checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_13(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        download_file(checksum_url, None, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_14(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        download_file(checksum_url, checksum_path, show_progress=None)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_15(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        download_file(checksum_path, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_16(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        download_file(checksum_url, show_progress=False)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_17(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        download_file(checksum_url, checksum_path, )
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_18(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        download_file(checksum_url, checksum_path, show_progress=True)
        return checksum_path

    except Exception as e:
        logger.warning(f"Failed to download checksum file {checksum_url}: {e}")
        return None


def x_download_checksum_file__mutmut_19(checksum_url: str, output_dir: pathlib.Path) -> pathlib.Path | None:
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
        logger.warning(None)
        return None

x_download_checksum_file__mutmut_mutants : ClassVar[MutantDict] = {
'x_download_checksum_file__mutmut_1': x_download_checksum_file__mutmut_1, 
    'x_download_checksum_file__mutmut_2': x_download_checksum_file__mutmut_2, 
    'x_download_checksum_file__mutmut_3': x_download_checksum_file__mutmut_3, 
    'x_download_checksum_file__mutmut_4': x_download_checksum_file__mutmut_4, 
    'x_download_checksum_file__mutmut_5': x_download_checksum_file__mutmut_5, 
    'x_download_checksum_file__mutmut_6': x_download_checksum_file__mutmut_6, 
    'x_download_checksum_file__mutmut_7': x_download_checksum_file__mutmut_7, 
    'x_download_checksum_file__mutmut_8': x_download_checksum_file__mutmut_8, 
    'x_download_checksum_file__mutmut_9': x_download_checksum_file__mutmut_9, 
    'x_download_checksum_file__mutmut_10': x_download_checksum_file__mutmut_10, 
    'x_download_checksum_file__mutmut_11': x_download_checksum_file__mutmut_11, 
    'x_download_checksum_file__mutmut_12': x_download_checksum_file__mutmut_12, 
    'x_download_checksum_file__mutmut_13': x_download_checksum_file__mutmut_13, 
    'x_download_checksum_file__mutmut_14': x_download_checksum_file__mutmut_14, 
    'x_download_checksum_file__mutmut_15': x_download_checksum_file__mutmut_15, 
    'x_download_checksum_file__mutmut_16': x_download_checksum_file__mutmut_16, 
    'x_download_checksum_file__mutmut_17': x_download_checksum_file__mutmut_17, 
    'x_download_checksum_file__mutmut_18': x_download_checksum_file__mutmut_18, 
    'x_download_checksum_file__mutmut_19': x_download_checksum_file__mutmut_19
}

def download_checksum_file(*args, **kwargs):
    result = _mutmut_trampoline(x_download_checksum_file__mutmut_orig, x_download_checksum_file__mutmut_mutants, args, kwargs)
    return result 

download_checksum_file.__signature__ = _mutmut_signature(x_download_checksum_file__mutmut_orig)
x_download_checksum_file__mutmut_orig.__name__ = 'x_download_checksum_file'


def x_parse_checksum_file__mutmut_orig(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_1(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_2(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = None
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_3(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line and line.startswith("#"):
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_4(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if line or line.startswith("#"):
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_5(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(None):
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_6(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("XX#XX"):
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_7(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    break

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) >= 2:
                    checksum = parts[0]
                    filename = parts[1]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_8(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = None
                if len(parts) >= 2:
                    checksum = parts[0]
                    filename = parts[1]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_9(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) > 2:
                    checksum = parts[0]
                    filename = parts[1]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_10(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) >= 3:
                    checksum = parts[0]
                    filename = parts[1]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_11(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) >= 2:
                    checksum = None
                    filename = parts[1]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_12(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) >= 2:
                    checksum = parts[1]
                    filename = parts[1]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_13(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) >= 2:
                    checksum = parts[0]
                    filename = None

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_14(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle different checksum file formats
                parts = line.split()
                if len(parts) >= 2:
                    checksum = parts[0]
                    filename = parts[2]

                    # Remove leading '*' or other markers
                    filename = filename.lstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_15(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                    filename = None

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_16(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                    filename = filename.lstrip(None)

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_17(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                    filename = filename.rstrip("*")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_18(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                    filename = filename.lstrip("XX*XX")

                    # Match target filename
                    if filename == target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_19(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                    if filename == target_filename and filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_20(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                    if filename != target_filename or filename.endswith(target_filename):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_21(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                    if filename == target_filename or filename.endswith(None):
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_22(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                        if logger.is_debug_enabled():
                            logger.debug(None)
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_23(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(None)
        return None

    except Exception as e:
        logger.error(f"Failed to parse checksum file {checksum_path}: {e}")
        return None


def x_parse_checksum_file__mutmut_24(checksum_path: pathlib.Path, target_filename: str) -> str | None:
    """Parse checksum file to find checksum for target filename."""

    if not checksum_path.exists():
        return None

    try:
        with checksum_path.open() as f:
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
                        if logger.is_debug_enabled():
                            logger.debug(f"Found checksum for {target_filename}: {checksum}")
                        return checksum

        logger.warning(f"Checksum not found for {target_filename} in {checksum_path}")
        return None

    except Exception as e:
        logger.error(None)
        return None

x_parse_checksum_file__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_checksum_file__mutmut_1': x_parse_checksum_file__mutmut_1, 
    'x_parse_checksum_file__mutmut_2': x_parse_checksum_file__mutmut_2, 
    'x_parse_checksum_file__mutmut_3': x_parse_checksum_file__mutmut_3, 
    'x_parse_checksum_file__mutmut_4': x_parse_checksum_file__mutmut_4, 
    'x_parse_checksum_file__mutmut_5': x_parse_checksum_file__mutmut_5, 
    'x_parse_checksum_file__mutmut_6': x_parse_checksum_file__mutmut_6, 
    'x_parse_checksum_file__mutmut_7': x_parse_checksum_file__mutmut_7, 
    'x_parse_checksum_file__mutmut_8': x_parse_checksum_file__mutmut_8, 
    'x_parse_checksum_file__mutmut_9': x_parse_checksum_file__mutmut_9, 
    'x_parse_checksum_file__mutmut_10': x_parse_checksum_file__mutmut_10, 
    'x_parse_checksum_file__mutmut_11': x_parse_checksum_file__mutmut_11, 
    'x_parse_checksum_file__mutmut_12': x_parse_checksum_file__mutmut_12, 
    'x_parse_checksum_file__mutmut_13': x_parse_checksum_file__mutmut_13, 
    'x_parse_checksum_file__mutmut_14': x_parse_checksum_file__mutmut_14, 
    'x_parse_checksum_file__mutmut_15': x_parse_checksum_file__mutmut_15, 
    'x_parse_checksum_file__mutmut_16': x_parse_checksum_file__mutmut_16, 
    'x_parse_checksum_file__mutmut_17': x_parse_checksum_file__mutmut_17, 
    'x_parse_checksum_file__mutmut_18': x_parse_checksum_file__mutmut_18, 
    'x_parse_checksum_file__mutmut_19': x_parse_checksum_file__mutmut_19, 
    'x_parse_checksum_file__mutmut_20': x_parse_checksum_file__mutmut_20, 
    'x_parse_checksum_file__mutmut_21': x_parse_checksum_file__mutmut_21, 
    'x_parse_checksum_file__mutmut_22': x_parse_checksum_file__mutmut_22, 
    'x_parse_checksum_file__mutmut_23': x_parse_checksum_file__mutmut_23, 
    'x_parse_checksum_file__mutmut_24': x_parse_checksum_file__mutmut_24
}

def parse_checksum_file(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_checksum_file__mutmut_orig, x_parse_checksum_file__mutmut_mutants, args, kwargs)
    return result 

parse_checksum_file.__signature__ = _mutmut_signature(x_parse_checksum_file__mutmut_orig)
x_parse_checksum_file__mutmut_orig.__name__ = 'x_parse_checksum_file'


def x_get_filename_from_url__mutmut_orig(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_1(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = None
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_2(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(None)
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_3(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = None

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_4(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(None).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_5(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(parsed_url.path).name

    if filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_6(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = None

    return filename


def x_get_filename_from_url__mutmut_7(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) | 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_8(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(None) & 0x7FFFFFFF}"

    return filename


def x_get_filename_from_url__mutmut_9(url: str) -> str:
    """Extract filename from download URL."""
    parsed_url = urlparse(url)
    filename = pathlib.Path(parsed_url.path).name

    if not filename:
        # Fallback to generating filename from URL
        filename = f"download_{hash(url) & 2147483648}"

    return filename

x_get_filename_from_url__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_filename_from_url__mutmut_1': x_get_filename_from_url__mutmut_1, 
    'x_get_filename_from_url__mutmut_2': x_get_filename_from_url__mutmut_2, 
    'x_get_filename_from_url__mutmut_3': x_get_filename_from_url__mutmut_3, 
    'x_get_filename_from_url__mutmut_4': x_get_filename_from_url__mutmut_4, 
    'x_get_filename_from_url__mutmut_5': x_get_filename_from_url__mutmut_5, 
    'x_get_filename_from_url__mutmut_6': x_get_filename_from_url__mutmut_6, 
    'x_get_filename_from_url__mutmut_7': x_get_filename_from_url__mutmut_7, 
    'x_get_filename_from_url__mutmut_8': x_get_filename_from_url__mutmut_8, 
    'x_get_filename_from_url__mutmut_9': x_get_filename_from_url__mutmut_9
}

def get_filename_from_url(*args, **kwargs):
    result = _mutmut_trampoline(x_get_filename_from_url__mutmut_orig, x_get_filename_from_url__mutmut_mutants, args, kwargs)
    return result 

get_filename_from_url.__signature__ = _mutmut_signature(x_get_filename_from_url__mutmut_orig)
x_get_filename_from_url__mutmut_orig.__name__ = 'x_get_filename_from_url'


def x_validate_download_url__mutmut_orig(url: str) -> bool:
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


def x_validate_download_url__mutmut_1(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = None

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_2(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(None)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_3(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme and not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_4(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_5(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_6(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return True

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_7(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.upper() in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_8(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() not in ["http", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_9(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["XXhttpXX", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_10(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["HTTP", "https"]

    except Exception:
        return False


def x_validate_download_url__mutmut_11(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "XXhttpsXX"]

    except Exception:
        return False


def x_validate_download_url__mutmut_12(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "HTTPS"]

    except Exception:
        return False


def x_validate_download_url__mutmut_13(url: str) -> bool:
    """Validate that download URL is properly formatted."""

    try:
        parsed = urlparse(url)

        # Must have valid scheme and netloc
        if not parsed.scheme or not parsed.netloc:
            return False

        # Must be HTTP or HTTPS
        return parsed.scheme.lower() in ["http", "https"]

    except Exception:
        return True

x_validate_download_url__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate_download_url__mutmut_1': x_validate_download_url__mutmut_1, 
    'x_validate_download_url__mutmut_2': x_validate_download_url__mutmut_2, 
    'x_validate_download_url__mutmut_3': x_validate_download_url__mutmut_3, 
    'x_validate_download_url__mutmut_4': x_validate_download_url__mutmut_4, 
    'x_validate_download_url__mutmut_5': x_validate_download_url__mutmut_5, 
    'x_validate_download_url__mutmut_6': x_validate_download_url__mutmut_6, 
    'x_validate_download_url__mutmut_7': x_validate_download_url__mutmut_7, 
    'x_validate_download_url__mutmut_8': x_validate_download_url__mutmut_8, 
    'x_validate_download_url__mutmut_9': x_validate_download_url__mutmut_9, 
    'x_validate_download_url__mutmut_10': x_validate_download_url__mutmut_10, 
    'x_validate_download_url__mutmut_11': x_validate_download_url__mutmut_11, 
    'x_validate_download_url__mutmut_12': x_validate_download_url__mutmut_12, 
    'x_validate_download_url__mutmut_13': x_validate_download_url__mutmut_13
}

def validate_download_url(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_download_url__mutmut_orig, x_validate_download_url__mutmut_mutants, args, kwargs)
    return result 

validate_download_url.__signature__ = _mutmut_signature(x_validate_download_url__mutmut_orig)
x_validate_download_url__mutmut_orig.__name__ = 'x_validate_download_url'


# 🧰🌍🔚
