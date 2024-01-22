#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_character = None
        len_sentence = len(sentence)
    else:
        first_character = sentence[0]
        len_sentence = len(sentence)
    return (len_sentence, first_character)
