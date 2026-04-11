from __future__ import annotations

from unittest.mock import patch

from provide.foundation.process import CompletedProcess, ProcessError
import pytest
from rich.console import Console

from wrknv.container.operations.build import ContainerBuilder
from wrknv.container.runtime.docker import DockerRuntime
from wrknv.wenv.schema import ContainerConfig


def make_runtime():
    return DockerRuntime(runtime_name="docker", runtime_command="docker")


def make_builder(runtime=None):
    if runtime is None:
        runtime = make_runtime()
    return ContainerBuilder(runtime=runtime, console=Console(quiet=True))


# ---------------------------------------------------------------------------
# build() — ProcessError path (lines 75-86)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerBuilderBuildErrors:
    def test_build_stream_output_process_error_no_stderr(self):
        """ProcessError with no stderr during stream build (lines 75-86)."""
        builder = make_builder()
        err = ProcessError(message="build failed")

        with patch("wrknv.container.operations.build.stream", side_effect=err):
            result = builder.build(
                dockerfile="Dockerfile",
                tag="myapp:latest",
                context=".",
                build_args=None,
                stream_output=True,
            )

        assert result is False

    def test_build_stream_output_process_error_with_stderr(self):
        """ProcessError with stderr prints extra line (line 85-86)."""
        builder = make_builder()
        err = ProcessError(message="build failed", stderr="some docker error")

        with patch("wrknv.container.operations.build.stream", side_effect=err):
            result = builder.build(
                dockerfile="Dockerfile",
                tag="myapp:latest",
                context=".",
                build_args=None,
                stream_output=True,
            )

        assert result is False

    def test_build_non_stream_process_error(self):
        """ProcessError from runtime.build_image (lines 75-86)."""
        runtime = make_runtime()
        builder = make_builder(runtime)
        err = ProcessError(message="build failed", stderr="daemon error")

        with patch("wrknv.container.runtime.docker.run", side_effect=err):
            result = builder.build(
                dockerfile="Dockerfile",
                tag="myapp:latest",
                context=".",
                build_args=None,
                stream_output=False,
            )

        assert result is False


# ---------------------------------------------------------------------------
# _build_command() — optional flags (lines 111, 114, 116, 118, 120)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerBuilderBuildCommand:
    def test_build_command_with_all_flags(self):
        """Covers no_cache, platform, pull, quiet branches (lines 111-120)."""
        builder = make_builder()
        cmd = builder._build_command(
            dockerfile="Dockerfile",
            tag="img:tag",
            context=".",
            build_args={"K": "V"},
            no_cache=True,
            platform="linux/amd64",
            pull=True,
            quiet=True,
        )

        assert "--no-cache" in cmd
        assert "--platform" in cmd
        assert "linux/amd64" in cmd
        assert "--pull" in cmd
        assert "--quiet" in cmd
        assert "--build-arg" in cmd
        assert "K=V" in cmd

    def test_build_command_no_optional_flags(self):
        """Covers the False branch for each optional flag."""
        builder = make_builder()
        cmd = builder._build_command(
            dockerfile="Dockerfile",
            tag="img:tag",
            context=".",
            build_args=None,
        )

        assert "--no-cache" not in cmd
        assert "--platform" not in cmd
        assert "--pull" not in cmd
        assert "--quiet" not in cmd


# ---------------------------------------------------------------------------
# tag_image() (lines 135-151)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerBuilderTagImage:
    def test_tag_image_success(self):
        """tag_image success path (lines 135-141). run is imported inline inside method."""
        builder = make_builder()
        with patch("provide.foundation.process.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = builder.tag_image("myapp:latest", "myapp:v1.0")

        assert result is True
        cmd = mock_run.call_args[0][0]
        assert "tag" in cmd
        assert "myapp:latest" in cmd
        assert "myapp:v1.0" in cmd

    def test_tag_image_failure(self):
        """tag_image ProcessError path (lines 143-151)."""
        builder = make_builder()
        with patch("provide.foundation.process.run", side_effect=ProcessError(message="tag failed")):
            result = builder.tag_image("myapp:latest", "myapp:v1.0")

        assert result is False


# ---------------------------------------------------------------------------
# push_image() (lines 162-175)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerBuilderPushImage:
    def test_push_image_success(self):
        """push_image success path (lines 162-170). run is imported inline inside method."""
        builder = make_builder()
        with patch("provide.foundation.process.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = builder.push_image("myapp:latest")

        assert result is True
        cmd = mock_run.call_args[0][0]
        assert "push" in cmd
        assert "myapp:latest" in cmd

    def test_push_image_failure(self):
        """push_image ProcessError path (lines 172-175)."""
        builder = make_builder()
        with patch("provide.foundation.process.run", side_effect=ProcessError(message="push failed")):
            result = builder.push_image("myapp:latest")

        assert result is False


# ---------------------------------------------------------------------------
# image_exists() (lines 198-201)
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerBuilderImageExists:
    def test_image_exists_not_in_list(self):
        """image_exists returns False when tag not in list (line 198). run imported inline."""
        builder = make_builder()
        with patch("provide.foundation.process.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=0, stdout="other:image\nanother:tag", stderr=""
            )
            result = builder.image_exists("myapp:latest")

        assert result is False

    def test_image_exists_process_error(self):
        """image_exists returns False on ProcessError (lines 200-201)."""
        builder = make_builder()
        with patch("provide.foundation.process.run", side_effect=ProcessError(message="no docker")):
            result = builder.image_exists("myapp:latest")

        assert result is False

    def test_image_exists_empty_stdout(self):
        """image_exists returns False when stdout is empty."""
        builder = make_builder()
        with patch("provide.foundation.process.run") as mock_run:
            mock_run.return_value = CompletedProcess(args=[], returncode=0, stdout="", stderr="")
            result = builder.image_exists("myapp:latest")

        assert result is False

    def test_image_exists_in_list(self):
        """image_exists returns True when tag is in list."""
        builder = make_builder()
        with patch("provide.foundation.process.run") as mock_run:
            mock_run.return_value = CompletedProcess(
                args=[], returncode=0, stdout="myapp:latest\nother:image", stderr=""
            )
            result = builder.image_exists("myapp:latest")

        assert result is True


# ---------------------------------------------------------------------------
# generate_dockerfile() — additional_packages branch + environment
# ---------------------------------------------------------------------------


@pytest.mark.container
class TestContainerBuilderGenerateDockerfile:
    def test_generate_dockerfile_with_additional_packages_and_environment(self):
        """Covers additional_packages and environment branches."""
        config = ContainerConfig(
            additional_packages=["vim", "wget"],
            environment={"MY_VAR": "hello"},
        )
        builder = make_builder()
        result = builder.generate_dockerfile(config)

        assert "vim" in result
        assert "wget" in result
        assert "ENV MY_VAR=hello" in result

    def test_generate_dockerfile_with_python_version_non_python_base(self):
        """Python install block only added when base_image is not python:*."""
        config = ContainerConfig(
            base_image="ubuntu:22.04",
            python_version="3.11",
        )
        builder = make_builder()
        result = builder.generate_dockerfile(config)

        assert "python3.11" in result

    def test_generate_dockerfile_python_base_skips_py_install(self):
        """Python install block NOT added when base_image starts with python:."""
        config = ContainerConfig(
            base_image="python:3.11-slim",
            python_version="3.11",
        )
        builder = make_builder()
        result = builder.generate_dockerfile(config)

        # Should not install python again
        assert "python3.11" not in result
