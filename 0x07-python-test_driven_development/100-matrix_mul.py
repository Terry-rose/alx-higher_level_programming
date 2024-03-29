#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
    - m_a (list): The first matrix as a list of lists of integers or floats.
    - m_b (list): The second matrix as a list of lists of integers or floats.

    Returns:
    A new matrix resulting from the multiplication of m_a and m_b.

    Raises:
    - ValueError: If m_a or m_b is not a list of lists or is empty.
    - TypeError: If one element in the matrices is not an integer or float.
    - ValueError: If m_a and m_b can't be multiplied due to incompatible dimensions.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

