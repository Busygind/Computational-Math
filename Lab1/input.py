def get_column(matrix, i):
    return [row[i] for row in matrix]


def greet():
    print("Добро пожаловать в решатель СЛАУ методом Гаусса!")
    print("------------------------------------------------")


def user_input():
    print("Введите тип ввода данных: ")
    print("1 - ввести матрицу вручную")
    print("2 - взять матрицу из файла")
    t = input()
    if t == "1":
        return fill_matrix_from_console()
    elif t == "2":
        print("Введите название файла: ")
        filename = input()
        return get_matrix_from_file(filename)
    else:
        print("Пожалуйста, напечатайте 1 или 2 в соответствии с типом ввода.")
        return user_input()


def fill_matrix_from_console():
    try:
        print("Введите размерность матрицы:")
        size = int(input())
        print("Введите матрицу построчно (разделитель - пробел). Чтобы закончить ввод, нажмите Enter: ")
        matrix = []
        for _ in range(size):
            row = input()
            row = list(map(float, row.split(" ")))
            if len(row) != size:
                print("Количество элементов в строке не соответствует размерности матрицы. Попробуйте еще раз.")
                return fill_matrix_from_console()
            matrix.append(row)
        print("Введите свободные члены (через пробел):")
        f = list(map(float, input().split(" ")))
        if len(f) != size:
            print("Количество свободных членов не равно размерности матрицы. Попробуйте еще раз.")
            return fill_matrix_from_console()
    except Exception:
        print("Ввод некорректен, попробуйте снова: ")
        return fill_matrix_from_console()
    return [matrix, f]


def get_matrix_from_file(filename):
    try:
        with open(filename, 'r') as f:
            matrix = [[float(num) for num in line.split(' ')] for line in f]
            f = get_column(matrix, len(matrix))
            for el in matrix:
                del el[len(matrix)]
            for el in matrix:
                if len(matrix) != len(el):
                    print("Матрица должна быть квадратной. Попробуйте еще раз. ")
                    return user_input()
            return [matrix, f]
    except Exception:
        print("Данные в файле некорректны или его не существует. Попробуйте еще раз. ")
        return user_input()
