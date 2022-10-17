from ..mylogicpackage import is_true


def is_even(number: int) -> bool:
    if not isinstance(number, int):
        return False
    return is_true(number % 2 == 0)
