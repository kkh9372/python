"""
날짜 : 2021/10/15
이름 : 김관후
내용 : 코딩테스트 - 다이나믹 프로그래밍 피보나치 탑다운 처리

다이나믹 프로그램이 탑다운(Top-Down)
- 재귀함수와 메모이제이션을 이용한 프로그래밍 방식
- 큰 문제를 해결하기 위해 작은 문제를 해결해 나가는 방식
"""
import time

# 프로그램 실행 시간 시작
start_time = time.time()

# DP(Dynamic Programming) 테이블 생성
d = [0] * 100
#print(d)

# 피보나치 함수
def fibo(n):
    if n <= 1:
        return n

    # 이미 계산한 적 있는 문제이면 DP테이블값 반환
    if d[n] !=0:
        return d[n]
    
    # 연산의 결과를 메모이제이션
    d[n] = fibo(n-1) + fibo(n-2)

    return d[n]

for i in range(40):
    print(fibo(i))

# 프로그램 실행 시간 종료
end_time = time.time()

# 전체 수행시간
total_time = end_time - start_time
print('프로그램 수행시간 :', total_time)
print(d)
