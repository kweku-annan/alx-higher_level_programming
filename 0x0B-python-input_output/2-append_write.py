#!/usr/bin/python3
"""Contains a function that appends text to a file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename:
            Name or path of the file
        text:
            Text/String to append to file
    Returns:
        The number of characters appended
    """
    if filename == "" or filename is None:
        return
    if not isinstance(text, str):
        text = str(text)
    with open(filename, 'a', encoding='utf-8') as a_file:
        n_bytes = a_file.write(text)
    return (n_bytes)
