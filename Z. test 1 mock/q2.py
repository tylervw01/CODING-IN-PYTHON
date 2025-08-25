#Question 2
# Travel Cost Calculator:
# Write a program that asks the user for the cost of three travel expenses: tranport, accomodation and meals.
# Display a neatly formatted summary showing:
# Subtotal of all expenses
# Service fee @ 10%
# Final total due (rounded to two decimals)#

transport = float(input("Enter the cost of transport: "))
accomodation = float(input("Enter the cost of accomodation: "))
meals = float(input("Enter the cost of meals: "))

subtotal = transport + accomodation + meals
service_fee = subtotal * 0.1
total = subtotal + service_fee

print("Subtotal:", subtotal)
print("Service fee:", service_fee)
print("Total:", total)
