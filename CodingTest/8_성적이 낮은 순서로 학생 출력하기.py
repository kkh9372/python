n = int(input())

dataset = []
for i in range(n):
    a, b = input().split()

    student = [a, int(b)]
    dataset.append(student)

#print(dataset)
scores = []
for i in range(len(dataset)):
    score = dataset[i][1]
    scores.append(score)

scores.sort()

names = []
for score in scores:
    for i, data in enumerate(dataset):
        if score == data[1]:
            names.append(data[0])
            dataset.pop(i)

print(names)