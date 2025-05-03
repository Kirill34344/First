cnt = 0

nb1 = int(input("Введите первое число: "))

nb2 = int(input("Введите второе число: "))

for i in range(nb1, nb2 + 1):
    cnt += i

print(cnt)
