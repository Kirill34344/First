def arithmetic(arg1, arg2, op):
    
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    elif op == "*":
        return arg1 * arg2
    elif op == "/":
        return arg1 / arg2
    else:
        return "Неизвестная операция"


if __name__ == "__main__":
    try:
        arg1 = int(input("Введите первое число: "))
        arg2 = int(input("Введите второе число: "))
        op = input("Введите одну из представленных операций (+ - * /)")
        result = arithmetic(arg1, arg2, op)
        print("Результат:", result)
    except Exception as e:
        print("Ошибка: ", e)
