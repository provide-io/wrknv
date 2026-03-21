#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""Tests for wrknv error classes."""

from __future__ import annotations

from provide.testkit import FoundationTestCase

from wrknv.errors import (
    CommandNotFoundError,
    ConfigurationError,
    ContainerAlreadyExistsError,
    ContainerBuildError,
    ContainerError,
    ContainerNotFoundError,
    ContainerNotRunningError,
    ContainerRuntimeError,
    DependencyError,
    ImageNotFoundError,
    NetworkError,
    PackageError,
    ProfileError,
    TaskError,
    TaskExecutionError,
    TaskNotFoundError,
    TaskTimeoutError,
    ToolNotFoundError,
    ValidationError,
    VolumeNotFoundError,
    WorkenvError,
    WrkenvError,
    WrkenvPermissionError,
)


class TestWrkenvError(FoundationTestCase):
    def test_basic_message(self) -> None:
        err = WrkenvError("something went wrong")
        assert err.message == "something went wrong"
        assert err.hint is None
        assert err.exit_code == 1

    def test_str_without_hint(self) -> None:
        err = WrkenvError("something went wrong")
        assert str(err) == "something went wrong"

    def test_str_with_hint(self) -> None:
        err = WrkenvError("something went wrong", hint="try this")
        s = str(err)
        assert "something went wrong" in s
        assert "try this" in s

    def test_custom_exit_code(self) -> None:
        err = WrkenvError("fatal", exit_code=2)
        assert err.exit_code == 2

    def test_hint_stored(self) -> None:
        err = WrkenvError("msg", hint="do this")
        assert err.hint == "do this"


class TestConfigurationError(FoundationTestCase):
    def test_without_line_number(self) -> None:
        err = ConfigurationError("bad config")
        assert "bad config" in err.message
        assert err.line_number is None

    def test_with_line_number(self) -> None:
        err = ConfigurationError("bad value", line_number=42)
        assert "42" in err.message
        assert "bad value" in err.message
        assert err.line_number == 42

    def test_with_hint(self) -> None:
        err = ConfigurationError("bad config", hint="check your TOML")
        assert err.hint == "check your TOML"

    def test_is_wrkenv_error(self) -> None:
        err = ConfigurationError("bad config")
        assert isinstance(err, WrkenvError)


class TestValidationError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ValidationError("invalid field")
        assert "invalid field" in err.message

    def test_inherits_configuration_error(self) -> None:
        err = ValidationError("invalid field")
        assert isinstance(err, ConfigurationError)

    def test_inherits_wrkenv_error(self) -> None:
        err = ValidationError("invalid field")
        assert isinstance(err, WrkenvError)

    def test_with_line_number(self) -> None:
        err = ValidationError("bad value", line_number=10)
        assert "10" in err.message
        assert err.line_number == 10


class TestProfileError(FoundationTestCase):
    def test_default_message(self) -> None:
        err = ProfileError("staging")
        assert "staging" in str(err)
        assert err.profile_name == "staging"
        assert err.hint is None

    def test_explicit_message(self) -> None:
        err = ProfileError("staging", message="profile is broken")
        assert "profile is broken" in err.message
        assert err.profile_name == "staging"

    def test_with_available_profiles(self) -> None:
        err = ProfileError("staging", available_profiles=["dev", "prod"])
        assert "dev" in err.hint
        assert "prod" in err.hint

    def test_without_available_profiles(self) -> None:
        err = ProfileError("staging")
        assert err.hint is None


