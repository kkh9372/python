from bisect import bisect_left

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자: '))

pos = bisect_left(dataset, value)
print('pos :', pos)

def BinarySearch(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target:
        return i
    else:
        return -1

value = int(input('검색할 숫자: '))
pos = BinarySearch(dataset, value)

if pos == -1:
    print('찾는 숫자 없음')
else:
    print('%d는 %d번째에 있음', (value, pos))