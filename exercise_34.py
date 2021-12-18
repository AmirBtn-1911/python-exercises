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

class text_finder:
    def __init__(self,t = '',f = ''):
        self.text = t
        self.file = f
    def finder(self,text,file):
        line = 0
        with open(file,'r') as f:
            content = f.readlines()
            for i in content:
                amount = f'no'
                index = i.find(text)
                if index == -1:
                    pass
                else:
                    amount = 1
                    while True:
                        if i.find(text, index + len(text)) == -1:
                            break
                        else:
                            index = i.find(text, index + len(text))
                            amount += 1
                line += 1
                print(str(amount) , f'"{text}" in line {line}')

import sys

# if you didn't enter a argv before executing the file, it aoutomatically asks you for file name :)
argv = sys.argv
if len(argv) > 1:
    file_name = argv[1]
else:
    file_name = input('enter the file name (same directory) : ')
text = input('enter the text: ')
file = file_explorer()
file = file.same(file_name)
texts = text_finder()
texts.finder(text,file)

# one of the classes are belong to last exercise (file_explorer)
# realy worked on it