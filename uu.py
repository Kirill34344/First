import random

num = [1, 2, 3, 4, 5]
print(num[0:5])

for i in range(5):
    a = int(random.random() * len(num))
    b = int(random.random() * len(num))
    num[a], num[b] = num[b], num[a]


print(num)
