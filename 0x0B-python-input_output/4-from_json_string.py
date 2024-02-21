#!/usr/bin/python3
"""Contains a function that returns an object represented by a json string"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args:
        my_str:
            JSON strong to convert to a Python Object
    Returns:
        The Object represented by the JSON string
    """
    if my_str == "" or my_str is None:
        return (None)

    my_object = json.loads(my_str)

    return (my_object)
