#!/usr/bin/env python
from platform import system
from osascript import *

# Darwin/Linux/Windows,Java
if system() != "Darwin":
    osascript('display dialog')