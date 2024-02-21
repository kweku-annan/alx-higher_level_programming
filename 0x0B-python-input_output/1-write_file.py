#!/usr/bin/python3
"""Contains a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file. Overwrites existing file
    Args:
        filename: Name or path of the file to write to
        text: Text to write to the file

    Returns:
        The number of characters written.

    """
    if filename == "" or filename is None:
        return None
    if not isinstance(text, str):
        text = str(text)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        n_bytes = file.tell()

    return (n_bytes)
