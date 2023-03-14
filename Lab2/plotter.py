from symengine import *
from sympy import plot_implicit, plot


def plot_system(system, xl, xr, yd, yt):
    x, y = symbols('x y')
    f = sympify(system.funcs[0])
    g = sympify(system.funcs[1])
    p = plot_implicit(f, (x, xl, xr), (y, yd, yt), show=False, line_color='r')
    p2 = plot_implicit(g, (x, xl, xr), (y, yd, yt), show=False)
    p.extend(p2)
    p.show()

def plot_equation(eq, xl, xr):
    x = symbols('x')
    f = sympify(eq)
    p = plot(f, (x, xl, xr), line_color='r')