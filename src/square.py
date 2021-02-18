from math import sqrt, floor


# Integer square root.
def int_sqrt(number: int) -> int:
    return int(sqrt(number))


# Check if number is perfect square.
def perfect_square(number: int) -> int:
    if sqrt(number) != floor(sqrt(number)):
        return False
    else:
        return True
