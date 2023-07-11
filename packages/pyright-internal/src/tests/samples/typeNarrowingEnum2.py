# This sample tests the type narrowing logic for
# enum values or False/True that are compared using the
# "is" and "is not" operators.

from enum import Enum
from typing import Literal, NoReturn, Union


class SomeEnum(Enum):
    VALUE1 = 1
    VALUE2 = 2


def assert_never(val: NoReturn):
    ...


def func1(a: SomeEnum):
    if a is not SomeEnum.VALUE1 and a is not SomeEnum.VALUE2:
        assert_never(a)


def func2(a: SomeEnum):
    if a is not SomeEnum.VALUE1:
        # This should generate an error because
        # a hasn't been narrowed to Never.
        assert_never(a)


def func3(a: SomeEnum):
    if a is not SomeEnum.VALUE1 and a is not SomeEnum.VALUE2:
        assert_never(a)


def func4(a: SomeEnum):
    if a is not SomeEnum.VALUE1:
        # This should generate an error because
        # a hasn't been narrowed to Never.
        assert_never(a)


def func5(a: Union[str, Literal[False]]) -> str:
    return "no" if a is False else a


def func6(a: Union[str, Literal[False]]) -> str:
    return a if a is not False else "no"


def func7(a: Union[str, bool]) -> str:
    if a is False:
        return "False"
    elif a is True:
        return "True"
    return a
