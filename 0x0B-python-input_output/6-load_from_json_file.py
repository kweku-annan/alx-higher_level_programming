#!/usr/bin/python3
"""Contains a function that reads from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an Objects from a JSON file
    Args:
        filename:
            File to read from
    Returns:
        An Object representation of what was read from `filename`
    """
    with open(filename, 'r', encoding='utf-8') as a_file:
        new_object = json.load(a_file)

    return (new_object)
