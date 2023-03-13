from input import *
from math_solution import *
from discrepancies import *


greet()
[matrix, f] = user_input()
print("------------------------------------------------")
print("Исходная матрица: ")
print_matrix(matrix, f)
buf_matrix = []
for i in range(len(matrix)):
    buf_matrix.append(list(matrix[i]))
buf_f = list(f)
x = gauss_method_solution([matrix, f])
dis = get_discrepancies(buf_matrix, x, buf_f)

for i in range(len(x)):
    print("x[", i+1, "] =", round(x[i], 5))
print("------------------------------------------------")
for i in range(len(dis)):
    print("r[", i+1, "] =", round(dis[i], 20))
print("------------------------------------------------")
