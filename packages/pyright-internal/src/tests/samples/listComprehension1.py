# This sample tests type checking for list comprehensions.

from typing import Any, Generator, Iterable, List, Literal

a = [1, 2, 3, 4]


def func1() -> Generator[int, None, None]:
    return iter(a)


def func2() -> List[int]:
    return list(a)


def func3() -> List[str]:
    return list(a)


def generate():
    yield from range(2)


# Verify that generate returns a Generator.
s = generate()
s.close()

# verify that literals are handled correctly.
FooOrBar = Literal["foo", "bar"]


def to_list(values: Iterable[FooOrBar]) -> List[FooOrBar]:
    return list(values)

x = 3
# This should generate a syntax error.
[x for in range(3)]
