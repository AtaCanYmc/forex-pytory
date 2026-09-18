# Getting Started

This guide walks through installing `forex-pytory` and setting up your local environment.

---

## Prerequisites

- **Python**: Version 3.10 or higher.
- **Git**: Installed and configured.

---

## Installation

### Via pip (Recommended)

Install the package directly from PyPI:

```bash
pip install forex-pytory
```

To include development and documentation dependencies:

```bash
pip install "forex-pytory[dev,docs]"
```

### From Source (Development)

Clone the repository and install in editable mode:

```bash
git clone https://github.com/AtaCanYmc/forex-pytory.git
cd forex-pytory
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"
```

### Optional Extras

To install development dependencies (testing, linting) and documentation tools:

```bash
# Install with dev and documentation tools
pip install -e ".[dev,docs]"
```

Or use the provided Makefile:

```bash
make install-dev
```

---

## Verifying the Installation

After installation, verify that the CLI tool is available in your shell:

```bash
forex-scraper --help
```

You should see output detailing the available flags (`--source`, `--date`, `--format`).

To verify the MCP server binary:

```bash
forex-mcp --help
```
