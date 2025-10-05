"""
Workspace Manager
================
Manage multi-repo workspaces with configuration synchronization.
"""

from __future__ import annotations

import json
import tomllib
from pathlib import Path
from typing import Any

from provide.foundation import logger

from .discovery import WorkspaceDiscovery
from .schema import WorkspaceConfig, RepoConfig, TemplateSource
from .sync import WorkspaceSync


class WorkspaceManager:
    """Manage multi-repo workspaces."""

    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()
        self.config_dir = self.root / ".wrknv"
        self.config_path = self.config_dir / "workspace.toml"
        self.discovery = WorkspaceDiscovery(self.root)

    def init_workspace(
        self, template_source: str | None = None, auto_discover: bool = True
    ) -> WorkspaceConfig:
        """Initialize workspace in current directory."""
        logger.info("🚀 Initializing workspace", root=str(self.root))

        # Create .wrknv directory
        self.config_dir.mkdir(exist_ok=True)

        # Auto-discover repositories if requested
        repos = []
        if auto_discover:
            discovered = self.discovery.discover_repos()
            repos = [
                RepoConfig(
                    path=repo.path,
                    name=repo.name or repo.path.name,
                    type=repo.detected_type or "unknown",
                    template_profile=self._get_default_profile(repo.detected_type),
                    features=self._get_default_features(repo.detected_type),
                )
                for repo in discovered
            ]
            logger.info("📋 Auto-discovered repositories", count=len(repos))

        # Set up template source
        source = None
        if template_source:
            source = TemplateSource(
                type="local" if Path(template_source).exists() else "git",
                location=template_source,
            )

        # Create workspace config
        config = WorkspaceConfig(
            root=self.root,
            repos=repos,
            template_source=source,
            global_standards=self._get_default_standards(),
        )

        # Save configuration
        self.save_config(config)

        logger.success("✅ Workspace initialized", repos=len(repos))
        return config

    def load_config(self) -> WorkspaceConfig | None:
        """Load workspace configuration."""
        if not self.config_path.exists():
            return None

        try:
            with open(self.config_path, "rb") as f:
                data = tomllib.load(f)
            return WorkspaceConfig.from_dict(data)

        except Exception as e:
            logger.error("❌ Failed to load workspace config", error=str(e))
            return None

    def save_config(self, config: WorkspaceConfig):
        """Save workspace configuration."""
        try:
            # Convert to TOML format
            toml_content = self._dict_to_toml(config.to_dict())
            self.config_path.write_text(toml_content)
            logger.debug("💾 Workspace config saved", path=str(self.config_path))

        except Exception as e:
            logger.error("❌ Failed to save workspace config", error=str(e))
            raise

    def add_repo(
        self,
        repo_path: Path | str,
        name: str | None = None,
        repo_type: str | None = None,
        template_profile: str | None = None,
    ) -> WorkspaceConfig:
        """Add repository to workspace."""
        repo_path = Path(repo_path)
        if not repo_path.exists():
            raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

        # Analyze repository
        repo_info = self.discovery.analyze_repo(repo_path)

        # Create repo config
        repo_config = RepoConfig(
            path=repo_path,
            name=name or repo_info.name or repo_path.name,
            type=repo_type or repo_info.detected_type or "unknown",
            template_profile=template_profile or self._get_default_profile(repo_info.detected_type),
            features=self._get_default_features(repo_info.detected_type),
        )

        # Load current config and add repo
        config = self.load_config()
        if config is None:
            config = self.init_workspace(auto_discover=False)

        updated_config = config.add_repo(repo_config)
        self.save_config(updated_config)

        logger.success("✅ Repository added to workspace", name=repo_config.name)
        return updated_config

    def remove_repo(self, name: str) -> WorkspaceConfig:
        """Remove repository from workspace."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        updated_config = config.remove_repo(name)
        self.save_config(updated_config)

        logger.success("✅ Repository removed from workspace", name=name)
        return updated_config

    async def sync_all(self, dry_run: bool = False) -> dict[str, Any]:
        """Sync configurations across all repos."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return await sync.sync_all(dry_run=dry_run)

    async def sync_repo(self, name: str, dry_run: bool = False) -> dict[str, Any]:
        """Sync configuration for specific repository."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        repo = config.find_repo(name)
        if repo is None:
            raise ValueError(f"Repository not found in workspace: {name}")

        sync = WorkspaceSync(config)
        return await sync.sync_repo(repo, dry_run=dry_run)

    def check_drift(self) -> dict[str, Any]:
        """Check for configuration drift."""
        config = self.load_config()
        if config is None:
            raise RuntimeError("No workspace configuration found")

        sync = WorkspaceSync(config)
        return sync.check_drift()

    def get_workspace_status(self) -> dict[str, Any]:
        """Get comprehensive workspace status."""
        config = self.load_config()
        if config is None:
            return {"error": "No workspace configuration found"}

        summary = self.discovery.get_workspace_summary()
        issues = self.discovery.validate_workspace_structure(self.root)

        return {
            "root": str(self.root),
            "config_path": str(self.config_path),
            "repos_configured": len(config.repos),
            "repos_discovered": summary["total_repos"],
            "type_distribution": summary["type_distribution"],
            "issues": issues,
            "sync_strategy": config.sync_strategy,
            "template_source": config.template_source.to_dict() if config.template_source else None,
        }

    def _get_default_profile(self, repo_type: str | None) -> str:
        """Get default template profile for repository type."""
        profiles = {
            "foundation": "foundation-based",
            "foundation-based": "foundation-based",
            "provider": "pyvider-plugin",
            "pyvider-plugin": "pyvider-plugin",
            "testkit": "testkit-extension",
            "packaging": "standalone",
        }
        return profiles.get(repo_type or "unknown", "standalone")

    def _get_default_features(self, repo_type: str | None) -> list[str]:
        """Get default features for repository type."""
        base_features = ["pyproject", "claude", "gitignore"]

        type_features = {
            "foundation-based": base_features + ["coverage"],
            "pyvider-plugin": base_features + ["coverage"],
            "testkit": base_features + ["coverage"],
        }

        return type_features.get(repo_type or "unknown", base_features)

    def _get_default_standards(self) -> dict[str, Any]:
        """Get default global standards."""
        return {
            "python_version": "3.11",
            "ruff_line_length": 111,
            "authors": [{"name": "Tim Perkins", "email": "code@tim.life"}],
            "maintainers": [{"name": "provide.io", "email": "code@provide.io"}],
            "license": "Apache-2.0",
            "development_status": "3 - Alpha",
        }

    def _dict_to_toml(self, data: dict[str, Any]) -> str:
        """Convert dictionary to TOML string."""
        try:
            import tomli_w

            return tomli_w.dumps(data)
        except ImportError:
            # Fallback to basic TOML generation
            return self._basic_toml_dump(data)

    def _basic_toml_dump(self, data: dict[str, Any], section: str = "") -> str:
        """Basic TOML generation fallback."""
        lines = []

        # Handle top-level values first
        for key, value in data.items():
            if not isinstance(value, (dict, list)):
                if isinstance(value, str):
                    lines.append(f'{key} = "{value}"')
                else:
                    lines.append(f"{key} = {json.dumps(value)}")

        # Handle sections
        for key, value in data.items():
            if isinstance(value, dict):
                section_name = f"{section}.{key}" if section else key
                lines.append(f"\n[{section_name}]")
                lines.append(self._basic_toml_dump(value, section_name))

            elif isinstance(value, list) and value and isinstance(value[0], dict):
                # Handle array of tables
                for item in value:
                    section_name = f"{section}.{key}" if section else key
                    lines.append(f"\n[[{section_name}]]")
                    lines.append(self._basic_toml_dump(item, ""))

        return "\n".join(lines)
