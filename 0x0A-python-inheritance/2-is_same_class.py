#!/usr/bin/python3
"""
Assess the type of an object
"""


def is_same_class(obj, a_class):
    """
    Determine if obj is an instance of a_class
    """
    return type(obj) == a_class
