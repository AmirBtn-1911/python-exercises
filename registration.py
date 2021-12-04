import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def registeration():
    global username , password
    username = input('make an username (ID): ')
    password = input('now make a password: ')
    confirm = input('Ok, now enter CONFIRM , if you want to make a profile, if not, enter anything else: ')
    if confirm == 'CONFIRM':
        clearConsole()
        def SignIn():
            SI_username = input('enter your username: ')
            if SI_username == username:
                SI_password = input('enter the password: ')
                if SI_password == password:
                    print('welcome')
                else:
                    print('incorrect password.')
                    #not yet created a loop
            else:
                print('incorrect username.')
                #not yet created a loop
        SignIn()
    else:
        clearConsole()
        print('Okay then ,bye.')

registeration()
#how to link a python script to a HTML file !!!