from random import random, seed

DARTS = eval(input())
# seed(1234)
hits = 0
for i in range(DARTS):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("{:.6f}".format(pi))