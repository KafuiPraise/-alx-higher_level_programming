#!/usr/bin/python3
"""Function that adds 2 integer.s"""


def add_integer(a, b=98):
    """adds the sum of two numbers
    float argument are typecasted to an ints before addition is done.
    Raises:
        TypError: if either a or b is a non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
