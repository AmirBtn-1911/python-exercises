# about fu**ing 5 hours 
names = []
cost_wight = {}

def sort(n, c, w):
    '''centering and sorting'''
    n = str(n); c = str(c); w = str(w)
    def cen(word,num):
        spaces = num - (len(word))
        if spaces % 2 != 0:
            spc1 = int(spaces / 2)
            spc2 = int(spaces / 2) + 1
            return (spc1*' ') + word + (spc2*' ')
        elif spaces % 2 == 0:
            spc = int(spaces / 2)
            return (spc*' ') + word + (spc*' ')
    print(cen(n,20) + '|' + cen(c,14) + '|' + cen(w,14))

def table(**c_w):
    '''making table of stats'''
    global costs , weights
    i = 0
    sort('product name','cost($)','weight(g)')
    print(50*'~')
    costs = list(c_w.keys())
    weights = list(c_w.values())
    while i < len(names):
        sort(names[i],costs[i],weights[i])
        i += 1

def summer():
    '''shows the overall weights and costs'''
    print(50*'=')
    sum_cost = sum_weight =  0
    for i in costs:
        sum_cost += int(i)
    for i in weights:
        sum_weight += int(i)
    sort('overall', sum_cost, sum_weight)

while True:
    name = input('product name : ')
    if name == 'end':
        break
    cost = input('its cost: ')
    weight = input('its weight: ')
    names.append(name)
    cost_wight.update({cost:weight})
    print()
print()

table(**cost_wight)
summer()
