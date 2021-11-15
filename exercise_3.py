num_scrs = int(input('enter the number of scores: ')) #3
avg2 = avg1 = count = 0
while count < num_scrs: # 5 10 15
    count += 1
    avg0 = float(input("enter the %s avg : " %count))
    if avg0 > avg1 :
        avg2 = avg1
        avg1 = avg0
    elif avg0 > avg2 :
        avg2 = avg0
print(avg2)
