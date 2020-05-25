from itertools import count
from math import factorial


def fgen():
    for i in count(1):
        yield factorial(i)


generat = fgen()
x = 0
for a in generat:
    if x < 5:
        print(a)
        x += 1
    else:
        break
