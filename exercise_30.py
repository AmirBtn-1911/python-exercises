# a = 97 122     A = 65 91
enter = input('input: ')
i = 0
while i < len(enter):
    if  i == 0 and 122 >= ord(enter[i]) >= 97:
        print(chr(ord(enter[i]) - 32),end = '')
    elif enter[i-1] == ' ' and 122 >= ord(enter[i]) >= 97:
        print(chr(ord(enter[i]) - 32),end = '')
    else:
        print(enter[i],end = '')
    i += 1
print()
