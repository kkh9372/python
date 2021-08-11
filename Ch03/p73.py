# (1) list에 자료 저장하기
import random

lst = []
for i in range(10):
    r = random.randint(1, 10)
    lst.append(r)
print('lst=', lst)

# (2) list에 자료 참조하기
for i in range(10):
    print(lst[i] * 0.25)