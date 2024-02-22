#!/usr/bin/python3
"""Contains a function that writes an object to a text file, using JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file in JSON representation
    Args:
        my_obj:
            Object to write to text file in JSON representation
        filename:
            File or Path to be written to
    Returns:
        None if there is an error.
    """
    if my_obj == "" or filename == "" or my_obj is None or filename is None:
        return (None)
    with open(filename, 'w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
