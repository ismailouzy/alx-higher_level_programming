#!/usr/bin/python3
"""a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """a function that make all the elements into a matrix
        Args:
            matrix: the matrix
            div: the number to divide the matrix on
    """
    if matrix is None or matrix == [] or len(matrix) == 3:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    nlist = [[] for n in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]
                    ) is not int and type(matrix[i][j]) is not float:
                raise TypeError(
                        "matrix must be a matrix (list of lists) "
                        "of integers/floats")
            elif len(set(len(row) for row in matrix)) > 1:
                raise TypeError(
                        "Each row of the matrix must have the same size")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            elif type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            else:
                nlist[i].append(round((matrix[i][j]/div), 2))

    return nlist
