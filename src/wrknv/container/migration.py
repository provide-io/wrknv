#
# wrknv/container/migration.py
#
"""
Container Storage Migration
===========================
Migration utilities for transitioning from old to new container storage structure.
"""

import shutil
import tarfile
from datetime import datetime
from pathlib import Path
from typing import Optional

from pyvider.telemetry import logger
from rich.console import Console


class ContainerStorageMigration:
    """Handles migration from old container storage to new structure."""
    
    def __init__(self):
        """Initialize migration handler."""
        self.console = Console()
        self.home = Path.home()
        self.wrknv_dir = self.home / ".wrknv"
        self.old_build_dir = self.wrknv_dir / "container-build"
        self.new_containers_dir = self.wrknv_dir / "containers"
    
    def needs_migration(self) -> bool:
        """Check if migration is needed.
        
        Returns:
            True if old structure exists and needs migration
        """
        return self.old_build_dir.exists()
    
    def migrate(
        self,
        container_manager,
        create_backup: bool = False,
        dry_run: bool = False,
        verbose: bool = False
    ) -> bool:
        """Migrate from old container storage structure to new.
        
        Args:
            container_manager: ContainerManager instance
            create_backup: Whether to create backup of old structure
            dry_run: Whether to perform a dry run without making changes
            verbose: Whether to print verbose output
            
        Returns:
            True if migration successful or not needed
        """
        if not self.needs_migration():
            if verbose:
                self.console.print("[green]No migration needed[/green]")
            return True
        
        if verbose:
            self.console.print("[yellow]Starting container storage migration[/yellow]")
        
        if dry_run:
            self.console.print("[cyan]DRY RUN - No changes will be made[/cyan]")
            self._print_migration_plan(container_manager, verbose)
            return True
        
        try:
            # Create backup if requested
            if create_backup:
                backup_path = self._create_backup()
                if verbose:
                    self.console.print(f"[green]Created backup: {backup_path}[/green]")
            
            # Perform migration
            if verbose:
                self.console.print("Migrating from old structure...")
            
            # Create new structure
            if verbose:
                self.console.print("Creating new directory structure...")
            container_manager._setup_storage()
            
            # Move old build content
            if self.old_build_dir.exists():
                new_build_dir = container_manager.get_container_path("build")
                if not any(new_build_dir.iterdir()):
                    if verbose:
                        self.console.print(f"Moving build files to {new_build_dir}")
                    self.copy_directory_contents(self.old_build_dir, new_build_dir)
                
                # Remove old directory
                shutil.rmtree(self.old_build_dir)
                if verbose:
                    self.console.print("[green]Removed old container-build directory[/green]")
            
            if verbose:
                self.console.print("[green]Migration completed successfully[/green]")
            
            return True
            
        except Exception as e:
            logger.error(f"Migration failed: {e}")
            if verbose:
                self.console.print(f"[red]Migration failed: {e}[/red]")
            return False
    
    def _print_migration_plan(self, container_manager, verbose: bool) -> None:
        """Print what migration would do without making changes.
        
        Args:
            container_manager: ContainerManager instance
            verbose: Whether to print verbose output
        """
        self.console.print("\n[bold]Migration Plan:[/bold]")
        
        if self.old_build_dir.exists():
            self.console.print(f"  Would migrate: {self.old_build_dir}")
            new_build = container_manager.get_container_path("build")
            self.console.print(f"  To: {new_build}")
            
            # List files that would be migrated
            if verbose:
                self.console.print("\n  Files to migrate:")
                for item in self.old_build_dir.iterdir():
                    self.console.print(f"    - {item.name}")
        
        self.console.print("\n  Would create structure:")
        container_dir = container_manager.get_container_path()
        self.console.print(f"    {container_dir}/")
        self.console.print(f"      volumes/")
        for vol in container_manager.container_config.persistent_volumes:
            self.console.print(f"        {vol}/")
        self.console.print(f"      build/")
        self.console.print(f"      logs/")
        self.console.print(f"      backups/")
    
    def _create_backup(self) -> Path:
        """Create backup of old structure before migration.
        
        Returns:
            Path to backup file
        """
        backup_dir = self.wrknv_dir / "migration-backups"
        backup_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_file = backup_dir / f"container-build-{timestamp}.tar.gz"
        
        with tarfile.open(backup_file, "w:gz") as tar:
            if self.old_build_dir.exists():
                tar.add(self.old_build_dir, arcname=self.old_build_dir.name)
        
        return backup_file
    
    def backup_directory(self, source: Path, dest: Path) -> Path:
        """Create a backup of a directory.
        
        Args:
            source: Directory to backup
            dest: Destination for backup file
            
        Returns:
            Path to created backup
        """
        with tarfile.open(dest, "w:gz") as tar:
            tar.add(source, arcname=source.name)
        return dest
    
    def copy_directory_contents(self, source: Path, dest: Path) -> None:
        """Copy contents of source directory to destination.
        
        Args:
            source: Source directory
            dest: Destination directory
        """
        dest.mkdir(parents=True, exist_ok=True)
        
        for item in source.iterdir():
            dest_item = dest / item.name
            if item.is_dir():
                shutil.copytree(item, dest_item, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest_item)
    
    def safe_move_directory(
        self,
        source: Path,
        dest: Path,
        merge: bool = False
    ) -> bool:
        """Safely move a directory with optional merging.
        
        Args:
            source: Source directory to move
            dest: Destination path
            merge: Whether to merge with existing destination
            
        Returns:
            True if successful
        """
        try:
            if dest.exists() and merge:
                # Merge contents
                self.copy_directory_contents(source, dest)
                shutil.rmtree(source)
            else:
                # Simple move
                shutil.move(str(source), str(dest))
            return True
        except Exception as e:
            logger.error(f"Failed to move directory: {e}")
            return False


# Global instance for convenient access
migrate_container_storage = ContainerStorageMigration()