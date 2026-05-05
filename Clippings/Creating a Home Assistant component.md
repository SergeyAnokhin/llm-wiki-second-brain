---
title: "Creating a Home Assistant component"
source: "https://svrooij.io/2023/01/18/home-assistant-component/"
author:
  - "[[Stephan van Rooij]]"
published: 2023-01-18
created: 2026-05-05
description: "Home automation is a topic that speaks to the imagination for most of us. Rooms that light up if you enter them, a notification on your phone when someone rings the doorbell. These thing tickled my personal interest years ago. Back then nobody was doing these kinds of things and as a developer I was intrigued.If you talk about Home Automation in 2023 you’re probably also talking about Home Assistant, if you’ve never heard about that. Go on check their website, it’s awesome. Open-source mostly local home automation with, “components” or “integrations” (they mix these terms, don’t know why) for thousands of devices. Out-of-the-box you have support for a lot of devices, but because it’s open-source you can easily add your own custom components. Home Assistant started as an applciation you would run on a simple raspberry pi you had laying around, recently more and more people are switching to a slightly more powerful system because the pi is no longer sufficient for their needs."
tags:
  - "clippings"
---
Home automation is a topic that speaks to the imagination for most of us. Rooms that light up if you enter them, a notification on your phone when someone rings the doorbell. These thing tickled my personal interest years ago. Back then nobody was doing these kinds of things and as a developer I was intrigued.

