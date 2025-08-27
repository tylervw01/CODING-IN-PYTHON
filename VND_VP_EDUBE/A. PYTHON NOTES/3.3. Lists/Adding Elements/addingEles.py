numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
###
numbers.append(4)

print(len(numbers))
print(numbers)
###
numbers.insert(0, 222)
print(len(numbers))
print(numbers)
#


###########################################################
#adding from the back creates [1, 2, 3, 4, 5]
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
####################################
#adding insert creates a lsit from the from [1, 2, 3, 4, 5]
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)
