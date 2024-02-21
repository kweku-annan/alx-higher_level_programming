#!/usr/bin/python3
"""Contains a function that returns Json representation of an object"""
import json


def to_json_string(my_obj):
    """Returns the string representation of my_obj
    Args:
        my_obj:
            Objects to return the JSON representation of
    Returns:
        The JSON/string representation of my_obj
    """
    if my_obj == "" or my_obj is None:
        return (None)
    my_json_rep = json.dumps(my_obj)
    return (my_json_rep)
