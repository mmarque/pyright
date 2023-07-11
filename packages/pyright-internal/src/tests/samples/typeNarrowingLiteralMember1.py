# This sample tests type narrowing based on member accesses
# to members that have literal types.

from typing import ClassVar, Literal, Type, Union


class A:
    kind: Literal["A"]
    kind_class: ClassVar[Literal["A"]]
    d: Literal[1, 2, 3]
    is_a: Literal[True]


class B:
    kind: Literal["B"]
    kind_class: ClassVar[Literal["B"]]
    d: Literal[3, 4, 5]
    is_a: Literal[False]


class C:
    kind: str
    kind_class: str
    c: int
    is_a: bool


class D:
    kind: Literal[1, 2, 3]


def eq_obj1(c: Union[A, B]):
    if c.kind == "A":
        reveal_type(c, expected_text="A")
    else:
        reveal_type(c, expected_text="B")


def is_obj1_1(c: Union[A, B]):
    reveal_type(c, expected_text="A | B")


def is_obj1_2(c: Union[A, B]):
    if c.is_a is False:
        reveal_type(c, expected_text="B")
    else:
        reveal_type(c, expected_text="A")


def eq_obj2(c: Union[A, B]):
    if c.kind != "A":
        reveal_type(c, expected_text="B")
    else:
        reveal_type(c, expected_text="A")


def is_obj2(c: Union[A, B]):
    reveal_type(c, expected_text="A | B")


def eq_obj3(c: Union[A, B, C]):
    if c.kind == "A":
        reveal_type(c, expected_text="A | C")
    else:
        reveal_type(c, expected_text="B | C")


def is_obj3(c: Union[A, B, C]):
    reveal_type(c, expected_text="A | B | C")


def eq_obj4(c: Union[A, B]):
    if c.d == 1:
        reveal_type(c, expected_text="A")
    elif c.d == 3:
        reveal_type(c, expected_text="A | B")


def is_obj4(c: Union[A, B]):
    if c.d is 1 or c.d is 3:
        reveal_type(c, expected_text="A | B")


def eq_obj5(d: D):
    if d.kind in [1, 2]:
        reveal_type(d, expected_text="D")


def is_obj5(d: D):
    if d.kind is 1 or d.kind is 2:
        reveal_type(d, expected_text="D")


def eq_class2(c: Union[Type[A], Type[B]]):
    if c.kind_class == "A":
        reveal_type(c, expected_text="Type[A]")
    else:
        reveal_type(c, expected_text="Type[B]")


def is_class2(c: Union[Type[A], Type[B]]):
    reveal_type(c, expected_text="Type[A] | Type[B]")


class E:
    @property
    def type(self) -> Literal[0]:
        return 0


class F:
    @property
    def type(self) -> Literal[1]:
        return 1


def test(x: E | F) -> None:
    if x.type == 1:
        reveal_type(x, expected_type="F")
    else:
        reveal_type(x, expected_type="E")

class G:
    type: Literal[0]

class H:
    type: Literal[1]

class I:
    thing: G | H

    def method1(self) -> None:
        if self.thing.type == 1:
            reveal_type(self.thing, expected_text="H")

        local = self.thing
        if local.type == 1:
            reveal_type(local, expected_text="H")

