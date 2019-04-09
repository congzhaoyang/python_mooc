tempStr = input()

if tempStr[0] in ['F', 'f']:
  temp = (eval(tempStr[1:]) - 32) / 1.8
  print("C{:.2f}".format(temp))
elif tempStr[0] in ['C', 'c']:
  temp = eval(tempStr[1:]) * 1.8 + 32
  print("F{:.2f}".format(temp))
else:
  print('输入格式错误')