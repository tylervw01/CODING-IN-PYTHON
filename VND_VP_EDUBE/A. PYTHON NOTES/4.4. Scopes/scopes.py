# <<4.4.1.5>> SECTION SUMMARY
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

#

def mult(x):
    var = 5
    return x * var


print(mult(7))    # outputs: 35
#
def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))    # outputs: 49
#
def adding(x):
    var = 7
    return x + var


print(adding(4))    # outputs: 11
print(var)    # NameError

#
var = 2
print(var)    # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())    # outputs: 5
print(var)    # outputs: 5

#
