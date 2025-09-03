#!/usr/bin/env python3
#
# wrknv/container/operations/build.py
#
"""
Container Build Operations
==========================
Build container images with streaming output.
"""

from typing import Any

from attrs import define
from provide.foundation import logger
from provide.foundation.process import ProcessError, stream_command
from rich.console import Console

from wrknv.container.runtime.base import ContainerRuntime


@define
class ContainerBuilder:
    """Handles container build operations."""
    
    runtime: ContainerRuntime
    console: Console
    
    def build(
        self,
        dockerfile: str,
        tag: str,
        context: str,
        build_args: dict[str, str] | None,
        stream_output: bool,
        **extra_options: Any,
    ) -> bool:
        """Build a container image.
        
        Args:
            dockerfile: Path to Dockerfile
            tag: Image tag
            context: Build context directory
            build_args: Build arguments
            stream_output: Whether to stream build output
            **extra_options: Runtime-specific build options
            
        Returns:
            True if build successful
        """
        try:
            if stream_output:
                # Build command for streaming
                cmd = self._build_command(
                    dockerfile=dockerfile,
                    tag=tag,
                    context=context,
                    build_args=build_args,
                    **extra_options
                )
                
                self.console.print(f"[cyan]🔨 Building image {tag}...[/cyan]")
                
                # Stream build output
                for line in stream_command(cmd):
                    self.console.print(line, end="")
                
                self.console.print(f"[green]✅ Image {tag} built successfully[/green]")
                logger.info("Image built successfully", tag=tag, dockerfile=dockerfile)
                return True
            else:
                # Use runtime's build method
                result = self.runtime.build_image(
                    dockerfile=dockerfile,
                    tag=tag,
                    context=context,
                    build_args=build_args,
                    **extra_options
                )
                
                self.console.print(f"[green]✅ Image {tag} built successfully[/green]")
                return True
                
        except ProcessError as e:
            logger.error(
                "Build failed",
                tag=tag,
                dockerfile=dockerfile,
                error=str(e),
                stderr=e.stderr,
            )
            self.console.print(f"[red]❌ Build failed: {e}[/red]")
            if e.stderr:
                self.console.print(f"[red]{e.stderr}[/red]")
            return False
    
    def _build_command(
        self,
        dockerfile: str,
        tag: str,
        context: str,
        build_args: dict[str, str] | None,
        **extra_options: Any,
    ) -> list[str]:
        """Construct build command.
        
        Args:
            dockerfile: Path to Dockerfile
            tag: Image tag
            context: Build context directory
            build_args: Build arguments
            **extra_options: Runtime-specific options
            
        Returns:
            Command list
        """
        cmd = [self.runtime.runtime_command, "build", "-f", dockerfile, "-t", tag]
        
        for key, value in (build_args or {}).items():
            cmd.extend(["--build-arg", f"{key}={value}"])
        
        if extra_options.get("no_cache"):
            cmd.append("--no-cache")
        if extra_options.get("platform"):
            cmd.extend(["--platform", extra_options["platform"]])
        if extra_options.get("pull"):
            cmd.append("--pull")
        if extra_options.get("quiet"):
            cmd.append("--quiet")
        
        cmd.append(context)
        return cmd
    
    def tag_image(self, source_tag: str, target_tag: str) -> bool:
        """Tag an existing image.
        
        Args:
            source_tag: Source image tag
            target_tag: Target image tag
            
        Returns:
            True if successful
        """
        try:
            from provide.foundation.process import run_command
            
            result = run_command(
                [self.runtime.runtime_command, "tag", source_tag, target_tag],
                check=True
            )
            
            logger.info("Image tagged", source=source_tag, target=target_tag)
            self.console.print(f"[green]✅ Tagged {source_tag} as {target_tag}[/green]")
            return True
            
        except ProcessError as e:
            logger.error(
                "Failed to tag image",
                source=source_tag,
                target=target_tag,
                error=str(e),
            )
            self.console.print(f"[red]❌ Failed to tag image: {e}[/red]")
            return False
    
    def push_image(self, tag: str) -> bool:
        """Push image to registry.
        
        Args:
            tag: Image tag to push
            
        Returns:
            True if successful
        """
        try:
            from provide.foundation.process import run_command
            
            self.console.print(f"[cyan]📤 Pushing image {tag}...[/cyan]")
            
            result = run_command(
                [self.runtime.runtime_command, "push", tag],
                check=True
            )
            
            logger.info("Image pushed", tag=tag)
            self.console.print(f"[green]✅ Pushed {tag} successfully[/green]")
            return True
            
        except ProcessError as e:
            logger.error("Failed to push image", tag=tag, error=str(e))
            self.console.print(f"[red]❌ Failed to push image: {e}[/red]")
            return False