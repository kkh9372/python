n = int(input())
array = []

for i in range(n):
    num = int(input())
    array.append(num)

array.sort(reverse=True)

for num in array:
    print(num, end='')