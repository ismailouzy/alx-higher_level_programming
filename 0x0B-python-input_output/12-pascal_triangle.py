#!/usr/bin/python3
"""input output

"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascals tria of n
        Args:
            n:
    """
    if n <= 0:
        return []

    tria = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = tria[i-1][j-1] + tria[i-1][j]
        tria.append(row)
    return tria
