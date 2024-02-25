#!/usr/bin/python3
"""Contains a function that divides all elements of
of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of 'matrix' with 'div' and rounds result to
    2 decimal places.
    Args:
        matrix (list of list):
            Must be a list of list of integers or floats.
            Each row of the matrix must be of the same size. i.e. Must
            have the same number of elements.
        div (float or int):
            Must be an integer or a float.
            Can't be equal to 0.

    Returns:
        A new matrix with elements in each row divided by 'div'
    """

    # Checking if 'matrix' is a list of list
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of "
                        "lists) of integers/floats")

    # Checking if each row of 'matrix' all contain ints or floats
    if not all(
            isinstance(
                item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Checking if all rows are of the same length
    len_matrix = [len(row) for row in matrix]
    if not all(length == len_matrix[0] for length in len_matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Checking if div is a float/int
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    # Checking if div is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for number in row:
            result = round((number / div), 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return (new_matrix)
