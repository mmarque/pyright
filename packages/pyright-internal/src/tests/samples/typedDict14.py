# This sample tests bidirectional type inference when assigning
# a value to a typedDict element.

from typing import List, Optional, TypedDict, Union


class Thing(TypedDict):
    v1: bool
    v2: str


class Thing2(TypedDict):
    v3: Optional[Thing]
    v4: Optional[List[Union[str, int]]]


thing2: Thing2 = {"v3": {"v1": False, "v2": "a"}, "v4": ["hi", 4.0]}
