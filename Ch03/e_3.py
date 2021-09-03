n = 0

for i in range(1, 101):
    n += i
    if(n % 3 == 0 and n % 2 != 0):
        print('수열=', n)

