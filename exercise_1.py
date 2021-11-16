name = input('Hello, write your name here : ')
print('Hello',name)
age = int(input('now write your age here : '))
if age > 105 or age < 0:
    print('the number is invalid.')
elif age >= 18:
    print('welcome to site',name)
else:
    print('dear',name + ',you are not allowed to enter the site.')
