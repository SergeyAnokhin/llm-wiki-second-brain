---
tags: [tool, home-assistant, hacs, custom-integration]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md]
created: 2026-05-05
updated: 2026-05-05
---

# HACS

**Home Assistant Community Store** — a custom integration that provides a UI for discovering and installing community-made custom components, themes, and plugins. The de-facto standard for distributing custom HA integrations.

**Website:** https://hacs.xyz  
**GitHub:** @ludeeus (primary author)

## Relevance to Custom Component Development

- HACS requires `version` field in `manifest.json`
- HACS requires a `hacs.json` file at the repository root
- The **hassfest** GitHub Action (by @ludeeus) validates that components meet HACS/HA requirements — used in [[GitHub Actions CI]]
- Making a component HACS-compatible makes it discoverable and installable by the community

## hacs.json Minimum

```json
{
  "name": "My Integration",
  "render_readme": true
}
```

## Related

- [[manifest.json]] — version field required for HACS
- [[Unit Testing HA]] — hassfest action
- [[Custom Component Structure]]
