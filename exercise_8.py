numbers = [10,20,1,.5,25,.6,.05,100,1001,100,200]
max = 0
min = numbers[0]
i = 0

# # for loop
# for i in numbers:
#     if i > max :
#         max = i
#     if i < min:
#         min = i

# while loop
while i < len(numbers):
    if numbers[i] > max:
        max = numbers[i]
    if min > numbers[i]:
        min = numbers[i]
    i += 1

print('the largest number is :',max)
print('the smallest number is :',min)

# I tried to run it via functions, but it will eccure an error called local statement(you havent tought this yet)