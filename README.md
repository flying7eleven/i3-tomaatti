# Tomaatti for i3
Tomaatti (Finnish for Tomato / Pomodoro) is a Pomodoro timer which can be integrated into your
regular i3 setup.

## Installation
TODO

### Requirements
* python 3.6+
* i3blocks
* Tkinter

### Package installation
Tomaatti is distributed through PyPI (the Python Package Index). For installing it, just
type ```sudo pip install tomaatti``` for installing it globally or ```pip install tomaatti --prefix ~/.local```
for a local installation. If you chose the local installation, ensure ```~/.local/lib/python3.6/site-packages``` is in your ```PYTHONPATH``` environment
variable and ```~/.local/bin``` in your ```PATH``` environment variable.

### i3 / i3bar configuration
TODO
```ini
[pomodoro]
interval=5
command=tomaatti
```

To ensure that the notification about an ended time periode will displayed correctly, add the following line to your i3 configuration:
```
for_window [title="(?i)tomaatti" class="(?i)tk"] floating enable move position center urgent
```

## FAQ

### The warning that a period ended will just show up if I am on a screen with a i3bar
If the i3 bar is not visible, the widgets are not triggered. The way the timer is currently implemented there is no way in showing
that the period ended without a query from the i3 bar itself.
