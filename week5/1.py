# CalStatisticsV1.py
def getNum():
  nums = []
  iNumStr = input("input num(press enter to exit:")
  while iNumStr != '':
    nums.append(eval(iNumStr))
    iNumStr = input("input num(press enter to exit:")
  return nums

def mean(numbers):
  s = 0.0
  for num in numbers:
    s += num
  return s / len(numbers)

def dev(numbers, mean):
  sdev = 0.0
  for num in numbers:
    sdev += pow(num - mean, 2)
  sdev = pow(sdev / (len(numbers) - 1), 0.5)
  return sdev

def median(numbers):
  sorted(numbers)
  size = len(numbers)
  if size % 2 == 0:
    med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
  else:
    med = numbers[size // 2]
  return med
  
n = getNum()
m = mean(n)
print("mean value:{}, devation value:{}, median value:{}".format(m, dev(n, m), median(n)))