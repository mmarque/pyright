# This file validates type narrowing that involve
# conditional binary expressions.

# pyright: reportOptionalMemberAccess=false


class Foo:
    def bar(self):
        return


maybe = True

a = None if maybe else Foo()
b = None if maybe else Foo()

a.bar()
b.bar()
a.bar()
b.bar()
# This should be flagged as an error
a.bar()
# This should be flagged as an error
b.bar()
a.bar()
b.bar()
a.bar()
b.bar()
