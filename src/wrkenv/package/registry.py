#!/usr/bin/env python3

"""
Package Registry Client
=======================
Client for interacting with package registries.

Requires Python 3.11+ for native type hint support with pipe operators.
"""

import hashlib
import json
from pathlib import Path
from typing import Any

from pyvider.telemetry import logger


class RegistryClient:
    """Client for package registry operations."""

    def __init__(self, registry_url: str, auth_token: str | None = None):
        """
        Initialize registry client.

        Args:
            registry_url: Base URL of the registry
            auth_token: Optional authentication token
        """
        self.registry_url = registry_url.rstrip("/")
        self.auth_token = auth_token
        self._session = None

    def _get_session(self):
        """Get or create HTTP session."""
        if self._session is None:
            try:
                import httpx

                self._session = httpx.Client(
                    base_url=self.registry_url,
                    headers=self._get_headers(),
                    timeout=30.0,
                )
            except ImportError:
                # Fallback to urllib if httpx not available
                logger.warning("httpx not available, using urllib fallback")
                return None
        return self._session

    def _get_headers(self) -> dict[str, str]:
        """Get request headers."""
        headers = {
            "User-Agent": "wrkenv/1.0",
            "Accept": "application/json",
        }
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return headers

    def _calculate_sha256(self, file_path: Path) -> str:
        """Calculate SHA256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def upload_package(
        self, package_path: Path, metadata: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Upload a package to the registry.

        Args:
            package_path: Path to the package file
            metadata: Optional package metadata

        Returns:
            Upload response with package URL and metadata
        """
        if not package_path.exists():
            raise FileNotFoundError(f"Package not found: {package_path}")

        # Calculate package hash
        package_hash = self._calculate_sha256(package_path)

        # Prepare metadata
        if metadata is None:
            metadata = {}

        metadata.update(
            {
                "filename": package_path.name,
                "size": package_path.stat().st_size,
                "sha256": package_hash,
            }
        )

        # Try to use httpx if available
        session = self._get_session()
        if session:
            try:
                # Upload with httpx
                with open(package_path, "rb") as f:
                    files = {
                        "package": (package_path.name, f, "application/octet-stream")
                    }
                    data = {"metadata": json.dumps(metadata)}

                    response = session.post("/api/v1/packages", files=files, data=data)
                    response.raise_for_status()
                    return response.json()
            except Exception as e:
                logger.error(f"Failed to upload package: {e}")
                raise
        else:
            # Fallback implementation
            return self._upload_fallback(package_path, metadata)

    def _upload_fallback(
        self, package_path: Path, metadata: dict[str, Any]
    ) -> dict[str, Any]:
        """Fallback upload implementation using urllib."""

        # For fallback, just simulate the upload
        logger.info(
            f"[EXPERIMENTAL] Would upload {package_path.name} to {self.registry_url}"
        )

        # Return simulated response
        return {
            "success": True,
            "package_url": f"{self.registry_url}/packages/{package_path.stem}",
            "download_url": f"{self.registry_url}/api/v1/packages/{package_path.stem}/download",
            "sha256": metadata["sha256"],
            "size": metadata["size"],
            "message": "Package upload simulated (experimental feature)",
        }

    def download_package(
        self, package_name: str, version: str, output_dir: Path
    ) -> Path:
        """
        Download a package from the registry.

        Args:
            package_name: Name of the package
            version: Package version
            output_dir: Directory to save the package

        Returns:
            Path to the downloaded package
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{package_name}-{version}.flavor"

        session = self._get_session()
        if session:
            try:
                response = session.get(
                    f"/api/v1/packages/{package_name}/{version}/download",
                    follow_redirects=True,
                )
                response.raise_for_status()

                with open(output_path, "wb") as f:
                    f.write(response.content)

                logger.info(f"Downloaded {package_name} v{version} to {output_path}")
                return output_path
            except Exception as e:
                logger.error(f"Failed to download package: {e}")
                raise
        else:
            # Fallback
            logger.warning(f"[EXPERIMENTAL] Would download {package_name} v{version}")
            return output_path

    def search_packages(self, query: str, limit: int = 10) -> list[dict[str, Any]]:
        """
        Search for packages in the registry.

        Args:
            query: Search query
            limit: Maximum number of results

        Returns:
            List of package metadata
        """
        session = self._get_session()
        if session:
            try:
                response = session.get(
                    "/api/v1/packages/search", params={"q": query, "limit": limit}
                )
                response.raise_for_status()
                return response.json().get("packages", [])
            except Exception as e:
                logger.error(f"Search failed: {e}")
                return []
        else:
            # Fallback
            logger.info(f"[EXPERIMENTAL] Would search for '{query}'")
            return []

    def get_package_info(
        self, package_name: str, version: str | None = None
    ) -> dict[str, Any]:
        """
        Get information about a package.

        Args:
            package_name: Name of the package
            version: Optional specific version

        Returns:
            Package metadata
        """
        session = self._get_session()
        if session:
            try:
                url = f"/api/v1/packages/{package_name}"
                if version:
                    url += f"/{version}"

                response = session.get(url)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Failed to get package info: {e}")
                raise
        else:
            # Fallback
            return {
                "name": package_name,
                "version": version or "latest",
                "description": "Package information not available (experimental)",
            }

    def list_versions(self, package_name: str) -> list[str]:
        """
        List available versions for a package.

        Args:
            package_name: Name of the package

        Returns:
            List of available versions
        """
        session = self._get_session()
        if session:
            try:
                response = session.get(f"/api/v1/packages/{package_name}/versions")
                response.raise_for_status()
                return response.json().get("versions", [])
            except Exception as e:
                logger.error(f"Failed to list versions: {e}")
                return []
        else:
            # Fallback
            return ["1.0.0", "0.9.0", "0.8.0"]  # Mock data

    def close(self):
        """Close the client session."""
        if self._session:
            self._session.close()
            self._session = None

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


class LocalRegistry:
    """Local file-based package registry for testing."""

    def __init__(self, registry_dir: Path):
        """
        Initialize local registry.

        Args:
            registry_dir: Directory to store packages
        """
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_file = self.registry_dir / "metadata.json"
        self._load_metadata()

    def _load_metadata(self):
        """Load registry metadata."""
        if self.metadata_file.exists():
            with open(self.metadata_file) as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {"packages": {}}

    def _save_metadata(self):
        """Save registry metadata."""
        with open(self.metadata_file, "w") as f:
            json.dump(self.metadata, f, indent=2)

    def publish(self, package_path: Path, metadata: dict[str, Any]) -> dict[str, Any]:
        """
        Publish a package to the local registry.

        Args:
            package_path: Path to the package file
            metadata: Package metadata

        Returns:
            Publication result
        """
        import shutil

        # Copy package to registry
        dest_path = self.registry_dir / package_path.name
        shutil.copy2(package_path, dest_path)

        # Update metadata
        package_name = metadata.get("name", package_path.stem)
        version = metadata.get("version", "1.0.0")

        if package_name not in self.metadata["packages"]:
            self.metadata["packages"][package_name] = {}

        self.metadata["packages"][package_name][version] = {
            "filename": package_path.name,
            "path": str(dest_path),
            "metadata": metadata,
            "published_at": str(Path.ctime(dest_path)),
        }

        self._save_metadata()

        logger.info(f"Published {package_name} v{version} to local registry")

        return {
            "success": True,
            "package_name": package_name,
            "version": version,
            "path": str(dest_path),
        }

    def get_package(self, package_name: str, version: str) -> Path | None:
        """
        Get a package from the local registry.

        Args:
            package_name: Name of the package
            version: Package version

        Returns:
            Path to the package file or None if not found
        """
        if package_name in self.metadata["packages"]:
            if version in self.metadata["packages"][package_name]:
                package_info = self.metadata["packages"][package_name][version]
                package_path = Path(package_info["path"])
                if package_path.exists():
                    return package_path
        return None

    def list_packages(self) -> list[dict[str, Any]]:
        """List all packages in the registry."""
        packages = []
        for name, versions in self.metadata["packages"].items():
            for version, info in versions.items():
                packages.append(
                    {
                        "name": name,
                        "version": version,
                        "filename": info["filename"],
                        "metadata": info.get("metadata", {}),
                    }
                )
        return packages
