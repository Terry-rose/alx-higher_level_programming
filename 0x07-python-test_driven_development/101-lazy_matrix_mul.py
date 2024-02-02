#!/usr/bin/python3
"""Lazy Matrix Multiplication using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Parameters:
    - m_a: a list of lists representing the first matrix
    - m_b: a list of lists representing the second matrix

    Returns:
    A new matrix resulting from the multiplication of m_a and m_b.

    Raises:
    - ValueError: if matrices can't be multiplied
    """

    try:
        result = np.dot(np.array(m_a), np.array(m_b))
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

    return result.tolist()

