# Tomaatti for i3
Tomaatti (Finnish for Tomato / Pomodoro) is a Pomodoro timer which can be integrated into your
regular i3 setup.

## Installation
TODO

### Requirements
* python 3 (`sudo apt install python3`)
* i3blocks (`sudo apt install i3blocks`)
* Tkinter (`sudo apt install python3-tk`)

#### Optional requirements
* Xcompmgr for transparent overlays (`sudo apt install xcompmgr`)

### Package installation
Tomaatti is distributed through PyPI (the Python Package Index). For installing it, just
type ```sudo pip install tomaatti``` for installing it globally or ```pip install tomaatti --prefix ~/.local```
for a local installation. If you chose the local installation, ensure ```~/.local/lib/python3.6/site-packages``` is in your ```PYTHONPATH``` environment
variable and ```~/.local/bin``` in your ```PATH``` environment variable.

### i3 / i3bar configuration
Currently the only supported configuration is i3blocks.

#### i3blocks configuration
This tool was mainly tested with i3blocks and this should be the primary way of using it. Please ensure in your i3 configuration file that you
use i3blocks as the block manager for your tool bar:
```
...
bar {
	status_command i3blocks -c ~/.config/i3/i3blocks.conf
	...
}
...
```

If you confirmed that you can run i3blocks, past the following snipped to your i3blocks configuration. This ensures that you can use
the pomodoro timer by simply clicking on it in your tool bar:

TODO
```ini
[pomodoro]
interval=5
command=tomaatti
```

Since tomaatti uses Tkinter for showing that a work or break period ended, it is recommended to add the following line to your i3 configuration to ensure the notification
will be displayed correctly:
```
for_window [title="(?i)tomaatti" class="(?i)tk"] floating enable move position center urgent
```

## Usage
| Action       | What it does                                   |
|      :-:     |     :-:                                        |
| Left click   | Start and stop the current timer               |
| Middle click | Nothing                                        |
| Right click  | Switch the timer between work and break period |

## FAQ

### The warning that a period ended will just show up if I am on a screen with a i3bar
If the i3 bar is not visible, the widgets are not triggered. The way the timer is currently implemented there is no way in showing
that the period ended without a query from the i3 bar itself.
