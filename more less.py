a = int(input())
b = int(input())
c = int(input())

if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

print(min_num)