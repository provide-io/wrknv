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
        self.assertEqual(err.message, "something went wrong")
        self.assertIsNone(err.hint)
        self.assertEqual(err.exit_code, 1)

    def test_str_without_hint(self) -> None:
        err = WrkenvError("something went wrong")
        self.assertEqual(str(err), "something went wrong")

    def test_str_with_hint(self) -> None:
        err = WrkenvError("something went wrong", hint="try this")
        self.assertIn("something went wrong", str(err))
        self.assertIn("try this", str(err))

    def test_custom_exit_code(self) -> None:
        err = WrkenvError("fatal", exit_code=2)
        self.assertEqual(err.exit_code, 2)

    def test_hint_stored(self) -> None:
        err = WrkenvError("msg", hint="do this")
        self.assertEqual(err.hint, "do this")


class TestConfigurationError(FoundationTestCase):
    def test_without_line_number(self) -> None:
        err = ConfigurationError("bad config")
        self.assertIn("bad config", err.message)
        self.assertIsNone(err.line_number)

    def test_with_line_number(self) -> None:
        err = ConfigurationError("bad value", line_number=42)
        self.assertIn("42", err.message)
        self.assertIn("bad value", err.message)
        self.assertEqual(err.line_number, 42)

    def test_with_hint(self) -> None:
        err = ConfigurationError("bad config", hint="check your TOML")
        self.assertEqual(err.hint, "check your TOML")

    def test_is_wrkenv_error(self) -> None:
        err = ConfigurationError("bad config")
        self.assertIsInstance(err, WrkenvError)


class TestValidationError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ValidationError("invalid field")
        self.assertIn("invalid field", err.message)

    def test_inherits_configuration_error(self) -> None:
        err = ValidationError("invalid field")
        self.assertIsInstance(err, ConfigurationError)

    def test_inherits_wrkenv_error(self) -> None:
        err = ValidationError("invalid field")
        self.assertIsInstance(err, WrkenvError)

    def test_with_line_number(self) -> None:
        err = ValidationError("bad value", line_number=10)
        self.assertIn("10", err.message)
        self.assertEqual(err.line_number, 10)


class TestProfileError(FoundationTestCase):
    def test_default_message(self) -> None:
        err = ProfileError("staging")
        self.assertIn("staging", str(err))
        self.assertEqual(err.profile_name, "staging")
        self.assertIsNone(err.hint)

    def test_explicit_message(self) -> None:
        err = ProfileError("staging", message="profile is broken")
        self.assertIn("profile is broken", err.message)
        self.assertEqual(err.profile_name, "staging")

    def test_with_available_profiles(self) -> None:
        err = ProfileError("staging", available_profiles=["dev", "prod"])
        self.assertIn("dev", err.hint)
        self.assertIn("prod", err.hint)

    def test_without_available_profiles(self) -> None:
        err = ProfileError("staging")
        self.assertIsNone(err.hint)


class TestToolNotFoundError(FoundationTestCase):
    def test_without_version(self) -> None:
        err = ToolNotFoundError("terraform")
        self.assertIn("terraform", str(err))
        self.assertEqual(err.tool, "terraform")
        self.assertIsNone(err.version)

    def test_with_version(self) -> None:
        err = ToolNotFoundError("terraform", version="1.5.0")
        self.assertIn("terraform", str(err))
        self.assertIn("1.5.0", str(err))
        self.assertEqual(err.version, "1.5.0")

    def test_without_available_versions(self) -> None:
        err = ToolNotFoundError("terraform")
        self.assertIsNone(err.hint)

    def test_with_available_versions_five_or_fewer(self) -> None:
        versions = ["1.3.0", "1.4.0", "1.5.0"]
        err = ToolNotFoundError("terraform", available_versions=versions)
        self.assertIn("1.3.0", err.hint)
        self.assertIn("1.5.0", err.hint)
        self.assertNotIn("...", err.hint)

    def test_with_available_versions_more_than_five(self) -> None:
        versions = ["1.1.0", "1.2.0", "1.3.0", "1.4.0", "1.5.0", "1.6.0"]
        err = ToolNotFoundError("terraform", available_versions=versions)
        self.assertIn("...", err.hint)
        self.assertIn("1.1.0", err.hint)


