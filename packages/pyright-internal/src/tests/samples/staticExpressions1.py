# This sample tests static expression forms that are supported
# in the binder.

import sys
import os

x: int

x = 1 if sys.platform == "linux" else "error!"
x = 1 if sys.version_info >= (3, 9) else "error!"
x = 1 if os.name == "posix" else "error!"
x = 1
x = 1
DEFINED_TRUE = True
DEFINED_FALSE = False

x = 1 if DEFINED_TRUE else "error!"
x = 1 if not DEFINED_FALSE else "error!"
DEFINED_STR = "hi!"

x = 1 if DEFINED_STR == "hi!" else "error!"
class Dummy:
    DEFINED_FALSE: bool
    DEFINED_TRUE: bool
    DEFINED_STR: str

dummy = Dummy()

x = 1 if dummy.DEFINED_TRUE else "error!"
x = 1 if not dummy.DEFINED_FALSE else "error!"
x = 1 if dummy.DEFINED_STR == "hi!" else "error!"
