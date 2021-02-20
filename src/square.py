from math import sqrt, floor


def perfect_square(number: int) -> int:
    if sqrt(number) != floor(sqrt(number)):
        return False
    else:
        return True
