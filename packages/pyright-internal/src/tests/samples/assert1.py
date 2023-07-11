# This sample tests the ability to detect errant assert calls
# that are always true - the "reportAssertAlwaysTrue" option.

from typing import Any, Tuple


def foo(a: Tuple[int, ...]):
    assert a


b = ()
assert b


c = (2, 3)

# This should generate a warning.
assert c
