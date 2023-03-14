import numpy as np
from sympy import sympify, symbols, diff, Mul, Add


#Returns NONE если интервал выбран неграмотно
def simple_iteration_method(func, a0, b0, eps):
    x = symbols('x')
    f = sympify(func)
    df = diff(f)
    l = -1 / max([abs(float(df.subs(x, xt))) for xt in np.arange(a0, b0, eps)])

    phi = Mul(f, l)
    phi = Add(phi, x)
    dphi = diff(phi)
    q = max([abs(float(dphi.subs(x, xt))) for xt in np.arange(a0, b0, eps)])
    if q >= 1:
        return "q >= 1, границы интервала выбраны некорректно"

    x_prev = (a0 + b0) / 2
    x_cur = float(phi.subs(x, x_prev))

    iters = 0
    while q / (1 - q) * abs(x_cur - x_prev) >= eps:
        x_prev = x_cur
        x_cur = float(phi.subs(x, x_prev))
        iters += 1

    return x_cur, float(f.subs(x, x_cur)), iters


if __name__ == '__main__':
    eps = 0.01
    interval = (-10, 100)
    root, iter_count = simple_iteration_method("x ** 3 - x + 4", interval, eps)
    print(f'Root: {root}, iterations: {iter_count}')