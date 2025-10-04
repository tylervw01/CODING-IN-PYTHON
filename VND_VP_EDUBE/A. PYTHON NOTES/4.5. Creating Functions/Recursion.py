#Some simple functions: recursion
# There's one more thing we want to show you to make everything complete - it's recursion.

# This term may describe many different concepts, but one of them is especially interesting - the one referring to computer programming.

# In this field, recursion is a technique where a function invokes itself.
###
# The definition of the ith number refers to the i-1 number, and so on, till you reach the first two.
# Can it be used in the code? Yes, it can. It can also make the code shorter and clearer.
# The second version of our fib() function makes direct use of this definition:
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)

#####################################

#####################################
#This is in fact a ready recipe for our new solution.
#Here it is:

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)


############
############

#Our short functional journey is almost over. The next section will take care of two curious Python data types: tuples and dictionaries.
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))
