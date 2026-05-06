---
tags: [home-assistant, custom-integration, ci, github-actions, testing, hassfest]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md, CONTRIBUTING.md]
created: 2026-05-06
updated: 2026-05-06
---

# GitHub Actions CI

Continuous integration setup for Home Assistant custom components using GitHub Actions. Two key workflows: **hassfest** (validates component structure) and **Python CI** (runs tests).

## Hassfest Workflow

Validates that a custom component meets HA requirements on every push:

```yaml
name: Validate with hassfest
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: home-assistant/actions/hassfest@master
```

Catches: missing `manifest.json` fields, invalid `iot_class` values, malformed translations, dependency issues. Created by ludeeus — same author as [[HACS]].

## Python CI Workflow

Runs the test suite on every push:

```yaml
name: Python CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: pip install -r requirements.test.txt
      - run: pytest
```

## Related

- [[Unit Testing HA]] — test suite these workflows execute
- [[manifest.json]] — hassfest validates its structure
- [[HACS]] — hassfest also used for HACS validation
- [[Pre-commit Hooks]] — local code quality checks that complement CI
