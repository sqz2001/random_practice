#use a for loop to print numbers from 1-20 inclusive

number_list = list(range(1, 21))
for number in number_list:
    print(number)

#add the numbers from 1 to 1 million. check min and max value added.
one_million = list(range(1, 100_000_001))
total = 0
for value in one_million:
    total += value

print(total)

"""make a list of the 1st 10 cubes (the cube of each integer from 1-10), using
a for loop"""
l = []
list_1 = list(range(1, 11))
for number in list_1:
    l.append(number**3)

print(l)



