.. image:: https://img.shields.io/pypi/v/osascript.svg
   :target: https://pypi.python.org/pypi/osascript

.. image:: https://img.shields.io/pypi/pyversions/osascript.svg
   :target: https://pypi.python.org/pypi/osascript

.. image:: https://img.shields.io/pypi/dm/osascript.svg
   :target: https://pypi.python.org/pypi/osascript

	

Install
~~~~~~~

github.com_: :code:`pip install git+git://github.com/russianidiot/osascript.py.git`

pypi.python.org_: :code:`pip install osascript`

download_: :code:`[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

.. _github.com: http://github.com/russianidiot/osascript.py
.. _pypi.python.org: https://pypi.python.org/pypi/osascript.py
.. _download: https://github.com/russianidiot/osascript.py/archive/master.zip

	

	

	

Usage
~~~~~

.. code-block:: python

	from osascript import *

	returncode,stdout,stderr = osascript('return "message"')

Links
~~~~~

*	osascript(1) Mac OS X Manual Page	- `https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/osascript.1.html <https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/osascript.1.html>`_

----

Feedback
~~~~~~~~

|github_issues| - Github Issues

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/osascript.py.svg
	:target: https://github.com/russianidiot/osascript.py/issues

|gitter| - **Chat** with me (english/russian) 

.. |gitter| image:: https://badges.gitter.im/russianidiot/osascript.py.svg
	:target: https://gitter.im/russianidiot/osascript.py

`russianidiot.github.io/python/`_  - my Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/