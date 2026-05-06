---
tags: [home-assistant, custom-integration, code-quality, pre-commit, linting]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md]
created: 2026-05-06
updated: 2026-05-06
---

# Pre-commit Hooks

`pre-commit` is a framework that runs code quality checks automatically before each `git commit`. Used in HA custom component projects to enforce consistent style and catch issues early.

## Tools Configured in Aaron Godfrey's Template

| Tool | Purpose |
|---|---|
| `pyupgrade` | Upgrades syntax to newer Python versions |
| `black` | Opinionated code formatter |
| `isort` | Sorts imports alphabetically |
| `flake8` | PEP8 linter |
| `mypy` | Static type checker |
| `bandit` | Security vulnerability scanner |
| `codespell` | Spell-checker for code comments |
| JSON validator | Validates `.json` files |

## Setup

```bash
pip install pre-commit
pre-commit install        # installs git hook
pre-commit run --all-files  # run manually on all files
```

## Bypassing

```bash
git commit --no-verify    # skip pre-commit (use sparingly)
```

## Relationship to CI

Pre-commit runs **locally** before each commit. [[GitHub Actions CI]] runs the same checks **remotely** on every push. Together they ensure code quality is enforced at both stages.

## Related

- [[GitHub Actions CI]] — remote CI that complements pre-commit
- [[Unit Testing HA]] — test suite run separately from pre-commit
