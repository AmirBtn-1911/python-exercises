# main topic
def echo():
    input_ = input('input: ')
    def character(inpt):
        l_inpt = inpt.split()
        for i in l_inpt:
            i = int(i)
            print(chr(i),end = '')
        else:
            print()
    def unicode(inpt):
        for i in inpt:
            print(ord(i),end = ' ')
        else:
            print()
    if 49<= ord(input_[0]) <=57:
        character(input_)
    else:
        unicode(input_)
# echo()

# enter any kind of input, it will work without any problem
# (don't forget to seperate the character numbers(no greater than 255) by ' '(space))
def echo2():
    input_ = input('enter anything, but seperate the character numbers by a "space": ')
    i = 0
    while i < len(input_):
        if 49<= ord(input_[i]) <=57:
            num = input_[i]
            if len(input_) > i+1 and input_[i+1] != ' ':
                num = num + input_[i+1]
                i+=1
                if len(input_) > i+1 and input_[i+1] != ' ':
                    num = num + input_[i+1]
                    i+=1
            print(chr(int(num)),end = '')
        elif input_[i] == ' ':
            print(end='')
        else:
            print(f" '{ord(input_[i])}' ",end = '')
        i += 1
    print()
# echo()
echo2()
