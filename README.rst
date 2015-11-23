	
Install
'''''''

github.com_: :code:`pip install git+git://github.com/b'russianidiot'/osascript.py.git`

pypi.python.org_: :code:`pip install osascript`

download_: :code:`python setup.py install` or :code:`setup/.setup.py develop.command`

.. _github.com: http://github.com/b'russianidiot'/osascript.py
.. _pypi.python.org: https://pypi.python.org/pypi/osascript
.. _download: https://github.com/b'russianidiot'/osascript.py/archive/master.zip

	

	

	

Usage 
'''''
.. code-block::

	from osascript import *

	returncode,stdout,stderr = osascript('return "message"')

------------

**Tested**: python 2.6, 2.7, 3+

**Bug Tracker**: `github.com/b'russianidiot'/osascript.py/issues`__

__ https://github.com/b'russianidiot'/osascript.py/issues