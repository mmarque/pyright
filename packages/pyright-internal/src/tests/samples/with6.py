# This sample tests that classes whose metaclass implements a context
# manager work with the "with" statement.

from types import TracebackType
from typing import Self


class ClassA(type):
    def __enter__(self) -> Self:
        print("Enter A")
        return self
    
    def __exit__(self, exc_typ: type[Exception], exc_val: Exception, exc_tbc: TracebackType) -> None:
        print("Exit A")

class ClassB(metaclass=ClassA):
    ...


with ClassB as b:
    ...

