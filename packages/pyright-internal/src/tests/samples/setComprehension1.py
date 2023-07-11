# This sample tests type checking for set comprehensions.

from typing import Generator, Set

a = [1, 2, 3, 4]


def func1() -> Generator[int, None, None]:
    return iter(a)


def func2() -> Set[int]:
    return set(a)


def func3() -> Set[str]:
    return set(a)


def generate():
    yield from range(2)


# Verify that generate returns a Generator.
s = generate()
s.close()
