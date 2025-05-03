import random


a = [1, 2, 3, 4, 5]



for i in range(5):
    b = round(random.random() * 4)
    print(a[b])