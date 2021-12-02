num = 1
res = 0
while num <= 10:
    i = 1
    while i <= 10:
        res = i * num
        print("%4i"%res,end='')
        i += 1
    print()
    num += 1
