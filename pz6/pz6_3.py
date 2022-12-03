# 3. Даны множества A и B, состоящие соответственно из N1 и N2 точек (точки заданы
# своими координатами x, у). Найти минимальное расстояние между точками этих
# множеств и сами точки, расположенные на этом расстоянии (вначале выводится
# точка из множества A, затем точка из множества B).

import random

N1, N2 = 5, 10
points1 = [(random.random(), random.random()) for i in range(N1)]
points2 = [(random.random(), random.random()) for i in range(N2)]

def dist(x, y): return (x[0]-y[0])**2+(x[1]-y[1])**2
s = dist(points1[0], points2[0])
pos = 0, 0

for i in range(N1):
    for j in range(N2):
        if s > dist(points1[i], points2[j]):
            s = dist(points1[i], points2[j])
            pos = i, j
print(points1[pos[0]], points2[pos[1]], s**0.5, sep='\n')