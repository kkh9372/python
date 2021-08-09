num1 = 100 # 피연산자1
num2 = 200 # 피연산자2

#두 관계식이 모두 같은지 판단
log_result = num1 >= 50 and num2 <=10
print(log_result)

#두 관계식 중 하나라도 같은지 판단
log_result = num1 >= 50 or num2 <=10
print(log_result)


log_result = num1 >= 50  #관계식 판단
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)