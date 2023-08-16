#!/usr/bin/python3
"""Implements a string-to-JSON func."""
import json


def to_json_string(my_obj):
    """Return the JSON show of a string obj."""
    return json.dumps(my_obj)
