#!/usr/bin/python3
""" rotate_2d_matrix Solution """


def rotate_2d_matrix(matrix):
    """ rotate_2d_matrix function """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
