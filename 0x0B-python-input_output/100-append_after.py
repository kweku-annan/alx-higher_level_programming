#!/usr/bin/python3
"""Inserts a line of text to a file, after each line containing
a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename:
            Name of file to workwith. Must not be an empty string
            or None
        search_string:
            Line of string to append new_string after.
        new_string:
            Line of string to append after search_string.

    Returns:
         Nothing
    """
    if filename == "" or filename is None:
        raise FileNotFoundError("File name cannot be empty or None")
    with open(filename, 'r', encoding='utf-8') as orig_file:
        lines = orig_file.readlines()

    strings = ""
    for line in lines:
        strings += line
        if search_string in line:
            strings += new_string

    with open(filename, 'w', encoding='utf-8') as new_file:
        new_file.write(strings)
