import numpy as np


def matrix_stats(n):
    """numpy: створює випадкову матрицю n x n, повертає слід і детермінант."""
    m = np.random.rand(n, n)
    return round(float(np.trace(m)), 3), round(float(np.linalg.det(m)), 3)
