s = input()

opStr = ['+', '-', '*', '/']

tag = -1
flag = True
m = ''
n = ''

if s[0] == '-':
  flag = False
  s = s[1:]

for i in range(len(s)):
  if s[i] in opStr:
    tag = i

for i in range(tag + 1):
  if(s[i] != ' ' and s[i] not in opStr):
    m += s[i]

for i in range(tag + 1, len(s)):
  if(s[i] != ' '):
    n += s[i]

result = 0
m = eval(m)
n = eval(n)
op = s[tag]

if op == '+':
  result = m + n
elif op == '-':
  result = m - n
elif op == '*':
  result = m * n
else:
  result = m / n

if flag == False:
  result = -result

print('{:.2f}'.format(result))