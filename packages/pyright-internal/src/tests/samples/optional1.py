# This sample tests use of "Optional" types.

from typing import Any, Optional


class Foo:
    def __init__(self):
        self.value = 3

    def do_stuff(self):
        pass

    def __enter__(self):
        return 3

    def __exit__(
        self,
        t: Optional[type] = None,
        exc: Optional[BaseException] = None,
        tb: Optional[Any] = None,
    ) -> bool:
        return True


a = None
a = Foo()

# If "reportOptionalMemberAccess" is enabled,
# this should generate an error.
a.value = 3


def foo():
    pass


b = None
b = foo

# If "reportOptionalCall" is enabled,
# this should generate an error.
b()


c = None
c = [3, 4, 5]

# If "reportOptionalSubscript" is enabled,
# this should generate an error.
c[2]


# If "reportOptionalContextManager" is enabled,
# this should generate an error.
cm = None
cm = Foo()
with cm as val:
    pass

# If "reportOptionalOperand" is enabled,
# this should generate 3 errors.
e = None
e = 4

v1 = e + 4
v2 = e < 5
v3 = not e
