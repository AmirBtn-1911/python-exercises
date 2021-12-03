# this is the exact code the teacher wrote
num_scrs = int(input('enter the number of scores: '));print()
avg2 = avg1 = counter = 0
while counter < num_scrs:
    counter += 1
    code = input('enter the %s student code : '%counter)
    avg0 = float(input("enter the %s avg : " %counter));print()
    st_num = {counter : code}
    if avg0 > avg1 :
        avg2 = avg1
        avg1 = avg0
    elif avg0 > avg2 :
        avg2 = avg0
        st_code = code  
print(avg2,st_code)