class TestToolNotFoundError(FoundationTestCase):
    def test_without_version(self) -> None:
        err = ToolNotFoundError("terraform")
        assert "terraform" in str(err)
        assert err.tool == "terraform"
        assert err.version is None

    def test_with_version(self) -> None:
        err = ToolNotFoundError("terraform", version="1.5.0")
        assert "terraform" in str(err)
        assert "1.5.0" in str(err)
        assert err.version == "1.5.0"

    def test_without_available_versions(self) -> None:
        err = ToolNotFoundError("terraform")
        assert err.context.get("hint") is None

    def test_with_available_versions_five_or_fewer(self) -> None:
        versions = ["1.3.0", "1.4.0", "1.5.0"]
        err = ToolNotFoundError("terraform", available_versions=versions)
        assert "1.3.0" in err.context["hint"]
        assert "1.5.0" in err.context["hint"]
        assert "..." not in err.context["hint"]

    def test_with_available_versions_more_than_five(self) -> None:
        versions = ["1.1.0", "1.2.0", "1.3.0", "1.4.0", "1.5.0", "1.6.0"]
        err = ToolNotFoundError("terraform", available_versions=versions)
        assert "..." in err.context["hint"]
        assert "1.1.0" in err.context["hint"]


class TestNetworkError(FoundationTestCase):
    def test_without_url(self) -> None:
        err = NetworkError("connection refused")
        assert "connection refused" in err.message
        assert err.url is None
        assert err.hint is not None

    def test_with_url(self) -> None:
        err = NetworkError("timeout", url="https://example.com/file.zip")
        assert "https://example.com/file.zip" in err.message
        assert "https://example.com/file.zip" in err.hint
        assert err.url == "https://example.com/file.zip"

    def test_hint_contains_connection_advice(self) -> None:
        err = NetworkError("connection refused")
        assert "internet connection" in err.hint


class TestWrkenvPermissionError(FoundationTestCase):
    def test_default_operation(self) -> None:
        err = WrkenvPermissionError("/etc/hosts")
        assert "/etc/hosts" in err.message
        assert "access" in err.message
        assert err.path == "/etc/hosts"

    def test_explicit_operation(self) -> None:
        err = WrkenvPermissionError("/etc/hosts", operation="write")
        assert "write" in err.message
        assert "/etc/hosts" in err.message

    def test_hint_contains_path(self) -> None:
        err = WrkenvPermissionError("/etc/hosts")
        assert "/etc/hosts" in err.hint


class TestDependencyError(FoundationTestCase):
    def test_git_dep(self) -> None:
        err = DependencyError(["git"])
        assert "git" in err.hint
        assert "git-scm.com" in err.hint
        assert "git" in err.missing_deps

    def test_curl_dep(self) -> None:
        err = DependencyError(["curl"])
        assert "curl" in err.hint

    def test_docker_dep(self) -> None:
        err = DependencyError(["docker"])
        assert "docker" in err.hint
        assert "docker.com" in err.hint

    def test_python3_dep(self) -> None:
        err = DependencyError(["python3"])
        assert "python3" in err.hint
        assert "python.org" in err.hint

    def test_unknown_dep(self) -> None:
        err = DependencyError(["myunknowntool"])
        assert "myunknowntool" in err.hint
        assert "package manager" in err.hint

    def test_without_required_for(self) -> None:
        err = DependencyError(["git"])
        assert "required for" not in err.message

    def test_with_required_for(self) -> None:
        err = DependencyError(["git"], required_for="version control")
        assert "version control" in err.message
        assert "required for" in err.message

    def test_multiple_deps(self) -> None:
        err = DependencyError(["git", "curl"])
        assert "git" in err.message
        assert "curl" in err.message
        assert err.missing_deps == ["git", "curl"]


class TestCommandNotFoundError(FoundationTestCase):
    def test_without_similar_commands(self) -> None:
        err = CommandNotFoundError("wroknv")
        assert "wroknv" in err.message
        assert err.hint is None
        assert err.command == "wroknv"

    def test_with_similar_commands(self) -> None:
        err = CommandNotFoundError("wroknv", similar_commands=["wrknv", "wrkenv"])
        assert "wrknv" in err.hint
        assert "wrkenv" in err.hint
        assert "Did you mean" in err.hint


class TestWorkenvError(FoundationTestCase):
    def test_without_workenv_path(self) -> None:
        err = WorkenvError("workenv broken")
        assert "workenv broken" in err.message
        assert err.hint is None
        assert err.workenv_path is None

    def test_with_workenv_path(self) -> None:
        err = WorkenvError("workenv broken", workenv_path="/project/workenv")
        assert "/project/workenv" in err.hint
        assert err.workenv_path == "/project/workenv"

    def test_is_wrkenv_error(self) -> None:
        err = WorkenvError("workenv broken")
        assert isinstance(err, WrkenvError)


