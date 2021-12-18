from os import name


class file_explorer:
    import sys
    def __init__(self,n = '', p = ''):
        self.name = n
        self.path = p
    def desk(self, name, path = ''):
        desk = self.sys.path[0].split('Desktop')
        desk_path = desk[0] + 'Desktop/'
        file = desk_path + '/' + path + '/' + name
        return file
    def same(self,name):
        file = self.sys.path[0] + '/' + name
        return file

print('This Python file, copy a file you want from any where in ur platform, then paste it to whenever you want\n')
while True:
    file_name = input('enter the file name you wanna copy it(including its .format): ')
    print('enter its location (Choose these options below) :')
    print('A. from same directory\nB. from desktop\nC. other (full path)')
    try:
        file = file_explorer()
        option = input('choose (A B C): ')
        if option == 'A' or option == 'a':
            file = file.same(file_name) 
        elif option == 'B' or option == 'b':
            file_path = input("if it's in desktop, leave the input, otherwise enter its path from Desktop: ")
            file = file.desk(file_name,file_path)
        elif option == 'C' or option == 'c':
            file_path = input('OK, enter its path: ')
            file = file_path + '/' + file_name
        else:
            raise NameError
    except NameError:
        print('an error has occurred: invalid input. enter again')

    try:
        with open(file,'r') as f:
            file_content = f.read()
        print('\nOK, this is the content of the file:\n')
        print(file_content + '\n') ; break
    except FileNotFoundError:
        print('invalid file path or name, again')

# copy function

print('lets go for copy function')
copy_file = file_explorer()
while True:
    copy_name = input('rename the file, otherwise leave the input(including its .format): ')
    if copy_name == '' or copy_name == ' ':
        copy_name = file_name
    print('choose one of these options: ')
    print('A. copy the file to Desktop directories\nB. same directory\nC. other(full path)')
    try:
        copy_file = file_explorer()
        option = input('Choose (A B C) : ')
        if option == 'A' or option == 'a':
            copy_path = input("if it's in desktop, leave the input, otherwise enter its path from Desktop: ")
            copy_file = copy_file.desk(copy_name,copy_path)
        elif option == 'B' or option == 'b':
            copy_file = copy_file.same(copy_name)
        elif option == 'C' or option == 'c':
            copy_path = input('OK, enter the full path')
            copy_file = copy_path + '/' + file_name
        else:
            raise NameError
    except NameError:
        print('invalid input, again')
    try:
        with open(copy_file,'w') as f:
            f.write(file_content)
        break
    except FileNotFoundError:
        print('invalid path or name(format), again')

print('mission accomplished, GoodBye.')