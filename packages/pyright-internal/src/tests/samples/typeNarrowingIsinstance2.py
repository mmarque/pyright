# This sample verifies that type narrowing for isinstance works
# on "self" and other bound TypeVars.


class Base:
    def get_value(self) -> int:
        return self.calculate() if isinstance(self, Derived) else 7


class Derived(Base):
    def calculate(self) -> int:
        return 2 * 2
