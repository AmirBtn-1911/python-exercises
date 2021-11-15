def factorial():
    '''the function, returns a factorial result'''
    num0 = int(input('enter a number to calculate its facctorial :  '))
    num1 = num2 = 0
    while num0 > 1:
        if num2 < num0:
            num1 = num0 - 1
            num2 = num0 * num1
            num0 -= 2
        elif num2 > num0:
            num2 = num2 * num0
            num0 -=1
    print(num2)
factorial()
