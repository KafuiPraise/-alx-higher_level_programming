#!/usr/bin/python3
"""Explains a file-writing function."""


def write_file(filename="", text=""):
    """Prints a str to a UTF8 txt file.

    Args:
        filename (str): The file name to write.
        text (str): Txt to write to the file.
    Returns:
        The nums of char written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
