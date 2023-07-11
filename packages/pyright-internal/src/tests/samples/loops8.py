# This sample tests a difficult set of circular dependencies
# between untyped variables.

# pyright: strict

from typing import Iterable


def test(parts: Iterable[str]):
    x: list[str] = []
    ns = ""
    for part in parts:
        ns += "a" if ns else part
        x.append(ns)
