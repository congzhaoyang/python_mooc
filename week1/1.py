tempStr = input()

if tempStr[-1] in ['F', 'f']:
  temp = (eval(tempStr[0: -1]) - 32) / 1.8
  print("{:.2f}C".format(temp))
elif tempStr[-1] in ['C', 'c']:
  temp = eval(tempStr[0: -1]) * 1.8 + 32
  print("{:.2f}F".format(temp))
else:
  print('输入格式错误')