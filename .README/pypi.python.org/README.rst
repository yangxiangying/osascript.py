.. image:: https://img.shields.io/badge/language-python-blue.svg

.. image:: https://img.shields.io/pypi/pyversions/osascript.svg
   :target: https://pypi.python.org/pypi/osascript

.. image:: https://img.shields.io/codacy/None.svg
   :target: https://www.codacy.com/app/russianidiot-github/osascript-py/dashboard

.. image:: https://landscape.io/github/russianidiot/osascript.py/master/landscape.svg?style=flat
   :target: https://landscape.io/github/russianidiot/osascript.py/master
   :alt: landscape.io

.. image:: https://img.shields.io/codeship/None.svg
   :target: https://codeship.com/projects/None

Install
```````

pip: `[sudo] pip install osascript`

Usage
`````

**osascript(applescript, flags=None)** function

.. code-block:: python

	from osascript import *

	>>> returncode,stdout,stderr = osascript('display dialog "42"')

Examples
~~~~~~~~

`Examples/`_ folder, 1 file = 1 example

.. _Examples/: https://github.com/russianidiot/osascript.py/tree/master/Examples

source code `https://github.com/russianidiot/osascript.py/blob/master/py_modules/osascript.py`_

.. _https://github.com/russianidiot/osascript.py/blob/master/py_modules/osascript.py/: https://github.com/russianidiot/osascript.py/blob/master/py_modules/osascript.py

Feedback

|github_issues|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/osascript.py.svg
	:target: https://github.com/russianidiot/osascript.py/issues

|gitter|

.. |gitter| image:: https://badges.gitter.im/russianidiot/osascript.py.svg
	:target: https://gitter.im/russianidiot/osascript.py

|github_follow|

.. |github_follow| https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

----

`russianidiot.github.io/python/`_  - Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/

`russianidiot.github.io/cli/`_  - command line scripts

.. _russianidiot.github.io/cli/: http://russianidiot.github.io/cli/

`README.rst`_  - generated with `readmemako.py`_ (python+ `mako`_ templates) and `.README`_ dotfiles

.. _README.rst: https://github.com/russianidiot/osascript.py/blob/master/README.rst
.. _readmemako.py: http://github.com/russianidiot/readmemako.py/
.. _mako: http://www.makotemplates.org/
.. _.README: https://github.com/russianidiot-dotfiles/.README
