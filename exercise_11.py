text = input('enter tour word : ')

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
