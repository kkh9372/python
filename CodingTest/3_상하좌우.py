n =int(input())
x, y = 1, 1
plans = input().split()

for plan in plans:

    if plan == 'L':
        if y == 1:
            continue
        else:
            y -= 1

    if plan == 'R':
        if n == 1:
            continue
        else:
            y += 1

    if plan == 'U':
        if x == 1:
            continue
        else:
            x -= 1

    if plan == 'D':
        if x == n:
            continue
        else:
            x += 1
print(x, y)
