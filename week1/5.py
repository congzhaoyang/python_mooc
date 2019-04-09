tempStr = input()

if tempStr[0:3] == 'RMB':
  temp = eval(tempStr[3:]) / 6.78
  print("USD{:.2f}".format(temp))
elif tempStr[0:3] == 'USD':
  temp = eval(tempStr[3:]) * 6.78
  print("RMB{:.2f}".format(temp))
else:
  print('输入格式错误')