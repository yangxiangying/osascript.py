![python](https://img.shields.io/badge/language-python-blue.svg)[![PyPI](https://img.shields.io/pypi/pyversions/osascript.svg)](https://pypi.python.org/pypi/osascript)

[![codacy.com](https://api.codacy.com/project/badge/Grade/3e30e0c2134544ddb7a70848b19f43de)](https://www.codacy.com/app/russianidiot-github/osascript-py/dashboard)
[![landscape.io](https://landscape.io/github/russianidiot/osascript.py/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/osascript.py)
[![codeclimate.com](https://codeclimate.com/github/russianidiot/osascript.py/badges/gpa.svg)](https://codeclimate.com/github/russianidiot/osascript.py)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/osascript.py/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/osascript.py/)

[![codecov.io](https://codecov.io/github/russianidiot/osascript.py/coverage.svg?branch=master)](https://codecov.io/github/russianidiot/osascript.py?branch=master)
[![drone.io](https://drone.io/github.com/russianidiot/osascript.py/status.png)](https://drone.io/github.com/russianidiot/osascript.py)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/osascript.py/badges/build.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/osascript.py/)
[![semaphoreci.com](https://semaphoreci.com/api/v1/russianidiot/osascript-py/branches/master/shields_badge.svg)](https://semaphoreci.com/russianidiot/osascript-py)
[![shippable.com](https://api.shippable.com/projects/57068cbb2a8192902e1bbbd1/badge?branch=master)](https://app.shippable.com/projects/57068cbb2a8192902e1bbbd1)
[![travis-ci.org](https://travis-ci.org/russianidiot/osascript.py.svg)](https://travis-ci.org/russianidiot/osascript.py)
[![wercker.com](https://app.wercker.com/status/9b568382fe980d02e6b671e3e1a3c434/s/master)](https://app.wercker.com/#applications/570bf18c3f1a891374046873)

[![PyPI](https://img.shields.io/pypi/v/osascript.svg)](https://pypi.python.org/pypi/osascript)
[![PyPI](https://img.shields.io/pypi/dm/osascript.svg)](https://pypi.python.org/pypi/osascript)
[![PyPI](https://img.shields.io/pypi/dd/osascript.svg)](https://pypi.python.org/pypi/osascript)

<p align="center">
    <b>osascript(applescript, flags=None) function - osascript (AppleScript) python implementation (OS X)</b>
</p>

#### Install

pip: 
`[sudo] pip install osascript`

#### Usage

```python
>>> from osascript import osascript

>>> returncode,stdout,stderr = osascript(code)

```

#### Example

```python
>>> returncode,stdout,stderr = osascript('display dialog "42"')

```

[Examples/](https://github.com/russianidiot/osascript.py/tree/master/Examples)

Sources:
*	[py_modules/osascript.py](https://github.com/russianidiot/osascript.py/blob/master/py_modules/osascript.py)

### Links

*	osascript(1) Mac OS X Manual Page - [developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/osascript.1.html](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/osascript.1.html)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/osascript.py.svg)](https://github.com/russianidiot/osascript.py/issues)
[![Join the chat at https://gitter.im/russianidiot/osascript.py](https://badges.gitter.im/russianidiot/osascript.py.svg)](https://gitter.im/russianidiot/osascript.py)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)

* * *

<p align="center">
	Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
	<img src="http://russianidiot.github.io/images/python/16.png" />
</p>
<p align="center">
	cli packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/cli/</a>
<img src="http://russianidiot.github.io/images/cli/16.png" />
</p>

<p align="center">
	repos list <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	<a href="https://raw.githubusercontent.com/russianidiot/osascript.py/master/README.md">README.md</a> generated with <a href="https://github.com/russianidiot/readme-mako.py">readmemako.py</a> (python+<a href="http://www.makotemplates.org/">mako</a> templates) and <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> dotfiles 
<img src="http://russianidiot.github.io/images/book/16.png">
</p>
