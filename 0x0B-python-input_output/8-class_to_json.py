#!/usr/bin/python3
"""Contains a function that returns the dictionary description with simple
data structure of an object"""


def class_to_json(obj):
    """Returns the dictionary representation of obj which is an
    object of a class"""
    return (obj.__dict__)
