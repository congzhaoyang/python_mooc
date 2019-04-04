inputStr = input()
numStr = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
result = ''

for s in inputStr:
  temp = eval(s)
  result += numStr[temp]
  
print(result)