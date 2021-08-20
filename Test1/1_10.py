"""
날짜 : 2021/08/12
이름 : 김관후
내용 : 파이썬 선택정렬 연습문제
"""

dataset = [3, 5, 1, 2, 4]
size = len(dataset)

for i in range(size - 1):

    for j in range(i+1, size):

        if dataset[i] > dataset[j]:
            tmp = dataset[i]

            dataset[j] = tmp

    print('%d Round : %s' % (i, dataset))

print('Result :', dataset)