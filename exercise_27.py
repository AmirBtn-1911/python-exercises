inpt = input('input: ')
word = 0
i = j = 0
while i < len(inpt):
    if len(inpt) < 2:
        print('go away u dum.')
        break
    elif inpt[i] != ' ' and inpt[i+1] != ' ':
        word += 1
        while inpt[i] == ' ':
            i += 1
        else:
            i += 1
    elif inpt[i] == 'a':
        word += 1
        i += 2
    else:
        i += 1

# not yet finished