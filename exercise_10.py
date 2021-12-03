enter = input('Circle, Square or Rectangle\nC for Circle, S for Square and R for Rectangle\nNow, choose(C-S-R):')
# <function>
def Circle(p,r):
    area = p * r * 2
    circumference = p * r * r
    print("\nYour Circle's area :",area,'\nAnd its circumference:', circumference)
def Square(w):
    area = w * 4
    circumference = w**2
    print("\nYour Square's area :",area,'\nAnd its circumference:', circumference)
def Rectangle(w,l):
    area = (w+l)*2
    circumference = w * l
    print("\nYour Rectangle's area :",area,'\nAnd its circumference:', circumference)
# </function>
# <condition>
while True:
    if enter == 'C' or enter == 'c':
        radius = int(input('Ok you choose Circle\nNow, enter its Radius: '))
        Circle(3.14,radius);break
    elif enter == 'S' or enter == 's':
        width = int(input('OK you choose Square\nNow, enter its width: '))
        Square(width);break
    elif enter == 'R' or enter == 'r':
        width = int(input('OK you choose Rectangle\nNow, enter its width: '))
        lengh = int(input('And its lengh: '))
        Rectangle(width,lengh);break
    else:
        enter = input('Enter the correct form(C-S-R): ')
# </condition>