num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
c = (input("Выберите одну из операций: + - / * "))

if c == "+":
    result = num1 + num2
    print(result)

elif c == "-":
    result = num1 - num2
    print(result)

elif c == "/":
    result = num1 / num2
    print(result)

elif c == "*":
    result = num1 * num2
    print(result)
