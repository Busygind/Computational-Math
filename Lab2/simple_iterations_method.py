import numpy as np
import math
from typing import Callable
from sys import exit


def simple_iteration_method(phi: Callable, phi_derivative: Callable, interval: tuple, eps: float) -> list:
    ''' Find a root of a non-linear equation using the simple iteration method.
        Returns an approximate root of the equation and the number of iterations.'''

    q = max([abs(phi_derivative(x)) for x in np.arange(interval[0], interval[1], eps)])
    if q >= 1:
        print('The function doesn\'t meet the second condition of convergence.')
        exit()

    x_prev = (interval[0] + interval[1]) / 2
    x_cur = phi(x_prev)

    iters = 0
    while q / (1 - q) * abs(x_cur - x_prev) >= eps:
        x_prev = x_cur
        x_cur = phi(x_prev)
        iters += 1

    return x_cur, iters


if __name__ == '__main__':
    phi = lambda x: math.sqrt((math.sin(x) + 0.5) / 2)
    phi_derivative = lambda x: math.cos(x) / (4 * math.sqrt((math.sin(x) + 0.5) / 2))
    eps = 0.0000001
    interval = (0.75, 0.8)
    root, iter_count = simple_iteration_method(phi, phi_derivative, interval, eps)
    print(f'Root: {root}, iterations: {iter_count}')