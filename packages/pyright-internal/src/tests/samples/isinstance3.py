# This sample tests the logic that validates the second parameter to
# an isinstance or issubclass call and ensures that it's a class or
# tuple of classes.


from abc import abstractmethod
from typing import Any, Generic, Tuple, Type, TypeVar, Union


_T = TypeVar("_T", int, str)


class A(Generic[_T]):
    pass


a = A()


class ClassA(Generic[_T]):
    v1: _T
    v2: Type[_T]

    @property
    @abstractmethod
    def _elem_type_(self) -> Union[Type[_T], Tuple[Type[_T], ...]]:
        raise NotImplementedError

    def check_type(self, var: Any) -> bool:
        return isinstance(var, self._elem_type_)

    def execute(self, var: Union[_T, Tuple[_T]]) -> None:
        pass
