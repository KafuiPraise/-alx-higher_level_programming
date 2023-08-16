#!/usr/bin/python3
"""Implements a JSON file-reading func."""
import json


def load_from_json_file(filename):
    “”"build a Python obj from a JSON file."""
    with open(filename) as f:
        return json.load(f)
