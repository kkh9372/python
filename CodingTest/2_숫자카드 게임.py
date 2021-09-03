n, m = map(int, input().split())
mins = []
result = 0

for i in range(n):
    # 행 데이터 입력하기
    data = list(map(int, input().split()))
    
    # 데이터 오름차순 정렬
    data.sort()
    
    # 최소값 구하기
    min = data[0]
    
    # 각 행의 최소값 저장하기
    mins.append(min)
result = max(mins)

print(result)