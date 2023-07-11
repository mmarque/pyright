# This sample tests the handling of a custom _generate_next_value_ override.

from enum import Enum, auto


class EnumA(Enum):
    x = auto()


reveal_type(EnumA.x.value, expected_text="int")


class EnumC(str, Enum):
    def _generate_next_value_(self, start, count, last_values) -> str:
        return self


class EnumD(EnumC):
    x = auto()


reveal_type(EnumD.x.value, expected_text="str")
