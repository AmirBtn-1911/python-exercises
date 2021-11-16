print('enter two numbers to compare'+'\n')
while True:
    x = int(input('enter the first number : '))
    y = int(input('enter the secend number : '))
    if x == y :
        print('the number', x,'and', y,'are equal')
    elif x > y :
        print('the number', x,'is greater than', y)
    elif x < y :
        print('the number', x, 'is smaller than', y)
#the rest of the code bellow is optional, by deleting it, it wont affect on the progect
    print('\n'+'\n'+'ok enter another numbers'+'\n')
    continue
