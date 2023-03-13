def func(x):
    return x ** 3 - x + 4  # todo


def solution(f, a0, b0, eps):
    n = 1
    a = a0
    b = b0
    x = (a + b) / 2
    while abs(a - b) > eps and abs(f(x)) >= eps:
        n += 1
        if f(x) * f(a) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2
        # print(abs(a - b), abs(f(x)))
    return x, n


if __name__ == '__main__':
    sol, num_of_iters = solution(func, -2, -1, 0.01)
    print("Найденный корень: ", sol)
    print("Количество итераций: ", num_of_iters)
