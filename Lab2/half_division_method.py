from symengine import sympify, symbols

from plotter import plot_equation

#Возвращает None при количестве итераций > 10**5
def half_division_method(func, a0, b0, eps):
    MAX_ITER = 10 ** 5
    x = symbols('x')
    f = sympify(func)
    n = 1
    a = a0
    b = b0
    xt = (a + b) / 2
    while abs(a - b) > eps and abs(float(f.subs(x, xt))) >= eps :
        n += 1
        if (n > MAX_ITER):
            return "Было превышено максимальное количество итераций"
        if float(f.subs(x, xt)) * float(f.subs(x, a)) > 0:
            a = xt
        else:
            b = xt
        xt = (a + b) / 2
    plot_equation(func, a0, b0)
    return xt, float(f.subs(x, xt)), n


if __name__ == '__main__':
    sol, num_of_iters = half_division_method("(log(x)) ** 2 + 2*x - 7.3", 0.00000001, 2, 0.000001)
    print("Найденный корень: ", sol)
    print("Количество итераций: ", num_of_iters)
