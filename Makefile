# Makefile (DEPRECATED)
# ⚠️  This Makefile is deprecated and maintained only for backward compatibility
# ⚠️  Please use 'we' commands instead:
#
#     make test     →  we test
#     make lint     →  we lint
#     make quality  →  we quality
#
# To see all available tasks: we tasks
# To learn more: docs/features/task-system.md

.PHONY: help test lint format quality build clean

# Colors for deprecation warnings
YELLOW := \033[0;33m
NC := \033[0m

help: ## Show this help (DEPRECATED: use 'we tasks')
	@echo '$(YELLOW)⚠️  DEPRECATED: This Makefile is deprecated. Use "we tasks" instead.$(NC)'
	@echo ''
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'
	@echo ''
	@echo '$(YELLOW)Migration: Replace "make <target>" with "we <target>"$(NC)'

test: ## Run tests (DEPRECATED: use 'we test')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we test" instead of "make test"$(NC)'
	@we run test

lint: ## Run linter (DEPRECATED: use 'we lint')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we lint" instead of "make lint"$(NC)'
	@we run lint

format: ## Format code (DEPRECATED: use 'we format')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we format" instead of "make format"$(NC)'
	@we run format

typecheck: ## Type check (DEPRECATED: use 'we typecheck')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we typecheck" instead of "make typecheck"$(NC)'
	@we run typecheck

quality: ## Run quality checks (DEPRECATED: use 'we quality')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we quality" instead of "make quality"$(NC)'
	@we run quality

build: ## Build package (DEPRECATED: use 'we build')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we build" instead of "make build"$(NC)'
	@we run build

clean: ## Clean artifacts (DEPRECATED: use 'we clean')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we clean" instead of "make clean"$(NC)'
	@we run clean

setup: ## Setup environment (DEPRECATED: use 'we setup')
	@echo '$(YELLOW)⚠️  DEPRECATED: Use "we setup" instead of "make setup"$(NC)'
	@we run setup

.DEFAULT_GOAL := help
