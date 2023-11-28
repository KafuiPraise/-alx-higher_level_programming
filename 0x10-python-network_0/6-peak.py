#!/usr/bin/python3
"""finder list of integers"""


def find_peak(list_of_integers):
    """func finds in list of int"""

    if not list_of_integers:
        return None

    up = 0
    down = len(list_of_integers) - 1

    while up < down:
        middle = (up + down) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            up = 1 + middle
        else:
            down = middle

    return list_of_integers[up]
