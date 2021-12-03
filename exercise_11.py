text = input('enter your word/sentence : ')

A = E = U = I = O = 'No result.'
for i in text:
    if i == 'a' or i == 'A':
        A = 0
        A += 1
    elif i == 'e' or i == 'E':
        E = 0
        E += 1
    elif i == 'u' or i == 'U':
        U = 0
        U += 1
    elif i == 'i' or i == 'I':
        I = 0
        I += 1
    elif i == 'o' or i == 'O':
        O = 0
        O += 1

print('letter Aa counts :',A)
print('letter Ee counts :',E)
print('letter Uu counts :',U)
print('letter Ii counts :',I)
print('letter Oo counts :',O)