class TestPackageError(FoundationTestCase):
    def test_without_package_name(self) -> None:
        err = PackageError("package error occurred")
        assert "package error occurred" in str(err)
        assert err.package_name is None

    def test_with_package_name(self) -> None:
        err = PackageError("package error occurred", package_name="requests")
        assert err.package_name == "requests"

    def test_with_hint(self) -> None:
        err = PackageError("package error occurred", hint="reinstall")
        assert err.context.get("hint") is not None


class TestContainerError(FoundationTestCase):
    def test_no_hint_no_name(self) -> None:
        err = ContainerError("container failed")
        assert "container failed" in err.message
        assert err.container_name is None
        assert "Docker" in err.hint

    def test_with_container_name(self) -> None:
        err = ContainerError("container failed", container_name="myapp")
        assert "myapp" in err.hint
        assert err.container_name == "myapp"

    def test_with_explicit_hint(self) -> None:
        err = ContainerError("container failed", hint="check logs")
        assert err.hint == "check logs"

    def test_is_wrkenv_error(self) -> None:
        err = ContainerError("container failed")
        assert isinstance(err, WrkenvError)


class TestContainerNotFoundError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ContainerNotFoundError("myapp")
        assert "myapp" in str(err)
        assert err.container_name == "myapp"
        assert "docker ps" in err.context["hint"]


class TestContainerNotRunningError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ContainerNotRunningError("myapp")
        assert "myapp" in str(err)
        assert err.container_name == "myapp"
        assert "docker start" in err.context["hint"]
        assert "myapp" in err.context["hint"]


class TestContainerAlreadyExistsError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ContainerAlreadyExistsError("myapp")
        assert "myapp" in str(err)
        assert err.container_name == "myapp"
        assert "docker rm" in err.context["hint"]
        assert "myapp" in err.context["hint"]


class TestImageNotFoundError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ImageNotFoundError("ubuntu:22.04")
        assert "ubuntu:22.04" in str(err)
        assert err.image_name == "ubuntu:22.04"
        assert "docker pull" in err.context["hint"]
        assert "ubuntu:22.04" in err.context["hint"]


class TestVolumeNotFoundError(FoundationTestCase):
    def test_basic(self) -> None:
        err = VolumeNotFoundError("mydata")
        assert "mydata" in str(err)
        assert err.volume_name == "mydata"
        assert "docker volume ls" in err.context["hint"]


class TestContainerRuntimeError(FoundationTestCase):
    def test_without_reason(self) -> None:
        err = ContainerRuntimeError("docker")
        assert "docker" in str(err)
        assert err.runtime == "docker"
        assert err.reason is None

    def test_with_reason(self) -> None:
        err = ContainerRuntimeError("docker", reason="daemon not running")
        assert "daemon not running" in str(err)
        assert err.reason == "daemon not running"

    def test_hint_contains_docker(self) -> None:
        err = ContainerRuntimeError("docker")
        assert "Docker" in err.context["hint"]


class TestContainerBuildError(FoundationTestCase):
    def test_without_reason(self) -> None:
        err = ContainerBuildError("myapp:latest")
        assert "myapp:latest" in str(err)
        assert err.image_tag == "myapp:latest"
        assert err.reason is None

    def test_with_reason(self) -> None:
        err = ContainerBuildError("myapp:latest", reason="syntax error in Dockerfile")
        assert "syntax error in Dockerfile" in str(err)
        assert err.reason == "syntax error in Dockerfile"

    def test_hint(self) -> None:
        err = ContainerBuildError("myapp:latest")
        assert "Dockerfile" in err.context["hint"]


class TestTaskError(FoundationTestCase):
    def test_basic(self) -> None:
        err = TaskError("task failed")
        assert "task failed" in err.message
        assert err.task_name is None

    def test_with_task_name(self) -> None:
        err = TaskError("task failed", task_name="build")
        assert err.task_name == "build"

    def test_with_hint(self) -> None:
        err = TaskError("task failed", hint="check config")
        assert err.hint == "check config"

    def test_is_wrkenv_error(self) -> None:
        err = TaskError("task failed")
        assert isinstance(err, WrkenvError)


