# score = 19
# if score >= 15:
#     print('you passed')
# elif score > 20:
#     print('number is invalid')
# elif score < 15:
#     print('you failed')

# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
#
# sum = 0
#
# for val in numbers:
#     sum = sum + val
#
# print("The sum is", sum)

# i = 0
# while i < 10:
#     i += 1
#     print (i)

# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum = 0
# i = 0
#
# for val in numbers:
#     sum = sum + val
#     i = i + 1
#     print(i, " : The sum is", sum, 'number ', val)

# numbers = [23,12,3,4,5,2,23,39]
# i= 0
# for i in numbers:
#
# counter = 0
#
# while counter < 3:  # 0 1 2
#     counter = counter + 1
#     print(counter)
#
# else:
#     print("Inside else")

# def amir():
#     x = 1
#     if x > 1:
#         print(x * 5)
#     else:
#         print(x * 2)
#
# amir()

# def number_check(number):
#     '''this func, check the number'''
#
#     if number > 6:
#         i = 3
#         while i:
#             i-=1
#             print('freezeman')
#     elif  3>number>0:
#         print(number)
#     else:
#         print('chetory')
#
# number = int(input('type a number: '))
# number_check(number)

# def faak(number):
#     '''factorial'''
#number = int(input('enter a number :'))

# n = int(input('enter a number: '))
# print(n, n * '+')

# st_scores = int(input('enter the number of scores : '))
# av2 = av1 = counter = 0
# while counter < st_scores:
#     counter +=1
#     av0 = float(input("enter the %s avarage : " %counter))
#     if av0 > av1:
#         av2 = av1
#         av1 = av0
#     elif av0 > av2:
#         av2 = av0
# print(av2)

# n=int(input("enter  :"))
# x=z=0
# y=1
# while True:
#     if z >= n:
#         break
#     print(y,end='\t')
#     z=x+y
#     x=y
#     y=z

# n = 5
# t =c =1
# while c<=n :
#     t = t*c
#     c += 1
# print(t)

# n=5
#
# if n < 0:
#     print('aa')
# else:
#     x = 1
#     while 1 <= n:
#         x *= n
#         n -= 1
#     print(x)

n = int(input('enter a number : '))
c1 = 1
while c1 <= n:
    print(c1 ,':', end='')
    c2 = 1
    while c2 <= c1:
        print('*',end = '')
        c2 += 1
    print()
    c1 += 1
