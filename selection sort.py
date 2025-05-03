numbers = [2, 1, 3, 4, 7, 11, 1, 0, 1, 0]


for i in range(len(numbers)):
    min = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min]:
            min = j
    numbers[i], numbers[min] = numbers[min], numbers[i]

print(numbers)


# Запомнить текущий элемент как первый
# Берется наименьшее число которые правее и включают текущий элемент
# меняются местами
# Текущий элемент становится следующим
# Повторять 2 - 4 пока текущий элемент не стал последним
