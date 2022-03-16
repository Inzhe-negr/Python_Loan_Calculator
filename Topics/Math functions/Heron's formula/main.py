from math import sqrt

sides = [int(input()) for _ in range(3)]
p = sum(sides) / 2
a = p
for side in sides:
    a *= p - side
print(sqrt(a))
