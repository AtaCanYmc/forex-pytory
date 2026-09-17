.DEFAULT_GOAL := help
PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

.PHONY: help install install-dev lint format test docs-serve docs-build clean

help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

install: ## Install package in editable mode
	$(PIP) install -e .

install-dev: ## Install package with development and documentation tools
	$(PIP) install -e ".[dev,docs]"

lint: ## Run code quality linters (flake8, black check, mypy)
	$(PYTHON) -m flake8 src/
	$(PYTHON) -m black --check src/
	$(PYTHON) -m mypy src/

format: ## Format codebase with Black
	$(PYTHON) -m black src/

test: ## Run unit tests with pytest
	@if [ -d "tests" ]; then \
		$(PYTHON) -m pytest tests/ --cov=src/ --cov-report=term; \
	else \
		echo "No tests directory found. Run tests after adding tests."; \
	fi

docs-serve: ## Start local MkDocs documentation server
	$(PYTHON) -m mkdocs serve

docs-build: ## Build static HTML documentation with strict validation
	$(PYTHON) -m mkdocs build --strict

clean: ## Remove build artifacts, cache files, and documentation output
	rm -rf build/ dist/ *.egg-info .eggs/
	rm -rf .pytest_cache/ .coverage coverage.xml
	rm -rf .mypy_cache/ site/ .cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
