num1 = int(input('first number: '))
num2 = int(input('second number: '))

def decor(func):
    print('welcome to todays lecture:\n')
    def insidedecor(n1,n2):
        func(n1,n2)
        if n1 == 0 or n2 == 0:
            print('error: you entered zero in one of the inputs.\n')
        else:
            print(f"{n1} / {n2} = {n1 / n2}\n")
    return insidedecor

@decor
def math(n1,n2):
    return n1,n2
math(num1, num2)
print('end of todays lesson.bye')