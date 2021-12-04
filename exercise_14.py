members = {1:3,2:2,3:4,4:1,5:5,6:3,7:2,8:3}
cost = int(input('enter the water price: '))
def operation(m):
    person = cost / m
    for i in members:
        unit = person * members[i]
        print('unit %s : %.0f tumans'%(i,unit))
operation(len(members))