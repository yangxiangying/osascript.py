#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import *
from subprocess import *
from fullpath import fullpath
import only
from public import public
from rm import rm
from subopen import subopen
from temp import tempfile
from tolist import tolist
from write import write


@only.osx
@public
def osascript(applescript, flags=None):
    """osascript applescript code or file
    """
    args = ["osascript"]
    if applescript and isinstance(applescript, list):
        applescript = "\n".join(applescript)
    temp = programfile = None
    if applescript and exists(applescript) or exists(applescript):
        programfile = applescript
    else:
        temp = programfile = tempfile()
        write(temp, applescript)
    try:
        if flags:
            args += ["-s", flags]
        if programfile:
            args.append(programfile)
        returncode, stdout, stderr = subopen(args)
        return (returncode, stdout, stderr)
    finally:
        rm(temp)
