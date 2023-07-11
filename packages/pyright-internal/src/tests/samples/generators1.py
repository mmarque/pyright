# This sample tests various type checking operations relating to
# generator functions (those with a "yield" method).

from typing import Any, Generator, Dict, Iterable, Iterator, List, TypedDict


class ClassA:
    pass


s = True


class ClassB:
    def shouldContinue(self):
        global s
        return s


class ClassC:
    pass


def generator1() -> Generator[ClassA, ClassB, ClassC]:
    cont = ClassB()
    while cont.shouldContinue():
        yield ClassA()

    return ClassC()


# This should generate an error because the function
# has no return statement at the bottom, so it
# returns None which is not assignable to ClassC.
def generator2() -> Generator[ClassA, ClassB, ClassC]:
    cont = ClassB()
    if cont.shouldContinue():
        # This should generate an error because False isn't
        # assignable to the return type (ClassC).
        return False

    while cont.shouldContinue():
        # This should generate an error because 3 isn't
        # assignable to the yield type (ClassA).
        yield 3


def generator3() -> Generator[ClassA, int, Any]:
    cont = ClassB()
    if cont.shouldContinue():
        return 3

    while cont.shouldContinue():
        # This should generate an error because 3 isn't
        # assignable to the yield type (ClassA).
        yield 3


def generator4() -> Iterable[ClassA]:
    yield ClassA()

    return True


def generator5() -> Iterator[ClassA]:
    # This should generate an error because ClassB isn't
    # assignable to ClassA.
    yield ClassB()


def generate():
    yield from range(2)


s = generate()

# Verify that a call to a Generator method succeeds
s.close()


def generator6():
    yield


def generator7() -> Generator[None, None, None]:
    yield


def generator8() -> Iterator[Dict[str, int]]:
    # This tests the bidirectional type inference
    # of dict types. It should not generate an error.
    yield {"hello": 3}


# This should generate an error.
def generator9() -> int:
    yield None
    return 3


# This should generate an error.
async def generator10() -> int:
    yield None


# This should generate an error.
def generator11() -> List[int]:
    yield 3


class TD1(TypedDict):
    x: str


def generator12() -> Generator[TD1, None, None]:
    yield {"x": "x"}

def generator13() -> Generator[TD1, None, None]:
    # This should generate an error.
    yield {"y": "x"}
