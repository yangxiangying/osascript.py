.. image:: https://img.shields.io/badge/language-python-blue.svg

.. image:: https://img.shields.io/pypi/pyversions/osascript.svg
   :target: https://pypi.python.org/pypi/osascript

|codacy| |landscape| |codeclimate| |scrutinizer|

.. |scrutinizer| image:: https://scrutinizer-ci.com/g/russianidiot/osascript.py/badges/build.png?b=master
   :target: https://scrutinizer-ci.com/g/russianidiot/osascript.py/
   :alt: scrutinizer-ci.com

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/3e30e0c2134544ddb7a70848b19f43de
   :target: https://www.codacy.com/app/russianidiot-github/osascript-py/dashboard
   :alt: codacy.com

.. |codeclimate| image:: https://codeclimate.com/github/russianidiot/osascript.py/badges/gpa.svg
   :target: https://codeclimate.com/github/russianidiot/osascript.py
   :alt: codeclimate.com

.. |landscape| image:: https://landscape.io/github/russianidiot/osascript.py/master/landscape.svg?style=flat
   :target: https://landscape.io/github/russianidiot/osascript.py/master/landscape.svg?style=flat
   :alt: landscape.io

Install
```````

:code:`[sudo] pip install osascript`

Usage
`````

.. code:: python
	
	>>> from osascript import osascript
	
	>>> returncode,stdout,stderr = osascript(code)
	

Example
```````

.. code:: python
	
	>>> returncode,stdout,stderr = osascript('display dialog "42"')
	

`Examples/`_

.. _Examples/: https://github.com/russianidiot/osascript.py/tree/master/Examples

Sources:

*	`py_modules/osascript.py`_

.. _`py_modules/osascript.py`: https://github.com/russianidiot/osascript.py/blob/master/py_modules/osascript.py

Feedback |github_issues| |gitter| |github_follow|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/osascript.py.svg
	:target: https://github.com/russianidiot/osascript.py/issues

.. |github_follow| image:: https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

.. |gitter| image:: https://badges.gitter.im/russianidiot/osascript.py.svg
	:target: https://gitter.im/russianidiot/osascript.py

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
