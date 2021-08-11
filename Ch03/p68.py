# (1) random 모듈 관련 함수 도움말
import random
help(random.randint)
help(random.choices) # 모집단에서 k 크기 목록 반환

# (2) 
names = ['홍길동', '이순신', '유관순']
print(names)
print(names[2])

# (3)
if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

# (4)

idx = random.randint(0, 2)
print(names[idx])