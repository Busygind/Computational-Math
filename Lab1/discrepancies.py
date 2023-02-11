def get_discrepancies(matrix, x, f):
    dis = []
    for i in range(len(matrix)):
        s = 0
        for j in range(len(matrix)):
            s += matrix[i][j] * x[j]
    return dis