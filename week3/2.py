# the power of daydayup

def dayUp(df):
  dayup = 1
  for i in range(365):
    if i % 7 in [6, 0]:
      dayup = dayup * 0.99
    else: 
      dayup = dayup * (1 + df)
  return dayup

dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
  dayfactor += 0.01

print("工作日努力参数是：{:.3f}".format(dayfactor))