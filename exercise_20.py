def Anonymous(name,flag):
    if flag == 'encode':
        for i in name:
            print(ord(i), end = ' ')
    if flag == 'decode':
        name = name.split()
        for i in name:
            print(int(chr(i)))
# enter ur name in first parameter and put encode for encoding your input, or
# enter ur code in first parameter and put decode for decoding your input
Anonymous('amir','encode')