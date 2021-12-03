values = []
index = 0
th = ''
# I put        11 because i started counting on number 0, so there are 12 numbers between 0 an 11
while index <= 11 :
    count = index + 1
    # This is an extra code for exercise (will be discussed) to line 18
    if -1<count<10  :
        countth = ('0'+str(count))
    else:
        countth = str(count)
    if countth[-1] == '1' and countth[-2] != '1':
        th = 'st'
    elif countth[-1] == '2' and countth[-2] != '1':
        th = 'nd'
    else :
        th = 'th'
    # Here
    salary = int(input('enter the amount of the {} month salary : '.format(countth + th)))
    values.insert(index,salary)
    index += 1
sumsalary = sum(values)
avgsalary = (sum(values)/count)
#                        I tried to find another way to put 4spaces but I realised nothing
print("\nThe whole salary in the passed year is :%4s%.2f"  %('',sumsalary))
print("The avarage of your salary is :%4s%.2f" %('',avgsalary))
