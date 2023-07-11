# This sample tests type narrowing of instance variables in the presence
# of a double nested loop.

def func1(x: str | None):
    assert x is not None

    x = f"{x}"
