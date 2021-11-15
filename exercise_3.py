num_scrs = int(input('enter the number of scores: ')) #3
avg2 = avg1 = counter = 0
while counter < num_scrs: # 5 10 15
    counter += 1
    avg0 = float(input("enter the %s avg : " %counter))
    if avg0 > avg1 :
        avg2 = avg1
        avg1 = avg0
    elif avg0 > avg2 :
        avg2 = avg0
print(avg2)
