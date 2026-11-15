# Contributing

Contributions to `forex-pytory` are welcome. Please adhere to the following workflow to ensure code quality, deterministic releases, and repository stability.

For full governance specifications, refer to [CONTRIBUTING.md](https://github.com/AtaCanYmc/forex-pytory/blob/main/CONTRIBUTING.md).

---

## Development Setup

1. Fork and clone the repository.
2. Set up the development environment using `uv` (recommended) or `venv`:
   ```bash
   # Using uv
   uv sync --all-extras

   # Or using Python venv
   python3 -m venv .venv
   source .venv/bin/activate
   make install-dev
   ```

---

## Commit Message Format

This repository enforces [Conventional Commits](https://www.conventionalcommits.org/):

- `feat`: New features or capabilities.
- `fix`: Bug fixes.
- `docs`: Documentation updates.
- `refactor`: Internal code refinements.
- `test`: Adding or updating test cases.
- `chore`: Tooling, CI, or dependency updates.

---

## Code Quality Standards

Before submitting a pull request, verify that all linters and tests pass:

```bash
# Run flake8, black check, and mypy
make lint

# Run unit tests
make test
```

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
2. Validate links and build output with strict validation:
   ```bash
   make docs-build
   ```

---

## Pull Request Checklist

- [ ] Commits adhere to Conventional Commits specification.
- [ ] Code follows project formatting (Black 88 character line limit).
- [ ] Type hints are provided and verified with Mypy (`mypy src/ tests/`).
- [ ] `make lint` and `make test` exit cleanly with zero errors.
- [ ] Any new feature is documented in `docs/` and referenced in `README.md`.
