num1 = int(input('enter an integer: '))
operation = input('enter the operation(/,*,+,-)')
while True:
    if operation == '*' or operation == '/' or operation == '+' or operation == '-':
        break
    else:
        operation = input('incorrect operation, enter again (/,*,+,-) : ')
num2 = int(input('enter an integer(secend number): '))
if operation == '*':
    result = num1 * num2
    print('Result:',result)
elif operation == '/':
    result = num1 / num2
    print('Result:',result)
elif operation == '+':
    result = num1 + num2
    print('Result:',result)
elif operation == '-':
    result = num1 - num2
    print('Result:',result)