inpt = input('input: ')
i = 0
while True:
    if len(inpt)-1 ==  i:
        print(ord(inpt[i]))
        break
    if inpt[i+1] == ' ':
        print(ord(inpt[i]),end = '  ')
    elif inpt[i] != ' ':
        print(ord(inpt[i]),end = '_')
    i += 1