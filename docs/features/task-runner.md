# Task Runner Feature Specification

## Overview

The task runner feature enables wrknv to execute predefined tasks from `wrknv.toml` configuration files, providing a unified interface for common development operations across all provide.io repositories.

## Goals

1. **Single Command Interface**: Developers run tasks via `wrknv run <task-name>`
2. **TOML-Based Configuration**: Tasks defined in existing `wrknv.toml` files
3. **Simple Syntax**: Both simple string commands and complex task definitions
4. **Composability**: Tasks can depend on or run other tasks
5. **Discoverability**: `wrknv tasks` lists all available tasks

## Non-Goals (Future Work)

- Workspace-level task orchestration (Phase 2)
- Parallel task execution (Phase 2)
- Task result caching (Phase 3)
- Remote task execution (Phase 3)

## Configuration Format

### Simple Tasks

```toml
[tasks]
test = "uv run pytest tests/"
lint = "uv run ruff check src/ tests/"
format = "uv run ruff format src/ tests/"
```

### Complex Tasks

```toml
[tasks.build]
run = "uv build"
description = "Build Python package"
env = { PYTHONPATH = "src" }
working_dir = "."

[tasks.test-verbose]
run = "uv run pytest tests/ -vvv --tb=long"
description = "Run tests with verbose output"
depends_on = ["format", "lint"]
```

### Composite Tasks

```toml
[tasks.quality]
run = ["lint", "typecheck"]
description = "Run all quality checks"

[tasks.ci]
run = ["quality", "test", "build"]
description = "Complete CI pipeline"
```

## Command Interface

### Run Tasks

```bash
# Run single task
wrknv run test

# Run multiple tasks sequentially
wrknv run lint format typecheck

# Show what would be executed
wrknv run build --dry-run

# Override environment variables
wrknv run test --env PYTEST_WORKERS=4 --env DEBUG=1

# Show task information
wrknv run test --info
```

### List Tasks

```bash
# List all tasks
wrknv tasks

# List with details
wrknv tasks --verbose
```

## Task Execution Model

### Execution Flow

1. Load `wrknv.toml` from current directory
2. Parse `[tasks]` section
3. Resolve task name to `TaskConfig`
4. If composite task, recursively resolve subtasks
5. Execute command(s) in subprocess
6. Capture stdout/stderr
7. Report results

### Environment

- Inherits current shell environment
- Merges task-specific `env` variables
- Supports `--env` CLI overrides

### Working Directory

- Defaults to repository root (directory containing `wrknv.toml`)
- Configurable via `working_dir` in task config

### Error Handling

- Non-zero exit code stops execution
- For composite tasks, first failure stops remaining tasks
- Error output displayed to stderr
- Exit code propagated to shell

## Data Models

### TaskConfig

```python
@define(frozen=True)
class TaskConfig:
    name: str
    run: str | list[str]  # Command or list of task names
    description: str | None = None
    env: dict[str, str] = field(factory=dict)
    depends_on: list[str] = field(factory=list)  # Future: dependency execution
    working_dir: str | None = None

    @property
    def is_composite(self) -> bool:
        """Check if task runs other tasks."""
        return isinstance(self.run, list)
```

### TaskResult

```python
@define
class TaskResult:
    task: TaskConfig
    success: bool
    exit_code: int
    stdout: str
    stderr: str
    duration: float
```

## Test Scenarios

### Basic Execution

- ✅ Load simple task from TOML
- ✅ Execute command and capture output
- ✅ Report success/failure
- ✅ Propagate exit codes

### Composite Tasks

- ✅ Execute multiple tasks in sequence
- ✅ Stop on first failure
- ✅ Aggregate results

### Environment Handling

- ✅ Inherit shell environment
- ✅ Merge task-specific environment
- ✅ Apply CLI overrides

### Error Cases

- ✅ Task not found
- ✅ Invalid TOML syntax
- ✅ Command execution failure
- ✅ Missing wrknv.toml file

### CLI Behavior

- ✅ `wrknv run <task>` executes task
- ✅ `wrknv run <task> --dry-run` shows command without executing
- ✅ `wrknv run <task> --info` displays task information
- ✅ `wrknv tasks` lists all tasks
- ✅ Exit codes match command results

## Examples

### Developer Workflow

```bash
# Morning: run tests
wrknv run test

# Before commit: quality checks
wrknv run quality

# Full CI locally
wrknv run ci

# Rebuild
wrknv run clean build
```

### Sample wrknv.toml

```toml
# wrknv/wrknv.toml

[tasks]
# Simple tasks
test = "uv run pytest tests/ -v"
lint = "uv run ruff check src/ tests/"
format = "uv run ruff format src/ tests/"
typecheck = "uv run mypy src/ --ignore-missing-imports"
clean = "rm -rf dist/ build/ *.egg-info .pytest_cache .mypy_cache .ruff_cache"

# Complex task with environment
[tasks.test-coverage]
run = "uv run pytest tests/ --cov=src/wrknv --cov-report=term-missing"
description = "Run tests with coverage report"
env = { COVERAGE_CORE = "sysmon" }

# Composite tasks
[tasks.quality]
run = ["lint", "typecheck"]
description = "Run all quality checks"

[tasks.ci]
run = ["quality", "test-coverage", "build"]
description = "Complete CI pipeline"

# Demo task
[tasks.hello]
run = "echo '🎉 Hello from wrknv! The work environment is ready to work! 🎉'"
description = "A friendly greeting from your work environment"
```

## Success Criteria

1. **Functional**: Can run simple and composite tasks
2. **Tested**: >90% code coverage with TDD-written tests
3. **Typed**: Passes mypy strict mode
4. **Documented**: Examples in README
5. **Demo**: `wrknv run hello` works and is delightful

## Future Enhancements (Not in MVP)

- Dependency execution (`depends_on` field)
- Parallel execution
- Task result caching
- Watch mode
- Interactive task selection
- Workspace-level coordination
