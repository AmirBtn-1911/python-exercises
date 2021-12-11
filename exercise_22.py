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
inpt = input('input: ')

for i in inpt:
    for key in dic.keys():
        num = 1
        for letter in dic[key]:
            if i == letter:
                dic2[key] = str(dic2[key]) + ' + ' + str(num);break
            num += 1

for n , m in dic2.items():
    m = m.lstrip(' +')
    print(f"key {n} : {m}")

# 26 lines without spaces :) - 9 lines for dictionary