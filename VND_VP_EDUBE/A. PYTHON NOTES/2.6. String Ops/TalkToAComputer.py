# The input() function - prohibited operations
# Look at the code in the editor. Run it, enter any number, and press Enter.
# Testing TypeError message.
####################################################

# PROHIBITED OPERATIONS
anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
####################################################

# TYPE CASTING
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
####################################################

#MORE ABOUT INPUT () AND TYPE CASTING
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
