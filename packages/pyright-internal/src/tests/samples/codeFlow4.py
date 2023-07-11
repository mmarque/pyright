# This sample tests the handling of if/elif chains that omit an else
# statement. The "implied else" statement should be assumed never taken if the
# final if/elif test expression evaluates to Never in the negative case.

from enum import Enum
from typing import Literal, Union


def func1(x: Union[int, str]):
    if isinstance(x, int):
        y = 0
    elif isinstance(x, str):
        y = 1

    print(y)


def func2(x: Literal[1, 2, 3, 4]):
    y = 0 if x in [1, 2] else 1
    print(y)


def func3(x: Literal[1, 2], y: Literal["one", "two"]):
    if x == 1 or y != "two":
        z = 0
    elif x == 2 or y != "one":
        z = 1

    print(z)


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    PERIWINKLE = 4


def func4(x: Color):
    if x == Color.RED:
        return

    if x == Color.GREEN or Color.PERIWINKLE == x:
        y = 2
    elif Color.BLUE == x:
        y = 3

    print(y)


def func5():
    y = 2

    print(y)


def func6():
    y = 2

    print(y)


def func7(color: Color) -> str:
    if color in [Color.RED, Color.BLUE]:
        return "yes"
    elif color in [Color.GREEN, Color.PERIWINKLE]:
        return "no"


def func8(color: Color) -> bool:
    if color in [Color.RED, Color.BLUE]:
        return True
    elif color in [Color.GREEN, Color.PERIWINKLE]:
        return False


reveal_type(func8(Color.RED), expected_text="bool")


def func9(a: Union[str, int], b: Union[str, int]) -> bool:
    if isinstance(a, str):
        return True
    elif isinstance(a, int):
        if isinstance(b, (str, int)):
            return False


def func10(foo: list[str]) -> bool:
    i = 0
    x: int | None = None

    while i < 5:
        foo[i]

        if x is None:
            return False
        reveal_type(x, expected_text="Never")
        i = x

    return True


class A:
    pass


class B(A):
    pass


def func11(val: A | B):
    if not (isinstance(val, (A, B))):
        raise Exception


reveal_type(func11(A()), expected_text="None")


def func12(val: A | B):
    if isinstance(val, (A, B)):
        raise Exception


reveal_type(func12(A()), expected_text="NoReturn")
