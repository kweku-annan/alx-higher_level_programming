#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        ascii_value = ord(i)
        if ascii_value >= 97 and ascii_value <= 122:
            ascii_value -= 32
            new_str += chr(ascii_value)
        else:
            new_str += chr(ascii_value)
    print("{}".format(new_str))
