#!/usr/bin/python3
"""Prints text with 2 new line after '.', '?', ':'"""


def text_indentation(text):
    """Prints text with 2 new line after '.', '?', ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    for char in text.split(" "):
        i += 1
        if '.' in char or ':' in char or '?' in char:
            print(char, end="")
            print("\n\n", end="")
        else:
            if len(text.split(" ")) == i:
                print(char, end="")
            else:
                print(char, end=" ")
