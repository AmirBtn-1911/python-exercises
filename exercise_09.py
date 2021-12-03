n = int(input('enter your number : '))
i = 2
# for i in range(2,n):
#     if n % i == 0:
#         n = int(input('again: '))
#         i = 2
while i < n:
    if n % i == 0:
        i = 2
        n = int(input('again'))
    elif n % i != 0:
        i += 1


#not yet finished
