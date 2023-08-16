#!/usr/bin/python3
"""nitializes a Python class-to-JSON func."""


def class_to_json(obj):
    """Return the dictionary output of a simple data struct."""
    return obj.__dict__
