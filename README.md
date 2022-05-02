## Win App Locker
***This project is still under construction...***

*Currently only kill mode (Kill app directedly when it runs) supported.*

### Introduction

Wants your children to stay away from games or unsafe apps?

Wants to keep your privacy from being compromised?

... 

Then this is the app for you!

**Win App Locker** is a tool which allows you to lock your app.

### How to use

#### Run

Locate to the project folder and run the following command to start the app in the background.

```shell
pythonw main.pyw
```

More easy to use, you can double click `tools/start.bat` to start the app.

#### Kill

Find `python.exe` or `pythonw.exe` in Task Manager and kill it.

Using `taskkill` command can be faster. 

```shell
taskkill /f /im pythonw.exe
```

More easy to use, you can double click `tools/stop.bat` to kill the app.

#### Start with Windows

Run `create_startup.py` in the `tools` of project folder to create a shortcut in the startup folder. After that, this app will be started when you start Windows next time.

### Configuration

The configuration file is in `data/config.json` in the project folder.

`preference` is the main configuration.

+ `frequency`: How often to check whether the banned app is running.

+ `warning_title`: Title of the warning window when the banned app is running.

+ `warning_message`: Message of the warning window when the banned app is running.

+ `mode`: How to lock the app.
    - Supported mode: `kill`

+ `read_banlist_mode`: How and where to read the banlist.
    - Supported mode: `json`, `txt`
        - `json`: Read the banlist from the value of `ban_list` in `data/config.json`
        - `txt`: Read the banlist from the file `data/banlist.txt`.
            - Write one app name per line.
