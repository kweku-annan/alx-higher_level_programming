#!/usr/bin/python3
"""Contains a function that reads a text file"""


def read_file(filename=""):
    """Reads a text file in a UTF8 encoding and prints content in the
    standard output.
    Args:
        filename: Name of file to open. It can also be path of the file

    Returns: Nothing
    """
    if filename == "" or filename is None:
        return
    with open(filename, 'r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
