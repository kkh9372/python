num = 9
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2
print('result =', result)

# 3항 연산자

result2 = num * 2 if num >= 5 else num + 2
print('result2 =', result2)