#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Determines if an object is an inherited instance of a class.
    Args:
        obj : Object to be checked.
        a_class (type): The target class
    Returns:
        If obj is a subtype of a_class, return True. Otherwise, return False.

    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
