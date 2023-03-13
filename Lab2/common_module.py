def greet():
    success = False
    system_was_chase = False
    print("Добро пожаловать в решатель нелинейных уравнений и их систем!")
    print("------------------------------------------------------")
    print("Если Вы хотите решить нелинейное уравнение - введите '1', если систему - '2'")
    while not success:
        if input() == '1':
            while not success:
                print("Выберите уравнение, корень/корни которого Вы хотите найти:")
                print("1. x^3 + 2,84x^2 - 5,606x - 14,766 = 0")
                print("2. x^3 - x + 4 = 0")
                print("3. ")
                print("4. ")
                print("Чтобы выбрать уравнение введите его номер и нажмите 'Enter'")
                try:
                    number = int(input())
                    if 1 <= number <= 4:
                        return number, system_was_chase
                    else:
                        print("Некорректный ввод, попробуйте еще раз.")
                except Exception:
                    print("Некорректный ввод, попробуйте еще раз.")
        elif input() == '2':
            system_was_chase = True
            while not success:
                print("Выберите систему, корни которой Вы хотите найти:")
                print("1. x^3 + 2,84x^2 - 5,606x - 14,766")
                print("2. ")
                print("Чтобы выбрать уравнение введите его номер и нажмите 'Enter'")
                try:
                    number = int(input())
                    if 1 <= number <= 2:
                        return number, system_was_chase
                    else:
                        print("Некорректный ввод, попробуйте еще раз.")
                except Exception:
                    print("Некорректный ввод, попробуйте еще раз.")


def eq_user_input(num):
    print("------------------------------------------------------")
    try:
        print("Введите погрешность, с которой необходимо производить вычисления:")
        eps = float(input())
    except Exception:
        print("Некорректный ввод, попробуйте еще раз.")
        eq_user_input(num)




def system_user_input(num):
    print("------------------------------------------------------")
