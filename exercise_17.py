# 65 90   97 122
def echo():
    dic = {'chr' : '', 'ord' : ''}
    dic['chr'] = input('enter the chr() numbers(seperate them with a space):')
    dic['ord'] = input('enter a word to I give you its charecter uni codes: ')
    def checker(**d):
        check = d['chr'].split()
        for i in check:
            if 65<=int(i)<=90 or 97<=int(i)<=122:
                print(chr(int(i)),end = '  ')
            else:
                print('(invalid)' ,end= '  ')
        else:
            print()
        for i in d['ord']:
            print(ord(i),end = '  ')
        else:
            print()
    checker(**dic)
echo()
