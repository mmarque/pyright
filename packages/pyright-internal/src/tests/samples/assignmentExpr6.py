# This sample tests that type guards work correctly
# with the walrus operator.

import re


def foo(s: str) -> str:
    return m[1] if (m := re.fullmatch("(test).+", s)) else "oops"
