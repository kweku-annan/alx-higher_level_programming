#!/usr/bin/python3
def best_score(a_dictionary):
    name = ""
    if a_dictionary is None or a_dictionary == {}:
        return None
    best_score = 0
    for i in a_dictionary:
        if a_dictionary[i] > best_score:
            best_score = a_dictionary[i]
            name = i
    return name
