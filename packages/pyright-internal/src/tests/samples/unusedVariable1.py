# This sample tests the reportUnusedVariable diagnostic check.


def func1(a: int):
    x = 4

    # This should generate an error if reportUnusedVariable is enabled.
    y = x

    _z = 4

    _ = 2

    __z__ = 5

    z = 3 if x + 1 else 5
