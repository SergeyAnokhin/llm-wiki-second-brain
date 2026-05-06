---
tags: [github, api, python, external-service]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md]
created: 2026-05-06
updated: 2026-05-06
---

# GitHub

Web-based platform for version control and collaboration, used in the Aaron Godfrey tutorial series as the **data source** for the example HA custom component. The component queries the GitHub REST API to expose repository statistics as sensor entities.

## Role in the Tutorial

[[Building a HA Custom Component Part 1: Project Structure and Basics]] uses a `PyGitHub` client to fetch repository data (stars, watchers, open issues) and expose them as `SensorEntity` instances in Home Assistant.

## Related

- [[Aaron Godfrey]] — uses GitHub API as tutorial data source
- [[GitHub Actions CI]] — GitHub's CI/CD platform used for HA component testing
- [[HACS]] — distributed through GitHub repositories
