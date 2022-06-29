#!/usr/bin/python3
"""Write a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix)):
        for elem in range(len(matrix[row])):
            if not isinstance(matrix[row][elem], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        row_size = len(matrix[row])
        if row != len(matrix) - 1:
            if len(matrix[row + 1]) != row_size:
                raise TypeError("Each row of the matrix must have "
                                "the same size")
    new_matrix = [[round(_ / div, 2) for _ in l] for l in matrix]
    return new_matrix
