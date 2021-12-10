# # # without built-in functions
# # words = ['amir','hossein','filif','hohoh','hello','minim','frined','dieid','oldlo','jimmy']
# words = ['','','','','','','','','','']
# i = 0
# while i < 10:
#     words[i] = input('input: ')
#     i += 1

# def checker(*w):
#     for i in w:
#         reverse = i[::-1]
#         if reverse == i:
#             print(reverse)
# checker(*words)

# # # why the code below eccure error???
# # words = ['','','','','','','','','','']
# # def add(*w):
# #     i = 0
# #     while i < 10:
# #         w[i] = input('input: ')
# #         i += 1
# #     print(words)
# # add(*words)

# # ---- with built-in functions -----
list = []
reverses = []
def add():
    q = int(input('how much words you wonna check? please enter a logical number: '))
    while q > 0:
        enter = input('input: ')
        list.append(enter)
        q -= 1
add()
def checker(*l):
    for i in l:
        reverse = i[::-1]
        if reverse == i:
            reverses.append(reverse)
    print(reverses)
checker(*list)

# my interpreater know *args as just a tuple object, no list!!! python 3.8.10
