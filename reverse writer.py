s = input('enter : ')
sl = -len(s)
i = -1
def rev1(i1):
    if i1 == sl:
        print(s[i1])
    else:
        print(s[i1], end='')
        rev1(i1-1)
#rev1(i)

def rev2(i2,st):
    if i2 == sl:
        return s[i2]
    return (st + rev2(i2-1, s[i2-1]))
# print(rev2(0, ''))