class TestNetworkError(FoundationTestCase):
    def test_without_url(self) -> None:
        err = NetworkError("connection refused")
        self.assertIn("connection refused", err.message)
        self.assertIsNone(err.url)
        self.assertIsNotNone(err.hint)

    def test_with_url(self) -> None:
        err = NetworkError("timeout", url="https://example.com/file.zip")
        self.assertIn("https://example.com/file.zip", err.message)
        self.assertIn("https://example.com/file.zip", err.hint)
        self.assertEqual(err.url, "https://example.com/file.zip")

    def test_hint_contains_connection_advice(self) -> None:
        err = NetworkError("connection refused")
        self.assertIn("internet connection", err.hint)


class TestWrkenvPermissionError(FoundationTestCase):
    def test_default_operation(self) -> None:
        err = WrkenvPermissionError("/etc/hosts")
        self.assertIn("/etc/hosts", err.message)
        self.assertIn("access", err.message)
        self.assertEqual(err.path, "/etc/hosts")

    def test_explicit_operation(self) -> None:
        err = WrkenvPermissionError("/etc/hosts", operation="write")
        self.assertIn("write", err.message)
        self.assertIn("/etc/hosts", err.message)

    def test_hint_contains_path(self) -> None:
        err = WrkenvPermissionError("/etc/hosts")
        self.assertIn("/etc/hosts", err.hint)


class TestDependencyError(FoundationTestCase):
    def test_git_dep(self) -> None:
        err = DependencyError(["git"])
        self.assertIn("git", err.hint)
        self.assertIn("git-scm.com", err.hint)
        self.assertIn("git", err.missing_deps)

    def test_curl_dep(self) -> None:
        err = DependencyError(["curl"])
        self.assertIn("curl", err.hint)

    def test_docker_dep(self) -> None:
        err = DependencyError(["docker"])
        self.assertIn("docker", err.hint)
        self.assertIn("docker.com", err.hint)

    def test_python3_dep(self) -> None:
        err = DependencyError(["python3"])
        self.assertIn("python3", err.hint)
        self.assertIn("python.org", err.hint)

    def test_unknown_dep(self) -> None:
        err = DependencyError(["myunknowntool"])
        self.assertIn("myunknowntool", err.hint)
        self.assertIn("package manager", err.hint)

    def test_without_required_for(self) -> None:
        err = DependencyError(["git"])
        self.assertNotIn("required for", err.message)

    def test_with_required_for(self) -> None:
        err = DependencyError(["git"], required_for="version control")
        self.assertIn("version control", err.message)
        self.assertIn("required for", err.message)

    def test_multiple_deps(self) -> None:
        err = DependencyError(["git", "curl"])
        self.assertIn("git", err.message)
        self.assertIn("curl", err.message)
        self.assertEqual(err.missing_deps, ["git", "curl"])


class TestCommandNotFoundError(FoundationTestCase):
    def test_without_similar_commands(self) -> None:
        err = CommandNotFoundError("wroknv")
        self.assertIn("wroknv", err.message)
        self.assertIsNone(err.hint)
        self.assertEqual(err.command, "wroknv")

    def test_with_similar_commands(self) -> None:
        err = CommandNotFoundError("wroknv", similar_commands=["wrknv", "wrkenv"])
        self.assertIn("wrknv", err.hint)
        self.assertIn("wrkenv", err.hint)
        self.assertIn("Did you mean", err.hint)


class TestWorkenvError(FoundationTestCase):
    def test_without_workenv_path(self) -> None:
        err = WorkenvError("workenv broken")
        self.assertIn("workenv broken", err.message)
        self.assertIsNone(err.hint)
        self.assertIsNone(err.workenv_path)

    def test_with_workenv_path(self) -> None:
        err = WorkenvError("workenv broken", workenv_path="/project/workenv")
        self.assertIn("/project/workenv", err.hint)
        self.assertEqual(err.workenv_path, "/project/workenv")

    def test_is_wrkenv_error(self) -> None:
        err = WorkenvError("workenv broken")
        self.assertIsInstance(err, WrkenvError)


