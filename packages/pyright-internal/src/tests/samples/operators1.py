# This sample tests the type checker's ability to check
# custom operator overrides.

from typing import Union


class A(object):
    def __eq__(self, Foo):
        return "equal"


class B(object):
    def __ne__(self, Bar):
        return self

    def __lt__(self, Bar):
        return "string"

    def __gt__(self, Bar):
        return "string"

    def __ge__(self, Bar):
        return "string"

    def __le__(self, Bar):
        return "string"


def needs_a_string(val: str):
    pass


def needs_a_string_or_bool(val: Union[bool, str]):
    pass


def test():
    a = A()
    needs_a_string(a == a)

    # This should generate an error because there
    # is no __ne__ operator defined, so a bool
    # value will result.
    needs_a_string(a != a)

    a = B()

    # At this point, a should be of type Union[Foo, Bar],
    # so the == operator should return either a str or
    # a bool.
    needs_a_string_or_bool(a == a)

    # This should generate an error.
    needs_a_string(a == a)

    # This should generate an error.
    needs_a_string_or_bool(a != a)

    b = B()
    needs_a_string(b < b)
    needs_a_string(b > b)
    needs_a_string(b <= b)
    needs_a_string(b >= b)


class C:
    def __getattr__(self, name: str, /):
        if name == "__add__":
            return lambda _: 0


a = C()
a.__add__

# This should generate an error because __getattr__ is not used
# when looking up operator overload methods.
b = a + 0


class D:
    def __init__(self):
        self.__add__ = lambda x: x


d = D()

# This should generate an error because __add__ is not a class variable.
_ = d + d


class E:
    __slots__ = ("__add__",)

    def __init__(self):
        self.__add__ = lambda x: x


e = E()

_ = e + e
