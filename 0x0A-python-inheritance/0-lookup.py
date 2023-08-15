#!/usr/bin/python3
“""Fetch an object attribute lookup function."""


def lookup(obj):
    """Return a list of attributes."""
    return (dir(obj))
