#!/usr/bin/python3
"""Prints text with 2 new line after '.', '?', ':'"""


def text_indentation(text):
    """Prints text with 2 new line after '.', '?', ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    list_text = text.split(" ")
    for char in list_text:
        i += 1
        punct_chars = ['.', ':', '?']
        if '.' in char or ':' in char or '?' in char:
            word_lst = list(char)
            for letter in word_lst:
                if letter in punct_chars:
                    letter_idx = word_lst.index(letter)
                    word_lst.insert(letter_idx + 1, '\n')
                    word_lst.insert(letter_idx + 1, '\n')
            new_char = ''.join(word_lst)
            if i == len(list_text):
                print(new_char)
            else:
                print(new_char, end="")
        else:
            if len(text.split(" ")) == i:
                print(char, end="")
            else:
                print(char, end=" ")
