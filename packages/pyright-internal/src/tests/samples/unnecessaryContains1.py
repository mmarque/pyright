# This sample tests the "reportUnnecessaryContains" diagnostic rule.

from typing import Literal, TypeVar

T1 = TypeVar("T1")
T2 = TypeVar("T2", bound=str)


def func1(x: str | int):
    if x in ("a",):
        return

    # This should generate an error if "reportUnnecessaryContains" is enabled.
    if x in (b"a",):
        return


def func2(x: Literal[1, 2, 3]):
    if x in ("4", 1):
        return

    # This should generate an error if "reportUnnecessaryContains" is enabled.
    if x in (4, 5):
        return


def func3(x: list[str]):
    if x in (["hi"], [2, 3]):
        return


def func4(x: list[T1]) -> T1:
    return x[0]


def func5(x: list[T2]) -> T2:
    return x[0]
