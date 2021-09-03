import random

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

# 가장 큰 수 ,두번째로 큰 수
first = data[0]
second = data[1]

result = 0
repeat = k

for i in range(m):

    if repeat > 0:
        result += first
        repeat -= 1
    else:
        result += second
        repeat = k

print(result)


