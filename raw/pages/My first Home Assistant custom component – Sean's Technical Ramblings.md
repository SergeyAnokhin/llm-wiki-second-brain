---
title: "My first Home Assistant custom component – Sean's Technical Ramblings"
source: "https://seanb.co.uk/2017/07/my-first-home-assistant-custom-component/"
author:
  - "[[seanb]]"
published: 2017-07-16
created: 2026-05-05
description:
tags:
  - "clippings"
---
[Last time](https://seanb.co.uk/2017/07/influxdb-with-home-assistant/) I looked at the InfluxDB component in Home Assistant, and today I’m going to look at using a custom component to get finer control over what goes into the Influx database.

The standard component is great, and there’s really no reason not to use it. When I was looking at the data, though, I noticed that I was getting entries from my Z-Wave temperature sensors even when the temperature hadn’t changed:

```
1500193299252081920 sidedoor_temperature 21.7
1500194438371282944 sidedoor_temperature 21.7
1500194455253585920 sidedoor_temperature 21.7
1500194497504056064 sidedoor_temperature 21.7
1500194734891258112 sidedoor_temperature 22.2
1500194766248593920 sidedoor_temperature 22.2
1500194789682566912 sidedoor_temperature 22.2
```

I’m guessing it might be because they’re multi purpose sensors and if any sensor triggers it causes the device to send an update for all of the sensors in the device. So, for example, if they detect motion they will send an update that includes the current temperature which triggers an event in Home Assistant.

That’s not a problem, it’s not a huge amount of data and I can live with it, but it made me think about ways to customise sending data.

Looking back at my original SmartThings [version](https://seanb.co.uk/2016/08/summers-here/), the InfluxDB schema had measurements called “temperature” that had a tag called “sensor”, whose values were what, in Home Assistant, equates to the friendly name of the entity.

The question is, can you do that in Home Assistant? And how about ensuring that you only record the temperature when it actually changes?

In other words, let’s say that instead of selecting data like this:

```
> select time, entity_id, value from "°C" where entity_id = 'frontdoor_temperature' order by time
```

You want to be able to select it like this:

```
> select time, sensor, value from temperature where sensor = 'Front Door' order by time
```

The answer is yes, you can, and the way to do it is with a custom component. Custom components can be set up to track state changes and act on them, and as they’re written in Python you can do just about anything with them.

A custom component needs a domain. The domain is the type of the component – built in domains include “sensor”, “switch” and so on.

Let’s call the domain “log\_temperature”. We can set the domain up in our configuration.yaml file in the same way as the standard components, and, like those components, they can take parameters.

Our custom component will take a list of the temperature sensing entities we want to record.

So, for example, my custom component is set up in my configuration.yaml as follows:

```
log_temperature:
  sensors:
    - sensor.yr_temperature
    - sensor.sidedoor_temperature
    - sensor.backdoor_temperature
    - sensor.frontdoor_temperature
    - sensor.thermostat_temperature
    - sensor.bedroom_temperature
    - sensor.outside_temperature
```

Notice that these don’t have to be Z-Wave sensors – I’m also taking the temperature from the [yr weather platform](https://home-assistant.io/components/sensor.yr/).

Now we can get to the code.

Custom component code lives in the custom\_components subdirectory under the Home Assistant config directory, so first of all we need to create the directory if it doesn’t exist and then create a file for our Python code. Let’s call it “log\_temperature.py” to match the domain name:

```python
""" Log temperature """
 
importlogging
 
importhomeassistant.loader as loader
fromhomeassistant.helpers.event importtrack_state_change
frominfluxdb importInfluxDBClient
 
DOMAIN ="log_temperature"
 
_LOGGER =logging.getLogger(__name__)
 
defsetup(hass, config):
 
    influxclient =InfluxDBClient('localhost', '8086', '', '', 'home')
 
    defstate_changed(entity_id, old_state, new_state):
 
        ifold_state isNoneornew_state isNone:
            return
 
        try:
            ifold_state.state !=new_state.state:
                data =[ { "measurement": "temperature",
                           "tags": { "sensor": new_state.name },
                           "fields": { "value": float(new_state.state) }
 
                       }]
     
                influxclient.write_points(data)
 
        exceptException as e:
            _LOGGER.warn("Unable to handle data: ", e)
 
    track_state_change(hass, config[DOMAIN]['sensors'], state_changed)
 
    returnTrue
```

Let’s go through it. Every custom component needs a setup function that will be called by Home Assistant when it starts up. In this function, the first thing to do is set up our connection to the Influx database:

```python
influxclient =InfluxDBClient('localhost', '8086', '', '', 'home')
```

OK, so for simplicity I’ve hardcoded this to point to localhost and a database called “home”, but you could also define other parameters for the component and use those in the same way as the standard Influx component.

Our component needs to listen for state changes in the sensors that we defined in our configuration, and for that we need the track\_state\_change helper method:

```python
track_state_change(hass, config[DOMAIN]['sensors'], state_changed)
```

This is simply taking the configuration for the domain we defined at the start of the code and registering the function that will be called when the state changes for the list of sensors. We can now write the function itself. It takes three parameters – the entity\_id of the entity whose state has changed, it’s previous (old) state and current (new) state. This allows us to look for changes, and only send our data when the temperature has changed.

```python
defstate_changed(entity_id, old_state, new_state):
```

On startup the states are usually empty, so we’ll ignore those ones:

```python
ifold_state isNoneornew_state isNone:
    return
```

Now we can look for changes, build up the JSON payload for the Influx client and send the data. Converting the state to a float ensures that we have a valid value and it’s passed as a number. We’ll put all of that in a try/except block to catch and log any errors.

Finally, we just need to restart Home Assistant and the new custom component should start up and start listening for the state changes. If there are any problems with our code we’ll get something in the log file to indicate where the error lies:

```
Jul 16 09:49:33 linux2 scl: track_state_change(hass, config[DOMAIN]['sensors'], state_changed)
Jul 16 09:49:33 linux2 scl: ^
Jul 16 09:49:33 linux2 scl: IndentationError: unindent does not match any outer indentation level
```

Using the custom component I find I get smoother graphs. Although the temperatures from my Z-Wave sensors appear to be accurate to 0.1°C I only seem to get jumps of at least 0.5°C. By recording only the changes, and not the intermediate values where there’s no change, I can avoid those sudden steps in the graphs:

![](https://seanb.co.uk/wp-content/uploads/2017/07/ha-grafana-comparison.png)

OK, so it’s not the most essential custom component, but hopefully it shows how you can use custom components to pick up on events in Home Assistant and do your own processing in Python.

There are other options – [AppDaemon](https://home-assistant.io/docs/ecosystem/appdaemon/) and the new Python scripting [component](https://home-assistant.io/components/python_script/) – that I’ll explore in the future.

in [Home Automation](https://seanb.co.uk/category/home-automation/ "View all posts in Home Automation")