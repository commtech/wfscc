# FSCC Wireshark Utility (wfscc)
This README file is best viewed [online](http://github.com/commtech/wfscc/).

## Downloading Utility
- You can use the pre-built utility files that are included with the driver
- Or, you can download the latest utility version from
[Github releases](https://github.com/commtech/wfscc/releases).


## Quick Start Guide

First, change to the wfscc directory and start the utility. 

```
# cd wfscc\
# python wfscc.py 0 1
Press Ctrl+C to exit
```

You have now set up the utility that takes data it receives on port's 0 and 1
and 'pipe' that data over to Wireshark.  Do not exit the terminal or press
Ctrl+C until you're done collecting data.  

We are now going to set up Wireshark to grab data on those 'pipes'.

#####Windows
```
1. Open Wireshark
2. Select 'Capture Options'
3. Select 'Manage Interfaces'
4. Select 'New'
5. Enter \\.\pipe\wireshark\fscc0
4. Select 'New'
5. Enter \\.\pipe\wireshark\fscc1
4. Select 'Save'
4. Select 'Start'
```
#####Linux
```
1. Open Wireshark
2. Select 'Capture Options'
3. Select 'Manage Interfaces'
4. Select 'New'
5. Enter /tmp/fscc0
4. Select 'New'
5. Enter /tmp/fscc1
4. Select 'Save'
4. Select 'Start'
```
Wireshark is now set up to retrieve data on fscc0 & fscc1 from the wfscc utility.


## Build Dependencies
- [Python 3](http://www.python.org/download/) (32-bit)
- [pywin32](http://sourceforge.net/projects/pywin32/)
- [pyfscc](http://github.com/commtech/pyfscc/)


## Run-time Dependencies
- OS: Windows XP+ & Linux


## Compatibility
We follow [Semantic Versioning](http://semver.org/) when creating releases.


## License

Copyright (C) 2014 [Commtech, Inc.](http://commtech-fastcom.com)

Licensed under the [GNU General Public License v3](http://www.gnu.org/licenses/gpl.txt).
