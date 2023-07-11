# This sample tests various unary expressions.


def returnsFloat1() -> float:
    a = 1
    return not a


def returnsInt1() -> int:
    a = 1
    return -a


def returnsInt2() -> int:
    a = 1
    return +a


def returnsInt3() -> int:
    a = 4
    return ~a
