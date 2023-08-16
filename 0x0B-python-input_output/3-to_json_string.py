#!/usr/bin/python3
"""Implaements a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON shows of a string obj."""
    return json.dumps(my_obj)
