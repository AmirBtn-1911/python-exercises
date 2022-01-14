class avg_finder:
    def find(self, scores):
        avg2 = avg1 = counter = 0
        while True:
            try:
                while counter < scores:
                    counter += 1
                    code = input('enter the %s student code : '%counter)
                    avg0 = float(input("enter the %s avg : " %counter));print()
                    if avg0 < 1 or avg0 > 20:
                        raise
                    if avg0 > avg1 :
                        avg2 = avg1
                        avg1 = avg0
                    elif avg0 > avg2 :
                        avg2 = avg0
                        st_code = code
                print(f'student code "{st_code} has the second highest score: {avg2}"')
                break
            except:
                print('wrong input, try again!')
                counter -= 1

class histogram:
    def echo(self, *LIST):
        LIST = list(LIST)
        print('your list is :', LIST)
        for i in LIST:
            plus = ''
            num = i
            spc = (3 - len(str(num))) * ' '
            while num > 0:
                plus += '+'
                num -= 1
            print(f'{i}{spc}: {plus}')

class fibonacci:
    def find(self, num):
        num3 = 1
        num1 = num2 = 0
        while True:
            if num3 >= num:
                break
            print(num3 , end=' ')
            num1 = num2 + num3
            num2 = num3
            num3 = num1

class geometry:
    def Circle(self,p,r):
        area = p * r * 2
        circumference = p * r * r
        print("\nYour Circle's area :",area,'\nAnd its circumference:', circumference)
    def Square(self, w):
        area = w * 4
        circumference = w**2
        print("\nYour Square's area :",area,'\nAnd its circumference:', circumference)
    def Rectangle(self, w,l):
        area = (w+l)*2
        circumference = w * l
        print("\nYour Rectangle's area :",area,'\nAnd its circumference:', circumference)

class vowels_finder:
    def __init__(self, text):
        A = E = U = I = O = 0
        for i in text:
            if i == 'a' or i == 'A':
                A += 1
            elif i == 'e' or i == 'E':
                E += 1
            elif i == 'u' or i == 'U':
                U += 1
            elif i == 'i' or i == 'I':
                I += 1
            elif i == 'o' or i == 'O':
                O += 1

        print('letter Aa counts :',A)
        print('letter Ee counts :',E)
        print('letter Uu counts :',U)
        print('letter Ii counts :',I)
        print('letter Oo counts :',O)

class calculator:
    def __init__(self, num1, oper, num2):
        if oper == '*':
            result = num1 * num2
            print(f'\nResult: {num1} {oper} {num2} = {result}')
        elif oper == '/':
            result = num1 / num2
            print(f'\nResult: {num1} {oper} {num2} = {result}')
        elif oper == '+':
            result = num1 + num2
            print(f'\nResult: {num1} {oper} {num2} = {result}')
        elif oper == '-':
            result = num1 - num2
            print(f'\nResult: {num1} {oper} {num2} = {result}')

class ReversesTrue:
    def __init__(self, *w):
        for i in w:
            reverse = i[::-1]
            if reverse == i:
                print(reverse)

class UpperCase:
    def __init__(self, t):
        for i in t:
            if 122 >= ord(i) >= 97:
                print(chr((ord(i) - 32)),end = '')
            else:
                print(i,end = '')
        print()

class EncodeDecode:
    def Encode(self, t):
        for i in t:
            if i == ' ':
                continue
            print(ord(i), end = ' ')
        else:
            print()
    def Decode(self, t):
        t = t.split()
        for i in t:
            print(chr(int(i)), end = ' ')
        else:
            print()

class PhoneButtons:
    def __init__(self, t):
        dic = {1 : ',._?!',
        2 : 'abc',
        3 : 'def',
        4 : 'ghi',
        5 : 'jkl',
        6 : 'mno',
        7 : 'pqzs',
        8 : 'tuv',
        9 : 'wxyz',
        0 : ' '}
        dic2 = dic.copy()
        for n , m in dic2.items():
            dic2[n] = ''

        for i in t:
            for key in dic.keys():
                num = 1
                for letter in dic[key]:
                    if i == letter:
                        dic2[key] = str(dic2[key]) + ' + ' + str(num);break
                    num += 1

        for n , m in dic2.items():
            m = m.lstrip(' +')
            print(f"key {n} : {m}")
    
