#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Parameters:
    - m_a: a list of lists representing the first matrix
    - m_b: a list of lists representing the second matrix

    Returns:
    A new matrix resulting from the multiplication of m_a and m_b.

    Raises:
    - TypeError: if m_a or m_b is not a list, not a list of lists, contains non-integer/float elements, or rows of different sizes
    - ValueError: if m_a or m_b is empty or if matrices can't be multiplied
    """

    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if not m_a or not all(row for row in m_a) or not m_b or not all(row for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(element, (int, float)) for row in m_a for element in row) or not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

