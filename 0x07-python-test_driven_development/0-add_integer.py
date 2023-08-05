#!/usr/bin/python3
"""

A function that adds 2 integers
Must be first casted to integers if they are float
Prints the sum to the stdout

"""


def add_integer(a, b=98):
    """adds the sum of two  numbers

     Performs the addition between two numbers.

    Args:
        a (:obj:`int, float`): The first number.
        b (:obj:`int, float`, optional): The second number.

    Returns:
        int: The result of the addition.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