class TestPackageError(FoundationTestCase):
    def test_without_package_name(self) -> None:
        err = PackageError("package error occurred")
        self.assertIn("package error occurred", str(err))
        self.assertIsNone(err.package_name)

    def test_with_package_name(self) -> None:
        err = PackageError("package error occurred", package_name="requests")
        self.assertEqual(err.package_name, "requests")

    def test_with_hint(self) -> None:
        err = PackageError("package error occurred", hint="reinstall")
        self.assertIsNotNone(err.hint)


class TestContainerError(FoundationTestCase):
    def test_no_hint_no_name(self) -> None:
        err = ContainerError("container failed")
        self.assertIn("container failed", err.message)
        self.assertIsNone(err.container_name)
        self.assertIn("Docker", err.hint)

    def test_with_container_name(self) -> None:
        err = ContainerError("container failed", container_name="myapp")
        self.assertIn("myapp", err.hint)
        self.assertEqual(err.container_name, "myapp")

    def test_with_explicit_hint(self) -> None:
        err = ContainerError("container failed", hint="check logs")
        self.assertEqual(err.hint, "check logs")

    def test_is_wrkenv_error(self) -> None:
        err = ContainerError("container failed")
        self.assertIsInstance(err, WrkenvError)


class TestContainerNotFoundError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ContainerNotFoundError("myapp")
        self.assertIn("myapp", str(err))
        self.assertEqual(err.container_name, "myapp")
        self.assertIn("docker ps", err.hint)


class TestContainerNotRunningError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ContainerNotRunningError("myapp")
        self.assertIn("myapp", str(err))
        self.assertEqual(err.container_name, "myapp")
        self.assertIn("docker start", err.hint)
        self.assertIn("myapp", err.hint)


class TestContainerAlreadyExistsError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ContainerAlreadyExistsError("myapp")
        self.assertIn("myapp", str(err))
        self.assertEqual(err.container_name, "myapp")
        self.assertIn("docker rm", err.hint)
        self.assertIn("myapp", err.hint)


class TestImageNotFoundError(FoundationTestCase):
    def test_basic(self) -> None:
        err = ImageNotFoundError("ubuntu:22.04")
        self.assertIn("ubuntu:22.04", str(err))
        self.assertEqual(err.image_name, "ubuntu:22.04")
        self.assertIn("docker pull", err.hint)
        self.assertIn("ubuntu:22.04", err.hint)


class TestVolumeNotFoundError(FoundationTestCase):
    def test_basic(self) -> None:
        err = VolumeNotFoundError("mydata")
        self.assertIn("mydata", str(err))
        self.assertEqual(err.volume_name, "mydata")
        self.assertIn("docker volume ls", err.hint)


class TestContainerRuntimeError(FoundationTestCase):
    def test_without_reason(self) -> None:
        err = ContainerRuntimeError("docker")
        self.assertIn("docker", str(err))
        self.assertEqual(err.runtime, "docker")
        self.assertIsNone(err.reason)

    def test_with_reason(self) -> None:
        err = ContainerRuntimeError("docker", reason="daemon not running")
        self.assertIn("daemon not running", str(err))
        self.assertEqual(err.reason, "daemon not running")

    def test_hint_contains_docker(self) -> None:
        err = ContainerRuntimeError("docker")
        self.assertIn("Docker", err.hint)


class TestContainerBuildError(FoundationTestCase):
    def test_without_reason(self) -> None:
        err = ContainerBuildError("myapp:latest")
        self.assertIn("myapp:latest", str(err))
        self.assertEqual(err.image_tag, "myapp:latest")
        self.assertIsNone(err.reason)

    def test_with_reason(self) -> None:
        err = ContainerBuildError("myapp:latest", reason="syntax error in Dockerfile")
        self.assertIn("syntax error in Dockerfile", str(err))
        self.assertEqual(err.reason, "syntax error in Dockerfile")

    def test_hint(self) -> None:
        err = ContainerBuildError("myapp:latest")
        self.assertIn("Dockerfile", err.hint)


class TestTaskError(FoundationTestCase):
    def test_basic(self) -> None:
        err = TaskError("task failed")
        self.assertIn("task failed", err.message)
        self.assertIsNone(err.task_name)

    def test_with_task_name(self) -> None:
        err = TaskError("task failed", task_name="build")
        self.assertEqual(err.task_name, "build")

    def test_with_hint(self) -> None:
        err = TaskError("task failed", hint="check config")
        self.assertEqual(err.hint, "check config")

    def test_is_wrkenv_error(self) -> None:
        err = TaskError("task failed")
        self.assertIsInstance(err, WrkenvError)


