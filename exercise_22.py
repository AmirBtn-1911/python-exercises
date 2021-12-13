inpt = input('input: ')
def checker(i):
    index = 0
    if len(i) < 10:
        print('u entered an input less than 10 characters', end = '')
    else:
        while index < len(i):
            print(i[index],end = '')
            if index > 9:
                if i[index:(index - 9):-1] == 'namezeerf': # haha, nice move (to myself)
                    print(' "Python tutorials by freezeman" ', end = '')
            index += 1
    print()
checker(inpt)