#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak in the list"""
    if not list_of_integers:
        return (None)
    peak = 0
    for i in list_of_integers:
        if i >= peak:
            peak = i
    return (peak)
