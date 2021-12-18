class number_creator:
    def __init__(self,pre):
        self.pre_number = pre
        self.file_name = pre + '.txt'
    def maker(self):
        with open(self.file_name,'w') as f:
            i = 0
            while i < 10000000:
                #      here the number of the '0's are the number of the numbers that should be put after 0936
                number = self.pre_number + ((7 - len(str(i))) * '0') + str(i)
                #                      here " " is the number of the numbers that should be put after 0936
                f.writelines(number + '\n')
                i += 1

cell = input('enter the 2 remaining numbers(for pre_number): 09')
cell = '09' + cell

number = number_creator(cell)
number.maker()

# i couldn't run this with my miserable and broken lap top, but it runs correctly