import random

words = ["1", "2", "3", "4", "5"]
n = len(words)
result = []

for i in range(n):
    index = int(random.random() * (n - i))
    result.append(words[index])
    words[index], words[n - i - 1] = words[n - i - 1], words[index]

print(result)
