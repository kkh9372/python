num1 = 100 # 피연산자1
num2 = 200 # 피연산자2

# (1) 동등비교
bool_result = num1 == num2  # 두 변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2  # 두 변수의 값이 다른지 비교
print(bool_result)

# (2) 크기비교
bool_result = num1 > num2  # num1 값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2  # num1 값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2   # num2 값이 큰지 비교
print(bool_result)
bool_result = num1 <= num2  # num2 값이 크거나 작은지 비교
print(bool_result)