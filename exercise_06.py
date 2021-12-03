#the code bellow is copy!!!
# def fibonacci(n):
#     if n<0:
#         print('incorrect input.')
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))

#this is mine:  (seriously)         0 1 1 2 3 5 8 13 21 ...     fibonacci       !!!First attempt
# in_num = int(input('enter a number : '))
# num4 = num1 = 0
# num2 = num3 = 1
# if in_num > 0 :
#     while in_num >= num4 :
#         if num3 + num2 >= in_num:
#             break
#         else:
#           num4 = num3 + num2
#           num2 = num3
#           num3 = num4
#           num1 = num2
#         print(num4 , ' ' , end='')
#         continue
# else:
#     print('unsopported number!')

#secend attempt
num3 = 1
num1 = num2 = 0
n = int(input('enter a number :'))
while True:
    if num3 >= n:     #here
        break
    print(num3 , end=' ')
    # num1 = num2 + num3
    # num2 = num3
    # num3 = num1

    #both sides work!!! but you should change the condition(if)

    num1 = num2
    num2 = num3
    num3 = num1 + num2