class TestTaskNotFoundError(FoundationTestCase):
    def test_without_available_tasks(self) -> None:
        err = TaskNotFoundError("deploy")
        self.assertIn("deploy", str(err))
        self.assertEqual(err.task_name, "deploy")
        self.assertIsNone(err.hint)

    def test_with_available_tasks_five_or_fewer(self) -> None:
        err = TaskNotFoundError("deploy", available_tasks=["build", "test", "lint"])
        self.assertIn("build", err.hint)
        self.assertNotIn("...", err.hint)

    def test_with_available_tasks_more_than_five(self) -> None:
        tasks = ["build", "test", "lint", "deploy", "release", "clean"]
        err = TaskNotFoundError("publish", available_tasks=tasks)
        self.assertIn("...", err.hint)
        self.assertIn("build", err.hint)


class TestTaskExecutionError(FoundationTestCase):
    def test_without_stderr(self) -> None:
        err = TaskExecutionError("build", exit_code=1)
        self.assertIn("build", str(err))
        self.assertIn("1", str(err))
        self.assertEqual(err.task_name, "build")
        self.assertEqual(err.exit_code, 1)
        self.assertIsNone(err.stderr)
        self.assertIsNone(err.hint)

    def test_with_short_stderr(self) -> None:
        err = TaskExecutionError("build", exit_code=2, stderr="compilation error")
        self.assertIn("compilation error", err.hint)
        self.assertEqual(err.stderr, "compilation error")

    def test_with_long_stderr(self) -> None:
        long_stderr = "x" * 300
        err = TaskExecutionError("build", exit_code=1, stderr=long_stderr)
        self.assertIn("...", err.hint)
        self.assertLessEqual(len(err.hint), 300)

    def test_retry_possible_default(self) -> None:
        err = TaskExecutionError("build", exit_code=1)
        self.assertFalse(err.retry_possible)

    def test_retry_possible_true(self) -> None:
        err = TaskExecutionError("build", exit_code=1, retry_possible=True)
        self.assertTrue(err.retry_possible)


class TestTaskTimeoutError(FoundationTestCase):
    def test_basic(self) -> None:
        err = TaskTimeoutError("build", timeout=30.0)
        self.assertIn("build", str(err))
        self.assertIn("30", str(err))
        self.assertEqual(err.task_name, "build")
        self.assertEqual(err.timeout, 30.0)

    def test_hint_contains_doubled_timeout(self) -> None:
        err = TaskTimeoutError("build", timeout=30.0)
        self.assertIn("60", err.hint)
        self.assertIn("build", err.hint)

    def test_hint_format(self) -> None:
        err = TaskTimeoutError("deploy", timeout=120.0)
        self.assertIn("240", err.hint)
        self.assertIn("deploy", err.hint)


class TestInheritance(FoundationTestCase):
    def test_validation_error_is_configuration_error(self) -> None:
        err = ValidationError("bad value")
        self.assertIsInstance(err, ConfigurationError)

    def test_validation_error_is_wrkenv_error(self) -> None:
        err = ValidationError("bad value")
        self.assertIsInstance(err, WrkenvError)

    def test_workenv_error_is_wrkenv_error(self) -> None:
        err = WorkenvError("env broken")
        self.assertIsInstance(err, WrkenvError)

    def test_container_error_is_wrkenv_error(self) -> None:
        err = ContainerError("container failed")
        self.assertIsInstance(err, WrkenvError)

    def test_task_error_is_wrkenv_error(self) -> None:
        err = TaskError("task failed")
        self.assertIsInstance(err, WrkenvError)

    def test_network_error_is_wrkenv_error(self) -> None:
        err = NetworkError("connection refused")
        self.assertIsInstance(err, WrkenvError)

    def test_dependency_error_is_wrkenv_error(self) -> None:
        err = DependencyError(["git"])
        self.assertIsInstance(err, WrkenvError)

    def test_profile_error_is_wrkenv_error(self) -> None:
        err = ProfileError("staging")
        self.assertIsInstance(err, WrkenvError)


# 🧰🌍🔚
