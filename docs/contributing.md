# Contributing

Contributions to `forex-pytory` are welcome. Please adhere to the following workflow to ensure code quality and stability.

---

## Development Setup

1. Fork and clone the repository.
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install development dependencies using the Makefile:
   ```bash
   make install-dev
   ```

---

## Code Quality Standards

Before submitting a pull request, verify that all linters pass:

```bash
make lint
```

This runs:
- `flake8`: PEP 8 compliance checks.
- `black --check`: Code formatting verification.
- `mypy`: Static type checks.

To automatically format code to project standards:

```bash
make format
```

---

## Documentation

When updating documentation files in `docs/`:

1. Preview changes in real time:
   ```bash
   make docs-serve
   ```
2. Validate links and build output:
   ```bash
   make docs-build
   ```

---

## Pull Request Checklist

- [ ] Code follows project formatting (Black 88 character line limit).
- [ ] Type hints are provided and verified with Mypy.
- [ ] `make lint` exits cleanly with zero errors.
- [ ] Any new feature is documented in `docs/` and referenced in `README.md`.
