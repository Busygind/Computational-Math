from equation_system import *
from symengine import *
from sympy import plot_implicit, Add, Mul, nsolve


def string2func(s):
    def func(x, y):
        return eval(s)

    return func

def plot(system):
    x, y = symbols('x y')
    f = sympify(system.funcs[0])
    g = sympify(system.funcs[1])
    p = plot_implicit(f, (x, -10, 10), (y, -10, 10), show=False, line_color='r')
    p2 = plot_implicit(g, (x, -10, 10), (y, -10, 10), show=False)
    p.extend(p2)
    p.show()


def newtons_method(system):
    ksi = 0.01
    vars = symbols('x y')
    f = sympify([elem for elem in system.funcs])
    J = zeros(len(f), len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            J[i, j] = diff(fi, s)
    dx, dy = symbols('dx dy')
    # plot(system)
    J[0] = Mul(J[0], dx)
    J[1] = Mul(J[1], dy)
    J[2] = Mul(J[2], dx)
    J[3] = Mul(J[3], dy)
    first = Add(J[0], J[1])
    second = Add(J[2], J[3])
    x0 = 1
    y0 = 2
    found = false
    f[0] = Mul(f[0], -1)
    f[1] = Mul(f[1], -1)
    xAns = 0
    yAns = 0
    k = 0
    while not found:
        k += 1
        firstTemp = first.subs(vars[0], x0)
        firstTemp = firstTemp.subs(vars[1], y0)
        secondTemp = second.subs(vars[0], x0)
        secondTemp = secondTemp.subs(vars[1], y0)
        f0Temp = f[0].subs(vars[0], x0)
        f0Temp = f0Temp.subs(vars[1], y0)
        f1Temp = f[1].subs(vars[0], x0)
        f1Temp = f1Temp.subs(vars[1], y0)
        firstTemp = Add(firstTemp, -1 * f0Temp)
        secondTemp = Add(secondTemp, -1 * f1Temp)
        ans = nsolve((firstTemp, secondTemp), (dx, dy), (0, 0))
        x1, y1 = x0 + float(ans[0]), y0 + float(ans[1])
        if abs(x1 - x0) <= ksi and abs(y1 - y0) <= ksi:
            found, xAns, yAns = true, x1, y1
        else:
            x0, y0 = x1, y1
    print_ans([xAns, yAns], k, [0,0])

def print_ans(ansVector, k, errorsVector):
    print("Вектор неизвестных: ")
    print(ansVector)
    print("Количество итераций: ")
    print(k)
    print("Вектор погрешностей: ")
    print(errorsVector)

if __name__ == '__main__':
    system = EquationSystem("y ** 2 + x ** 2 - 4", "-3 * x ** 2 + y")
    newtons_method(system)
