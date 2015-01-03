# vi:set ts=8 sts=4 sw=4 et tw=80:
"""
The clewn package.
"""

# Python 2-3 compatibility.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

__all__ = [str(x) for x in
               ('__version__', 'PY3', 'PY26', 'text_type', 'ClewnError',)]

__version__ = '2.0'

# Python 2.6 or older
PY26 = (sys.version_info < (2, 7))

# Python 3.0 or newer
PY3 = (sys.version_info >= (3,))

# Python 3.1 or newer
PY31 = (sys.version_info >= (3, 1))

text_type = str if PY3 else unicode

class ClewnError(Exception):
    """Base class for pyclewn exceptions."""

# pyclewn uses OrderedDict (added in Python 3.1).
if PY26 or (PY3 and not PY31):
    raise NotImplementedError('Python 2.7 or Python 3.1 or newer is required.')

