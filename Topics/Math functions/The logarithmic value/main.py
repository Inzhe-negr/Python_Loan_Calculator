from math import log

a, b = int(input()), int(input())
if b < 2:
    print(round(log(a), 2))
else:
    print(round(log(a, b), 2))
