def swap_lines(matrix, f):
    for i in range(len(matrix) - 1):
        if matrix[i][i] == 0:
            buf = matrix[i]
            matrix[i] = matrix[i + 1]
            matrix[i + 1] = buf
            buf = f[i]
            f[i] = f[i + 1]
            f[i + 1] = buf
    return [matrix, f]


def print_matrix(matrix, f):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(round(matrix[i][j], 5), end=" ")
        print(round(f[i], 5))
    print("------------------------------------------------")


def gauss_method_solution(matrix_list):
    matrix = matrix_list[0]
    n = len(matrix)
    f = matrix_list[1]
    for i in range(n - 1):
        [matrix, f] = swap_lines(matrix, f)
        for k in range(i+1, n):
            c = matrix[k][i]/matrix[i][i]
            matrix[k][i] = 0
            for j in range(i+1, n):
                matrix[k][j] = matrix[k][j] - c * matrix[i][j]
            f[k] = f[k] - c * f[i]
        print("Шаг №", i + 1, ":")
        print_matrix(matrix, f)
    x = [0] * n
    for i in range(n - 1, 0, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + matrix[i][j] * x[j]
        x[i] = (f[i] - s) / matrix[i][i]

    return x