def end(program): print(f'\nEnd of the program {program}\n');
error = 'Wrong input, try again!'
while True:
    # try:
        print('--List of the programs--')
        print('1.Avarage finder')
        print('2.Histofram')
        print('3.Fibonacci')
        print('4.Geometry')
        print('5.vowels finder')
        print('6.Calculator')
        print('7.Normal = reversed')
        print('8.Upper text')
        print('9.Encode Decoder')
        print('10.Phone buttons')
        print('11.Posetive finer')
        print('12.File Copier')
        print('13.txt finder')
        print('14.TicTacToe')
        print('15.SHOP')
        option = input('enter the program number: ')

        if option == '1': # avarage finder
            while True:
                try:
                    num_scrs = int(input('enter the number of scores: '));print()
                    break
                except:
                    print(error)
            second_avg = avg_finder()
            second_avg.find(num_scrs)
            end(option)
        elif option == '2': # Histogram
            num_list = []
            while True:
                num = input('enter ur numbers (leave the input if u are finished): ')
                if num == '': break
                try:
                    num = int(num)
                    if num < 0: raise
                except:
                    print(error)
                    continue
                num_list = num_list + [num]
            histograms = histogram()
            histograms.echo(*num_list)
            end(option)
        elif option == '3': # Fibonacci
            while True:
                try:
                    number = int(input('enter a number and I show the fibonacci numbers shorter than ur number:'))
                    if number < 3:
                        raise
                    break
                except:
                    print('wrong input, try again!')
                    continue
            fibo = fibonacci()
            fibo.find(number)
            end(option)
        elif option == '4': # geometry
            enter = input('Circle, Square or Rectangle\nC for Circle, S for Square and R for Rectangle\nNow, choose(C-S-R):')
            geo = geometry()
            while True:
                if enter == 'C' or enter == 'c':
                    while True:
                        try:
                            radius = int(input('OK you choosed Square\nNow, enter its width: '))
                            if radius < 1:
                                raise
                            break
                        except:
                            print(error); continue
                    geo.Circle(3.14,radius);break
                elif enter == 'S' or enter == 's':
                    while True:
                        try:
                            width = int(input('OK you choosed Square\nNow, enter its width: '))
                            if width < 1:
                                raise
                            break
                        except:
                            print(error); continue
                    geo.Square(width);break
                elif enter == 'R' or enter == 'r':
                    while True:
                        try:
                            width = int(input('OK you choosed Rectangle\nNow, enter its width: '))
                            lengh = int(input('And its lengh: '))
                            if width < 1 or lengh < 1:
                                raise
                            break
                        except:
                            print(error);continue
                    geo.Rectangle(width,lengh);break
                else:
                    enter = input('Enter the correct form(C-S-R): ')
            end(option)
        elif option == '5': # vowels
            inpt = input('enter a text then I will find the vowels: ')
            vowels = vowels_finder(inpt)
            end(option)
        elif option == '6': # calculator
            while True:
                try:
                    number_1 = float(input('enter a number: '))
                    operation = input('enter the operation(/,*,+,-): ')
                    if operation == '*' or operation == '/' or operation == '+' or operation == '-':
                        pass
                    else:
                        raise
                    number_2 = float(input('enter the second number: '))
                    break
                except:
                    print(error);continue
            result = calculator(number_1, operation, number_2)
            end(option)
        elif option == '7': # ReversesTrue
            words = []
            while True:
                try:
                    word = input('enter ur words (leave the input wehn u are done): ')
                    if word == '':
                        break
                    words += [word]
                except:
                    print(error); continue
                print()
            reverses = ReversesTrue(*words)
            end(option)
        elif option == '8': # upper text
            while True:
                try:
                    text = input('Enter a text: ')
                    break
                except:
                    print(error); continue
            upper = UpperCase(text)
            end(option)
        elif option == '9': # encode decode
            while True:
                try:
                    choose = input('what do you wanna do? encode or decode? D for decode, E for encode: ')
                    if choose == 'D' or choose == 'd':
                        text = input('ok you choosed decode, give me your codes then I will decode it for you (): ')
                        decode = EncodeDecode()
                        decode.Decode(text)
                    elif choose == 'E' or choose == 'e':
                        text = input('ok you choosed encode, give me a sentence to encode it for you: ')
                        encode = EncodeDecode()
                        encode.Encode(text)
                    else:
                        raise
                    break
                except:
                    print(error); continue
            end(option)
        elif option == '10': # phone buttons
            while True:
                try:
                    text = input('enter your text: ')
                    buttons = PhoneButtons(text)
                    break
                except:
                    print(error); continue
            end(option)
        elif option.lower() == 'end':
            break
