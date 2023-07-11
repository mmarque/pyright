# This sample tests the handling of isinstance and issubclass type
# narrowing in the case where there is no overlap between the
# value type and the test type.

from typing import Type, TypeVar


class A:
    a_val: int


class B:
    b_val: int


class C:
    c_val: int


def func1(val: A):
    val.a_val
    val.b_val

    if isinstance(val, B):
        # This should generate an error
        val.c_val

        reveal_type(val, expected_text="<subclass of A and B>")

        if isinstance(val, C):
            val.a_val
            val.b_val
            val.c_val
            reveal_type(val, expected_text="<subclass of <subclass of A and B> and C>")

    else:
        reveal_type(val, expected_text="A")


def func2(val: Type[A]):
    val.a_val
    val.b_val

    if issubclass(val, B):
        # This should generate an error
        val.c_val

        reveal_type(val, expected_text="Type[<subclass of A and B>]")

        if issubclass(val, C):
            val.a_val
            val.b_val
            val.c_val
            reveal_type(
                val, expected_text="Type[<subclass of <subclass of A and B> and C>]"
            )

    else:
        reveal_type(val, expected_text="Type[A]")


_T1 = TypeVar("_T1", bound=A)


def func3(val: _T1) -> _T1:
    return val
