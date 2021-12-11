tup = (19,19.5,14,16,11,15.5,16.5,16,15,12.5,17,18.5)
all = 0
for i in tup:
    all += i
avg = all / len(tup)
# print(f"you have {len(tup)} scores, overall scores is {all} , and avarage is {avg}.")
# print("you have %i scores, overall scores is %.2f, and avarage is %.2f."%(len(tup),all,avg))
# print("you have {} scores, overall scores is {}, and avarage is {}.".format(len(tup),all,avg))