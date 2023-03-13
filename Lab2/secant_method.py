from sys import exit


def secant(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > eps and iteration_counter < 100 and abs(x0 - x1) > eps:
        try:
            denominator = float(f_x1 - f_x0) / (x1 - x0)
            x = x1 - float(f_x1) / denominator
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
            exit(1)  # Abort with error
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1
    # Here, either a solution is found, or too many iterations
    if abs(f_x1) > eps or abs(x0 - x1) >= eps:
        iteration_counter = -1
    return x, iteration_counter


def f(x):
    return x ** 3 - x + 4


if __name__ == '__main__':
    x0 = -1.5
    x1 = -2

    solution, no_iterations = secant(f, x0, x1, eps=0.01)

    if no_iterations > 0:  # Solution found
        print("Number of function calls: %d" % (2 + no_iterations))
        print("A solution is: %f" % (solution))
    else:
        print("Solution not found!")