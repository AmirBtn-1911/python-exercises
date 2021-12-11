numbers = [3, 4.5, 6, 100, -69, 55, -1, 0, -.1, .0001, 99, -.5, .5]
func = list(filter(lambda num : num >= 0 , numbers))
print(func)