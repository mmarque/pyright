# This sample tests a loop with self-references.

a: bool = False
x: int = 0

while len(input()) < 42:

    x += 43

    if a:
        continue

    x += 44
