
# secret_number = 333
# # float(input("Enter the first number (var1): "))

# while secret_number != 0:
#     print("Inside the loop.", secret_number)
#     secret_number -= 1
# print("Outside the loop.", secret_number)

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

secret_numbers = 333
even_numbers = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Ha ha! You're stuck in my loop!:", odd_numbers)
print("Well done, muggle! You are free now.:", even_numbers)

