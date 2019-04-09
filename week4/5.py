for i in range(1000, 10000):
  s = str(i)
  p1, p2, p3, p4 = eval(s[0]), eval(s[1]), eval(s[2]), eval(s[3])
  temp = pow(p1, 4) + pow(p2, 4) + pow(p3, 4) + pow(p4, 4)
  if temp == i:
     print(s)