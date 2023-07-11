# This sample tests the reportSelfClsParameterName setting.


from typing import Union, overload


def foo():
    pass


class Class1:
    # This should generate an error or warning if the setting
    # is enabled because it's missing a "self" parameter.
    def foo1():
        return 3

    # This should generate an error or warning if the setting
    # is enabled because "self" is misspelled.
    def foo2(self):
        return 4

    # This should generate an error or warning if the setting
    # is enabled because "self" is misspelled.
    def foo3(self):
        return 4

    @classmethod
    def foo4(cls):
        return 4

    @classmethod
    def foo5(cls):
        return 4

    @overload
    # This should generate an error or warning if the setting
    # is enabled because "self" is expected.
    def foo6(x: int) -> int:
        ...

    @overload
    # This should generate an error or warning if the setting
    # is enabled because "self" is expected.
    def foo6(x: str) -> str:
        ...

    # This should generate an error or warning if the setting
    # is enabled because "self" is expected.
    def foo6(self) -> Union[int, str]:
        ...


class Metaclass(type):
    # This should not generate a error because the class derives
    # from type and is assumed to be a metaclass.
    def foo1(self):
        return 3