If you talk about Home Automation in 2023 you’re probably also talking about [Home Assistant](https://www.home-assistant.io/), if you’ve never heard about that. Go on check their website, it’s awesome. Open-source mostly **local** home automation with, “components” or “integrations” (they mix these terms, don’t know why) for thousands of devices. Out-of-the-box you have support for a lot of devices, but because it’s open-source you can easily add your own custom components. Home Assistant started as an applciation you would run on a simple raspberry pi you had laying around, recently more and more people are switching to a slightly more powerful system because the pi is no longer sufficient for their needs.

## Sonos2mqtt

Back in 2017 I released the [v1.0.0](https://github.com/svrooij/sonos2mqtt/releases/tag/v1.0.0) version of Sonos2mqtt. An application meant to run permanently on a local server, like a raspberry pi. It would listen to notifications from Sonos speakers and relay that information to a local mqtt server. Back then I automated some tasks around the house using a combination of the following applications:

- MQTT a super fast pub/sub message bus (I believe MOSQUITTO back then)
- [Node-RED](https://nodered.org/) a local graphical programming interface. Just take some building blocks and draw lines between them.
- [hue2mqtt](https://github.com/hobbyquaker/hue2mqtt.js) ann app that connected my Hue lightbulbs to mqtt
- A custom dashboard build for a tablet (I cannot find the source anymore)

I also had some sonos speakers that I wanted to control, but could not find any good tools to do just that. And their own app was horrible to use (it still is but more on that later). These circumstances where a good reason to create my own application to do just this. Back to 2023, Sonos2mqtt has more then **335k** pulls on [Dockerhub](https://hub.docker.com/r/svrooij/sonos2mqtt)! And those stats are not the total downloads, since it’s also available in the Github Container registry.

## Home Assistant

Back in 2017, Home assistant was at version [0.34.5](https://github.com/home-assistant/core/releases/tag/0.34.5) and it was written in python, not my strong suit. I knew about it existence, but choose not to use it, I had a pretty solid setup. In 2023 you cannot get around home assistant if you really want to build awesome stuff for you home. The build-in [Dashboards](https://www.home-assistant.io/dashboards/) are so easy to use, that is what I wanted.

It even has a [sonos](https://www.home-assistant.io/integrations/sonos/) integration build-in. Sonos2mqtt will become absolute?

## Sonos2mqtt companion

Sonos2mqtt has this awesome feature to play some song and then revert back to the previous playing song since [Febuary 2018](https://github.com/svrooij/sonos2mqtt/tree/29eb51b4a159643aaac62ca5f976c35fffe36867). This exact feature is what I’m using in a lot of my automations. Let’s say I cannot do without this feature.

And while this feature should be implemented in the build-in sonos integration, I cannot seem to get it to work reliably. And I must admit that this is not the easiest feature to implement, you have to take a lot into account. This feature works really solid in sonos2mqtt, and seeing the amount of users, I’m not ready to throw that all away.

Let’s see if I can integrate sonos2mqtt into home assistant, I though, it has [mqtt discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) so I started sending “discovery” messages only to figure out that **media\_players** are not supported through the default mqtt component.

I then discovered you can add custom components by adding them to a special folder in your config folder. There even is a [Home Assistant Community Store](https://hacs.xyz/) (HACS for short) for custom components (among other things). So there we have it, I’m going to build a custom component to integrate all the goodies from sonos2mqtt right into home assistant.

Check out my new component here: [Sonos2mqtt companion](https://github.com/svrooij/home-assistant-mqtt-component) for Home Assistant. You can install it through the HACS, by adding it as a custom repository (for now).

At the moment (Jan 18th 2023) I’ve just started with the component, it has all the basic features you would expect from a media player integration, but it’s still missing some must-have features. In the long run this integration might even replace the build-in sonos component, who knows what the future will bring.

## Debugging a custom component

When developing software (especially in a language you never used before) it’s really important to debug. This way you can actually see what is happening and follow right along your code. Home Assistant is build in Python, so all components have to be build in Python as well. How to do this for custom components is not documented as good as I had wished.

I eventually figured out the best way to debug a custom home assistant component is by using a specially crafted [dev container](https://github.com/svrooij/home-assistant-mqtt-component#developer-information).

For a custom component it’s a matter of adding these three files to your repository, after that is’s just a matter of pressing `F5` and home assistant will start in debug mode with your custom component loaded. You can put breakpoints in your code and they just work. You can also debug the loading part since home assistant is actually started by the debugger.

The debug experience using this method is really good, I can recommend all other developers of custom components to switch to this way instead of the other examples I could find on the internet.

[.devcontainer/devcontainer.json](https://github.com/svrooij/home-assistant-mqtt-component/blob/main/.devcontainer/devcontainer.json):

```jsonc
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/python
{
    "name": "Python 3",
    // Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
    "image": "mcr.microsoft.com/devcontainers/python:0-3.10",
    "features": {
        "ghcr.io/devcontainers-contrib/features/pylint:2": {}
    },
    // Features to add to the dev container. More info: https://containers.dev/features.
    // "features": {},
    // Use 'forwardPorts' to make a list of ports inside the container available locally.
    // "forwardPorts": [],
    // Use 'postCreateCommand' to run commands after the container is created.
    "postCreateCommand": "git config --global --add safe.directory ${containerWorkspaceFolder} && git config --global user.email \"${localEnv:GIT_EMAIL}\" && git config --global user.name \"${localEnv:GIT_NAME}\" && pip3 install --user -r requirements.txt",
    // Configure tool-specific properties.
    // "customizations": {},
    // Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
    // "remoteUser": "root"
    // Customizations
    "extensions": [
        "ms-python.python",
        "github.vscode-pull-request-github",
        "ryanluker.vscode-coverage-gutters",
        "ms-python.vscode-pylance"
    ],
    "settings": {
        "terminal.integrated.defaultProfile.linux": "bash",
        "terminal.integrated.profiles.linux": {
            "bash": {
                "path": "bash",
                "icon": "terminal-bash"
            }
        },
        "files.eol": "\n",
        "editor.tabSize": 4,
        "python.pythonPath": "/usr/bin/python3",
        "python.analysis.autoSearchPaths": false,
        // This makes sure the home assistant types are loaded into the editor
        "python.analysis.extraPaths": [
            "/home/vscode/.local/lib/python3.10/site-packages/"
        ],
        "python.linting.pylintEnabled": true,
        "python.linting.enabled": true,
        "python.formatting.provider": "black",
        "editor.formatOnPaste": false,
        "editor.formatOnSave": true,
        "editor.formatOnType": true,
        "files.trimTrailingWhitespace": true
    },
    "appPort": 8123
}
```

A default configuration, enabling debug logging [config/configuration.yaml](https://github.com/svrooij/home-assistant-mqtt-component/blob/main/config/configuration.yaml):

```yml
# Example configuration.yaml entry
default_config:

logger:
  default: info
  logs:
    # Change this to your own component name
    custom_components.mqtt_sonos: debug

# Run with debugpy and wait for debugger to connect
# debugpy:
#   start: true
#   wait: true

# Enable this part if you want to use CodeSpaces
# http:
#   use_x_forwarded_for: true
#   trusted_proxies:
#     - 127.0.0.1
#   ip_ban_enabled: true
#   login_attempts_threshold: 3
```

And lastly a launch configuration [.vscode/launch.json](https://github.com/svrooij/home-assistant-mqtt-component/blob/main/.vscode/launch.json):

```jsonc
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Home Assistant",
            "type": "python",
            "request": "launch",
            "module": "homeassistant",
            "justMyCode": false,
            "args": [
                "--debug",
                "-c",
                "config"
            ]
        },
        {
            "name": "Home Assistant (skip pip)",
            "type": "python",
            "request": "launch",
            "module": "homeassistant",
            "justMyCode": false,
            "args": [
                "--debug",
                "-c",
                "config",
                "--skip-pip"
            ]
        }
    ]
}
```

## Conclusion

Getting started developing a new component was **REALLY** hard, I must admit to that, but once you figure out the debugging part, thing get a lot easier.

In the next months I’ll slowly building out this custom component and see what you guys think. For now if you never tried home assistant, go do that this weekend. You’ll love it! If you’re already using home assistant and have some sonos speakers in your house, try out sonos2mqtt and the home assistant integration. It won’t bite the existing sonos integration.

Please let me know what you thing, and please share this information with other.