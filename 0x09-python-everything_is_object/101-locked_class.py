#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Computes LockedClass attributes
    for only attributes declared as 'first_name'.
    """

    __slots__ = ["first_name"]
