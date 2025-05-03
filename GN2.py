import random


def is_valid2(number, lower, upper):
    if  (lower.isdigit() and upper.isdigit() and lower <= int(number) <= upper):
        return True


def is_valid(number):
    if  (number.isdigit() and 1 <= int(number) <= 100):
        return True



def play_game():

    print('Добро пожаловать в программу угадай число!')


    while True:
        random_str = input("Если хотите ввести границы случайного числа нажмите (y/n) ")
        if random_str == "y":
            lower = int(input("Нижняя граница: "))
            upper = int(input("Вверхняя граница: "))
            random_number = random.randint(lower, upper)
            cnt = 0
            print("Рандомное число:", random_number)
            number = (input(f"Введите число от {lower} до {upper}: "))
            break
        else:
            random_number = random.randint(1, 100)
            cnt = 0
            print("Рандомное число:", random_number)
            break


    while True:

        if is_valid2(number, lower, upper):
            cnt += 1
            number = int(number)
            if number > random_number:
                print("Слишком много, попробуйте еще раз")
            elif number < random_number:
                print("Слишком мало, попробуйте еще раз")
            else:
                print("Вы угадали, поздравляем!", end="\n\n")
                break
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")

    print("Спасибо, что играли в программу угадай число.", end="\n\n")

    print("Количество попыток:", cnt)
    cnt = 0

# Сделать отдельную обработку для ввода границ

    while True:

        if is_valid(number):
            cnt += 1
            number = int(number)
            if number > random_number:
                print("Слишком много, попробуйте еще раз")
            elif number < random_number:
                print("Слишком мало, попробуйте еще раз")
            else:
                print("Вы угадали, поздравляем!", end="\n\n")
                break
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")

    print("Спасибо, что играли в программу угадай число.", end="\n\n")

    print("Количество попыток:", cnt)
    cnt = 0


    while True:
        number = input("Если хотите сыграть еще раз нажмите (y/n)")
        if number == "y":
            play_game()
        elif number == "n":
            break


play_game()

# Сделать обработку исключения для повторной игры
# Понять почему работает блок кода с 44 до 48 строки
# Добавить возможность указания границы для случайного выбора числа