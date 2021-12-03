n = int(input('enter your number : ')); i = 2
while True:
    while i < n:
        if n % i == 0:
            n = int(input('entered number is not a prime number, enter again: '));continue
        elif n % i != 0:
            i += 1;continue
    print('the number is prime number, goodbye');break
