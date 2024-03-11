#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return (0)

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    int_rep = 0
    roman_string = roman_string.upper()
    string_len = len(roman_string)

    if string_len >= 2:
        str_index = 0
        while str_index < string_len:
            current_letter = roman_string[str_index]
            current_value = roman_dict[current_letter]
            if str_index + 1 < string_len:
                next_letter = roman_string[str_index + 1]
                next_value = roman_dict[next_letter]
            if current_value < next_value:
                actual_value = next_value - current_value
                int_rep += actual_value
                str_index += 2
            else:
                int_rep += current_value
                str_index += 1
    else:
        int_rep = roman_dict[roman_string]

    return (int_rep)
