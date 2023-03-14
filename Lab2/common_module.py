import pathlib
import traceback

from equation_system import EquationSystem
from half_division_method import half_division_method
from newtons_method_for_system import newtons_method
from secant_method import secant_method
from simple_iterations_method import simple_iteration_method


def greet():
    equations = ["x ** 3 + 2.84 * x ** 2 - 5.606 * x - 14.766", "x^3 - x + 4", "−1.78* x ** 3 − 5.05 * x ** 2 + 3.64 * x + 1.37", "sin(x) - 2 * x"]
    systems_of_equations = [EquationSystem("y ** 2 + x ** 2 - 4", "-3 * x ** 2 + y"), EquationSystem("sin(x) - y", "cos(x) - y")]
    equation_solver = {
        1: ["Метод половинного деления", half_division_method],
        2: ["Метод простых итераций", simple_iteration_method],
        3: ["Метод секущих", secant_method]
    }
    success = False
    print("Добро пожаловать в решатель нелинейных уравнений и их систем!")
    print("------------------------------------------------------")
    print("Если Вы хотите решить нелинейное уравнение - введите '1', если систему - '2'")
    while not success:
        choice = input()
        if choice == '1':
            while not success:
                print("Выберите уравнение, корень/корни которого Вы хотите найти:")
                for i in range(0, len(equations)):
                    print(i + 1, ": ", equations[i], " = 0")
                print("Чтобы выбрать уравнение введите его номер и нажмите 'Enter'")
                try:
                    number = int(input())
                    if 1 <= number <= 4:
                        f = choose_equation_solver(equation_solver)
                        a, b, eps = input_borders_and_eps()
                        ans = f(equations[number - 1], a, b, eps)
                        if (isinstance(ans, str)):
                            print("Ошибка: ")
                            print(ans)
                        else:
                            x, x_val, n = ans
                            print("Корень: ", x)
                            print("Значение функции в корне: ", x_val)
                            print("Количество итераций: ", n)
                        success = True
                    else:
                        print("Некорректный ввод, попробуйте еще раз.")
                except Exception as e:
                    tb = traceback.format_exc()
                    print(str(tb))
                    print("Некорректный ввод, попробуйте еще раз. asdasd")
        elif choice == '2':
            while not success:
                print("Выберите систему, корни которой Вы хотите найти:")
                for i in range(0, len(systems_of_equations)):
                    print(i + 1, ":")
                    print(systems_of_equations[i].to_string())
                print("Чтобы выбрать уравнение введите его номер и нажмите 'Enter'")
                try:
                    number = int(input())
                    if 1 <= number <= 2:
                        a, b, eps = input_borders_and_eps()
                        ansVector, k, errorsVector = newtons_method(systems_of_equations[number-1], a, b, eps)
                        print("Вектор неизвестных: ", ansVector)
                        print("Количество итераций: ", k)
                        print("Вектор погрешностей: ", errorsVector)
                        success = True
                    else:
                        print("Некорректный ввод, попробуйте еще раз.")
                except Exception:
                    print("Некорректный ввод, попробуйте еще раз.")


def choose_equation_solver(equations_dict):
    chosen = False
    while not chosen:
        print()
        print("Выберите метод решения уравнения: ")
        for key in equations_dict:
            print(key, ": ", equations_dict[key][0])
        print("Чтобы выбрать метод решения введите его номер и нажмите 'Enter'")
        try:
            number = int(input())
            if 1 <= number <= 3:
                return equations_dict[number][1]
            else:
                print("Некорректный ввод, попробуйте еще раз.")
        except Exception:
            print("Некорректный ввод, попробуйте еще раз.")


def input_borders_and_eps():
    print("Как вы хотите ввести границы промежутка и погрешность вычисления? 1 - руками, 2 - файлом")
    type = input()
    if type == '1':
        while True:
            print("Введите левую границу промежутка:")
            try:
                a = float(input())
                print("Введите правую границу промежутка: ")
                try:
                    b = float(input())
                    if a >= b:
                        print("Левая граница не может быть больше правой")
                        continue
                    print("Введите ε:")
                    try:
                        eps = float(input())
                        return a, b, eps
                    except Exception:
                        print("Введите число")
                except Exception:
                    print("Введите число")
            except Exception:
                print("Введите число")
    elif type == '2':
        while True:
            print("Введите путь до файла")
            path = input()
            if (path[0] != '/'):
                path += pathlib.Path().resolve()
            try:
                f = open(path, "r")
                try:
                    a, b, eps = map(float, f.readline().split())
                    return a, b, eps
                except Exception:
                    print("Файл содержит некорректную информацию")
            except IOError:
                print("Такого файла не существует!")
    else:
        print('Введите 1 или 2!')
        return input_borders_and_eps()


if __name__ == '__main__':
    greet()