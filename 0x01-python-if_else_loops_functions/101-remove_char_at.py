#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    new_str = ""
    for i in str:
        if i == str[n]:
            pass
        else:
            new_str += i
    return new_str
