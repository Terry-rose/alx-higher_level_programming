#!/usr/bin/python3
def matrix_divided(matrix, div):
    Divides elements of a matrix by a number (div).

    Parameters:
    - matrix: a list of lists of integers or floats
    - div: a number (integer or float) that is not equal to 0

    Returns:
    A new matrix with elements rounded to 2 decimal places.

    Raises:
    - TypeError: if the matrix is not a list of lists of integers/floats,
                 or if each row of the matrix doesn't have the same size,
                 or if div is not a number (integer or float).
    - ZeroDivisionError: if div is equal to 0.

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return result_matrix

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

