---
title: "Developing Home Assistant Core in a VSCode Devcontainer"
source: "https://community.home-assistant.io/t/developing-home-assistant-core-in-a-vscode-devcontainer/235650"
author:
  - "[[MizterB]]"
published: 2023-01-11
created: 2026-05-05
description: "Developing Home Assistant Core in a VSCode Devcontainer Setting Up the Local Repository Ensure that git installed on your development woks"
tags:
  - "clippings"
---
## Setting Up the Local Repository

1. Ensure that `git` installed on your development wokstation
2. Visit the [Home Assistant Core](https://github.com/home-assistant/core) repository and click **Fork**.
3. Open a terminal and set up your local repository
```bash
git clone https://github.com/YOUR_GIT_USERNAME/core.git Home Assistant-core
cd Home Assistant-core
git remote add upstream https://github.com/home-assistant/core.git
```
4. Create a new feature branch that tracks the `dev` branch in
```css
git checkout -b my_dev_branch --track origin/dev
```
5. Open the local repository in VSCode

### Configuring Home Assistant

By default, the devcontainer will create the `config` directory inside the container if it doesn’t already exist. Optionally, you can override this by bind mounting a `config` directory from your local filesystem, which can be helpful for long-term persistence or swapping in/out different configurations to support development.

To do this, include a list of `mounts` inside `/.devcontainer/devcontainer.json`:

```perl
"mounts": [
    // Custom configuration directory
    "source=${localEnv:HOME}/path/to/config,target=${containerWorkspaceFolder}/config,type=bind",
  ]
```

If these mounts are modified, then the DevContainer must to be rebuilt

- Press `F1`, and enter `Remote-Containers: Rebuild Container`

See [Working with containers in Visual Studio Code](https://code.visualstudio.com/docs/remote/containers-advanced#_adding-another-local-file-mount) for more information.

### Running Home Assistant

If this the first time running Home Assistant, or the container has been rebuilt, you should use this method for starting Home Assistant. This method will install all of the out-of-the-box libraries required to run HA (including the debugger, which can then be used later).

1. Open the the local repository in VSCode
2. Accept the prompt to “Reopen in Container”
3. Start HA in the container via the menu options:
	`Terminal | Run Task... | Run Home Assistant Core`
4. Open HA in a web browser at [http://localhost:8123](http://localhost:8123/)

See **Debugging Home Assistant** for more information about debug mode.

## Keeping Code Up To Date

*This is adapted from [Catching up with Reality | Home Assistant Developer Docs](https://developers.home-assistant.io/docs/development_catching_up)*

The following commands will keep your local feature branch up-to-date with Home Assistant’s official `dev` branch.  
*Reminder: `upstream` is the official HA repository, `origin` is your remote repository that was forked from it*

- Switch to a local feature branch
- Pull the latest commits from a HA’s `upstream/dev` branch
- Replay the upstream commits to the local branch, then re-applies local changes
- Push the combined commits back to the forked repository on GitHub
```sql
git checkout my_dev_branch
git fetch upstream dev
git rebase upstream/dev
git push origin --force
```

## Debugging Home Assistant

### Set Up Home Assistant’s Remote Python Debugger

Add the following to `/config/configuration.yaml`:

```yaml
debugpy:
  start: true
  wait: false
```

See [Remote Python Debugger - Home Assistant](https://www.home-assistant.io/integrations/debugpy/) for more information.

### Start Debugging

Using the debugger after using the **Running Home Assistant** startup method is not preferred for debugging, as it the debugger does not attach at the very beginning of the Home Assistant startup process. To start Home Assistant immediately in debug mode, do the following.

1. Stop any running tasks if you used the **Running Home Assistant** method  
	`Terminal | Terminate Task... | Run Home Assistant Core`
2. Switch to the VSCode Run & Debug view
3. Select the `Home Assistant` launch configuration from the dropdown
4. Start the debugger

#### If You Use *Run Task* to Start Home Assistant

1. Ensure that the HA devcontainer is running (\`Terminal | Run Task… | Run Home Assistant Core\`\`)
2. Switch to the VSCode Run & Debug view
3. Select the `Home Assistant: Attach Local` launch configuration from the dropdown
4. Start the debugger

## Debugging Custom Components and Libraries

When developing custom components or libraries that exist in other local respoitories on your development machine, the easiest way to incorporate these into Home Assistant is to bind mount those repositories into HA’s `config` directory.

To do this, include a list of `mounts` inside `/.devcontainer/devcontainer.json`, similar to this example:

```perl
"mounts": [
    // Custom configuration directory
    "source=${localEnv:HOME}/path/to/config,target=${containerWorkspaceFolder}/config,type=bind",
    // Custom component
    "source=${localEnv:HOME}/path/to/custom_repo/custom_components/component_name,target=${containerWorkspaceFolder}/config/custom_components/component_name,type=bind",
    //Custom library
    //"source=${localEnv:HOME}/path/to/custom_repo/custom_libraries/library_name,target=${containerWorkspaceFolder}/config/custom_libraries/library_name,type=bind",
  ]
```

Add more bind mounts as needed for your use case.

If these mounts are modified, then the devcontainer must to be rebuilt

- Press `F1`, and enter `Remote-Containers: Rebuild Container`

### Custom Components

Custom components are mounted in the container under `config/custom_components`, which is a Home Assistant standard.

### Custom Libraries

Custom libraries are mounted under `config/custom_libraries`. Note that `custom_libraries` is a personal naming preference, and is not prescribed in the Home Assistant docs.

In order to develop a custom library, HA needs to be started with the `--skip-pip` argument as described here: [Building a Python library for an API | Home Assistant Developer Docs](https://developers.home-assistant.io/docs/api_lib_index)

This launch config option is available in the Run & Debug view as `Home Assistant (skip pip)`

#### Prerequisites

Before starting HA in *skip pip* mode, start HA at least once in *normal* mode, which will install all out-of the-box libraries the via the normal HA boot process. This can be done via either of these methods:

- **Running Home Assistant**
- **Debugging Home Assistant**

#### Overriding an Out-Of-The-Box Library

If overriding a out-of-the-box-in library, it must first be removed from the DevContainer. Go to the VSCode terminal and enter the following:

`pip uninstall library_name`

### Installing a Custom Library

To then enable a custom library, have pip install it from the filesystem. It should be accessible via the bind mount(s) created above. Go to the VSCode terminal and enter the following:

`pip install -e ./config/custom_libraries/library_name`

### Using the Custom Library

Stop the running instance of Home Assistant, then restart using the `Home Assistant (skip pip)` debug option shown above