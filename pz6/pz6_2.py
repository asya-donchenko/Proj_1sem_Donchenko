# 2. Даны два списка A и B одинакового размера N. Сформировать новый список C того
# же размера, каждый элемент которого равен максимальному из элементов списков
# A и B.

import random

N = random.randrange(2, 15)
a = [random.randrange(1, 15) for i in range(N)]
b = [random.randrange(1, 15) for i in range(N)]
c = []

print("N:", N)
print("Array a:\n", a)
print("Array b:\n", b)

for i in range(0, N):
    c.append(max(a[i], b[i]))


print("Array c:\n", c)