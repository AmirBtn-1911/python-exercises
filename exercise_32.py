from datetime import datetime

old = str(datetime.now().second)
h = str(datetime.now().hour)
m = str(datetime.now().minute)
s = str(datetime.now().second)
print('time: ',h + ':' +  m + ':' + s)

while True:
    h = str(datetime.now().hour)
    m = str(datetime.now().minute)
    s = str(datetime.now().second)

    if old != datetime.now().second:
        print('updated: ' + h + ':' + m + ':' + s) # when I put end = ' ' in the print() my code won't run (whithout occurring any errors)
        old = datetime.now().second
    else:
        pass