# Arithmetic operators: exponentiation
# A ** (double asterisk) sign is an exponentiation (power) operator. Its left argument is the base, its right, the exponent.

# Classical mathematics prefers notation with superscripts, just like this: 23. Pure text editors don't accept that, so Python uses ** instead, e.g., 2 ** 3.
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
# Remember: It's possible to formulate the following rules based on this result:

# when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.
# This is an important distinction to remember.
########################################################
# Arithmetic operators: division
# A / (slash) sign is a divisional operator.
# The value in front of the slash is a dividend, the value behind the slash, a divisor.
# Run the code below and analyze the results.
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
################################################################
# Arithmetic operators: integer division
# A // (double slash) sign is an integer divisional operator. It differs from the standard / operator in two details:

# its result lacks the fractional part - it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded;
# it conforms to the integer vs. float rule.
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
################
# As you can see, integer by integer division gives an integer result. All other cases produce floats.
# Let's do some more advanced tests.
# Look at the following snippet:
print(6 // 4)
print(6. // 4)
#####################################################################
