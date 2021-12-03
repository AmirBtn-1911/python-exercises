#first part
# print('First Part')
# n = int(input('enter a number: '))
# print(n, n * '+'+'\n')

#secend part
print('Secend Part')
list = [3,7,16,8,6]
for index in list:

    # Multiplication *
    #print("%2i%s"%(index,index * '+'))

    # Plus action +
    print(index, end='')
    while index > 0 :
        print('+' , end='')
        index -= 1
    else:
        print()
