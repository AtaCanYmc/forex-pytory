# Contributing to forex-pytory

Thank you for your interest in contributing. Please adhere to the following guidelines to maintain code quality, deterministic releases, and repository governance.

---

## Code of Conduct & Anti-Slop Policy

- Maintain technical precision and minimalism.
- Do not introduce AI boilerplate, buzzwords, or unverified claims.
- Every change must include a verifiable test or reproduction step.

---

## Development Setup

1. Clone your fork of the repository:
   ```bash
   git clone https://github.com/AtaCanYmc/forex-pytory.git
   cd forex-pytory
   ```

2. Set up the development environment using `uv` (recommended) or `venv`:
   ```bash
   # Using uv
   uv sync --all-extras

   # Or using standard venv and Makefile
   python3 -m venv .venv
   source .venv/bin/activate
   make install-dev
   ```

---

## Git Workflow & Branching

Create dedicated feature or fix branches branching off `main`:

```bash
git checkout -b feat/your-feature-name
# or
git checkout -b fix/issue-description
```

---

## Commit Message Format

This repository strictly enforces [Conventional Commits](https://www.conventionalcommits.org/) to power automated CHANGELOG generation and semantic releases via Release Please.

Format: `<type>(<scope>): <subject>`

Allowed types:
- `feat`: New feature or capability
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding or correcting tests
- `chore`: Tooling, build configuration, or dependency updates

Examples:
- `feat(scraper): add custom timezone offset handling`
- `fix(cli): correct error code on invalid date input`
- `docs(readme): add docker fast-path instructions`

---

## Code Quality Standards

All pull requests must pass local verification before submission:

```bash
# Run all linters (flake8, black check, mypy)
make lint

# Automatically format code with Black
make format

# Run test suite with pytest
make test

# Verify documentation builds cleanly without broken references
make docs-build
```

---

## Pull Request Checklist

Before opening a pull request, ensure:

- [ ] Commits adhere to Conventional Commits format.
- [ ] Code is formatted with `black src/ tests/` (88 character limit).
- [ ] Type annotations pass `mypy src/ tests/`.
- [ ] All unit tests pass with `pytest`.
- [ ] Documentation in `docs/` and `README.md` is updated if applicable.
- [ ] No temporary files or cache artifacts are committed.
