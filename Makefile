.DEFAULT_GOAL := help
PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

.PHONY: help install install-dev lint format format-check typecheck test check security build docs-serve docs-build clean

help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

install: ## Install package in editable mode
	$(PIP) install -e .

install-dev: ## Install package with development tools
	$(PIP) install -e ".[dev]"

lint: ## Run flake8
	$(PYTHON) -m flake8 src/ tests/

format-check: ## Verify Black formatting
	$(PYTHON) -m black --check src/ tests/

typecheck: ## Run mypy
	$(PYTHON) -m mypy src/ tests/

check: lint format-check typecheck test ## Run all CI checks

format: ## Format codebase with Black
	$(PYTHON) -m black src/ tests/

test: ## Run unit tests with pytest
	@if [ -d "tests" ]; then \
		$(PYTHON) -m pytest tests/ --cov=src/ --cov-report=term; \
	else \
		echo "No tests directory found. Run tests after adding tests."; \
	fi

build: ## Build sdist and wheel
	$(PYTHON) -m build

security: ## Run security audits with Bandit and pip-audit
	$(PYTHON) -m bandit -r src/
	$(PYTHON) -m pip_audit

docs-serve: ## Start local static documentation server
	$(PYTHON) -m http.server 8000 --directory site

docs-build: ## Verify static documentation site assets
	@for f in index.html style.css app.js; do test -f site/$$f || { echo "Missing site/$$f"; exit 1; }; done; echo "Static documentation site assets verified in site/."

clean: ## Remove build artifacts and caches
	rm -rf build/ dist/ *.egg-info .eggs/
	rm -rf .pytest_cache/ .coverage coverage.xml
	rm -rf .mypy_cache/ .ruff_cache/ .cache/
	find . -type d -name "__pycache__" -not -path "./.venv/*" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
