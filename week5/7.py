import random

def genpwd(length):
    a = pow(10, length - 1)  # 定义一个下限
    b = pow(10, length) - 1  # 定义一个上限
    return "{}".format(random.randint(a, b))
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))