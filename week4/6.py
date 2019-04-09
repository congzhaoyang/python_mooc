import math

sum = 0

def isPrime(i):
  if i <= 1:
    return False
  for k in range(2, int(math.sqrt(i)) + 1):
    if i % k == 0:
      return False
  return True

for i in range(2, 101):
  if(isPrime(i)):
    sum += i

print(sum)
  