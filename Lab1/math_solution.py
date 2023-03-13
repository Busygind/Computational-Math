# def swap_lines(matrix, f):
#     for i in range(len(matrix) - 1):
#         if matrix[i][i] == 0:
#             buf = matrix[i]
#             matrix[i] = matrix[i + 1]
#             matrix[i + 1] = buf
#             buf = f[i]
#             f[i] = f[i + 1]
#             f[i + 1] = buf
#     return [matrix, f]

import sys


def swap_lines(matrix, i, f):
    for j in range(i + 1, len(matrix)):
        if matrix[j][i] != 0:
            # print_matrix(f"matrix before swap line i={i} and line j={j}", matrix)
            matrix[j], matrix[i] = matrix[i], matrix[j]
            f[j], f[i] = f[i], f[j]
            # print_matrix(f"matrix after swap line i={i} and line j={j}", matrix)
            return [matrix, f]
    print("У матрицы нет уникальных решений!")
    sys.exit(0)


def print_matrix(matrix, f):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(round(matrix[i][j], 5), end=" ")
        print(round(f[i], 5))
    print("------------------------------------------------")


def det_calc(matrix, k):
    det = -1 ** k
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det


def gauss_method_solution(matrix_list):
    matrix = matrix_list[0]
    n = len(matrix)
    f = matrix_list[1]
    swaps = 0
    for i in range(n - 1):
        if matrix[i][i] == 0:
            [matrix, f] = swap_lines(matrix, i, f)
            swaps += 1
        for k in range(i+1, n):
            c = matrix[k][i]/matrix[i][i]
            matrix[k][i] = 0
            for j in range(i+1, n):
                matrix[k][j] = matrix[k][j] - c * matrix[i][j]
            f[k] = f[k] - c * f[i]
        print("Шаг №", i + 1, ":")
        print_matrix(matrix, f)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + matrix[i][j] * x[j]
        if matrix[i][i] == 0:
            print("У матрицы нет уникальных решений!")
            sys.exit(0)
        x[i] = (f[i] - s) / matrix[i][i]
    print("Определитель матрицы: ", det_calc(matrix, swaps))
    print("------------------------------------------------")
    return x
