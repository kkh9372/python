"""
날짜 : 2021/10/15
이름 : 김관후
내용 : 코딩테스트 - 다이나믹 프로그래밍 피보나치 바텀업 처리

다이나믹 프로그램이 바텀업(Bottom-Up)
- 반복문을 이용하여 문제를 해결하는  프로그래밍 방식
- 작은 문제부터 차근차근 해결해 나가는 방식
"""
import time

# 프로그램 실행 시간 시작
start_time = time.time()

# DP(Dynamic Programming) 테이블 생성
d = [0] * 100
d[0] = 0
d[1] = 1

print(d[0])
print(d[1])

# 피보나치 반복문 처리
for n in range(2, 40):
    d[n] = d[n-1] + d[n-2]
    print(d[n])

# 프로그램 실행 시간 종료
end_time = time.time()

# 전체 수행시간
total_time = end_time - start_time
print('프로그램 수행시간 :', total_time)
