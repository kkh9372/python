
def binary_search(dataset, target):
    start = 0
    end = len(dataset) - 1
    pos = -1

    while start <= end:
        mid = (start + end) // 2

        if dataset[mid] > target:
            end = mid - 1
        elif dataset[mid] < target:
            pos = mid
            break
    return pos

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자: '))

pos = binary_search(dataset, value)

if pos == -1:
    print('찾는 숫자 없음')
else:
    print('%d는 %d번째에 있음' % (value, pos))