class TestTaskNotFoundError(FoundationTestCase):
    def test_without_available_tasks(self) -> None:
        err = TaskNotFoundError("deploy")
        assert "deploy" in str(err)
        assert err.task_name == "deploy"
        assert err.context.get("hint") is None

    def test_with_available_tasks_five_or_fewer(self) -> None:
        err = TaskNotFoundError("deploy", available_tasks=["build", "test", "lint"])
        assert "build" in err.context["hint"]
        assert "..." not in err.context["hint"]

    def test_with_available_tasks_more_than_five(self) -> None:
        tasks = ["build", "test", "lint", "deploy", "release", "clean"]
        err = TaskNotFoundError("publish", available_tasks=tasks)
        assert "..." in err.context["hint"]
        assert "build" in err.context["hint"]


class TestTaskExecutionError(FoundationTestCase):
    def test_without_stderr(self) -> None:
        err = TaskExecutionError("build", exit_code=1)
        assert "build" in str(err)
        assert "1" in str(err)
        assert err.task_name == "build"
        assert err.exit_code == 1
        assert err.stderr is None
        assert err.context.get("hint") is None

    def test_with_short_stderr(self) -> None:
        err = TaskExecutionError("build", exit_code=2, stderr="compilation error")
        assert "compilation error" in err.context["hint"]
        assert err.stderr == "compilation error"

    def test_with_long_stderr(self) -> None:
        long_stderr = "x" * 300
        err = TaskExecutionError("build", exit_code=1, stderr=long_stderr)
        assert "..." in err.context["hint"]
        assert len(err.context["hint"]) <= 300

    def test_retry_possible_false_by_default(self) -> None:
        err = TaskExecutionError("build", exit_code=1)
        assert err.context["runtime.retry_possible"] is False

    def test_retry_possible_true(self) -> None:
        err = TaskExecutionError("build", exit_code=1, retry_possible=True)
        assert err.context["runtime.retry_possible"] is True


class TestTaskTimeoutError(FoundationTestCase):
    def test_basic(self) -> None:
        err = TaskTimeoutError("build", timeout=30.0)
        assert "build" in str(err)
        assert "30" in str(err)
        assert err.task_name == "build"
        assert err.timeout == 30.0

    def test_hint_contains_doubled_timeout(self) -> None:
        err = TaskTimeoutError("build", timeout=30.0)
        assert "60" in err.context["hint"]
        assert "build" in err.context["hint"]

    def test_hint_format(self) -> None:
        err = TaskTimeoutError("deploy", timeout=120.0)
        assert "240" in err.context["hint"]
        assert "deploy" in err.context["hint"]


class TestInheritance(FoundationTestCase):
    def test_validation_error_is_configuration_error(self) -> None:
        err = ValidationError("bad value")
        assert isinstance(err, ConfigurationError)

    def test_validation_error_is_wrkenv_error(self) -> None:
        err = ValidationError("bad value")
        assert isinstance(err, WrkenvError)

    def test_workenv_error_is_wrkenv_error(self) -> None:
        err = WorkenvError("env broken")
        assert isinstance(err, WrkenvError)

    def test_container_error_is_wrkenv_error(self) -> None:
        err = ContainerError("container failed")
        assert isinstance(err, WrkenvError)

    def test_task_error_is_wrkenv_error(self) -> None:
        err = TaskError("task failed")
        assert isinstance(err, WrkenvError)

    def test_network_error_is_wrkenv_error(self) -> None:
        err = NetworkError("connection refused")
        assert isinstance(err, WrkenvError)

    def test_dependency_error_is_wrkenv_error(self) -> None:
        err = DependencyError(["git"])
        assert isinstance(err, WrkenvError)

    def test_profile_error_is_wrkenv_error(self) -> None:
        err = ProfileError("staging")
        assert isinstance(err, WrkenvError)

# 🧰🌍🔚
