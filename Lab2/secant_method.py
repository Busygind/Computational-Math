from sys import exit

from symengine import symbols, sympify


#Возвращает None при делении на ноль и -1 в количестве шагов, если кол-во шагов перевалило за 10 ** 5
def secant_method(func, x0, x1, eps):
    MAX_ITER = 10 ** 5
    x = symbols('x')
    f = sympify(func)
    f_x0 = float(f.subs(x, x0))
    f_x1 = float(f.subs(x, x1))
    iteration_counter = 0
    while abs(f_x1) > eps and abs(x0 - x1) > eps:
        try:
            denominator = float(f_x1 - f_x0) / (x1 - x0)
            xt = x1 - float(f_x1) / denominator
        except ZeroDivisionError:
            return "При решении возникло деление на 0"
        x0 = x1
        x1 = xt
        f_x0 = f_x1
        f_x1 = float(f.subs(x, x1))
        iteration_counter += 1
        if (iteration_counter > MAX_ITER):
            return "Было превышено максимальное количество итераций"
    return xt, float(f.subs(x, xt)) , iteration_counter




if __name__ == '__main__':
    x0 = -100
    x1 = 100

    ans = secant_method("x^3 - x + 4", x0, x1, eps=0.0001)
    print(ans)