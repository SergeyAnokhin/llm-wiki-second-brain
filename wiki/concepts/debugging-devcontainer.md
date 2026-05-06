---
tags: [home-assistant, custom-integration, debugging, vscode, devcontainer, docker]
sources: [Building a Home Assistant Custom Component Part 5 Debugging.md]
created: 2026-05-05
updated: 2026-05-05
---

# Debugging Devcontainer

The recommended way to debug a Home Assistant custom component locally. Uses the devcontainer from `home-assistant/core` to run a full HA instance inside Docker — without touching your production instance.

## Why Devcontainer

Before this approach, the typical workflow was:
1. Edit file locally
2. `scp` to the HA instance
3. Restart HA
4. Check logs

This is slow and risky — your production HA goes down on every change. The devcontainer solves both problems.

## Prerequisites

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
3. VS Code extension: **Dev Containers** (`ms-vscode-remote.remote-containers`)

## Setup

```bash
git clone https://github.com/home-assistant/core
cd core
code .
```

VS Code detects the `.devcontainer/` folder and prompts: **"Reopen in Container"** → click yes.

First build takes a few minutes. Subsequent opens reuse the built image and start in seconds.

## Install Your Custom Component

Inside the devcontainer terminal (has root):

```bash
mkdir -p config/custom_components
cp -r /your/local/path/my_integration config/custom_components/my_integration
```

> Files created by Docker are owned by root. Use the built-in VS Code terminal (root prompt) instead of copying from host OS.

For config-flow-based integrations, no `configuration.yaml` changes are needed — configure via the UI.

## Run Home Assistant

1. Open Run panel: `Ctrl+Shift+D`
2. Select **"Home Assistant"** from the dropdown
3. Click the green triangle ▶

HA logs appear in the Terminal panel. Navigate to `http://localhost:8123` for the UI. Complete the initial setup (create user, location, etc.) — this only happens once per container build.

## Debug Toolbar

Appears at the top-center when debugger is running:

| Button | Action |
|---|---|
| ▶ | Resume (continue after breakpoint) |
| ↷ | Step over |
| ↓ | Step into |
| ↑ | Step out |
| ↺ | Restart HA |
| ■ | Stop |

Most used: **Resume** (after inspecting a breakpoint) and **Restart** (after changing Python code).

## Setting Breakpoints

Click to the left of any line number → red dot appears.

When HA execution reaches that line, it pauses. The Run panel shows:
- **Local variables** and their current values
- **Global variables**
- **Call stack**

After inspecting, click Resume to continue.

## Typical Debugging Workflow

1. Set breakpoint in `async_setup_entry` or `async_update`
2. Start HA (or trigger a config flow / sensor poll)
3. Execution pauses at breakpoint → inspect variables
4. Fix code → click Restart to reload HA with changes
5. Repeat

## Logging

Add debug logging to your component:

```python
import logging
_LOGGER = logging.getLogger(__name__)

_LOGGER.debug("Fetched data: %s", data)
_LOGGER.error("API call failed: %s", exc)
```

In `configuration.yaml` inside the devcontainer, enable debug logs:

```yaml
logger:
  default: info
  logs:
    custom_components.my_integration: debug
```

## Alternative: Remote Debugging

For debugging against a real HA instance (not devcontainer), use `debugpy`:

```python
import debugpy
debugpy.listen(5678)
```

Configure VS Code `launch.json` to attach to port 5678. This approach is more complex but allows debugging production-like environments.

## Related

- [[Custom Component Structure]] — file placement inside devcontainer
- [[Unit Testing HA]] — complement to interactive debugging
