import os
import random
import time
from typing import Counter

os.system('cls' if os.name == 'nt' else 'clear')

def sorter(number1,number2,number3,   last = False):
    td = '  ' + number1 + '  |  '+ number2 + '  |  ' + number3 + '  '
    if last == False:
        line = len(td) * '-'
        return  ' ' + td + '\n' + ' ' + line
    return ' ' + td

def winner(*l):
    l = list(l)
    for i in [0,3,6]:
        if l[i] == l[i+1] == l[i+2]:
            return True and l[i]
    for i in [0,1,2]:
        if l[i] == l[i+3] == l[i+6]:
            return True and l[i]
    if l[0] == l[4] == l[8]:
        return True and l[0]
    
    if l[2] == l[4] == l[6]:
        return True and l[2]
count = 0
def dooz(XO, *l):
    global count
    os.system('cls' if os.name == 'nt' else 'clear')
    print(' ~~ Tic-Tac-Toe ~~\n')
    l = list(l)
    print(sorter(l[0],l[1],l[2]))
    print(sorter(l[3],l[4],l[5]))
    print(sorter(l[6],l[7],l[8],True))
    if winner(*l):
        print(f'\n\nCongratulations, Player "{winner(*l)}" won the game!!!\nnumber of the moves: {count}\n\n')
        return True
    again = ''
    count += 1
    while True:
        choose = input(f'\n{count}. {again}player "{XO}", enter the cell: ')
        if choose == '':
            break
        i = 0
        while i < len(l):
            if l[i] == choose:
                l[i] = XO ; break
            i += 1
        else:
            again = 'wrong inpput, again\n'
            continue
        if XO == 'X' :
            return dooz('O', *l)
        elif XO == 'O':
            return dooz('X', *l)

numbers = ['1','2','3','4','5','6','7','8','9']
print(' ~~ Tic-Tac-Toe ~~\n')
print('Welcome, this is TicTocToe game\n')
print('who wants to begin first, Choose between "X" and "O"')
player = input('or if you want the game select randomly, enter "random"\n(X - O - random) : ')

while True:
    if player.lower() == 'random':
        player = random.choice(['X','O'])
    elif player == 'X' or player == 'x':
        player = 'X' ; break
    elif player == 'O' or player ==  'o':
        player = 'O' ; break
    else:
        player = input('wrong input! choose between "X" and "O" : ')

os.system('cls' if os.name == 'nt' else 'clear')
print(' ~~ Tic-Tac-Toe ~~\n')
print(f'OK, player "{player}" has the first move\n')
time.sleep(1)
for i in range(3,0,-1):
    print(f'the game will begins in   {i}  ', end = '\r')
    time.sleep(1)

dooz(player, *numbers)
