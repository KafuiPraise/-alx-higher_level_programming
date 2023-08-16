#!/usr/bin/python3
"""Implements a file-appending function."""


def append_write(filename="", text=""):
    """Adds a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to add to the file.
    Returns:
        The nums of char appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
