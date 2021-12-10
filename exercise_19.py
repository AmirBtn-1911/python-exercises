# a = 97 122     A = 65 91
enter = input('input: ')
for i in enter:
    if 122 >= ord(i) >= 97:
        print(chr((ord(i) - 32)),end = '')
    else:
        print(i,end = '')
print()
