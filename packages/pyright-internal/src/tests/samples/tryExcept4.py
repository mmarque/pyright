# This sample validates that the exception type provided
# within a raise statement is valid.

a: bool = True


class CustomException1(BaseException):
    def __init__(self, code: int):
        pass


# This should generate an error because CustomException1
# requires an argument to instantiate.
if a:
    raise CustomException1

class CustomException2:
    pass
