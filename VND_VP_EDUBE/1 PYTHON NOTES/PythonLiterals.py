#NOTES 
# Literals - the data in itself
# Now that you have a little knowledge of some of the powerful features offered by the print() function, it's time to learn about some new issues, and one important new term - the literal.
# A literal is data whose values are determined by the literal itself.
# You use literals to encode data and to put them into your code. We're now going to show you some conventions you have to obey when using Python.
#######################################

# The print() function presents them in exactly the same way - this example is obvious, as their human-readable representation is also the same. Internally, in the computer's memory, these two values are stored in completely different ways - the string exists as just a string - a series of letters.
# print("2")
# print(2)

#########################################

# Integers
# You may already know a little about how computers perform calculations on numbers. Perhaps you've heard of the binary system, and know that it's the system computers use for storing numbers, and that they can perform any operation upon them.

# We won't explore the intricacies of positional numeral systems here, but we'll say that the numbers handled by modern computers are of two types:

# integers, that is, those which are devoid of the fractional part;
# and floating-point numbers (or simply floats), that contain (or are able to contain) the fractional part.

################################################


# Integers: octal and hexadecimal numbers
# There are two additional conventions in Python that are unknown to the world of mathematics. The first allows us to use numbers in an octal representation.

# If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.
# OCTAL - print(0o123)